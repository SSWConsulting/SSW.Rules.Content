#!/usr/bin/env python3
"""
Script to add Microsoft Creator IDs to relevant URLs in markdown files.
Uses pattern matching and heuristics to categorize content and choose appropriate Creator IDs.
"""

import re
import glob
from typing import List, Tuple, Dict
from urllib.parse import urlparse
import argparse

def get_creator_ids(creator_id_base: str) -> Dict[str, str]:
    """Generate Creator IDs dictionary with the provided base ID."""
    return {
        'OSS': f'?WT.mc_id=OSS-{creator_id_base}',
        'Mixed Reality': f'?WT.mc_id=MR-{creator_id_base}',
        'Business Apps': f'?WT.mc_id=DX-{creator_id_base}',
        'IoT': f'?WT.mc_id=IoT-{creator_id_base}',
        'Enterprise Mobility': f'?WT.mc_id=EM-{creator_id_base}',
        'Security': f'?WT.mc_id=ES-{creator_id_base}',
        'AI': f'?WT.mc_id=AI-{creator_id_base}',
        'Developer Technologies': f'?WT.mc_id=DT-{creator_id_base}',
        'Microsoft Azure': f'?WT.mc_id=AZ-{creator_id_base}',
        'Data Platform': f'?WT.mc_id=DP-{creator_id_base}',
        'Windows Development': f'?WT.mc_id=WDIT-{creator_id_base}',
        'Developer / DevOps': f'?WT.mc_id=DOP-{creator_id_base}',
        'Microsoft365': f'?WT.mc_id=M365-{creator_id_base}'
    }

# Microsoft domains that should get Creator IDs
MICROSOFT_DOMAINS = [
    'docs.microsoft.com',
    'learn.microsoft.com',
    'social.technet.microsoft.com',
    'azure.microsoft.com',
    'techcommunity.microsoft.com',
    'social.msdn.microsoft.com',
    'devblogs.microsoft.com',
    'developer.microsoft.com',
    'channel9.msdn.com',
    'gallery.technet.microsoft.com',
    'cloudblogs.microsoft.com',
    'technet.microsoft.com',
    'msdn.microsoft.com',
    'blogs.msdn.microsoft.com',
    'blogs.technet.microsoft.com',
    'microsoft.com/handsonlabs'
]

