#!/usr/bin/env python3
"""
Map SSW Rules page URLs to local repo file paths.

Mapping rule:
    https://[www.]ssw.com.au/rules/{slug}[/]
    → {repo_root}/public/uploads/rules/{slug}/rule.mdx

The folder name in the repo always equals the rule's `uri` frontmatter field,
which is also the last path segment of the published URL.
"""

import os
import re


# URL patterns that identify SSW Rules pages.
# Add alternatives here if the site uses other domains or path prefixes.
_RULES_URL_RE = re.compile(
    r"^https?://(?:www\.)?ssw\.com\.au/rules/([^/?#]+)/?$",
    re.IGNORECASE,
)


def extract_slug(url: str) -> str | None:
    """Extract the rule slug from an SSW Rules URL. Returns None if not a rules URL."""
    m = _RULES_URL_RE.match(url.strip())
    return m.group(1) if m else None


def slug_to_file_path(slug: str, repo_root: str) -> str | None:
    """
    Resolve a rule slug to its absolute file path.
    Returns the path if the file exists on disk, otherwise None.
    """
    candidate = os.path.join(repo_root, "public", "uploads", "rules", slug, "rule.mdx")
    return candidate if os.path.isfile(candidate) else None


def map_urls_to_files(urls: list[str], repo_root: str) -> dict[str, str]:
    """
    Map a list of URLs to local file paths.

    Returns {url: absolute_file_path} for every URL that could be resolved.
    Logs and skips anything that cannot be confidently mapped.
    """
    result: dict[str, str] = {}
    skipped_not_rules = 0
    skipped_not_found = 0

    for url in urls:
        slug = extract_slug(url)
        if slug is None:
            print(f"[map] SKIP (not a /rules/ URL): {url}")
            skipped_not_rules += 1
            continue

        file_path = slug_to_file_path(slug, repo_root)
        if file_path is None:
            print(f"[map] SKIP (file not found on disk): {url}  ->  public/uploads/rules/{slug}/rule.mdx")
            skipped_not_found += 1
            continue

        result[url] = file_path

    print(
        f"[map] Mapped {len(result)} URL(s) to files  "
        f"({skipped_not_rules} not-rules, {skipped_not_found} not-found skipped)"
    )
    return result
