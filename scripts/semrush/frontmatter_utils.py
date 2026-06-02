#!/usr/bin/env python3
"""
Read and update frontmatter fields in rule.mdx files.

Strategy: regex-based. Only the target field line(s) are replaced;
everything else is preserved byte-for-byte.
"""

import re


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
    """Always emit a double-quoted YAML scalar — safe for any AI-generated string."""
    escaped = value.replace('\\', '\\\\').replace('"', '\\"')
    return f'"{escaped}"'


if __name__ == "__main__":
    import json
    import sys

    cmd = sys.argv[1] if len(sys.argv) > 1 else ""

    if cmd == "read":
        _file = sys.argv[2]
        _fields = read_frontmatter_fields(_file)
        if _fields is None:
            print(json.dumps({"error": "Could not parse frontmatter"}))
            sys.exit(1)
        print(json.dumps({
            "title": _fields.get("title") or "",
            "seoDescription": _fields.get("seoDescription") or "",
        }))

    elif cmd == "write":
        _file, _field, _value = sys.argv[2], sys.argv[3], sys.argv[4]
        if _field == "seoDescription":
            _ok = update_seo_description(_file, _value)
        elif _field == "title":
            _ok = update_title(_file, _value)
        else:
            print(f"ERROR: unknown field {_field!r}", file=sys.stderr)
            sys.exit(1)
        if _ok:
            print("OK")
        else:
            print("FAIL", file=sys.stderr)
            sys.exit(1)

    else:
        print("Usage: frontmatter_utils.py read <file>", file=sys.stderr)
        print("       frontmatter_utils.py write <file> <field> <value>", file=sys.stderr)
        sys.exit(1)
