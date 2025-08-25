"""
------------------------------------------------------------
Script: Markdown to MDX Transformer
------------------------------------------------------------

This script transforms Markdown (.md) files (used in SSW Rules)
into MDX files with special components for images, videos,
email templates, and aside blocks.

Usage:
    python convert-rule-md-to-mdx.py [path] [file_name]

Parameters:
    path        - Optional. Can be a Markdown file path or a directory path.
                  - If it's a Markdown file: transforms just that file.
                  - If it's a directory: processes subdirectories inside it.
                    Looks for Markdown files to transform (default: rule.md).

    file_name   - Optional. Only used when 'path' is a directory.
                  Specifies which .md file to process in each subfolder.
                  If omitted, the first .md file in each subfolder is used.

Examples:
    python convert-rule-md-to-mdx.py                              # Transforms all rule.md files in ./rules/
    python convert-rule-md-to-mdx.py rules custom_rule.md         # Transforms custom_rule.md in each subfolder under ./rules/
    python convert-rule-md-to-mdx.py rules/someRule/rule.md       # Transforms only the specified file

Notes:
    - The original .md file will be deleted after successful transformation.
    - The resulting .mdx file will be saved in the same directory.
    - Files listed in IGNORE_FILES will be skipped.
"""

import os
import re
from pathlib import Path
import time
import sys

# ----------------------------- #
# Configuration
# ----------------------------- #

DEFAULT_BASE_DIR = 'rules'
DEFAULT_FILE_NAME = 'rule.md'
SRC_PREFIX_BASE = '/uploads/rules/'
IGNORE_FILES = ['pull_request_template.md']  # List of file names to ignore (e.g., ['ignore_this.md', 'example.md'])

# ----------------------------- #
# Regex patterns
# ----------------------------- #

YOUTUBE_BLOCK_REGEX = r'`youtube:\s*(https?://[^\s]+)`(?:\s*\n\*\*(.*?)\*\*)?'
IMAGE_BLOCK_REGEX = r'::: (bad|ok|good)\s+(!\[Figure:.*?\]\(.*?\))\s+:::'
STANDALONE_IMAGE_REGEX = r'!\[Figure:\s*(.*?)\]\((.*?)\)'
EMAIL_BLOCK_REGEX = (
    r'::: email-template\s+(.*?)'
    r'::: email-content\s+(.*?)'
    r':::\s+:::\s+'
    r'(:::\s*(good|bad|ok).*?:::)'
)
SIMPLE_FIGURE_BLOCK_REGEX = r':::\s*(good|bad|ok)\s*\n(.*?)\n:::' 
CUSTOM_SIZE_IMAGE_BLOCK_REGEX = r':::\s*(img-small|img-medium|img-large|no-border)\s*\n\s*!\[Figure:\s*(.*?)\]\((.*?)\)\s*:::'
RAW_IMAGE_REGEX = r'!\[(?!Figure:)(.*?)\]\((.*?)\)'
INTRO_WITH_FM_REGEX = r'^(?P<fm>---\s*\n.*?\n---\s*\n)?(?P<intro>.*?)(?:\r?\n)?<!--\s*endintro\s*-->\s*'

# ----------------------------- #
# Utilities
# ----------------------------- #

def escape_single_quotes(text):
    return text.replace("'", "\\'")

def mdx_safe_template_vars(text):
    return text.replace("{{", "&#123;&#123;").replace("}}", "&#125;&#125;")

def parse_email_table(table_text):
    result = {'from': '', 'to': '', 'cc': '', 'bcc': '', 'subject': ''}
    for line in table_text.splitlines():
        parts = line.split('|')
        if len(parts) < 3:
            continue
        key = parts[1].replace(":", "").strip().lower()
        value = mdx_safe_template_vars(parts[2].strip())
        if key in result:
            result[key] = value
    return result

def clean_email_body(body_text):
    cleaned = mdx_safe_template_vars(body_text)
    cleaned = cleaned.replace(r'\>', '&gt;')
    return re.sub(r'^###', '##', cleaned, flags=re.MULTILINE)

def clean_image_src(src):
    return re.sub(r'(\.(?:png|jpg|jpeg|gif))\s.*$', r'\1', src, flags=re.IGNORECASE)

def prefix_raw_image_src(m, src_prefix):
    alt_text = m.group(1).strip()
    raw_src = m.group(2).strip()
    clean_src = clean_image_src(raw_src)

    if clean_src.startswith('/') or clean_src.startswith('http'):
        return m.group(0)

    prefixed_src = f"{src_prefix}/{clean_src}"
    return f'![{alt_text}]({prefixed_src})'

# ----------------------------- #
# Replacements
# ----------------------------- #

def replace_youtube_block(m):
    url = m.group(1).strip()
    desc = m.group(2).strip() if m.group(2) else ""
    return f'<youtubeEmbed url="{url}" description="{desc}" />'

