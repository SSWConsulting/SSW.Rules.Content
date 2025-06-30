import os
import glob
import re
from pathlib import Path

def modify_markdown_files(categories_root='categories'):
    # Find all index.md files in subfolders of categories
    pattern = os.path.join(categories_root, '**', 'index.md')
    md_files = glob.glob(pattern, recursive=True)
    
    # Get the absolute path of the root index.md to exclude it
    root_index_path = os.path.abspath(os.path.join(categories_root, 'index.md'))
    
    for file_path in md_files:
        # Skip the root categories/index.md file
        if os.path.abspath(file_path) == root_index_path:
            print(f"Skipping root index file: {file_path}")
            continue
            
        print(f"Processing: {file_path}")
        
        # Get the subfolder name (category name)
        subfolder = os.path.basename(os.path.dirname(file_path))
        
        # Read the entire file content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split into frontmatter and body
        fm_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
        if not fm_match:
            print(f"No frontmatter found in {file_path}, skipping")
            continue
            
        fm_content, body = fm_match.groups()
        
        # Initialize update flag
        needs_update = False
        
        # 1. ADD _template FIELD
        if '_template:' not in fm_content:
            # Insert after the opening ---
            fm_content = '_template: top_category\n' + fm_content
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
                            
                            # Only modify if not already in category format
                            if not (item_content.startswith('category:') or ':' in item_content):
                                clean_item = item_content.replace('.md', '').strip("'\"")
                                new_line = f"{indent}- category: categories/{subfolder}/{clean_item}.mdx"
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
        
        # Only write back if changes were made
        if needs_update:
            new_content = f"---\n{fm_content}\n---\n{body}"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            new_file_path = Path(file_path).with_suffix('.mdx')
            os.rename(file_path, new_file_path)
            print(f"Successfully updated: {file_path}")
            print("Changes made:")
            print(f"1. Added _template: top_category")
            print(f"2. Updated index items to new format")
        else:
            print(f"No changes needed for: {file_path}")

if __name__ == '__main__':
    modify_markdown_files()
    print("All files processed!")