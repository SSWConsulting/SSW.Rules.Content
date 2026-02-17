#!/usr/bin/env python3
"""
SSW URL Linter for CI/CD

Checks MDX files for URLs missing the 'www' prefix on ssw.com.au domain.
The Cloudflare worker redirects ssw.com.au to www.ssw.com.au, so links
without "www" can't be indexed properly.

Usage:
  # Read file list from stdin (one file per line) - recommended for large file lists
  git diff --name-only ... -- '*.mdx' | python lint-ssw-urls.py

  # Or check all MDX files in content directories
  python lint-ssw-urls.py

Output:
  - Prints markdown-formatted report to stdout
  - Writes report to $URL_LINT_REPORT_PATH if set
  - Sets GITHUB_OUTPUT has_issues=true if issues found
  - Always exits 0 (warnings only, never fails build)
"""

import os
import re
import sys
from pathlib import Path
from typing import List
from dataclasses import dataclass

# Pattern to match URLs missing www prefix
# Matches: https://ssw.com.au or http://ssw.com.au
# Does NOT match: https://subdomain.ssw.com.au or https://www.ssw.com.au
MISSING_WWW_PATTERN = re.compile(
    r'https?://ssw\.com\.au(?![a-z0-9-]*\.)',
    re.IGNORECASE
)


@dataclass
class UrlIssue:
    """Represents a single URL issue found in a file."""
    file_path: str
    line_num: int
    original: str
    suggested: str


def find_issues_in_file(file_path: Path) -> List[UrlIssue]:
    """Find all URL issues in a single file."""
    issues = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                for match in MISSING_WWW_PATTERN.finditer(line):
                    original = match.group(0)
                    suggested = original.replace('ssw.com.au', 'www.ssw.com.au')
                    issues.append(UrlIssue(
                        file_path=str(file_path),
                        line_num=line_num,
                        original=original,
                        suggested=suggested
                    ))
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}", file=sys.stderr)
    return issues


def generate_markdown_report(issues: List[UrlIssue], files_checked: int) -> str:
    """Generate a markdown report of all issues found."""
    if not issues:
        return ""

    report = "## :warning: URL Linter Warning\n\n"
    report += f"Found **{len(issues)} URL(s)** missing the `www` prefix in {files_checked} file(s) checked.\n\n"
    report += "URLs using `ssw.com.au` should use `www.ssw.com.au` instead.\n"
    report += "The Cloudflare worker redirects non-www to www, which means links without 'www' can't be indexed properly.\n\n"
    report += "### Issues Found\n\n"
    report += "| File | Line | Current | Should Be |\n"
    report += "|------|------|---------|----------|\n"

    for issue in issues:
        # Shorten file path for readability
        short_path = issue.file_path
        if len(short_path) > 50:
            short_path = "..." + short_path[-47:]
        report += f"| `{short_path}` | {issue.line_num} | `{issue.original}` | `{issue.suggested}` |\n"

    report += "\n---\n"
    report += "<sub>This is a warning only and does not block the PR.</sub>\n"

    return report


def set_github_output(name: str, value: str):
    """Set a GitHub Actions output variable."""
    github_output = os.environ.get('GITHUB_OUTPUT')
    if github_output:
        with open(github_output, 'a') as f:
            f.write(f"{name}={value}\n")


def main():
    files_to_check = []

    # Check if stdin has data (piped input)
    if not sys.stdin.isatty():
        # Read file list from stdin (one file per line)
        for line in sys.stdin:
            file_path = line.strip()
            if file_path and file_path.endswith('.mdx'):
                files_to_check.append(Path(file_path))
    else:
        # No stdin - check all MDX files in content directories
        script_dir = Path(__file__).parent
        project_root = script_dir.parent.parent

        # Content directories in SSW.Rules.Content repo
        content_dirs = [
            project_root / 'public' / 'uploads' / 'rules',
            project_root / 'categories',
        ]

        for content_dir in content_dirs:
            if content_dir.exists():
                files_to_check.extend(content_dir.rglob('*.mdx'))

    if not files_to_check:
        print("No MDX files to check.")
        set_github_output('has_issues', 'false')
        sys.exit(0)

    # Find all issues
    all_issues: List[UrlIssue] = []
    files_checked = 0

    for file_path in files_to_check:
        if not Path(file_path).exists():
            continue
        files_checked += 1
        issues = find_issues_in_file(Path(file_path))
        all_issues.extend(issues)

    # Generate report
    report = generate_markdown_report(all_issues, files_checked)

    if report:
        # Print to stdout
        print(report)

        # Write to report file if path is set
        report_path = os.environ.get('URL_LINT_REPORT_PATH')
        if report_path:
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report)

        # Set GitHub output
        set_github_output('has_issues', 'true')
        set_github_output('issue_count', str(len(all_issues)))
    else:
        print(f"Checked {files_checked} file(s) - no URL issues found.")
        set_github_output('has_issues', 'false')
        set_github_output('issue_count', '0')

    # Always exit 0 - this is a warning, not an error
    sys.exit(0)


if __name__ == '__main__':
    main()
