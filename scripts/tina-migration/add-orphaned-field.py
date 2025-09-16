import os
import glob
import re
import json
from pathlib import Path

def extract_frontmatter(content):
    """Extract frontmatter from markdown content"""
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return None, content

def extract_rule_uri_from_path(rule_path):
    """Extract rule URI from file path: public/uploads/rules/rule-name/rule.mdx -> rule-name"""
    path_parts = Path(rule_path).parts
    if 'rules' in path_parts:
        rules_index = path_parts.index('rules')
        if rules_index + 1 < len(path_parts):
            return path_parts[rules_index + 1]
    return None

def is_rule_archived(frontmatter):
    """Check if a rule is archived based on its frontmatter"""
    # Primary check: isArchived field (should be correctly set by migrate-history.py)
    archived_match = re.search(r'^isArchived:\s*(true|false)', frontmatter, re.MULTILINE)
    if archived_match and archived_match.group(1).lower() == 'true':
        return True
    
    # Fallback: check archivedreason directly (in case migrate-history.py wasn't run yet)
    # Look for archivedreason: followed by actual content on the same line
    reason_match = re.search(r'^archivedreason:\s*(.+)$', frontmatter, re.MULTILINE)
    if reason_match:
        reason = reason_match.group(1).strip()
        # Consider archived only if reason has meaningful content
        if not reason:  # Empty string after stripping
            return False
        if reason.lower() in ['null', 'undefined', 'none']:
            return False
        return True
    
    # Also check for archivedreason: on its own line followed by content on next line
    archivedreason_pattern = r'^archivedreason:\s*$'
    archivedreason_match = re.search(archivedreason_pattern, frontmatter, re.MULTILINE)
    if archivedreason_match:
        # Find the line after archivedreason:
        lines_list = frontmatter.split('\n')
        for i, line in enumerate(lines_list):
            if re.match(archivedreason_pattern, line):
                # Check if there's a next line with content
                if i + 1 < len(lines_list):
                    next_line = lines_list[i + 1].strip()
                    # If next line has content and doesn't start a new field, consider it the reason
                    if next_line and not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*:', next_line):
                        if next_line.lower() not in ['null', 'undefined', 'none']:
                            return True
                break
    
    return False

def add_orphaned_field_to_rules(categories_root='categories'):
    """Add isOrphaned field to rules that are not in categories AND not archived"""
    
    # Get script directory and project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.join(script_dir, '..', '..')
    
    # Path to rule-to-categories.json mapping
    rule_to_cats_file = os.path.join(script_dir, 'rule-to-categories.json')
    
    if not os.path.exists(rule_to_cats_file):
        print(f"Error: {rule_to_cats_file} not found. Please run build-rule-category-map.py first.")
        return
    
    print(f"Reading rule-to-categories mapping from {rule_to_cats_file}")
    
    # Load existing rule-to-categories mapping
    with open(rule_to_cats_file, 'r', encoding='utf-8') as f:
        rule_to_categories = json.load(f)
    
    referenced_rules = set(rule_to_categories.keys())
    print(f"Found {len(referenced_rules)} rules referenced in categories")
    
    # Find all rule files
    rules_pattern = os.path.join(project_root, 'public', 'uploads', 'rules', '*', 'rule.mdx')
    rule_files = glob.glob(rules_pattern, recursive=False)
    
    print(f"Found {len(rule_files)} total rule files")
    
    # Statistics
    orphaned_count = 0
    referenced_count = 0
    archived_count = 0
    updated_count = 0
    
    for rule_file in rule_files:
        try:
            # Extract rule URI from path
            rule_uri = extract_rule_uri_from_path(rule_file)
            if not rule_uri:
                print(f"Warning: Could not extract rule URI from {rule_file}")
                continue
            
            # Read file content
            with open(rule_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract frontmatter
            frontmatter, body = extract_frontmatter(content)
            if not frontmatter:
                print(f"Warning: No frontmatter found in {rule_file}")
                continue
            
            # Check if rule file has the correct type
            if 'type: rule' not in frontmatter:
                print(f"Warning: Not a rule file (missing 'type: rule'): {rule_file}")
                continue
            
            # Check if rule is archived
            rule_is_archived = is_rule_archived(frontmatter)
            
            # Determine if rule is orphaned:
            # - Not referenced in any category AND
            # - Not archived
            in_category = rule_uri in referenced_rules
            is_orphaned = not in_category and not rule_is_archived
            
            # Check if isOrphaned field already exists
            has_orphaned_field = re.search(r'^isOrphaned:\s*(?:true|false)', frontmatter, re.MULTILINE)
            
            # Process frontmatter lines
            fm_lines = frontmatter.split('\n')
            new_fm_lines = []
            orphaned_field_added = False
            
            for line in fm_lines:
                if line.startswith('isOrphaned:'):
                    # Update existing field
                    new_fm_lines.append(f"isOrphaned: {str(is_orphaned).lower()}")
                    orphaned_field_added = True
                    updated_count += 1
                else:
                    new_fm_lines.append(line)
            
            # Add isOrphaned field if it doesn't exist
            if not orphaned_field_added:
                # Insert after type: rule line
                for i, line in enumerate(new_fm_lines):
                    if line.startswith('type: rule'):
                        new_fm_lines.insert(i + 1, f"isOrphaned: {str(is_orphaned).lower()}")
                        orphaned_field_added = True
                        updated_count += 1
                        break
                
                # If type: rule not found, add at the beginning
                if not orphaned_field_added:
                    new_fm_lines.insert(0, f"isOrphaned: {str(is_orphaned).lower()}")
                    updated_count += 1
            
            # Update statistics
            if rule_is_archived:
                archived_count += 1
            elif in_category:
                referenced_count += 1
            else:
                # Not in category and not archived = orphaned
                orphaned_count += 1
            
            # Write back only if we made changes or it's the first time
            if not has_orphaned_field or orphaned_field_added:
                new_frontmatter = '\n'.join(new_fm_lines)
                new_content = f"---\n{new_frontmatter}\n---\n{body}"
                
                with open(rule_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
        
        except Exception as e:
            print(f"Error processing {rule_file}: {str(e)}")
            continue
    
    print(f"\nSummary:")
    print(f"  • Total rules processed: {len(rule_files)}")
    print(f"  • Referenced in categories: {referenced_count}")
    print(f"  • Archived rules: {archived_count}")
    print(f"  • Orphaned rules (not in categories & not archived): {orphaned_count}")
    print(f"  • Rules updated with isOrphaned field: {updated_count}")
    
    print(f"\nSuccessfully added isOrphaned field to all rules!")
    print(f"Logic: A rule is orphaned only if it's NOT in any category AND NOT archived")

if __name__ == '__main__':
    add_orphaned_field_to_rules()