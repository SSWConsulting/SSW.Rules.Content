#!/usr/bin/env python3
"""
Script to add Microsoft Creator IDs to relevant URLs in markdown files.
Uses pattern matching and heuristics to categorize content and choose appropriate Creator IDs.
Handles markdown autolinks with external WT.mc_id tags by normalizing them.
"""

import re
import glob
import logging
import argparse
from urllib.parse import urlparse
from typing import List, Dict

# Creator ID categories
def get_creator_ids(base: str) -> Dict[str, str]:
    return {
        'OSS': f'?WT.mc_id=OSS-{base}',
        'Mixed Reality': f'?WT.mc_id=MR-{base}',
        'Business Apps': f'?WT.mc_id=DX-{base}',
        'IoT': f'?WT.mc_id=IoT-{base}',
        'Enterprise Mobility': f'?WT.mc_id=EM-{base}',
        'Security': f'?WT.mc_id=ES-{base}',
        'AI': f'?WT.mc_id=AI-{base}',
        'Developer Technologies': f'?WT.mc_id=DT-{base}',
        'Microsoft Azure': f'?WT.mc_id=AZ-{base}',
        'Data Platform': f'?WT.mc_id=DP-{base}',
        'Windows Development': f'?WT.mc_id=WDIT-{base}',
        'Developer / DevOps': f'?WT.mc_id=DOP-{base}',
        'Microsoft365': f'?WT.mc_id=M365-{base}'
    }

# Domains and paths to match Microsoft URLs
MICROSOFT_HOSTS = [
    'docs.microsoft.com', 'learn.microsoft.com', 'social.technet.microsoft.com',
    'azure.microsoft.com', 'techcommunity.microsoft.com', 'social.msdn.microsoft.com',
    'devblogs.microsoft.com', 'developer.microsoft.com', 'channel9.msdn.com',
    'gallery.technet.microsoft.com', 'cloudblogs.microsoft.com', 'technet.microsoft.com',
    'msdn.microsoft.com', 'blogs.msdn.microsoft.com', 'blogs.technet.microsoft.com',
    'microsoft.com'
]
MICROSOFT_PATH_PREFIXES = ['/handsonlabs']

# Compile category patterns
CATEGORY_PATTERNS = {
    'Microsoft Azure': [r'azure\.microsoft\.com', r'/azure/', r'/cloud/', r'/storage/', r'/compute/', r'/networking/', r'\bazure\b', r'\bcloud\b', r'\bapp service\b', r'\bfunction apps?\b', r'\bazure devops\b', r'\bcontainer\b', r'\bkubernetes\b', r'\baks\b'],
    'Data Platform': [r'/sql/', r'/database/', r'/analytics/', r'/data/', r'\bsql server\b', r'\bdatabase\b', r'\bentity framework\b', r'\bef core\b', r'\bdata\b', r'\banalytics\b', r'\bquery\b', r'\btable\b', r'\bindex\b'],
    'Security': [r'/security/', r'/identity/', r'/authentication/', r'/authorization/', r'\bsecurity\b', r'\bauthentication\b', r'\bauthorization\b', r'\bidentity\b', r'\boauth\b', r'\bssl\b', r'\btls\b', r'\bpassword\b', r'\bmfa\b', r'\bmulti.?factor\b'],
    'AI': [r'/ai/', r'/cognitive/', r'/machine-?learning/', r'/ml/', r'\bai\b', r'\bartificial intelligence\b', r'\bmachine learning\b', r'\bcognitive\b', r'\bgpt\b', r'\bchatgpt\b', r'\bcopilot\b', r'\bneural\b', r'\bllm\b'],
    'Developer / DevOps': [r'/devops/', r'/git/', r'/build/', r'/deploy/', r'/pipeline/', r'/ci-?cd/', r'\bdevops\b', r'\bgit\b', r'\bci/cd\b', r'\bcontinuous integration\b', r'\bcontinuous deployment\b', r'\bbuild\b', r'\bpipeline\b', r'\brelease\b', r'\bscrum\b', r'\bagile\b', r'\btfs\b'],
    'Microsoft365': [r'/office/', r'/teams/', r'/sharepoint/', r'/outlook/', r'/exchange/', r'/microsoft-365/', r'/office-365/', r'\boffice 365\b', r'\bmicrosoft 365\b', r'\bteams\b', r'\bsharepoint\b', r'\boutlook\b', r'\bexchange\b', r'\bpower platform\b', r'\bpower apps?\b', r'\bpower automate\b'],
    'Developer Technologies': [r'/dotnet/', r'/csharp/', r'/visual-?studio/', r'/asp\.net/', r'/blazor/', r'\.net\b', r'\bc#\b', r'\bcsharp\b', r'\bvisual studio\b', r'\basp\.net\b', r'\bblazor\b', r'\bmaui\b', r'\bxamarin\b', r'\bapi\b', r'\brest\b', r'\bwebapi\b'],
    'Business Apps': [r'/dynamics/', r'/power-?platform/', r'/power-?apps/', r'/power-?automate/', r'/business/', r'\bdynamics\b', r'\bpower platform\b', r'\bpower apps?\b', r'\bpower automate\b', r'\bflow\b', r'\bcanvas app\b', r'\bmodel.?driven\b', r'\bcrm\b'],
    'Windows Development': [r'/windows/', r'/uwp/', r'/wpf/', r'/winui/', r'\bwindows\b', r'\buwp\b', r'\bwpf\b', r'\bwinui\b', r'\bdesktop\b', r'\bwin32\b'],
    'IoT': [r'/iot/', r'/internet-?of-?things/', r'\biot\b', r'\binternet of things\b', r'\bsensor\b', r'\bembedded\b', r'\braspberry pi\b', r'\barduino\b'],
    'Enterprise Mobility': [r'/intune/', r'/mobility/', r'/mobile/', r'/mdm/', r'\bintune\b', r'\bmobile device management\b', r'\bmdm\b', r'\bmobile\b', r'\bmam\b'],
    'Mixed Reality': [r'/mixed-?reality/', r'/hololens/', r'/vr/', r'/ar/', r'\bmixed reality\b', r'\bhololens\b', r'\bvirtual reality\b', r'\baugmented reality\b', r'\bvr\b', r'\bar\b', r'\bmr\b']
}
# Precompile regexes
COMPILED_CATEGORIES = {cat: [re.compile(p, re.IGNORECASE) for p in pats] for cat, pats in CATEGORY_PATTERNS.items()}
OSS_REGEXES = [re.compile(p, re.IGNORECASE) for p in [r'\bopen.?source\b', r'\bgithub\b', r'\bcontribut\w+\b', r'\bfork\b', r'\bpull request\b', r'\bmit license\b']]

