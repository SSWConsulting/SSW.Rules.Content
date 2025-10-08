import os
import glob
import re
import json
from pathlib import Path

# ----------------------------- #
# Regex patterns
# ----------------------------- #

YOUTUBE_BLOCK_REGEX = r'`youtube:\s*(https?://[^\s]+)`'

# ----------------------------- #
# Utilities
# ----------------------------- #

def js_string(text: str) -> str:
    return json.dumps(text, ensure_ascii=False)

def replace_youtube_block(m):
    url = m.group(1).strip()
    return f'<youtubeEmbed url="{url}" description={{""}} />'

def modify_category_files(categories_root=None):
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    # Go up two levels to get to the project root (from scripts/tina-migration/ to project root)
    project_root = script_dir.parent.parent

    # Default categories_root to the categories folder in the project root
    if categories_root is None:
        categories_root = project_root / 'categories'
    else:
        # If provided, make it relative to project root
        categories_root = project_root / categories_root
    # Find all *.md files in subfolders of categories except index.md
    pattern = os.path.join(categories_root, '**', '*.md')
    md_files = glob.glob(pattern, recursive=True)
    md_files = [f for f in md_files if not f.endswith('index.md')]
    
    for file_path in md_files:
        print(f"Processing: {file_path}")
        
        # Read the entire file content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split into frontmatter and body
        fm_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
        if not fm_match:
            print(f"No frontmatter found in {file_path}, skipping")
            continue
            
        fm_content, body = fm_match.groups()
        
        # Check if this is a category file
        if 'type: category' not in fm_content:
            print(f"Skipping (not a category file): {file_path}")
            continue
        
        # Track if we need to update the file
        needs_update = False
        new_fm_lines = fm_content.split('\n')
        
        # Add _template if missing (insert after first line)
        if not any(line.startswith('_template:') for line in new_fm_lines):
            new_fm_lines.insert(0, '_template: category')
            needs_update = True
        
        # Process index field if it exists
        index_pos = None
        for i, line in enumerate(new_fm_lines):
            if line.startswith('index:'):
                index_pos = i
                break
        
        if index_pos is not None:
            # Process index items
            new_index_lines = []
            index_modified = False
            i = index_pos
            while i < len(new_fm_lines):
                line = new_fm_lines[i]
                if i == index_pos:  # The 'index:' line
                    new_index_lines.append(line)
                    i += 1
                    continue

                # Check if this is an empty line
                if line.strip() == '':
                    # Skip empty lines and continue
                    new_index_lines.append(line)
                    i += 1
                    continue

                # Check if this is a comment line
                if re.match(r'^\s*#', line):
                    # Skip comment lines and continue
                    new_index_lines.append(line)
                    i += 1
                    continue

                # Check if this is an index item
                if re.match(r'^\s*-', line):
                    item = line.strip()[2:]  # Remove '- '
                    if not (item.startswith('rule:') or ':' in item):
                        # Convert to new format
                        indent = re.match(r'^\s*', line).group()
                        clean_item = item.replace('.md', '').strip("'\"")
                        new_line = f"{indent}- rule: public/uploads/rules/{clean_item}/rule.mdx"
                        new_index_lines.append(new_line)
                        index_modified = True
                        needs_update = True
                    else:
                        new_index_lines.append(line)
                    i += 1
                else:
                    break

            # Replace the index section if we made changes to the index
            if index_modified:
                new_fm_lines = new_fm_lines[:index_pos] + new_index_lines + new_fm_lines[i:]
                needs_update = True
        
        # Process body content to convert YouTube embeds
        original_body = body
        body = re.sub(YOUTUBE_BLOCK_REGEX, replace_youtube_block, body, flags=re.MULTILINE)

        # Check if body was modified
        if body != original_body:
            needs_update = True

        # Write back if changes were made
        if needs_update:
            new_fm_content = '\n'.join(new_fm_lines)
            new_content = f"---\n{new_fm_content}\n---\n{body}"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Successfully updated: {file_path}")

        # Always rename .md to .mdx (even if no content changes)
        new_file_path = Path(file_path).with_suffix('.mdx')
        if file_path.endswith('.md'):
            # Delete existing .mdx file if it exists
            if new_file_path.exists():
                new_file_path.unlink()

            os.rename(file_path, new_file_path)
            print(f"Renamed to: {new_file_path}\n")
        else:
            print(f"Already .mdx: {file_path}\n")

if __name__ == '__main__':
    modify_category_files()
    print("All category files processed!")