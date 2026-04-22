#!/usr/bin/env python3
"""
Generate unique replacement titles for a group of pages that share the same title.

Strategy: one API call per duplicate group. The model receives the full group
context and returns a JSON array of {file_path, new_title} objects so all
titles within the group are distinct from each other.

Rules enforced:
- Each title must be non-empty
- All titles within the group must be distinct from each other
- No surrounding quotes in output
- Returns None on any failure so the caller can safely skip the group
"""

import json
import os
import re
import sys

try:
    import openai
except ImportError:
    print(
        "ERROR: 'openai' package not installed. Run: pip install openai",
        file=sys.stderr,
    )
    sys.exit(1)

_MODEL = "gpt-4o-mini"
_MAX_TITLE_CHARS = 60

_SYSTEM_PROMPT = """\
You are an SEO copywriter producing page titles for SSW's technical rules website.

Requirements for EACH title:
- Under 60 characters
- No surrounding quotes
- Unique — every title in your response must be different from the others
- Specific and concrete — capture what makes this rule distinct
- No filler: do not start with "Learn", "Discover", "Find out", "How to" (unless genuinely instructional)

Output format: valid JSON array only, no preamble, no markdown fences.
Each element: {"file_path": "<exact file_path from input>", "new_title": "<replacement title>"}\
"""

_USER_TEMPLATE = """\
The following pages all share the same title: "{shared_title}"

Generate a distinct replacement title for each one.

Pages:
{pages_json}

Return a JSON array with one object per page, preserving the exact file_path values.\
"""


def _build_excerpt(file_content: str, max_chars: int = 400) -> str:
    body = re.sub(r"^---[\s\S]*?---\s*", "", file_content, count=1)
    body = re.sub(r"<[^>]+?>", " ", body)
    body = re.sub(r"^#+\s+", "", body, flags=re.MULTILINE)
    body = re.sub(r"\s+", " ", body).strip()
    return body[:max_chars]


def generate_titles(
    group: list[dict],
    max_retries: int = 2,
) -> dict[str, str] | None:
    """
    Generate distinct replacement titles for a group of pages sharing the same title.

    group: list of dicts, each with keys:
        file_path    - absolute path to the rule.mdx file
        title        - current (duplicate) title
        seoDescription - current seoDescription (may be None)
        _content     - full file content for excerpt extraction

    Returns dict mapping file_path -> new_title on success, or None on failure.
    """
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        print("  [ai] ERROR: OPENAI_API_KEY is not set.", file=sys.stderr)
        sys.exit(1)

    client = openai.OpenAI(api_key=api_key)

    shared_title = group[0]["title"]

    pages_input = [
        {
            "file_path": item["file_path"],
            "seoDescription": item.get("seoDescription") or "(none)",
            "excerpt": _build_excerpt(item.get("_content", "")),
        }
        for item in group
    ]

    user_msg = _USER_TEMPLATE.format(
        shared_title=shared_title,
        pages_json=json.dumps(pages_input, indent=2),
    )

    for attempt in range(1, max_retries + 1):
        if attempt > 1:
            print(f"  [ai] Retry {attempt - 1}/{max_retries - 1}...")

        try:
            response = client.responses.create(
                model=_MODEL,
                instructions=_SYSTEM_PROMPT,
                input=user_msg,
                max_output_tokens=500,
            )
            raw = response.output_text.strip()
        except Exception as exc:
            print(f"  [ai] API call failed: {exc}")
            return None

        # Strip markdown code fences if the model added them
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)

        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError as exc:
            print(f"  [ai] JSON parse error: {exc} — raw: {raw!r}")
            continue

        if not isinstance(parsed, list) or len(parsed) != len(group):
            print(
                f"  [ai] Expected list of {len(group)} items, got: {type(parsed).__name__} "
                f"with {len(parsed) if isinstance(parsed, list) else '?'} items"
            )
            continue

        result: dict[str, str] = {}
        valid = True

        for item in parsed:
            fp = item.get("file_path", "")
            title = str(item.get("new_title", "")).strip().strip('"\'')
            if not fp or not title:
                print(f"  [ai] Missing file_path or new_title in item: {item}")
                valid = False
                break
            if len(title) > _MAX_TITLE_CHARS:
                print(f"  [ai] Title too long ({len(title)} chars): {title!r}")
                valid = False
                break
            result[fp] = title

        if not valid:
            continue

        # All titles must be distinct from each other
        titles = list(result.values())
        if len(set(t.lower() for t in titles)) < len(titles):
            print(f"  [ai] Duplicate titles within group: {titles}")
            continue

        return result

    print(f"  [ai] SKIP group: all {max_retries} attempt(s) failed")
    return None
