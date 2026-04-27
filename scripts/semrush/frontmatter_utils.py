#!/usr/bin/env python3
"""
Read and update frontmatter fields in rule.mdx files.

Strategy: regex-based. Only the target field line(s) are replaced;
everything else is preserved byte-for-byte.
"""

import re


# Characters that require a YAML scalar to be double-quoted to avoid parse errors.
# Colon-space (": ") is the most common culprit in English meta descriptions.
_NEEDS_QUOTING_RE = re.compile(r'(?:: )|(?:^[{[\|>&!%@`*?#])')


def read_frontmatter_fields(file_path: str) -> dict | None:
    """
    Parse title, seoDescription, and raw content from an MDX file.

    Returns a dict on success:
        {
            "title": str | None,
            "seoDescription": str | None,
            "_content": str,      # full file content, used for AI excerpt
        }
    Returns None if the file cannot be read or has no frontmatter block.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except OSError as exc:
        print(f"  [fix] Cannot read file: {exc}")
        return None

    fm_match = re.match(r"^---([\s\S]*?)---", content)
    if not fm_match:
        print(f"  [fix] No frontmatter block found in: {file_path}")
        return None

    fm = fm_match.group(1)
    return {
        "title": _extract_scalar(fm, "title"),
        "seoDescription": _extract_scalar(fm, "seoDescription"),
        "_content": content,
    }


def update_seo_description(file_path: str, new_desc: str) -> bool:
    """
    Replace the seoDescription value in the file's frontmatter.

    Writes in-place. Only the seoDescription line is changed.
    Returns True on success, False on any failure.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except OSError as exc:
        print(f"  [fix] Cannot read file: {exc}")
        return False

    # Locate frontmatter block
    fm_match = re.match(r"^(---[\s\S]*?---)", content)
    if not fm_match:
        print(f"  [fix] No frontmatter block found in: {file_path}")
        return False

    fm_block = fm_match.group(1)
    safe_value = _yaml_scalar(new_desc)
    new_fm_block, n = re.subn(
        r"^seoDescription:[ \t]*.*(?:\n[ \t]+.*)*",
        f"seoDescription: {safe_value}",
        fm_block,
        flags=re.MULTILINE,
    )

    if n == 0:
        print(f"  [fix] seoDescription field not found in frontmatter: {file_path}")
        return False

    new_content = content.replace(fm_block, new_fm_block, 1)

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
    except OSError as exc:
        print(f"  [fix] Cannot write file: {exc}")
        return False

    return True


def update_title(file_path: str, new_title: str) -> bool:
    """
    Replace the title value in the file's frontmatter.

    Writes in-place. Only the title line is changed.
    Returns True on success, False on any failure.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except OSError as exc:
        print(f"  [fix] Cannot read file: {exc}")
        return False

    fm_match = re.match(r"^(---[\s\S]*?---)", content)
    if not fm_match:
        print(f"  [fix] No frontmatter block found in: {file_path}")
        return False

    fm_block = fm_match.group(1)
    safe_value = _yaml_scalar(new_title)
    new_fm_block, n = re.subn(
        r"^title:[ \t]*.*(?:\n[ \t]+.*)*",
        f"title: {safe_value}",
        fm_block,
        flags=re.MULTILINE,
    )

    if n == 0:
        print(f"  [fix] title field not found in frontmatter: {file_path}")
        return False

    new_content = content.replace(fm_block, new_fm_block, 1)

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
    except OSError as exc:
        print(f"  [fix] Cannot write file: {exc}")
        return False

    return True


# ── Helpers ──────────────────────────────────────────────────────────────────

def _extract_scalar(frontmatter: str, field: str) -> str | None:
    """Extract a plain scalar YAML field value, including indented continuation lines."""
    m = re.search(
        rf"^{re.escape(field)}:\s*(.*(?:\n[ \t]+.*)*)",
        frontmatter,
        re.MULTILINE,
    )
    if not m:
        return None
    # Join continuation lines into a single string
    value = " ".join(part.strip() for part in m.group(1).splitlines()).strip()
    # Strip matching surrounding quotes
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
        value = value[1:-1]
    return value or None


def _yaml_scalar(value: str) -> str:
    """
    Return a YAML-safe representation of a string scalar.
    Wraps in double quotes only when the value contains characters
    that would break bare YAML parsing.
    """
    if _NEEDS_QUOTING_RE.search(value):
        escaped = value.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{escaped}"'
    return value
