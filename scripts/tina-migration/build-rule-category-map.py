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

def build_rule_category_maps(categories_root='categories'):
    output_dir = os.getcwd()
    rule_to_cats_file = os.path.join(output_dir, 'rule-to-categories.json')
    cat_title_map_file = os.path.join(output_dir, 'category-uri-title-map.json')

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

    print(f"Generated {rule_to_cats_file} with {len(rule_to_categories)} rules.")
    print(f"Generated {cat_title_map_file} with {len(category_title_map)} categories.")

if __name__ == '__main__':
    build_rule_category_maps()