#!/usr/bin/env python3
import os
import sys
import yaml
from datetime import date, datetime
from pathlib import Path
from algoliasearch.search_client import SearchClient

script_dir = Path(__file__).parent
project_root = script_dir.parent.parent
rules_dir = project_root / 'public' / 'uploads' / 'rules'

APP_ID = os.environ.get('NEXT_PUBLIC_ALGOLIA_APP_ID')
ADMIN_KEY = os.environ.get('NEXT_PUBLIC_ALGOLIA_ADMIN_KEY')
INDEX_NAME = os.environ.get('NEXT_PUBLIC_ALGOLIA_INDEX_NAME', 'index-json')

if not APP_ID or not ADMIN_KEY:
    print('Skipping Algolia sync: NEXT_PUBLIC_ALGOLIA_APP_ID or NEXT_PUBLIC_ALGOLIA_ADMIN_KEY not set')
    sys.exit(0)

def normalize(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    if isinstance(obj, dict):
        return {k: normalize(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [normalize(v) for v in obj]
    return obj

def parse_rule(folder_path):
    rule_file = folder_path / 'rule.mdx'
    if not rule_file.exists():
        return None
    try:
        content = rule_file.read_text(encoding='utf-8')
        if not content.startswith('---'):
            return None
        parts = content.split('---', 2)
        if len(parts) < 3:
            return None
        frontmatter = normalize(yaml.safe_load(parts[1]))
        if not frontmatter.get('uri'):
            return None
        slug = frontmatter['uri']
        return {**frontmatter, 'objectID': slug, 'slug': slug}
    except Exception as e:
        print(f'Error reading {rule_file}: {e}')
        return None

print('Step 1: Collecting current rules from disk...')
current_objects = []
for folder in os.listdir(rules_dir):
    folder_path = rules_dir / folder
    if not folder_path.is_dir():
        continue
    obj = parse_rule(folder_path)
    if obj:
        current_objects.append(obj)

current_ids = {obj['objectID'] for obj in current_objects}
print(f'Found {len(current_objects)} rules')

print('\nStep 2: Fetching existing Algolia records...')
client = SearchClient.create(APP_ID, ADMIN_KEY)
index = client.init_index(INDEX_NAME)

stale_ids = []
total = 0
for hit in index.browse_objects({'attributesToRetrieve': ['objectID']}):
    total += 1
    if hit['objectID'] not in current_ids:
        stale_ids.append(hit['objectID'])

print(f'Fetched {total} existing records, {len(stale_ids)} stale')

print('\nStep 3: Deleting stale records...')
if stale_ids:
    for obj_id in stale_ids:
        print(f'  Deleting: {obj_id}')
    index.delete_objects(stale_ids).wait()
else:
    print('No stale records found')

print('\nStep 4: Upserting current rules...')
index.save_objects(current_objects).wait()
print(f'Upserted {len(current_objects)} records')

print('\nDone')