# Category matching patterns
CATEGORY_PATTERNS = {
    'Microsoft Azure': [
        # URL patterns
        r'azure\.microsoft\.com',
        r'/azure/',
        r'/cloud/',
        r'/storage/',
        r'/compute/',
        r'/networking/',
        # Content patterns
        r'\bazure\b',
        r'\bcloud\b',
        r'\bapp service\b',
        r'\bfunction apps?\b',
        r'\bazure devops\b',
        r'\bcontainer\b',
        r'\bkubernetes\b',
        r'\baks\b'
    ],
    'Data Platform': [
        # URL patterns
        r'/sql/',
        r'/database/',
        r'/analytics/',
        r'/data/',
        # Content patterns
        r'\bsql server\b',
        r'\bdatabase\b',
        r'\bentity framework\b',
        r'\bef core\b',
        r'\bdata\b',
        r'\banalytics\b',
        r'\bquery\b',
        r'\btable\b',
        r'\bindex\b'
    ],
    'Security': [
        # URL patterns
        r'/security/',
        r'/identity/',
        r'/authentication/',
        r'/authorization/',
        # Content patterns
        r'\bsecurity\b',
        r'\bauthentication\b',
        r'\bauthorization\b',
        r'\bidentity\b',
        r'\boauth\b',
        r'\bssl\b',
        r'\btls\b',
        r'\bpassword\b',
        r'\bmfa\b',
        r'\bmulti.?factor\b'
    ],
    'AI': [
        # URL patterns
        r'/ai/',
        r'/cognitive/',
        r'/machine-?learning/',
        r'/ml/',
        # Content patterns
        r'\bai\b',
        r'\bartificial intelligence\b',
        r'\bmachine learning\b',
        r'\bcognitive\b',
        r'\bgpt\b',
        r'\bchatgpt\b',
        r'\bcopilot\b',
        r'\bneural\b',
        r'\bllm\b'
    ],
    'Developer / DevOps': [
        # URL patterns
        r'/devops/',
        r'/git/',
        r'/build/',
        r'/deploy/',
        r'/pipeline/',
        r'/ci-?cd/',
        # Content patterns
        r'\bdevops\b',
        r'\bgit\b',
        r'\bci/cd\b',
        r'\bcontinuous integration\b',
        r'\bcontinuous deployment\b',
        r'\bbuild\b',
        r'\bpipeline\b',
        r'\brelease\b',
        r'\bscrum\b',
        r'\bagile\b',
        r'\btfs\b'
    ],
    'Microsoft365': [
        # URL patterns
        r'/office/',
        r'/teams/',
        r'/sharepoint/',
        r'/outlook/',
        r'/exchange/',
        r'/microsoft-365/',
        r'/office-365/',
        # Content patterns
        r'\boffice 365\b',
        r'\bmicrosoft 365\b',
        r'\bteams\b',
        r'\bsharepoint\b',
        r'\boutlook\b',
        r'\bexchange\b',
        r'\bpower platform\b',
        r'\bpower apps?\b',
        r'\bpower automate\b'
    ],
    'Developer Technologies': [
        # URL patterns
        r'/dotnet/',
        r'/csharp/',
        r'/visual-?studio/',
        r'/asp\.net/',
        r'/blazor/',
        # Content patterns
        r'\.net\b',
        r'\bc#\b',
        r'\bcsharp\b',
        r'\bvisual studio\b',
        r'\basp\.net\b',
        r'\bblazor\b',
        r'\bmaui\b',
        r'\bxamarin\b',
        r'\bapi\b',
        r'\brest\b',
        r'\bwebapi\b'
    ],
    'Business Apps': [
        # URL patterns
        r'/dynamics/',
        r'/power-?platform/',
        r'/power-?apps/',
        r'/power-?automate/',
        r'/business/',
        # Content patterns
        r'\bdynamics\b',
        r'\bpower platform\b',
        r'\bpower apps?\b',
        r'\bpower automate\b',
        r'\bflow\b',
        r'\bcanvas app\b',
        r'\bmodel.?driven\b',
        r'\bcrm\b'
    ],
    'Windows Development': [
        # URL patterns
        r'/windows/',
        r'/uwp/',
        r'/wpf/',
        r'/winui/',
        # Content patterns
        r'\bwindows\b',
        r'\buwp\b',
        r'\bwpf\b',
        r'\bwinui\b',
        r'\bdesktop\b',
        r'\bwin32\b'
    ],
    'IoT': [
        # URL patterns
        r'/iot/',
        r'/internet-?of-?things/',
        # Content patterns
        r'\biot\b',
        r'\binternet of things\b',
        r'\bsensor\b',
        r'\bembedded\b',
        r'\braspberry pi\b',
        r'\barduino\b'
    ],
    'Enterprise Mobility': [
        # URL patterns
        r'/intune/',
        r'/mobility/',
        r'/mobile/',
        r'/mdm/',
        # Content patterns
        r'\bintune\b',
        r'\bmobile device management\b',
        r'\bmdm\b',
        r'\bmobile\b',
        r'\bmam\b'
    ],
    'Mixed Reality': [
        # URL patterns
        r'/mixed-?reality/',
        r'/hololens/',
        r'/vr/',
        r'/ar/',
        # Content patterns
        r'\bmixed reality\b',
        r'\bhololens\b',
        r'\bvirtual reality\b',
        r'\baugmented reality\b',
        r'\bvr\b',
        r'\bar\b',
        r'\bmr\b'
    ]
}

def categorize_content(file_path: str, url: str, context: str) -> str:
    """Categorize content using pattern matching to choose appropriate Creator ID."""
    
    # Extract relevant context around the URL
    lines = context.split('\n')
    url_line_idx = None
    for i, line in enumerate(lines):
        if url in line:
            url_line_idx = i
            break
    
    if url_line_idx is not None:
        # Get context around the URL (10 lines before and after)
        start = max(0, url_line_idx - 10)
        end = min(len(lines), url_line_idx + 11)
        relevant_context = '\n'.join(lines[start:end])
    else:
        # Fallback to first 2000 characters
        relevant_context = context[:2000]
    
    # Combine URL, file path, and context for analysis
    text_to_analyze = f"{url} {file_path} {relevant_context}".lower()
    
    # Score each category based on pattern matches
    category_scores = {}
    
    for category, patterns in CATEGORY_PATTERNS.items():
        score = 0
        for pattern in patterns:
            matches = len(re.findall(pattern, text_to_analyze, re.IGNORECASE))
            score += matches
        category_scores[category] = score
    
    # Find the category with the highest score
    if category_scores:
        best_category = max(category_scores, key=category_scores.get)
        if category_scores[best_category] > 0:
            return best_category
    
    # Special handling for OSS if we see open source indicators
    oss_patterns = [r'\bopen.?source\b', r'\bgithub\b', r'\bcontribut\w+\b', r'\bfork\b', r'\bpull request\b', r'\bmit license\b']
    for pattern in oss_patterns:
        if re.search(pattern, text_to_analyze, re.IGNORECASE):
            return 'OSS'
    
    # Default fallback
    return 'Developer Technologies'

def has_creator_id(url: str) -> bool:
    """Check if URL already has a Creator ID."""
    return 'WT.mc_id=' in url

