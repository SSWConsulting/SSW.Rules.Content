import os
import json
import re
from datetime import datetime, timezone

# Resolve root from script location
ROOT_DIR = os.path.abspath(os.path.join(__file__, "../../.."))
HISTORY_PATH = os.path.join(ROOT_DIR, "history.json")

def to_utc(date_str):
    dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    return dt.astimezone(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")

def to_mdx_path(md_path):
    if not md_path.endswith(".md"):
        return None
    if md_path.startswith("rules/"):
        md_path = md_path.replace("rules/", "public/uploads/rules/")
    return os.path.join(ROOT_DIR, md_path.replace(".md", ".mdx"))

def patch_frontmatter_lines(lines, updates):
    start, end = None, None
    for i, line in enumerate(lines):
        if line.strip() == "---":
            if start is None:
                start = i
            else:
                end = i
                break
    if start is None or end is None:
        return lines  # no frontmatter found

    frontmatter = lines[start + 1:end]
    keys = list(updates.keys())

    patched = []
    seen = set()
    for line in frontmatter:
        key = line.split(":", 1)[0].strip()
        if key in updates:
            patched.append(f"{key}: {updates[key]}")
            seen.add(key)
        else:
            patched.append(line)

    for key in keys:
        if key not in seen:
            patched.append(f"{key}: {updates[key]}")

    return lines[:start + 1] + patched + lines[end:]

def has_meaningful_archive_reason(lines):
    """Check if the file has a meaningful archivedreason"""
    content = '\n'.join(lines)
    reason_match = re.search(r'^archivedreason:\s*(.+)', content, re.MULTILINE)
    if reason_match:
        reason = reason_match.group(1).strip()
        # Consider meaningful if not null, empty, or just whitespace
        return reason and reason.lower() not in ['null', '', 'none'] and len(reason.strip()) > 0
    return False

def update_file(filepath, meta):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    updates = {
        "lastUpdated": to_utc(meta["lastUpdated"]),
        "lastUpdatedBy": meta["lastUpdatedBy"],
        "lastUpdatedByEmail": meta["lastUpdatedByEmail"],
        "created": to_utc(meta["created"]),
        "createdBy": meta["createdBy"],
        "createdByEmail": meta["createdByEmail"],
    }
    
    if "public/uploads/rules/" in filepath:
        # Check if rule should be archived based on:
        # 1. History data has isArchived: true, OR
        # 2. File has meaningful archivedreason content
        should_be_archived = meta.get("isArchived") is True or has_meaningful_archive_reason(lines)
        updates["isArchived"] = "true" if should_be_archived else "false"

    new_lines = patch_frontmatter_lines(lines, updates)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines) + "\n")

# Main
with open(HISTORY_PATH, "r", encoding="utf-8") as f:
    history = json.load(f)

for item in history:
    mdx_path = to_mdx_path(item["file"])
    if not mdx_path or not os.path.isfile(mdx_path):
        continue
    try:
        update_file(mdx_path, item)
    except Exception as e:
        print(f"Error: {mdx_path} - {e}")
