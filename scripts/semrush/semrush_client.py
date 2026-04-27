#!/usr/bin/env python3
"""
SEMrush Site Audit API client.

All endpoint paths and the duplicate-meta issue type ID are defined in one place
at the top of this file so they are easy to adjust when you verify them against
a real API response.

Required env vars:
    SEMRUSH_API_KEY     - Your SEMrush API key
    SEMRUSH_PROJECT_ID  - The SEMrush project ID for ssw.com.au
"""

import os
import sys

try:
    import requests
except ImportError:
    print("ERROR: 'requests' package not installed. Run: pip install requests", file=sys.stderr)
    sys.exit(1)

# ── Adapter constants — adjust here if SEMrush changes their API ─────────────

SEMRUSH_API_BASE = "https://api.semrush.com"

# Site Audit endpoint paths (project_id is substituted at call time)
# Reference: https://developer.semrush.com/api/v2/site-audit/
_EP_AUDIT_INFO   = "/reports/v1/projects/{project_id}/siteaudit/"
_EP_AUDIT_PAGES  = "/reports/v1/projects/{project_id}/siteaudit/pages"
_EP_AUDIT_ISSUES = "/reports/v1/projects/{project_id}/siteaudit/issues"

# SEMrush numeric issue IDs.
# SEMrush uses integers, not strings, for issue IDs.
# Run --list-issues to see all IDs present in your snapshot.
ISSUE_DUPLICATE_META  = 15   # "Duplicate meta description"
ISSUE_DUPLICATE_TITLE = 6    # "Duplicate title tag" — verify with --list-issues if this changes

# ─────────────────────────────────────────────────────────────────────────────


class SEMrushClient:
    def __init__(self, api_key: str, project_id: str, snapshot_id: str | None = None):
        self.api_key = api_key
        self.project_id = project_id
        self._snapshot_id = snapshot_id  # explicit override; skips get_latest_snapshot_id()
        self._session = requests.Session()

    def _get(self, endpoint_template: str, params: dict = None) -> dict:
        url = SEMRUSH_API_BASE + endpoint_template.format(project_id=self.project_id)
        params = dict(params or {})
        params["key"] = self.api_key
        resp = self._session.get(url, params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()

    def get_latest_snapshot_id(self) -> str:
        """Return the snapshot_id of the most recent completed audit.

        If SEMRUSH_SNAPSHOT_ID is set, that value is returned directly without
        making an API call — use this to pin a known-good snapshot ID in CI or
        to bypass the response-shape uncertainty below.
        """
        if self._snapshot_id:
            return self._snapshot_id

        data = self._get(_EP_AUDIT_INFO)
        # The exact key name has not been verified against a live API response.
        # If this lookup fails, set SEMRUSH_SNAPSHOT_ID to the correct value
        # (visible in the SEMrush UI URL) to bypass it permanently.
        snapshot_id = (
            data.get("snapshot_id")
            or data.get("snapshotId")
            or data.get("id")
            or (data.get("data") or {}).get("snapshot_id")
        )
        if not snapshot_id:
            raise ValueError(
                f"Could not find snapshot_id in SEMrush response. "
                f"Response keys: {list(data.keys())}. "
                f"Set SEMRUSH_SNAPSHOT_ID env var to bypass this lookup."
            )
        return str(snapshot_id)

    def get_duplicate_meta_pages(self, snapshot_id: str = None) -> list[str]:
        """
        Return source_urls of all pages flagged for duplicate meta descriptions.

        Uses _EP_AUDIT_ISSUES which returns per-issue data including the
        affected page list directly in the response.
        """
        if snapshot_id is None:
            print("[semrush] Fetching latest snapshot ID...")
            snapshot_id = self.get_latest_snapshot_id()
            print(f"[semrush] Using snapshot: {snapshot_id}")

        all_issues = self._get_all_issues(snapshot_id)

        issue_entry = next(
            (i for i in all_issues if i.get("issue_id") == ISSUE_DUPLICATE_META),
            None,
        )
        if issue_entry is None:
            available = [i.get("issue_id") for i in all_issues]
            print(
                f"[semrush] Issue {ISSUE_DUPLICATE_META} not found in snapshot.\n"
                f"          Available issue IDs: {available}"
            )
            return []

        total = issue_entry.get("total", 0)
        limit = issue_entry.get("limit", 100)
        items = issue_entry.get("data", [])

        if total > limit:
            print(
                f"[semrush] WARNING: {total} pages found but only {limit} returned "
                f"(pagination not yet implemented — processing {limit})."
            )

        urls = [item["source_url"] for item in items if item.get("source_url")]
        print(
            f"[semrush] Found {len(urls)} pages with duplicate meta descriptions "
            f"(issue {ISSUE_DUPLICATE_META}, total reported: {total})"
        )
        return urls


    def get_duplicate_title_pages(self, snapshot_id: str = None) -> list[str]:
        """
        Return source_urls of all pages flagged for duplicate title tags.

        Mirrors get_duplicate_meta_pages() but uses ISSUE_DUPLICATE_TITLE.
        """
        if snapshot_id is None:
            print("[semrush] Fetching latest snapshot ID...")
            snapshot_id = self.get_latest_snapshot_id()
            print(f"[semrush] Using snapshot: {snapshot_id}")

        all_issues = self._get_all_issues(snapshot_id)

        issue_entry = next(
            (i for i in all_issues if i.get("issue_id") == ISSUE_DUPLICATE_TITLE),
            None,
        )
        if issue_entry is None:
            available = [i.get("issue_id") for i in all_issues]
            print(
                f"[semrush] Issue {ISSUE_DUPLICATE_TITLE} not found in snapshot.\n"
                f"          Available issue IDs: {available}"
            )
            return []

        total = issue_entry.get("total", 0)
        limit = issue_entry.get("limit", 100)
        items = issue_entry.get("data", [])

        if total > limit:
            print(
                f"[semrush] WARNING: {total} pages found but only {limit} returned "
                f"(pagination not yet implemented — processing {limit})."
            )

        urls = [item["source_url"] for item in items if item.get("source_url")]
        print(
            f"[semrush] Found {len(urls)} pages with duplicate title tags "
            f"(issue {ISSUE_DUPLICATE_TITLE}, total reported: {total})"
        )
        return urls

    def _get_all_issues(self, snapshot_id: str) -> list[dict]:
        """Fetch the full issues list for a snapshot."""
        data = self._get(_EP_AUDIT_ISSUES, {"snapshot_id": snapshot_id})
        if isinstance(data, list):
            return data
        return data.get("issues") or data.get("data") or []

    def list_issues(self, snapshot_id: str = None) -> list[dict]:
        """Return all issue types in the snapshot. Useful for discovering the correct issue_id."""
        if snapshot_id is None:
            snapshot_id = self.get_latest_snapshot_id()
        return self._get_all_issues(snapshot_id)


def client_from_env() -> SEMrushClient:
    """Build a SEMrushClient from environment variables. Exits if vars are missing."""
    api_key = os.environ.get("SEMRUSH_API_KEY", "")
    project_id = os.environ.get("SEMRUSH_PROJECT_ID", "")
    snapshot_id = os.environ.get("SEMRUSH_SNAPSHOT_ID") or None
    missing = []
    if not api_key:
        missing.append("SEMRUSH_API_KEY")
    if not project_id:
        missing.append("SEMRUSH_PROJECT_ID")
    if missing:
        print(
            f"ERROR: Missing required environment variable(s): {', '.join(missing)}",
            file=sys.stderr,
        )
        sys.exit(1)
    return SEMrushClient(api_key, project_id, snapshot_id=snapshot_id)
