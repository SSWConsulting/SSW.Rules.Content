#!/usr/bin/env python3
"""
Agentic SEMrush SEO fixer — OpenAI tool use (gpt-4o).

Instead of a fixed pipeline, an LLM drives the full workflow: it decides
which tools to call and in what order, reasons about the content of each
page, generates unique replacements, and handles retries when the tool
rejects a value (too long, duplicate, etc.).

Usage:
    python scripts/semrush/run_agent.py
    python scripts/semrush/run_agent.py --dry-run --limit 3 --issue duplicate_meta
    python scripts/semrush/run_agent.py --urls-file urls.txt --issue duplicate_title

Required env vars:
    OPENAI_API_KEY
    SEMRUSH_API_KEY, SEMRUSH_PROJECT_ID   (not needed with --urls-file)

Optional env vars:
    AGENT_MODEL   OpenAI model to use (default: gpt-4o)
    REPO_ROOT     Absolute path to repo root (defaults to ../../ from this script)
"""

import argparse
import json
import os
import sys

_SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, _SCRIPT_DIR)

from semrush_client import client_from_env
from map_urls_to_files import map_urls_to_files
from fix_duplicate_meta import read_frontmatter_fields, update_seo_description, update_title
import github_pr

try:
    import openai
except ImportError:
    print("ERROR: 'openai' not installed. Run: pip install openai", file=sys.stderr)
    sys.exit(1)

_REPO_ROOT = os.environ.get("REPO_ROOT") or os.path.abspath(os.path.join(_SCRIPT_DIR, "..", ".."))
_MODEL = os.environ.get("AGENT_MODEL", "gpt-4o")

# ── Per-run session state ─────────────────────────────────────────────────────

_state: dict = {}


def _reset_state(dry_run: bool, limit: int, urls_file: str | None) -> None:
    _state.clear()
    _state.update({
        "dry_run": dry_run,
        "limit": limit,
        "urls_file": urls_file,
        "used_values": set(),          # normalised values already written this session
        "changed_files": [],           # absolute paths of all successfully written files
        "mappings": {                  # issue_type -> [(rel_path, old_value, new_value)]
            "duplicate_meta": [],
            "duplicate_title": [],
        },
    })


# ── Tool implementations ──────────────────────────────────────────────────────

def _tool_fetch_flagged_pages(issue_type: str) -> dict:
    """Fetch SEMrush-flagged pages and map them to repo files."""
    if _state.get("urls_file"):
        with open(_state["urls_file"], encoding="utf-8") as f:
            urls = [l.strip() for l in f if l.strip() and not l.startswith("#")]
        print(f"[tool] Loaded {len(urls)} URL(s) from {_state['urls_file']!r}")
    else:
        semrush = client_from_env()
        urls = (
            semrush.get_duplicate_meta_pages()
            if issue_type == "duplicate_meta"
            else semrush.get_duplicate_title_pages()
        )

    if _state["limit"]:
        urls = urls[: _state["limit"]]

    url_to_file = map_urls_to_files(urls, _REPO_ROOT)
    pages = [{"url": url, "file_path": fp} for url, fp in url_to_file.items()]
    print(f"[tool] fetch_flagged_pages({issue_type!r}): {len(pages)} page(s)")
    return {"pages": pages, "count": len(pages)}


def _tool_read_rule_file(file_path: str) -> dict:
    """Return frontmatter fields and a body excerpt for a rule file."""
    fields = read_frontmatter_fields(file_path)
    if fields is None:
        return {"error": "Could not parse frontmatter"}
    return {
        "title": fields.get("title") or "",
        "seoDescription": fields.get("seoDescription") or "",
        "excerpt": (fields.get("_content") or "")[:600],
    }


def _tool_write_frontmatter_field(
    file_path: str,
    field: str,
    value: str,
    old_value: str = "",
) -> dict:
    """Validate and write one frontmatter field. Returns an error dict on rejection."""
    norm = value.lower().strip()

    if field == "seoDescription" and len(value) > 160:
        return {
            "success": False,
            "error": f"Value is {len(value)} chars — must be under 160. Shorten it and retry.",
        }

    if norm in _state["used_values"]:
        return {
            "success": False,
            "error": "This value was already written in this session. Generate a different one.",
        }

    rel = os.path.relpath(file_path, _REPO_ROOT)
    issue_type = "duplicate_meta" if field == "seoDescription" else "duplicate_title"

    print(f"[tool] write {field!r} → {rel}")
    print(f"  old: {old_value!r}")
    print(f"  new: {value!r}")

    if _state["dry_run"]:
        _state["used_values"].add(norm)
        _state["mappings"][issue_type].append((rel, old_value, value))
        return {"success": True, "note": "dry-run — file not written"}

    ok = (update_seo_description if field == "seoDescription" else update_title)(file_path, value)
    if not ok:
        return {"success": False, "error": "File write failed — check the path and frontmatter"}

    _state["used_values"].add(norm)
    _state["changed_files"].append(file_path)
    _state["mappings"][issue_type].append((rel, old_value, value))
    return {"success": True}