def replace_youtube_block_inside_intro(m):
    url = m.group(1).strip()
    desc = m.group(2).strip() if m.group(2) else ""
    return f'<introYoutube url="{url}" description="{desc}" />'

def wrap_intro_embed(m):
    fm = m.group('fm') or ''
    intro = m.group('intro') or ''
    intro_processed = re.sub(YOUTUBE_BLOCK_REGEX, replace_youtube_block_inside_intro, intro.strip(), flags=re.MULTILINE)
    return f'''{fm}<introEmbed
  body={{<>
{intro_processed}
  </>}}
/>
'''

def replace_image_block(m, src_prefix):
    preset = m.group(1).strip()
    image_line = m.group(2).strip()
    alt_match = re.match(r'!\[Figure:\s*(.*?)\]\((.*?)\)', image_line)
    if not alt_match:
        return m.group(0)
    figure = alt_match.group(1).strip()
    raw_src = alt_match.group(2).strip()
    src = f"{src_prefix}/{clean_image_src(raw_src)}"

    return f'''<imageEmbed
  alt="Image"
  size="large"
  showBorder={{false}}
  figureEmbed={{{{
    preset: "{preset}Example",
    figure: '{escape_single_quotes(figure)}',
    shouldDisplay: true
  }}}}
  src="{src}"
/>'''

def replace_custom_size_image_block(m, src_prefix):
    variant = m.group(1).strip()
    figure = escape_single_quotes(m.group(2).strip())
    raw_src = m.group(3).strip()
    src = f"{src_prefix}/{clean_image_src(raw_src)}"

    size = {
        "img-small": "small",
        "img-medium": "medium",
        "img-large": "large",
        "no-border": "large"
    }.get(variant, "large")

    show_border = "false" if variant == "no-border" else "true"

    return f'''<imageEmbed
  alt="Image"
  size="{size}"
  showBorder={{{show_border}}}
  figureEmbed={{{{
    preset: "default",
    figure: '{figure}',
    shouldDisplay: true
  }}}}
  src="{src}"
/>'''

def replace_standalone_image(m, src_prefix):
    figure = m.group(1).strip()
    raw_src = m.group(2).strip()
    src = f"{src_prefix}/{clean_image_src(raw_src)}"

    return '\n' + f'''<imageEmbed
  alt="Image"
  size="large"
  showBorder={{false}}
  figureEmbed={{{{
    preset: "default",
    figure: '{escape_single_quotes(figure)}',
    shouldDisplay: true
  }}}}
  src="{src}"
/>'''

def replace_email_block(m):
    table = m.group(1)
    body = m.group(2).strip()
    figure_block = m.group(3)

    email_data = parse_email_table(table)
    cleaned_body = clean_email_body(body)

    preset_match = re.match(r'::: (good|bad|ok)', figure_block.strip())
    preset = f"{preset_match.group(1)}Example" if preset_match else "default"
    figure_match = re.search(r'Figure:\s*(.*)', figure_block)
    figure = figure_match.group(1).strip() if figure_match else "Example"
    should_display = 'Figure:' in figure_block

    return f'''<emailEmbed
  from="{email_data['from']}"
  to="{email_data['to']}"
  cc="{email_data['cc']}"
  bcc="{email_data['bcc']}"
  subject="{email_data['subject']}"
  body={{<>
    {cleaned_body}
  </>}}
  figureEmbed={{{{
    preset: "{preset}",
    figure: "{figure}",
    shouldDisplay: {"true" if should_display else "false"}
  }}}}
/>'''

def replace_simple_figure_block(m):
    preset = m.group(1).strip()
    figure = m.group(2).strip()
    return f'''<figureEmbed figureEmbed={{{{
  preset: "{preset}Example",
  figure: '{escape_single_quotes(figure)}',
  shouldDisplay: true
}} }} />\n'''

