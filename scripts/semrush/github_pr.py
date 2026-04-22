#!/usr/bin/env python3
"""
GitHub PR automation for SEMrush duplicate-field fixers.

Uses the `gh` CLI and standard `git` commands (both must be available on PATH).
All operations are run with cwd=repo_root so this module is location-independent.

Constants at the top define the defaults for the meta-description flow.
Pass branch_name / pr_title / pr_body explicitly for other flows (e.g. title fix).
"""

import os
import subprocess
import sys

# ── Meta-description flow defaults ───────────────────────────────────────────
BRANCH_NAME = "semrush/fix-duplicate-meta"
PR_TITLE    = "[SEMrush] Fix duplicate meta descriptions for /rules"
BASE_BRANCH = "main"
# ─────────────────────────────────────────────────────────────────────────────

# ── Title-tag flow constants ──────────────────────────────────────────────────
TITLE_BRANCH_NAME = "semrush/fix-duplicate-titles"
TITLE_PR_TITLE    = "[SEMrush] Fix duplicate title tags for /rules"
# ─────────────────────────────────────────────────────────────────────────────

_PR_BODY_TEMPLATE = """\
## Summary

This PR was generated automatically by the SEMrush duplicate meta description fixer \
(`scripts/semrush/run_duplicate_meta_fix.py`).

### What changed

- Only `seoDescription` frontmatter fields were updated
- Only `/rules` pages flagged by SEMrush Site Audit (duplicate meta descriptions, issue #15) were processed
- Page body content, titles, and all other frontmatter fields are **unchanged**
- {file_count} file(s) updated: {file_list}

### How descriptions were generated

1. SEMrush Site Audit identified pages sharing identical `seoDescription` values
2. Each page's title, current description, and body excerpt were sent to OpenAI (`gpt-4o-mini`)
3. Generated descriptions were validated: under 160 chars, no filler phrases, unique within batch
4. Retried automatically if the first attempt exceeded the character limit

### Before merging

- [ ] Review each changed description for accuracy and tone
- [ ] Run frontmatter validation on changed files:
  ```
  cd scripts/frontmatter-validator && npm install
  node frontmatter-validator.js '<comma-separated file paths>'
  ```
- [ ] Edit any unsatisfactory descriptions directly on this branch

> **Human review is required before merge.**
"""


def _run(cmd: list[str], repo_root: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd,
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=check,
    )