def _tool_open_pull_request(issue_type: str) -> dict:
    """Commit all files changed for an issue type and open a GitHub PR."""
    if _state["dry_run"]:
        return {"note": "dry-run — PR skipped"}

    mappings = _state["mappings"].get(issue_type, [])
    if not mappings:
        return {"note": "No changes recorded for this issue type — PR skipped"}

    rel_set = {rel for rel, _, _ in mappings}
    changed = [fp for fp in _state["changed_files"]
               if os.path.relpath(fp, _REPO_ROOT) in rel_set]
    if not changed:
        return {"note": "No written files found to commit"}

    def _safe(v: str) -> str:
        return v.replace("\n", " ").replace("\r", "").replace("|", "\\|")

    if issue_type == "duplicate_meta":
        field_label, col1, col2 = "seoDescription", "Old description", "New description"
        branch, pr_title = github_pr.BRANCH_NAME, github_pr.PR_TITLE
    else:
        field_label, col1, col2 = "title", "Old title", "New title"
        branch, pr_title = github_pr.TITLE_BRANCH_NAME, github_pr.TITLE_PR_TITLE

    rows = "\n".join(
        f"| `{rel}` | {_safe(old)} | {_safe(new)} |"
        for rel, old, new in mappings
    )
    pr_body = (
        f"Fixes duplicate `{field_label}` frontmatter on {len(mappings)} /rules page(s) "
        f"flagged by SEMrush Site Audit. Only frontmatter was modified — page body and all "
        f"other fields are unchanged. Values were generated by an AI agent.\n\n"
        f"| File | {col1} | {col2} |\n"
        f"|------|{'-' * len(col1)}|{'-' * len(col2)}|\n"
        f"{rows}\n\n"
        f"> AI-generated — human review required before merge.\n"
    )

    success = github_pr.run_pr_flow(
        _REPO_ROOT, changed,
        branch_name=branch, pr_title=pr_title, pr_body=pr_body,
    )
    return {"success": success}


# ── Tool registry ─────────────────────────────────────────────────────────────

_TOOLS = {
    "fetch_flagged_pages": _tool_fetch_flagged_pages,
    "read_rule_file": _tool_read_rule_file,
    "write_frontmatter_field": _tool_write_frontmatter_field,
    "open_pull_request": _tool_open_pull_request,
}

_TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "fetch_flagged_pages",
            "description": (
                "Fetch all pages flagged by SEMrush for a given duplicate SEO issue. "
                "Returns a list of {url, file_path} objects."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "issue_type": {
                        "type": "string",
                        "enum": ["duplicate_meta", "duplicate_title"],
                        "description": (
                            "duplicate_meta = fix seoDescription; "
                            "duplicate_title = fix title"
                        ),
                    },
                },
                "required": ["issue_type"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_rule_file",
            "description": (
                "Read the title, seoDescription, and body excerpt from a rule.mdx file. "
                "Use the returned content to inform the replacement you generate."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Absolute path to the rule.mdx file",
                    },
                },
                "required": ["file_path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_frontmatter_field",
            "description": (
                "Write a new value for one frontmatter field. "
                "Returns {success: false, error: ...} if the value is too long or a duplicate — "
                "in that case, generate a different value and call this tool again."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {"type": "string"},
                    "field": {
                        "type": "string",
                        "enum": ["seoDescription", "title"],
                        "description": "The frontmatter field to update",
                    },
                    "value": {
                        "type": "string",
                        "description": "The replacement value to write",
                    },
                    "old_value": {
                        "type": "string",
                        "description": "The current field value, for the PR table (pass from read_rule_file output)",
                    },
                },
                "required": ["file_path", "field", "value"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "open_pull_request",
            "description": (
                "Commit all files changed for an issue type and open a GitHub PR. "
                "Call once per issue type, only after all pages for that type are processed."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "issue_type": {
                        "type": "string",
                        "enum": ["duplicate_meta", "duplicate_title"],
                    },
                },
                "required": ["issue_type"],
            },
        },
    },
]