def process_custom_aside_blocks(content):
    lines = content.splitlines()
    output = []
    i = 0
    in_box = False
    box_type = ""
    buffer = []

    while i < len(lines):
        line = lines[i].rstrip()

        match_start = re.match(r":::\s*(greybox|highlight|china|info|todo|codeauditor)\s*$", line)
        if match_start and not in_box:
            in_box = True
            box_type = match_start.group(1)
            buffer = []
            i += 1
            continue

        if in_box and line.strip() == ":::":

            preset = "default"
            figure = "XXX"
            show = False

            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                single_line = re.match(r"^:::\s*(good|bad|ok)\s+Figure:\s*(.*?)\s+:::", next_line)
                if single_line:
                    preset = f"{single_line.group(1)}Example"
                    figure = single_line.group(2)
                    show = True
                    i += 1
                else:
                    alt_caption = re.match(r"^\*\*Figure:\s*(.*?)\*\*", next_line)
                    if alt_caption:
                        figure = alt_caption.group(1)
                        show = True
                        i += 1
                    elif (
                        i + 3 < len(lines)
                        and (match_l1 := re.match(r"^:::\s*(good|bad|ok)\s*$", lines[i + 1].strip()))
                        and (match_l2 := re.match(r"^Figure:\s*(.*?)\s*$", lines[i + 2].strip()))
                        and lines[i + 3].strip() == ":::"
                    ):
                        preset = f"{match_l1.group(1)}Example"
                        figure = match_l2.group(1).strip()
                        show = True
                        i += 3

            body = '\n'.join(buffer).replace("`<", "&lt;").replace(">`", "&gt;")
            embed = f'''<asideEmbed
  variant="{box_type}"
  body={{<>
    {body}
  </>}}
  figureEmbed={{{{
    preset: "{preset}",
    figure: '{escape_single_quotes(figure)}',
    shouldDisplay: {"true" if show else "false"}
  }}}}
/>'''
            output.append(embed)
            in_box = False
            i += 1
            continue

        if in_box:
            buffer.append(line)
        else:
            output.append(line)

        i += 1

    return '\n'.join(output)

# ----------------------------- #
# Main Transform Function
# ----------------------------- #

def transform_md_to_mdx(file_path):
    path = Path(file_path)
    if not path.exists():
        print(f"File not found: {file_path}")
        return

    folder_name = path.parent.name
    src_prefix = f"{SRC_PREFIX_BASE}{folder_name}"
    content = path.read_text(encoding='utf-8')

    content = mdx_safe_template_vars(content)
    content = re.sub(INTRO_WITH_FM_REGEX, wrap_intro_embed, content, flags=re.IGNORECASE | re.DOTALL)

    content = process_custom_aside_blocks(content)
    content = re.sub(YOUTUBE_BLOCK_REGEX, replace_youtube_block, content, flags=re.MULTILINE)
    content = re.sub(IMAGE_BLOCK_REGEX, lambda m: replace_image_block(m, src_prefix), content, flags=re.DOTALL)
    content = re.sub(CUSTOM_SIZE_IMAGE_BLOCK_REGEX, lambda m: replace_custom_size_image_block(m, src_prefix), content, flags=re.DOTALL)
    content = re.sub(STANDALONE_IMAGE_REGEX, lambda m: replace_standalone_image(m, src_prefix), content)
    content = re.sub(EMAIL_BLOCK_REGEX, replace_email_block, content, flags=re.DOTALL)
    content = re.sub(SIMPLE_FIGURE_BLOCK_REGEX, replace_simple_figure_block, content, flags=re.DOTALL)
    content = re.sub(RAW_IMAGE_REGEX, lambda m: prefix_raw_image_src(m, src_prefix), content)

    output_path = path.with_suffix('.mdx')
    output_path.write_text(content, encoding='utf-8')

    print(f"Transformed content saved to: {output_path}")
    path.unlink()  # delete original .md file

def transform_all_mds(base_dir=DEFAULT_BASE_DIR, file_name=DEFAULT_FILE_NAME):
    """
    Transform all Markdown (.md) files in each subdirectory of the given base directory.

    :param base_dir: The base directory containing rule folders.
    :param file_name: The specific file name to look for in each folder. If None, process any .md file.
    :param ignore_files: A list of file names to ignore.
    """
    start_time = time.time()
    base_path = Path(base_dir)
    if not base_path.exists():
        print(f"Base path not found: {base_dir}")
        return

    count = 0
    for rule_dir in base_path.iterdir():
        if rule_dir.is_dir():
            # If a specific file name is provided, look for it; otherwise, find any .md file
            if file_name:
                rule_md = rule_dir / file_name
                if not rule_md.exists() or rule_md.name in IGNORE_FILES:
                    print(f"[WARNING] File not found or ignored: {rule_md}")
                    continue
            else:
                md_files = [f for f in rule_dir.glob('*.md') if f.name not in IGNORE_FILES]
                if not md_files:
                    print(f"[WARNING] No .md files found in: {rule_dir}")
                    continue
                rule_md = md_files[0]  # Process the first .md file found

            print(f"[INFO] Processing: {rule_md}")
            try:
                transform_md_to_mdx(rule_md)
                count += 1
            except Exception as e:
                print(f"[ERROR] Failed to process {rule_md}: {e}")

    end_time = time.time()
    elapsed = end_time - start_time
    print(f"\n✅ Finished processing {count} rule files in {elapsed:.2f} seconds.")

# ----------------------------- #
# Entry Point
# ----------------------------- #

if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        path = Path(arg)
        if path.is_file():
            transform_md_to_mdx(arg)
        elif path.is_dir():
            file_name = sys.argv[2] if len(sys.argv) > 2 else None
            transform_all_mds(arg, file_name)
        else:
            print(f"Error: The provided path '{arg}' is neither a file nor a directory.")
    else:
        transform_all_mds()