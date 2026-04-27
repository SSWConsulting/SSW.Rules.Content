#!/usr/bin/env python3
"""
Generate unique SEO descriptions using the OpenAI API (Responses API).

Rules enforced:
- Under 160 characters
- No filler phrases or meta-commentary
- Unique within the current batch (caller passes in a set of used descriptions)
- Returns None on any failure so the caller can safely skip
"""

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

# Model to use. gpt-4o-mini is fast and cost-effective for short text generation.
# Swap to gpt-4o for higher quality on difficult cases.
_MODEL = "gpt-4o-mini"
_MAX_CHARS = 160

_SYSTEM_PROMPT = """\
You are an SEO copywriter producing meta descriptions for SSW's technical rules website.

Requirements:
- Exactly one sentence
- Under 160 characters (count carefully before responding)
- No filler: do not start with "Learn", "Discover", "Find out", "In this article", "This page"
- No trailing full stop
- No surrounding quotes
- Output ONLY the description — nothing else, no preamble, no label, no commentary\
"""

_USER_TEMPLATE = """\
Page title: {title}

Current description (flagged as duplicate — must be replaced with something unique):
{current_desc}

Content excerpt (first ~600 chars of body):
{excerpt}

Write a replacement meta description that captures the specific, concrete value of this page.\
"""

# Phrases that indicate the model leaked its own commentary into the output
_FILLER_PATTERNS = [
    r"\bhere is\b",
    r"\bgenerated seo\b",
    r"\bseo description\b",
    r"\bi'?ve generated\b",
    r"\bthis (page|rule|article) (explains|covers|describes|provides)\b",
]


def _build_excerpt(file_content: str, max_chars: int = 600) -> str:
    """Extract the first meaningful body text after the frontmatter."""
    # Remove frontmatter block
    body = re.sub(r"^---[\s\S]*?---\s*", "", file_content, count=1)
    # Strip JSX/MDX components and HTML tags
    body = re.sub(r"<[^>]+?>", " ", body)
    # Strip markdown heading markers
    body = re.sub(r"^#+\s+", "", body, flags=re.MULTILINE)
    # Collapse whitespace
    body = re.sub(r"\s+", " ", body).strip()
    return body[:max_chars]


def generate_description(
    title: str,
    current_desc: str,
    file_content: str,
    used_descriptions: set[str],
    max_retries: int = 2,
) -> str | None:
    """
    Generate a new, unique seoDescription.

    Retries up to max_retries times. On a length failure the retry prompt
    includes the over-length draft so the model can shorten it directly.

    Returns the description string on success, or None if all attempts fail.
    """
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        print("  [ai] ERROR: OPENAI_API_KEY is not set.", file=sys.stderr)
        sys.exit(1)

    client = openai.OpenAI(api_key=api_key)
    excerpt = _build_excerpt(file_content)

    base_user_msg = _USER_TEMPLATE.format(
        title=title,
        current_desc=current_desc or "(none)",
        excerpt=excerpt or "(no body content extracted)",
    )

    user_msg = base_user_msg
    previous_draft: str | None = None
    failure_reason: str | None = None  # "too_long" | "filler" | "duplicate"

    for attempt in range(1, max_retries + 1):
        if attempt > 1:
            print(f"  [ai] Retry {attempt - 1}/{max_retries - 1}...")
            if failure_reason == "too_long" and previous_draft is not None:
                user_msg = (
                    f"{base_user_msg}\n\n"
                    f"Your previous attempt was {len(previous_draft)} characters — "
                    f"that is {len(previous_draft) - _MAX_CHARS} characters too long.\n"
                    f"Previous draft: {previous_draft}\n\n"
                    f"Rewrite it to be strictly under {_MAX_CHARS} characters. "
                    f"Cut words, do not cut meaning."
                )
            else:
                user_msg = (
                    f"{base_user_msg}\n\n"
                    f"Your previous attempt was rejected. Try a different angle — "
                    f"be specific and concrete. Output must be under {_MAX_CHARS} characters."
                )

        try:
            response = client.responses.create(
                model=_MODEL,
                instructions=_SYSTEM_PROMPT,
                input=user_msg,
                max_output_tokens=200,
            )
            raw = response.output_text.strip()
        except Exception as exc:
            print(f"  [ai] API call failed: {exc}")
            return None

        desc = raw.strip('"\'')

        if len(desc) > _MAX_CHARS:
            print(f"  [ai] Too long ({len(desc)} chars) — {desc!r}")
            previous_draft = desc
            failure_reason = "too_long"
            continue

        for pattern in _FILLER_PATTERNS:
            if re.search(pattern, desc, re.IGNORECASE):
                print(f"  [ai] Filler phrase detected — {desc!r}")
                previous_draft = desc
                failure_reason = "filler"
                desc = None
                break

        if desc is None:
            continue

        if desc.lower().strip() in used_descriptions:
            print(f"  [ai] Duplicate within batch — {desc!r}")
            previous_draft = desc
            failure_reason = "duplicate"
            continue

        return desc

    print(f"  [ai] SKIP: all {max_retries} attempt(s) failed")
    return None