# ── System prompt ─────────────────────────────────────────────────────────────

_SYSTEM_PROMPT = """\
You are an SEO automation agent for SSW's rules website (ssw.com.au/rules).
Your job is to fix duplicate SEO fields flagged by SEMrush Site Audit.

For each issue type you are asked to fix, follow this workflow:
1. Call fetch_flagged_pages to get all affected pages.
2. For each page:
   a. Call read_rule_file to get the current title, seoDescription, and body excerpt.
   b. Generate a unique replacement value informed by the page content.
   c. Call write_frontmatter_field. If it returns success=false, read the error,
      adjust your value accordingly, and retry.
3. After all pages for an issue type are processed, call open_pull_request for that type.

Generation rules:
- seoDescription: strictly under 160 characters, no filler openers (Learn / Discover /
  Find out / In this article / This page), no trailing full stop, specific and concrete.
- title: unique, descriptive, concise, faithful to the page content.
- Never reuse a value already written this session (the tool will reject duplicates — generate something different).
- Always pass old_value to write_frontmatter_field so the PR table shows before/after.
- Skip a file only if read_rule_file returns an error or the title field is empty.
"""

# ── Agent loop ────────────────────────────────────────────────────────────────

def _safe_call(fn, args: dict) -> dict:
    try:
        return fn(**args)
    except Exception as exc:
        return {"error": str(exc)}


def run_agent(issue_types: list[str]) -> None:
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        print("ERROR: OPENAI_API_KEY is not set", file=sys.stderr)
        sys.exit(1)

    client = openai.OpenAI(api_key=api_key)
    messages = [
        {"role": "system", "content": _SYSTEM_PROMPT},
        {"role": "user", "content": f"Fix the following issue type(s): {', '.join(issue_types)}"},
    ]

    print(f"\n[agent] model={_MODEL!r}  issues={issue_types}")
    step = 0

    while True:
        step += 1
        print(f"\n[agent] step {step} — calling model...")
        response = client.chat.completions.create(
            model=_MODEL,
            messages=messages,
            tools=_TOOL_SCHEMAS,
            tool_choice="auto",
        )
        msg = response.choices[0].message
        messages.append(msg)

        if not msg.tool_calls:
            print(f"\n[agent] done.\n{msg.content or ''}")
            break

        for call in msg.tool_calls:
            name = call.function.name
            args = json.loads(call.function.arguments)
            print(f"[agent] → {name}({json.dumps(args, ensure_ascii=False)[:200]})")

            fn = _TOOLS.get(name)
            result = (
                {"error": f"Unknown tool: {name}"} if fn is None
                else _safe_call(fn, args)
            )
            print(f"[agent] ← {json.dumps(result, ensure_ascii=False)[:300]}")

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": json.dumps(result),
            })


# ── CLI ───────────────────────────────────────────────────────────────────────

def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Agentic SEMrush SEO fixer (OpenAI tool use)")
    p.add_argument(
        "--dry-run", action="store_true",
        help="Log planned changes without writing files or creating a PR",
    )
    p.add_argument(
        "--issue",
        choices=["duplicate_meta", "duplicate_title", "both"],
        default="both",
        help="Which issue type(s) to fix (default: both)",
    )
    p.add_argument(
        "--limit", type=int, default=0, metavar="N",
        help="Process at most N pages per issue type (0 = no limit)",
    )
    p.add_argument(
        "--urls-file", metavar="PATH",
        help="Load URLs from a plain-text file instead of calling SEMrush",
    )
    return p.parse_args()


def main() -> None:
    args = _parse_args()
    _reset_state(args.dry_run, args.limit, args.urls_file)

    issue_types = (
        ["duplicate_meta", "duplicate_title"] if args.issue == "both"
        else [args.issue]
    )

    print("=" * 60)
    print("SEMrush SEO Fixer — Agentic mode (OpenAI tool use)")
    print("=" * 60)
    if args.dry_run:
        print("MODE: DRY RUN\n")
    print(f"Model     : {_MODEL}")
    print(f"Issues    : {', '.join(issue_types)}")
    print(f"Repo root : {_REPO_ROOT}")
    if args.limit:
        print(f"Limit     : {args.limit} pages per issue type")

    run_agent(issue_types)


if __name__ == "__main__":
    main()