# URL matching regex (matches URLs within text)
hosts_union = '|'.join(re.escape(h) for h in MICROSOFT_HOSTS)
URL_REGEX = re.compile(
    r"(https?://(?:www\.)?(?:" + hosts_union + r")(?:/[^\s)'>]*)?(?:\?WT\.mc_id=[^\s)'>]+)?)",
    re.IGNORECASE
)


def categorize_content(file_path: str, url: str, context: str) -> str:
    """Choose best category by scoring context and URL."""
    text_lower = f"{url} {file_path} {context[:2000]}".lower()
    scores = {cat: sum(len(rx.findall(text_lower)) for rx in rx_list)
              for cat, rx_list in COMPILED_CATEGORIES.items()}
    best = max(scores, key=scores.get)
    if scores[best] > 0:
        return best
    for rx in OSS_REGEXES:
        if rx.search(text_lower):
            return 'OSS'
    return 'Developer Technologies'


def has_creator_id(url: str) -> bool:
    return 'WT.mc_id=' in url


def add_creator_id_to_url(url: str, creator_param: str) -> str:
    if has_creator_id(url):
        return url
    sep = '&' if '?' in url else '?'
    return f"{url}{sep}{creator_param.lstrip('?')}"


def is_microsoft_url(url: str) -> bool:
    parsed = urlparse(url)
    return any(parsed.netloc.endswith(host) for host in MICROSOFT_HOSTS) or \
           any(parsed.path.startswith(pref) for pref in MICROSOFT_PATH_PREFIXES)


def process_markdown_file(path: str, creator_ids: Dict[str, str], dry_run: bool) -> int:
    try:
        content = open(path, encoding='utf-8').read()
    except Exception as e:
        logging.error(f"Error reading {path}: {e}")
        return 0

    # Normalize autolinks: move external WT params into angle bracket
    content = re.sub(
        r"<(https?://[^>]+)>\?WT\.mc_id=([^\s>]+)",
        r"<\1?WT.mc_id=\2>",
        content
    )

    changes: List[tuple] = []
    def repl(match):
        orig_url = match.group(1)
        # Fix misplaced WT param before path: domain?WT.../path -> domain/path?WT...
        m2 = re.match(r"(https?://[^?]+)\?WT\.mc_id=([^/]+)(/.*)", orig_url)
        if m2:
            orig_url = f"{m2.group(1)}{m2.group(3)}?WT.mc_id={m2.group(2)}"
        if not is_microsoft_url(orig_url) or has_creator_id(orig_url):
            return orig_url
        cat = categorize_content(path, orig_url, content)
        new_url = add_creator_id_to_url(orig_url, creator_ids.get(cat, creator_ids['Developer Technologies']))
        changes.append((orig_url, new_url, cat))
        return new_url

    new_content = URL_REGEX.sub(repl, content)
    for old, new, cat in changes:
        logging.info(f"{old} -> {new} (Category: {cat})")

    if changes and not dry_run:
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
        except Exception as e:
            logging.error(f"Error writing {path}: {e}")
            return 0

    return len(changes)


def main():
    parser = argparse.ArgumentParser(description='Add MS Creator IDs to Markdown URLs')
    parser.add_argument('--creator-id', required=True, help='Base ID (e.g., MVP-33518)')
    parser.add_argument('--dry-run', action='store_true', help='Show changes only')
    parser.add_argument('--pattern', nargs='+', default=['rules/**/*.md'], help='File globs to process')
    parser.add_argument('--limit', type=int, help='Max files (>=1)')
    parser.add_argument('--file', help='Specific file to process')
    parser.add_argument('--verbose', action='store_true', help='Enable DEBUG logging')
    args = parser.parse_args()

    if args.limit is not None and args.limit < 1:
        parser.error('--limit must be >= 1')

    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(format='%(levelname)s: %(message)s', level=level)

    creator_ids = get_creator_ids(args.creator_id)
    files = [args.file] if args.file else sum((glob.glob(p, recursive=True) for p in args.pattern), [])
    if args.limit:
        files = files[:args.limit]

    logging.info(f"Processing {len(files)} files with base ID {args.creator_id}")
    if args.dry_run:
        logging.info("--dry-run mode, no files will be modified")

    total_changes = 0
    for idx, filepath in enumerate(files, start=1):
        if idx % 100 == 0:
            logging.debug(f"Progress: {idx}/{len(files)}")
        total_changes += process_markdown_file(filepath, creator_ids, args.dry_run)

    logging.info(f"Done! Total URLs updated: {total_changes}")


if __name__ == '__main__':
    main()