def check_gh_available() -> bool:
    """
    Return True if the `gh` CLI is installed and has credentials available.

    In GitHub Actions, authentication is via the GH_TOKEN env var (no interactive
    login needed). Locally, `gh auth login` is required.
    """
    which = subprocess.run(
        ["gh", "--version"],
        capture_output=True,
        text=True,
        check=False,
    )
    if which.returncode != 0:
        print(
            "[pr] ERROR: `gh` CLI not found on PATH.\n"
            "     Install it from https://cli.github.com/ then run: gh auth login",
            file=sys.stderr,
        )
        return False

    if os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN"):
        return True

    result = subprocess.run(
        ["gh", "auth", "status"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        print(
            "[pr] ERROR: `gh` CLI is not authenticated.\n"
            "     Run: gh auth login",
            file=sys.stderr,
        )
        return False
    return True


def check_open_pr(repo_root: str, branch_name: str = BRANCH_NAME) -> str | None:
    """
    Return the URL of an already-open PR for branch_name, or None if there is none.
    """
    result = _run(
        [
            "gh", "pr", "list",
            "--head", branch_name,
            "--state", "open",
            "--json", "url,title",
            "--jq", ".[0].url // empty",
        ],
        repo_root,
        check=False,
    )
    url = result.stdout.strip()
    return url if url else None


def _branch_exists_locally(repo_root: str, branch_name: str) -> bool:
    result = _run(
        ["git", "show-ref", "--verify", "--quiet", f"refs/heads/{branch_name}"],
        repo_root,
        check=False,
    )
    return result.returncode == 0


def get_current_branch(repo_root: str) -> str:
    result = _run(["git", "rev-parse", "--abbrev-ref", "HEAD"], repo_root)
    return result.stdout.strip()


def create_branch(repo_root: str, branch_name: str = BRANCH_NAME) -> bool:
    """
    Create the fix branch from BASE_BRANCH.

    If the branch already exists locally (and we already confirmed no open PR),
    it is deleted and recreated cleanly.
    """
    current = get_current_branch(repo_root)
    print(f"[pr] Current branch: {current}")

    if current == branch_name:
        print(f"[pr] Already on {branch_name} — nothing to do for branch creation")
        return True

    if _branch_exists_locally(repo_root, branch_name):
        print(f"[pr] Deleting stale local branch: {branch_name}")
        result = _run(["git", "branch", "-D", branch_name], repo_root, check=False)
        if result.returncode != 0:
            print(f"[pr] ERROR: Could not delete branch: {result.stderr.strip()}", file=sys.stderr)
            return False

    print(f"[pr] Creating branch {branch_name!r} from {BASE_BRANCH!r}...")
    result = _run(
        ["git", "checkout", "-b", branch_name],
        repo_root,
        check=False,
    )
    if result.returncode != 0:
        print(f"[pr] ERROR: Could not create branch: {result.stderr.strip()}", file=sys.stderr)
        return False

    return True


def commit_changes(repo_root: str, changed_files: list[str], commit_msg: str = None) -> bool:
    """
    Stage only the changed rule files and create a commit.

    changed_files should be absolute paths; they are converted to repo-relative
    paths for git add.
    """
    rel_files = [os.path.relpath(f, repo_root) for f in changed_files]

    print(f"[pr] Staging {len(rel_files)} file(s)...")
    result = _run(["git", "add", "--"] + rel_files, repo_root, check=False)
    if result.returncode != 0:
        print(f"[pr] ERROR: git add failed: {result.stderr.strip()}", file=sys.stderr)
        return False

    status = _run(["git", "diff", "--cached", "--quiet"], repo_root, check=False)
    if status.returncode == 0:
        print("[pr] Nothing staged — files may already be up to date. Skipping commit.")
        return False

    if commit_msg is None:
        commit_msg = (
            f"fix(seo): replace duplicate meta descriptions [SEMrush audit]\n\n"
            f"Automatically generated by scripts/semrush/run_duplicate_meta_fix.py.\n"
            f"{len(rel_files)} file(s) updated."
        )
    print("[pr] Committing...")
    result = _run(["git", "commit", "-m", commit_msg], repo_root, check=False)
    if result.returncode != 0:
        print(f"[pr] ERROR: git commit failed: {result.stderr.strip()}", file=sys.stderr)
        return False

    print(f"[pr] Committed {len(rel_files)} file(s)")
    return True


def push_branch(repo_root: str, branch_name: str = BRANCH_NAME) -> bool:
    """Push the fix branch to origin."""
    print(f"[pr] Pushing {branch_name!r} to origin...")
    result = _run(
        ["git", "push", "--force-with-lease", "origin", branch_name],
        repo_root,
        check=False,
    )
    if result.returncode != 0:
        print(f"[pr] ERROR: git push failed: {result.stderr.strip()}", file=sys.stderr)
        return False
    return True


def open_pr(
    repo_root: str,
    changed_files: list[str],
    branch_name: str = BRANCH_NAME,
    pr_title: str = PR_TITLE,
    pr_body: str = None,
) -> str | None:
    """
    Create a GitHub pull request and return its URL.
    Returns None on failure.
    """
    if pr_body is None:
        rel_files = [os.path.relpath(f, repo_root) for f in changed_files]
        if len(rel_files) <= 20:
            file_list = ", ".join(f"`{f}`" for f in rel_files)
        else:
            shown = ", ".join(f"`{f}`" for f in rel_files[:20])
            file_list = f"{shown}, and {len(rel_files) - 20} more"
        pr_body = _PR_BODY_TEMPLATE.format(
            file_count=len(rel_files),
            file_list=file_list,
        )

    print(f"[pr] Creating pull request: {pr_title!r}...")
    result = _run(
        [
            "gh", "pr", "create",
            "--base", BASE_BRANCH,
            "--head", branch_name,
            "--title", pr_title,
            "--body", pr_body,
        ],
        repo_root,
        check=False,
    )
    if result.returncode != 0:
        print(f"[pr] ERROR: gh pr create failed: {result.stderr.strip()}", file=sys.stderr)
        return None

    pr_url = result.stdout.strip()
    print(f"[pr] Pull request created: {pr_url}")
    return pr_url


def run_pr_flow(
    repo_root: str,
    changed_files: list[str],
    branch_name: str = BRANCH_NAME,
    pr_title: str = PR_TITLE,
    pr_body: str = None,
    commit_msg: str = None,
) -> bool:
    """
    Orchestrate the full branch -> commit -> push -> PR flow.

    Returns True if a PR was successfully created, False otherwise.
    Safe to call even if something goes wrong — errors are logged, not raised.
    """
    if not changed_files:
        print("[pr] No changed files — skipping PR creation")
        return False

    if not check_gh_available():
        return False

    existing_pr = check_open_pr(repo_root, branch_name)
    if existing_pr:
        print(
            f"[pr] An open PR for branch {branch_name!r} already exists: {existing_pr}\n"
            f"[pr] Skipping PR creation to avoid duplicates.\n"
            f"[pr] Close or merge that PR first, then re-run."
        )
        return False

    if not create_branch(repo_root, branch_name):
        return False

    if not commit_changes(repo_root, changed_files, commit_msg):
        return False

    if not push_branch(repo_root, branch_name):
        return False

    pr_url = open_pr(repo_root, changed_files, branch_name, pr_title, pr_body)
    return pr_url is not None
