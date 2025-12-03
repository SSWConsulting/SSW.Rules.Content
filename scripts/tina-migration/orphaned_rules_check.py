#!/usr/bin/env python3
import json
import os
import yaml
import glob
from pathlib import Path

# Get paths relative to script location
script_dir = Path(__file__).parent
project_root = script_dir.parent.parent
rules_dir = project_root / 'public' / 'uploads' / 'rules'
categories_dir = project_root / 'categories'

def extract_uri_from_rule(rule_folder_path):
    """Extract URI from rule.md file and check if it's archived"""
    rule_file = os.path.join(rule_folder_path, 'rule.mdx')
    if not os.path.exists(rule_file):
        return None, True  # No file = skip

    try:
        with open(rule_file, 'r', encoding='utf-8') as f:
            content = f.read()

        if not content.startswith('---'):
            return None, True  # No frontmatter = skip

        parts = content.split('---', 2)
        if len(parts) < 2:
            return None, True  # Invalid frontmatter = skip

        frontmatter_text = parts[1]
        frontmatter = yaml.safe_load(frontmatter_text)

        uri = frontmatter.get('uri')
        # Check for archivedreason (both spellings)
        archived_reason = frontmatter.get('archievedreason') or frontmatter.get('archivedreason')
        is_archived = bool(archived_reason and str(archived_reason).strip())

        return uri, is_archived

    except Exception as e:
        print(f"Error reading {rule_file}: {e}")
        return None, True  # Error = skip

def extract_index_from_category(content):
    """Extract rule file paths from category frontmatter"""
    if not content.startswith('---'):
        return []

    parts = content.split('---', 2)
    if len(parts) < 2:
        return []

    frontmatter_text = parts[1]

    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        index_items = frontmatter.get('index', [])

        rule_paths = []
        if isinstance(index_items, list):
            for item in index_items:
                if item is not None:
                    if isinstance(item, dict) and 'rule' in item:
                        # Extract file path from rule object
                        rule_paths.append(item['rule'])
                    elif isinstance(item, str):
                        # Handle old format if any exist
                        rule_paths.append(item)

        return rule_paths
    except yaml.YAMLError as e:
        print(f"YAML Error: {e}")
        return []

print("Step 1: Finding all non-archived rule files...")
# Get all rule files from rule folders (excluding archived ones)
rule_folders = [d for d in os.listdir(rules_dir) if os.path.isdir(os.path.join(rules_dir, d))]
print(f"Found {len(rule_folders)} rule folders")

rule_files = {}  # folder_name -> file_path mapping
rule_file_paths = set()  # all actual rule file paths (non-archived)
archived_count = 0

for folder in rule_folders:
    folder_path = os.path.join(rules_dir, folder)
    uri, is_archived = extract_uri_from_rule(folder_path)
    rule_file_path = os.path.join(rules_dir, folder, 'rule.mdx')
    # Create relative path from project root for consistent comparison with category files
    relative_path = f"public/uploads/rules/{folder}/rule.mdx"

    if not is_archived and os.path.exists(rule_file_path):
        rule_files[folder] = relative_path
        rule_file_paths.add(relative_path)
    elif is_archived:
        archived_count += 1
    elif not os.path.exists(rule_file_path):
        print(f"No rule.mdx found for folder: {folder}")

print(f"Found {len(rule_file_paths)} valid non-archived rule files")
print(f"Skipped {archived_count} archived rules")

print("\nStep 2: Extracting rule file paths from category files...")
# Get all rule file paths from category files
category_files = glob.glob(str(categories_dir / '**' / '*.mdx'), recursive=True)
category_files = [f for f in category_files if not f.endswith('index.mdx')]

category_rule_paths = set()

for file_path in category_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        rule_paths = extract_index_from_category(content)
        category_rule_paths.update(rule_paths)

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print(f"Found {len(category_rule_paths)} rule file paths referenced in categories")

print("\nStep 3: Finding orphaned non-archived rules...")
# Find orphaned rule files (from non-archived rules only)
orphaned_file_paths = rule_file_paths - category_rule_paths
orphaned_folders = []

# Map back to folder names
for folder, file_path in rule_files.items():
    if file_path in orphaned_file_paths:
        orphaned_folders.append(folder)

print(f"Found {len(orphaned_file_paths)} orphaned non-archived rules")

# Create objects with folderName and filePath, and extract URI for compatibility
orphaned_rules = []
for folder, file_path in rule_files.items():
    if file_path in orphaned_file_paths:
        # Extract URI from the rule file for the output
        folder_path = os.path.join(rules_dir, folder)
        uri, _ = extract_uri_from_rule(folder_path)

        orphaned_rules.append({
            "folderName": folder,
            "uri": uri or folder,  # fallback to folder name if no URI
            "filePath": file_path
        })

# Sort by uri
orphaned_rules.sort(key=lambda x: x['uri'])

# Save results
with open(script_dir / 'orphaned_rules.json', 'w') as f:
    json.dump(orphaned_rules, f, indent=2)

# Show some examples of folder -> file path mapping for verification
print(f"\nSample folder -> file path mappings:")
sample_mappings = list(rule_files.items())[:10]
for folder, file_path in sample_mappings:
    status = "ORPHANED" if file_path in orphaned_file_paths else "categorized"
    print(f"  {folder} -> {file_path} ({status})")

print(f"\nResults saved to:")
print(f"- orphaned_rules.json ({len(orphaned_rules)} rules)")

 