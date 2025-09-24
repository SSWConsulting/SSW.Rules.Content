import os
import glob
import re
import json

def extract_frontmatter(content):
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if match:
        return match.group(1)
    return None

def parse_frontmatter(fm_text):
    lines = fm_text.split('\n')
    data = {}
    index_lines = []
    in_index = False

    for line in lines:
        if line.strip().startswith('index:'):
            in_index = True
            data['index'] = []
            continue
        if in_index:
            if re.match(r'^\s*- ', line):
                index_lines.append(line)
            else:
                in_index = False
        if not in_index:
            if ':' in line:
                key, val = line.split(':', 1)
                data[key.strip()] = val.strip()

    if index_lines:
        data['index'] = index_lines

    return data

def extract_rule_key(rule_line):
    match = re.search(r'rule: public/uploads/rules/(.*?)/rule\.mdx', rule_line)
    if match:
        return match.group(1)
    return None

def get_all_rules_from_history():
    """Get all rule keys from history.json with their metadata"""
    ROOT_DIR = os.path.abspath(os.path.join(__file__, "../../.."))
    history_file = os.path.join(ROOT_DIR, 'history.json')

    try:
        with open(history_file, 'r', encoding='utf-8') as f:
            history_data = json.load(f)
    except Exception as e:
        print(f"Error: Could not read history.json: {e}")
        return {}

    rules_metadata = {}
    for entry in history_data:
        file_path = entry.get('file', '')

        # Check if this is a rule file
        if file_path.startswith('rules/') and '/rule.' in file_path:
            # Extract rule key from path like "rules/rule-name/rule.md"
            path_parts = file_path.split('/')
            if len(path_parts) >= 2:
                rule_key = path_parts[1]  # Get the rule directory name

                is_archived = entry.get('isArchived', None)

                rules_metadata[rule_key] = {
                    'isArchived': is_archived
                }

    return rules_metadata

def build_rule_category_maps(categories_root='categories'):
    output_dir = os.getcwd()
    rule_to_cats_file = os.path.join(output_dir, 'rule-to-categories.json')
    cat_title_map_file = os.path.join(output_dir, 'category-uri-title-map.json')
    orphaned_rules_file = os.path.join(output_dir, 'orphaned_rules.json')

    os.makedirs(output_dir, exist_ok=True)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    categories_path = os.path.join(script_dir, '..', '..', categories_root)
    pattern = os.path.join(categories_path, '**', '*.mdx')
    mdx_files = glob.glob(pattern, recursive=True)

    mdx_files = [f for f in mdx_files if not f.endswith('index.mdx')]

    rule_to_categories = {}
    category_title_map = {}

    for file_path in mdx_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        fm_text = extract_frontmatter(content)
        if not fm_text:
            continue

        fm_data = parse_frontmatter(fm_text)
        if 'index' not in fm_data:
            continue

        category_uri = fm_data.get('uri', '')
        category_title = fm_data.get('title', '')

        if category_uri and category_title:
            category_title_map[category_uri] = category_title

        for line in fm_data['index']:
            if 'rule:' in line:
                rule_key = extract_rule_key(line)
                if rule_key:
                    if rule_key not in rule_to_categories:
                        rule_to_categories[rule_key] = []
                    if category_uri not in rule_to_categories[rule_key]:
                        rule_to_categories[rule_key].append(category_uri)

    with open(rule_to_cats_file, 'w', encoding='utf-8') as f:
        json.dump(rule_to_categories, f, indent=4, ensure_ascii=False)

    with open(cat_title_map_file, 'w', encoding='utf-8') as f:
        json.dump({"categories": category_title_map}, f, indent=4, ensure_ascii=False)

    # Generate orphaned rules file
    history_rules_metadata = get_all_rules_from_history()

    # Also get all rules from filesystem to catch rules not in history.json
    rules_path = os.path.join(script_dir, '..', '..', 'public', 'uploads', 'rules')
    rules_pattern = os.path.join(rules_path, '*', 'rule.mdx')
    rule_files = glob.glob(rules_pattern)
    all_filesystem_rules = set()
    for rule_file in rule_files:
        rule_key = os.path.basename(os.path.dirname(rule_file))
        all_filesystem_rules.add(rule_key)

    orphaned_rules = []

    # Check all rules that exist in filesystem
    for rule_key in all_filesystem_rules:
        # Check if rule is not in categories
        if rule_key not in rule_to_categories or not rule_to_categories[rule_key]:
            # Get metadata from history.json if available
            if rule_key in history_rules_metadata:
                is_archived = history_rules_metadata[rule_key].get('isArchived')

                # Include in orphaned rules only if:
                # - isArchived is false
                # Exclude if isArchived is null or true
                if is_archived == False:
                    orphaned_rules.append(rule_key)
                # Otherwise (isArchived is null or true), exclude it
            else:
                # Rule not in history.json, include it
                orphaned_rules.append(rule_key)

    # Sort orphaned rules for consistency
    orphaned_rules.sort()

    orphaned_data = {
        "orphaned_rules": orphaned_rules,
    }

    with open(orphaned_rules_file, 'w', encoding='utf-8') as f:
        json.dump(orphaned_data, f, indent=4, ensure_ascii=False)

    print(f"Generated {rule_to_cats_file} with {len(rule_to_categories)} rules.")
    print(f"Generated {cat_title_map_file} with {len(category_title_map)} categories.")
    print(f"Generated {orphaned_rules_file} with {len(orphaned_rules)} orphaned rules.")

if __name__ == '__main__':
    build_rule_category_maps()