def add_creator_id_to_url(url: str, creator_id: str) -> str:
    """Add Creator ID to URL."""
    if has_creator_id(url):
        return url
    
    if '?' in url:
        # URL already has query parameters, append with &
        separator = '&'
        new_url = url + separator + creator_id.lstrip('?')
    else:
        # URL has no query parameters, append with ?
        new_url = url + creator_id
    
    return new_url

def find_microsoft_urls(content: str) -> List[Tuple[int, int, str]]:
    """Find all Microsoft URLs in the content."""
    urls_found = []
    
    # Pattern to match markdown links [text](url) and bare URLs
    # This is a comprehensive pattern that handles both formats
    patterns = [
        # Markdown links with Microsoft URLs
        r'\[([^\]]*)\]\((https?://(?:www\.)?(?:' + '|'.join(re.escape(domain) for domain in MICROSOFT_DOMAINS) + r')[^\)]*)\)',
        # Bare Microsoft URLs
        r'(?<!\]\()(?<!["\'])(https?://(?:www\.)?(?:' + '|'.join(re.escape(domain) for domain in MICROSOFT_DOMAINS) + r')[^\s\)]*)'
    ]
    
    for pattern in patterns:
        for match in re.finditer(pattern, content):
            if len(match.groups()) >= 2:
                # Markdown link format
                url = match.group(2)
                start_pos = match.start()
                end_pos = match.end()
            else:
                # Bare URL
                url = match.group(1) if len(match.groups()) >= 1 else match.group(0)
                start_pos = match.start()
                end_pos = match.end()
            
            # Check if it's actually a Microsoft domain and doesn't have Creator ID
            parsed = urlparse(url)
            if any(domain in parsed.netloc for domain in MICROSOFT_DOMAINS) and not has_creator_id(url):
                urls_found.append((start_pos, end_pos, url))
    
    # Remove duplicates and sort by position (reverse order for replacement)
    urls_found = list(set(urls_found))
    urls_found.sort(key=lambda x: x[0], reverse=True)
    
    return urls_found

def process_markdown_file(file_path: str, creator_ids: Dict[str, str], dry_run: bool = False) -> Tuple[int, List[str]]:
    """Process a single markdown file to add Creator IDs."""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0, []
    
    original_content = content
    changes = []
    
    # Find Microsoft URLs
    urls_to_process = find_microsoft_urls(content)
    
    # Process URLs in reverse order to maintain string positions
    for start_pos, end_pos, url in urls_to_process:
        # Categorize content
        category = categorize_content(file_path, url, content)
        creator_id_param = creator_ids.get(category, creator_ids['Developer Technologies'])
        
        # Add Creator ID to URL
        new_url = add_creator_id_to_url(url, creator_id_param)
        
        # Replace the URL in content
        content = content[:start_pos] + content[start_pos:end_pos].replace(url, new_url) + content[end_pos:]
        
        changes.append(f"  {url} -> {new_url} (Category: {category})")
    
    # Write back if changes were made and not dry run
    if content != original_content and not dry_run:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing {file_path}: {e}")
            return 0, []
    
    return len(urls_to_process), changes

def main():
    parser = argparse.ArgumentParser(description='Add Microsoft Creator IDs to URLs in markdown files')
    parser.add_argument('--creator-id', required=True, help='Creator ID base (e.g., MVP-33518)')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be changed without making changes')
    parser.add_argument('--pattern', default='rules/**/*.md', help='File pattern to process (default: rules/**/*.md)')
    parser.add_argument('--limit', type=int, help='Limit number of files to process (for testing)')
    parser.add_argument('--file', help='Process a specific file instead of pattern')
    
    args = parser.parse_args()
    
    # Generate Creator IDs with the provided base
    creator_ids = get_creator_ids(args.creator_id)
    
    # Find markdown files
    if args.file:
        markdown_files = [args.file]
    else:
        markdown_files = glob.glob(args.pattern, recursive=True)
    
    if args.limit:
        markdown_files = markdown_files[:args.limit]
    
    print(f"Found {len(markdown_files)} markdown files to process")
    print(f"Using Creator ID base: {args.creator_id}")
    
    if args.dry_run:
        print("🔍 DRY RUN MODE - No files will be modified")
    
    total_changes = 0
    files_changed = 0
    
    for i, file_path in enumerate(markdown_files):
        if i % 100 == 0 and i > 0:
            print(f"Progress: {i}/{len(markdown_files)} files processed")
        
        try:
            changes_count, changes_list = process_markdown_file(file_path, creator_ids, args.dry_run)
            
            if changes_count > 0:
                files_changed += 1
                total_changes += changes_count
                print(f"\n📝 {file_path}")
                for change in changes_list:
                    print(change)
        
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    print(f"\n✅ Complete!")
    print(f"Files processed: {len(markdown_files)}")
    print(f"Files with changes: {files_changed}")
    print(f"Total URLs updated: {total_changes}")
    
    if args.dry_run:
        print("\n🔄 Run without --dry-run to apply changes")

if __name__ == "__main__":
    main()
