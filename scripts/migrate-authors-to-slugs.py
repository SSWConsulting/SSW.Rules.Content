#!/usr/bin/env python3
"""
Migrate Authors to Slugs

This script migrates existing rule files from the legacy author format
(objects with title/url) to the new slug-based format.

NOTE: This script is designed to run from SSW.Rules.Content repository.

Usage: python scripts/migrate-authors-to-slugs.py [--dry-run] [--verbose]

Options:
    --dry-run   Show what would change without modifying files
    --verbose   Show detailed output for each file

Environment Variables:
    PEOPLE_INDEX_PATH - Path to people-index.json (default: ../SSW.Rules/people-index.json)

Default rules location: ./public/uploads/rules
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path

import yaml

# Parse command line arguments
parser = argparse.ArgumentParser(description="Migrate authors to slug format")
parser.add_argument("--dry-run", action="store_true", help="Show what would change without modifying files")
parser.add_argument("--verbose", action="store_true", help="Show detailed output for each file")
args = parser.parse_args()

DRY_RUN = args.dry_run
VERBOSE = args.verbose

# Statistics
stats = {
    "total_rules": 0,
    "rules_with_authors": 0,
    "rules_migrated": 0,
    "rules_already_migrated": 0,
    "authors_converted": 0,
    "authors_not_mapped": 0,
    "errors": 0,
}

# Track unmapped authors for reporting
unmapped_authors = set()


def load_people_index():
    """Load the people index for slug lookup"""
    custom_path = os.environ.get("PEOPLE_INDEX_PATH")
    
    if custom_path:
        index_path = Path(__file__).parent.parent / custom_path
    else:
        # Default: look in sibling SSW.Rules repo
        index_path = Path(__file__).parent.parent.parent / "SSW.Rules" / "people-index.json"
    
    if not index_path.exists():
        print(f"⚠️  people-index.json not found at: {index_path}")
        print("   Run 'npm run generate:people' in the SSW.Rules repo first.")
        print("   Or set PEOPLE_INDEX_PATH environment variable to override.")
        print("   Continuing without slug validation...\n")
        return None
    
    with open(index_path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_slug_from_url(url):
    """Extract slug from a legacy author URL"""
    if not url:
        return None
    
    # SSW People URL: https://ssw.com.au/people/bob-northwind
    if "ssw.com.au/people/" in url:
        match = re.search(r"people/([^/?#]+)", url)
        return match.group(1).lower() if match else None
    
    # GitHub URL: https://github.com/username
    if "github.com/" in url:
        parts = url.split("github.com/")
        if len(parts) > 1:
            username = parts[1].split("/")[0]
            return f"gh-{username.lower()}" if username else None
    
    return None


def convert_author_to_slug(author, people_index):
    """Convert a legacy author object to a slug"""
    global stats
    
    if isinstance(author, str):
        # Already a slug
        return {"slug": author, "was_converted": False}
    
    if not isinstance(author, dict):
        return {"slug": None, "was_converted": False}
    
    url_slug = extract_slug_from_url(author.get("url"))
    
    if url_slug:
        # Validate against people index if available
        if people_index and url_slug not in people_index and not url_slug.startswith("gh-"):
            unmapped_authors.add(f"{author.get('title', 'Unknown')} ({author.get('url')})")
            stats["authors_not_mapped"] += 1
        stats["authors_converted"] += 1
        return {"slug": url_slug, "was_converted": True}
    
    # Can't extract slug - try to derive from title
    title = author.get("title")
    if title:
        # Convert title to slug
        derived_slug = title.lower()
        derived_slug = re.sub(r"[''']", "", derived_slug)
        derived_slug = re.sub(r"[^a-z0-9]+", "-", derived_slug)
        derived_slug = derived_slug.strip("-")
        
        if derived_slug:
            unmapped_authors.add(f"{title} (no URL, derived slug: {derived_slug})")
            stats["authors_not_mapped"] += 1
            stats["authors_converted"] += 1
            return {"slug": derived_slug, "was_converted": True}
    
    # Can't convert
    unmapped_authors.add(f"{author.get('title', 'Unknown')} ({author.get('url', 'no URL')})")
    stats["authors_not_mapped"] += 1
    return {"slug": None, "was_converted": False}


def is_already_migrated(authors):
    """Check if authors are already in the new object format [{ author: "slug" }]"""
    if not authors or not isinstance(authors, list) or len(authors) == 0:
        return False
    # Check if all items are objects with an "author" key
    return all(isinstance(a, dict) and "author" in a for a in authors)


def parse_frontmatter(content):
    """Parse YAML frontmatter from MDX content"""
    if not content.startswith("---"):
        return None, content
    
    # Find the closing ---
    end_match = re.search(r"\n---\s*\n", content[3:])
    if not end_match:
        return None, content
    
    end_pos = end_match.start() + 3
    frontmatter_str = content[4:end_pos]
    body = content[end_pos + end_match.end() - end_match.start():]
    
    try:
        frontmatter = yaml.safe_load(frontmatter_str)
        return frontmatter, body
    except yaml.YAMLError as e:
        print(f"     YAML parse error: {e}")
        return None, content


def stringify_frontmatter(frontmatter):
    """Convert frontmatter dict back to YAML string"""
    return yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)


def migrate_rule_file(file_path, people_index):
    """Migrate a single rule file"""
    global stats
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        frontmatter, body = parse_frontmatter(content)
        stats["total_rules"] += 1
        
        if frontmatter is None:
            if VERBOSE:
                print(f"  ⏭️  {file_path.parent.name}: No frontmatter")
            return False
        
        authors = frontmatter.get("authors")
        if not authors or not isinstance(authors, list) or len(authors) == 0:
            if VERBOSE:
                print(f"  ⏭️  {file_path.parent.name}: No authors")
            return False
        
        stats["rules_with_authors"] += 1
        
        if is_already_migrated(authors):
            stats["rules_already_migrated"] += 1
            if VERBOSE:
                print(f"  ✅ {file_path.parent.name}: Already migrated")
            return False
        
        # Convert authors to slugs
        slug_results = [convert_author_to_slug(a, people_index) for a in authors]
        slug_results = [r for r in slug_results if r["slug"] is not None]
        
        if len(slug_results) == 0:
            if VERBOSE:
                print(f"  ⚠️  {file_path.parent.name}: Could not convert any authors")
            return False
        
        # Create new format: [{ author: "slug" }, ...]
        new_authors = [{"author": r["slug"]} for r in slug_results]
        slug_list = [r["slug"] for r in slug_results]
        
        # Update frontmatter
        frontmatter["authors"] = new_authors
        
        # Reconstruct file content
        new_frontmatter_str = stringify_frontmatter(frontmatter)
        new_content = f"---\n{new_frontmatter_str}---\n{body}"
        
        if DRY_RUN:
            print(f"  📝 {file_path.parent.name}: Would migrate {len(authors)} authors → [{', '.join(slug_list)}]")
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            if VERBOSE:
                print(f"  ✏️  {file_path.parent.name}: Migrated {len(authors)} authors → [{', '.join(slug_list)}]")
        
        stats["rules_migrated"] += 1
        return True
        
    except Exception as e:
        print(f"  ❌ Error processing {file_path}: {e}")
        stats["errors"] += 1
        return False


def find_rule_files(rules_dir):
    """Find all rule.mdx files in the content directory"""
    files = []
    for root, dirs, filenames in os.walk(rules_dir):
        for filename in filenames:
            if filename in ("rule.mdx", "rule.md"):
                files.append(Path(root) / filename)
    return files


def migrate():
    """Main migration function"""
    print("🚀 Author Migration Script")
    print("==========================")
    print(f"   Mode: {'DRY RUN (no changes will be made)' if DRY_RUN else 'LIVE'}")
    print(f"   Verbose: {'Yes' if VERBOSE else 'No'}")
    print("")
    
    # Determine rules directory
    rules_dir = Path(__file__).parent.parent / "public" / "uploads" / "rules"
    
    if not rules_dir.exists():
        print(f"❌ Rules directory not found: {rules_dir}")
        print("   Make sure you're running this script from the SSW.Rules.Content repository.")
        sys.exit(1)
    
    print(f"📁 Rules directory: {rules_dir}")
    
    # Load people index for validation
    people_index = load_people_index()
    if people_index:
        print(f"👥 People index loaded: {len(people_index)} people")
    print("")
    
    # Find all rule files
    print("🔍 Scanning for rule files...")
    rule_files = find_rule_files(rules_dir)
    print(f"   Found {len(rule_files)} rule files\n")
    
    # Migrate each file
    print("📝 Processing rules...")
    for file_path in rule_files:
        migrate_rule_file(file_path, people_index)
    
    # Print summary
    print("\n" + "=" * 50)
    print("📊 Migration Summary")
    print("=" * 50)
    print(f"   Total rules scanned:    {stats['total_rules']}")
    print(f"   Rules with authors:     {stats['rules_with_authors']}")
    print(f"   Already migrated:       {stats['rules_already_migrated']}")
    print(f"   {'Would migrate' if DRY_RUN else 'Migrated'}:          {stats['rules_migrated']}")
    print(f"   Authors converted:      {stats['authors_converted']}")
    print(f"   Authors not in index:   {stats['authors_not_mapped']}")
    print(f"   Errors:                 {stats['errors']}")
    
    if unmapped_authors:
        print("\n⚠️  Authors not found in people index:")
        for author in sorted(unmapped_authors):
            print(f"   - {author}")
        print("\n   These authors may need to be added to the People repository,")
        print("   or their URLs may be incorrect in the rule files.")
    
    if DRY_RUN:
        print("\n📌 This was a DRY RUN. No files were modified.")
        print("   Run without --dry-run to apply changes.")
    else:
        print("\n✅ Migration complete!")


if __name__ == "__main__":
    migrate()
