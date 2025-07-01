import os
import glob
import re
from pathlib import Path

def modify_category_files(categories_root='categories'):
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
            i = index_pos
            while i < len(new_fm_lines):
                line = new_fm_lines[i]
                if i == index_pos:  # The 'index:' line
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
                        needs_update = True
                    else:
                        new_index_lines.append(line)
                    i += 1
                else:
                    break
            
            # Replace the index section if we made changes
            if needs_update:
                new_fm_lines = new_fm_lines[:index_pos] + new_index_lines + new_fm_lines[i:]
        
        # Only write back if changes were made
        if needs_update:
            new_fm_content = '\n'.join(new_fm_lines)
            new_content = f"---\n{new_fm_content}\n---\n{body}"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            new_file_path = Path(file_path).with_suffix('.mdx')
            os.rename(file_path, new_file_path)
            print(f"Successfully updated: {file_path}\n")
        else:
            print(f"No changes needed for: {file_path}\n")

if __name__ == '__main__':
    modify_category_files()
    print("All category files processed!")