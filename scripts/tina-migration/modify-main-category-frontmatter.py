import os
import re
from pathlib import Path

def modify_main_category_file(categories_root='categories'):
    # Target the root categories/index.mdx file
    file_path = os.path.join(categories_root, 'index.mdx')

    if not os.path.exists(file_path):
        print(f"Main category file not found: {file_path}")
        return

    print(f"Processing: {file_path}")

    # Read the entire file content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into frontmatter and body
    fm_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not fm_match:
        print(f"No frontmatter found in {file_path}, skipping")
        return

    fm_content, body = fm_match.groups()

    # Initialize update flag
    needs_update = False

    # 1. ADD _template FIELD
    if '_template:' not in fm_content:
        # Insert after the opening ---
        fm_content = '_template: main\n' + fm_content
        needs_update = True

    # 2. PROCESS INDEX ITEMS
    if 'index:' in fm_content:
        # Split into lines for precise processing
        lines = fm_content.split('\n')
        new_lines = []
        i = 0

        while i < len(lines):
            line = lines[i]
            new_lines.append(line)

            # When we find the index declaration
            if line.strip() == 'index:':
                i += 1
                # Process all subsequent indented lines
                while i < len(lines) and (lines[i].startswith('  ') or lines[i].startswith('\t') or lines[i].startswith('-')):
                    original_line = lines[i]
                    indent = re.match(r'^[ \t]*', original_line).group()

                    # Handle list items
                    if original_line.lstrip().startswith('-'):
                        item_content = original_line.lstrip()[1:].strip()

                        # Only modify if not already in top_category format
                        if not (item_content.startswith('top_category:') or ':' in item_content):
                            clean_item = item_content.strip("'\"")
                            new_line = f"{indent}- top_category: categories/{clean_item}/index.mdx"
                            new_lines.append(new_line)
                            needs_update = True
                            i += 1
                        else:
                            new_lines.append(original_line)
                            i += 1
                    else:
                        new_lines.append(original_line)
                        i += 1
            else:
                i += 1

        fm_content = '\n'.join(new_lines)

    # Write back if changes were made
    if needs_update:
        new_content = f"---\n{fm_content}\n---\n{body}"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated: {file_path}")

if __name__ == '__main__':
    modify_main_category_file()
    print("Main category file processed!")