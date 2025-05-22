import os
import glob
import re
import json
from pathlib import Path

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
    match = re.search(r'rule: rules/(.*?)/rule\.md', rule_line)
    if match:
        return match.group(1)
    return None

def build_rule_category_map(categories_root='../../categories', output_file='rule-category-mapping.json'):
    pattern = os.path.join(categories_root, '**', '*.md')
    md_files = glob.glob(pattern, recursive=True)
    md_files = [f for f in md_files if not f.endswith('index.md')]

    rule_map = {}

    for file_path in md_files:
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

        for line in fm_data['index']:
            if 'rule:' in line:
                rule_key = extract_rule_key(line)
                if rule_key:
                    rule_entry = {
                        'categoryUri': category_uri,
                        'categoryTitle': category_title
                    }
                    if rule_key not in rule_map:
                        rule_map[rule_key] = [rule_entry]
                    else:
                        if rule_entry not in rule_map[rule_key]:
                            rule_map[rule_key].append(rule_entry)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(rule_map, f, indent=4, ensure_ascii=False)

    print(f"Successfully generated {output_file}")
    print(f"Total unique rule keys: {len(rule_map)}")

if __name__ == '__main__':
    build_rule_category_map()
