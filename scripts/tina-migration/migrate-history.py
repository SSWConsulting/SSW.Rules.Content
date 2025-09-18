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

def should_be_archived_based_on_reason(lines):
    """Check if the rule should be archived based on archivedreason field
    
    New logic:
    - If rule has no archivedreason, add an empty one and set isArchived: false
    - If archivedreason is empty, null, undefined, or "", then isArchived: false
    - If archivedreason has content, then isArchived: true
    """
    content = '\n'.join(lines)
    # Look for archivedreason: followed by actual content on the same line
    reason_match = re.search(r'^archivedreason:\s*(.*)$', content, re.MULTILINE)
    if reason_match:
        reason = reason_match.group(1).strip()
        # Rule should be archived if archivedreason has actual content
        if not reason:  # Empty string after stripping
            return False
        if reason.lower() in ['null', 'undefined', 'none']:
            return False
        if reason == '""':  # Handle explicit empty string quotes
            return False
        return True
    
    # Also check for archivedreason: on its own line followed by content on next line
    # This handles YAML multiline scenarios
    archivedreason_pattern = r'^archivedreason:\s*$'
    archivedreason_match = re.search(archivedreason_pattern, content, re.MULTILINE)
    if archivedreason_match:
        # Find the line after archivedreason:
        lines_list = content.split('\n')
        for i, line in enumerate(lines_list):
            if re.match(archivedreason_pattern, line):
                # Check if there's a next line with content
                if i + 1 < len(lines_list):
                    next_line = lines_list[i + 1].strip()
                    # If next line has content and doesn't start a new field, consider it the reason
                    if next_line and not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*:', next_line):
                        if next_line.lower() in ['null', 'undefined', 'none']:
                            return False
                        if next_line == '""':  # Handle explicit empty string quotes
                            return False
                        return True
                # If archivedreason: is on its own line with no content following, consider it empty
                return False
    
    # If no archivedreason field is found, it will be added as empty, so should not be archived
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
        updates["isArchived"] = "true" if meta.get("isArchived") is True else "false"

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

# After processing all history items, add orphaned fields to rules
print("\nAdding orphaned fields to rules...")
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    add_orphaned_script = os.path.join(script_dir, "add-orphaned-field.py")
    
    if os.path.exists(add_orphaned_script):
        print("Running add-orphaned-field.py...")
        import subprocess
        import sys
        result = subprocess.run([sys.executable, add_orphaned_script], 
                              capture_output=True, text=True, cwd=script_dir)
        
        if result.returncode == 0:
            print("Orphaned fields added successfully!")
            if result.stdout:
                print(result.stdout)
        else:
            print(f"Error adding orphaned fields: {result.stderr}")
    else:
        print(f"Warning: {add_orphaned_script} not found, skipping orphaned field processing")
        
except Exception as e:
    print(f"Error running add-orphaned-field.py: {e}")
