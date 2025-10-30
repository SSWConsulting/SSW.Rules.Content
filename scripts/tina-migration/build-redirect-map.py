#!/usr/bin/env python3
"""
Build redirect mapping from MDX frontmatter.

This script extracts 'uri' and 'redirects' fields from rule and category MDX files
and creates redirects.json, an inverted mapping file (old URIs -> current URIs) for use in redirects.
"""

import os
import re
import json
import glob


def extract_frontmatter(content):
    """Extract frontmatter text from MDX content."""
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if match:
        return match.group(1)
    return None


def parse_frontmatter_field(fm_text, field_name):
    """Parse a specific field from frontmatter text."""
    # First check for multi-line array field (starts with field_name:, followed by lines starting with "  - ")
    array_match = re.search(
        rf'^{field_name}:\s*$\n((?:  - .+$\n?)+)',
        fm_text,
        re.MULTILINE
    )
    if array_match:
        items = []
        for line in array_match.group(1).split('\n'):
            line_stripped = line.strip()
            if line_stripped.startswith('- '):
                # Remove the leading "- " and any surrounding whitespace
                items.append(line_stripped[2:].strip())
        return items if items else None

    # Check if field exists but has no value on the same line (e.g., "redirects:" followed by newline)
    # This must be checked BEFORE the single-line match to avoid matching the next line's content
    empty_match = re.search(rf'^{field_name}:\s*$', fm_text, re.MULTILINE)
    if empty_match:
        return None

    # Match single-line field (including empty array [] or null)
    # Only match content that's actually on the same line (no newlines)
    single_match = re.search(rf'^{field_name}:\s*([^\n]+)$', fm_text, re.MULTILINE)
    if single_match:
        value = single_match.group(1).strip()
        # Check for empty array or null values
        if value in ['[]', 'null', '']:
            return None
        return value

    return None


def process_mdx_file(file_path):
    """
    Process a single MDX file and extract uri and redirects.

    Returns:
        tuple: (uri, redirects_list) or (None, None) on error
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        fm_text = extract_frontmatter(content)
        if not fm_text:
            return None, None

        uri = parse_frontmatter_field(fm_text, 'uri')
        redirects = parse_frontmatter_field(fm_text, 'redirects')

        # Ensure redirects is a list or None
        if redirects and not isinstance(redirects, list):
            redirects = [redirects]

        return uri, redirects

    except Exception as e:
        print(f"WARNING: Error reading {file_path}: {e}")
        return None, None


def build_redirect_map():
    """Main function to build the redirect mapping."""
    # Resolve paths relative to script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.join(script_dir, '..', '..')

    rules_path = os.path.join(repo_root, 'public', 'uploads', 'rules')
    categories_path = os.path.join(repo_root, 'categories')
    output_file = os.path.join(script_dir, 'redirects.json')

    # Find all MDX files
    rule_files = glob.glob(os.path.join(rules_path, '*', 'rule.mdx'), recursive=False)
    category_files = glob.glob(os.path.join(categories_path, '**', '*.mdx'), recursive=True)

    all_files = rule_files + category_files

    print(f"Found {len(rule_files)} rule files and {len(category_files)} category files")
    print("Processing files...\n")

    # Track all existing URIs and build redirect map
    existing_uris = set()
    redirect_map = {}  # old_uri -> current_uri
    redirect_sources = {}  # old_uri -> file_path (for conflict detection)

    # First pass: collect all existing URIs
    for file_path in all_files:
        uri, _ = process_mdx_file(file_path)
        if uri:
            existing_uris.add(uri)

    # Second pass: build redirect mapping
    conflict_count = 0
    redirect_count = 0

    for file_path in all_files:
        uri, redirects = process_mdx_file(file_path)

        # Skip if no URI or no redirects (including empty arrays)
        if not uri or not redirects or len(redirects) == 0:
            continue

        for old_uri in redirects:
            # Type 1 Conflict: Redirect URI conflicts with existing URI
            if old_uri in existing_uris:
                conflict_count += 1
                print(f"WARNING: REDIRECT CONFLICT: Cannot redirect '{old_uri}' -> '{uri}'")
                print(f"    '{old_uri}' already exists as a rule URI")
                print(f"    Skipping this redirect.\n")
                continue

            # Type 2 Conflict: Multiple rules claim same redirect
            if old_uri in redirect_map:
                conflict_count += 1
                print(f"WARNING: REDIRECT CONFLICT: Multiple rules claim redirect '{old_uri}':")
                print(f"    - '{redirect_map[old_uri]}' (in {redirect_sources[old_uri]})")
                print(f"    - '{uri}' (in {file_path})")
                print(f"    Using first occurrence: '{redirect_map[old_uri]}'")
                print(f"    Skipping subsequent claims.\n")
                continue

            # No conflicts - add to map
            redirect_map[old_uri] = uri
            redirect_sources[old_uri] = file_path
            redirect_count += 1

    # Write output file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(redirect_map, f, indent=4, ensure_ascii=False)

    # Print summary
    print("=" * 60)
    print(f"SUCCESS: Generated {output_file}")
    print(f"SUCCESS: Created {redirect_count} redirect mappings")
    if conflict_count > 0:
        print(f"WARNING: Found {conflict_count} conflicts (skipped)")
    print("=" * 60)


if __name__ == '__main__':
    build_redirect_map()
