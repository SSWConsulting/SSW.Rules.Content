"""
------------------------------------------------------------
Script: Markdown to MDX Transformer
------------------------------------------------------------

This script transforms .md and .mdx files (used in SSW Rules)
into MDX files with special components for images, videos,
email templates, and aside blocks.

Usage:
    python convert-rule-md-to-mdx.py [path] [file_name]
    python convert-rule-md-to-mdx.py --update-categories [rules_dir]

Parameters:
    path        - Optional. Can be a .md/.mdx file path or a directory path.
                  - If it's a file: transforms just that file.
                  - If it's a directory: processes subdirectories inside it.
                    Looks for .md/.mdx files to transform (default: rule.mdx,
                    falling back to rule.md).

    file_name   - Optional. Only used when 'path' is a directory.
                  Specifies which .md/.mdx file to process in each subfolder.
                  If omitted, the first .mdx file in each subfolder is used; 
                  if none, the first .md file is used.

    --update-categories - Flag to update existing MDX files with categories
                          from rule-to-categories.json. If categories already
                          exist in the file, they are preserved.

Examples:
    python convert-rule-md-to-mdx.py                              # Transforms all rule.mdx files in ./public/uploads/rules/
    python convert-rule-md-to-mdx.py rules custom_rule.md         # Transforms custom_rule.md in each subfolder under ./rules/
    python convert-rule-md-to-mdx.py rules/someRule/rule.md       # Transforms only the specified file
    python convert-rule-md-to-mdx.py --update-categories public/uploads/rules  # Updates categories in all rule.mdx files

Notes:
    - If the input is a .md file, the original .md file will be deleted after successful transformation.
    - The resulting .mdx file will be saved in the same directory.
    - Files listed in IGNORE_FILES will be skipped.
"""


import os
import re
from pathlib import Path
import time
import sys
import json
import glob

# ----------------------------- #
# Configuration
# ----------------------------- #

DEFAULT_BASE_DIR = 'public/uploads/rules'
DEFAULT_FILE_NAME = 'rule.mdx'
SRC_PREFIX_BASE = '/uploads/rules/'
IGNORE_FILES = ['pull_request_template.md']  # List of file names to ignore (e.g., ['ignore_this.md', 'example.md'])

# ----------------------------- #
# Regex patterns
# ----------------------------- #

YOUTUBE_BLOCK_REGEX = r'`youtube:\s*(https?://[^\s]+)`(?:\s*\n\*\*(.*?)\*\*)?'
# IMAGE_BLOCK_REGEX = r'::: (bad|ok|good)\s+(!\[Figure:.*?\]\(.*?\))\s+:::'
# Allow leading whitespace for indented blocks
IMAGE_BLOCK_REGEX = r'^\s*:::\s*(bad|ok|good)\s+(!\[(?:Figure:\s*)?.*?\]\(.*?\))\s+:::'
STANDALONE_IMAGE_REGEX = r'!\[Figure:\s*(.*?)\]\((.*?)\)'
EMAIL_BLOCK_REGEX = (
    r'::: email-template\s+(.*?)'
    r'::: email-content\s+(.*?)'
    r':::\s+:::\s+'
    r'(:::\s*(good|bad|ok).*?:::)'
)
EMAIL_BLOCK_NO_RATING_REGEX = (
    r'::: email-template\s+(.*?)'
    r'::: email-content\s+(.*?)'
    r':::\s+:::\s*'
    r'(?:\*\*Figure:\s*(.*?)\*\*\s*)?'
)
# Allow leading whitespace for indented blocks
SIMPLE_FIGURE_BLOCK_REGEX = r'^\s*:::\s*(good|bad|ok)\s*\n(.*?)\n\s*:::'
CUSTOM_SIZE_IMAGE_BLOCK_REGEX = r'^\s*:::\s*([^\n]+?)\s*\n\s*!\[(?:Figure:\s*)?(.*?)\]\((.*?)\)\s*:::'
RAW_IMAGE_REGEX = r'!\[(?!Figure:)(.*?)\]\((.*?)\)'
INTRO_WITH_FM_REGEX = r'^(?P<fm>---\s*\n.*?\n---\s*\n)?(?P<intro>.*?)(?:\r?\n)?<!--\s*endintro\s*-->\s*'
# Matches both orders: "good img-medium" OR "img-medium good" - allow leading whitespace
PRESET_AND_SIZE_IMAGE_BLOCK_REGEX = r'^\s*:::\s*(?:(?P<preset1>good|bad|ok)\s+(?P<size1>img-small|img-medium|img-large|small|medium|large|no-border)|(?P<size2>img-small|img-medium|img-large|small|medium|large|no-border)\s+(?P<preset2>good|bad|ok))\s*\n\s*!\[Figure:\s*(?P<figure>.*?)\]\((?P<src>.*?)\)\s*:::'
MARK_TAG_REGEX = r'<\s*mark\b[^>]*>(.*?)<\s*/\s*mark\s*>'
# Matches Markdown inline links that are not images, capturing the link text, href, and optional title.
ASSET_LINK_REGEX = r'(?<!\!)\[(?P<text>[^\]]+)\]\((?P<href>[^)\s]+)(?:\s+"(?P<title>[^"]*)")?\)'


# ----------------------------- #
# Utilities
# ----------------------------- #

def js_string(text: str) -> str:
    return json.dumps(text, ensure_ascii=False)

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
    cleaned = convert_angle_bracket_links(cleaned)
    cleaned = cleaned.replace(r'\>', '&gt;')
    cleaned = escape_angle_brackets_except(cleaned, allowed_tags=("mark",))
    return re.sub(r'^###', '##', cleaned, flags=re.MULTILINE)


def clean_image_src(src):
    return re.sub(r'(\.(?:png|jpg|jpeg|gif))\s.*$', r'\1', src, flags=re.IGNORECASE)

def prefix_raw_image_src(m, src_prefix):
    alt_text = m.group(1).strip()
    raw_src = m.group(2).strip()
    clean_src = clean_image_src(raw_src)
    if clean_src.lstrip('/').startswith(src_prefix.lstrip('/') + '/'):
        return m.group(0)

    new_src = add_prefix_if_relative(raw_src, src_prefix)
    return f'![{alt_text}]({new_src})'

def convert_angle_bracket_links(text: str) -> str:
    return re.sub(
        r'(?<!&lt;)<([a-zA-Z][a-zA-Z0-9+.-]*:[^>\s]+)>(?!&gt;)',
        r'[\1](\1)',
        text
    )

def escape_angle_brackets_except(text: str, allowed_tags=("mark",)) -> str:
    tag_names = "|".join(re.escape(t) for t in allowed_tags)
    placeholders = []

    def protect(m):
        placeholders.append(m.group(0))
        return f"__TAG_PLACEHOLDER_{len(placeholders)-1}__"

    protected = re.sub(rf"</?({tag_names})>", protect, text)

    protected = re.sub(r"(?<!&lt;)<", "&lt;", protected)
    protected = re.sub(r"(?<!&gt;)>", "&gt;", protected)

    def restore(m):
        idx = int(m.group(1))
        return placeholders[idx]

    return re.sub(r"__TAG_PLACEHOLDER_(\d+)__", restore, protected)

def convert_mark_tags_to_md_highlight(text: str) -> str:
    return re.sub(MARK_TAG_REGEX, lambda m: f"=={m.group(1)}==", text, flags=re.IGNORECASE | re.DOTALL)

def is_inside_any_embed_body(s: str, pos: int, component_tags=("<emailEmbed", "<asideEmbed", "<introEmbed")) -> bool:
    body_start = s.rfind('body={<>', 0, pos)
    if body_start == -1:
        return False

    window_start = max(0, body_start - 5000)
    pre_segment = s[window_start:body_start]
    if not any(tag in pre_segment for tag in component_tags):
        return False

    body_end = s.find('</>}', body_start)
    return body_end != -1 and pos < body_end

def keep_markdown_figure_with_prefix(m, src_prefix: str) -> str:
    figure = m.group(1).strip()
    raw_src = m.group(2).strip()
    src = add_prefix_if_relative(raw_src, src_prefix)
    return f'![Figure: {figure}]({src})'

def add_prefix_if_relative(raw_src: str, src_prefix: str) -> str:
    clean = clean_image_src(raw_src)
    if re.match(r'https?://', clean, flags=re.IGNORECASE):
        return clean
    clean = clean.lstrip('/')
    return f"{src_prefix}/{clean}"

def keep_image_block_with_prefixed_src(m, src_prefix: str) -> str:
    image_line = m.group(2)
    def _repl(md_img_m):
        alt = md_img_m.group(1).strip()
        raw_src = md_img_m.group(2).strip()
        new_src = add_prefix_if_relative(raw_src, src_prefix)
        return f'![{alt}]({new_src})'
    return re.sub(r'!\[(?:Figure:\s*)?(.*?)\]\((.*?)\)', _repl, image_line)

def keep_simple_block_with_prefixed_images(m, src_prefix: str) -> str:
    body = m.group(2)
    def _repl(md_img_m):
        alt = md_img_m.group(1).strip()
        raw_src = md_img_m.group(2).strip()
        new_src = add_prefix_if_relative(raw_src, src_prefix)
        return f'![{alt}]({new_src})'
    return re.sub(r'!\[(?:Figure:\s*)?(.*?)\]\((.*?)\)', _repl, body)

def replace_asset_link(m, src_prefix: str) -> str:
    text = m.group('text')
    href = m.group('href').strip()
    title = m.group('title')

    if re.match(r'^(https?:|mailto:|#|/)', href, flags=re.IGNORECASE):
        return m.group(0)

    if not re.search(r'\.(pdf|doc|docx|xls|xlsx|ppt|pptx|zip|mp4|mov|csv|txt)$', href, flags=re.IGNORECASE):
        return m.group(0)

    new_href = add_prefix_if_relative(href, src_prefix)
    return f'[{text}]({new_href} "{title}")' if title else f'[{text}]({new_href})'


# ----------------------------- #
# Replacements
# ----------------------------- #

def replace_youtube_block(m):
    url = m.group(1).strip()
    desc = m.group(2).strip() if m.group(2) else ""
    desc_js = js_string(desc)
    return f'\n<youtubeEmbed url="{url}" description={{{desc_js}}} />\n'

def replace_youtube_block_inside_intro(m):
    url = m.group(1).strip()
    desc = m.group(2).strip() if m.group(2) else ""
    desc_js = js_string(desc)
    return f'<introYoutube url="{url}" description={{{desc_js}}} />'

def wrap_intro_embed(m):
    fm = m.group('fm') or ''
    intro = m.group('intro') or ''

    intro_processed = intro.strip()
    intro_processed = re.sub(
        YOUTUBE_BLOCK_REGEX, replace_youtube_block_inside_intro,
        intro_processed, flags=re.MULTILINE
    )
    intro_processed = convert_angle_bracket_links(intro_processed)
    # intro_processed = escape_angle_brackets_except(intro_processed, allowed_tags=("mark",))

    return f'''{fm}<introEmbed
  body={{<>
{intro_processed}
  </>}}
/>
'''

def replace_image_block(m, src_prefix):
    preset = m.group(1).strip()
    image_line = m.group(2).strip()
    alt_match = re.match(r'!\[(?:Figure:\s*)?(.*?)\]\((.*?)\)', image_line)
    if not alt_match:
        return m.group(0)
    figure = alt_match.group(1).strip()
    raw_src = alt_match.group(2).strip()
    src = add_prefix_if_relative(raw_src, src_prefix)

    figure_js = js_string(figure)

    return f'''
<imageEmbed
  alt="Image"
  size="large"
  showBorder={{false}}
  figureEmbed={{ {{
    preset: "{preset}Example",
    figure: {figure_js},
    shouldDisplay: true
  }} }}
  src="{src}"
/>
'''


def replace_custom_size_image_block(m, src_prefix):
    variants_str = m.group(1).strip()
    figure_raw = m.group(2).strip()
    raw_src = m.group(3).strip()
    src = add_prefix_if_relative(raw_src, src_prefix)

    # Parse multiple variants (e.g., "img-small no-border")
    variants = variants_str.split()

    # Determine size
    size = "large"  # default
    for v in variants:
        if v in ("img-small", "small"):
            size = "small"
            break
        elif v in ("img-medium", "medium"):
            size = "medium"
            break
        elif v in ("img-large", "large"):
            size = "large"
            break

    # Determine border
    show_border = "false" if "no-border" in variants else "true"

    # If figure is empty, set shouldDisplay to false
    should_display = "true" if figure_raw else "false"
    figure_js = js_string(figure_raw)

    return f'''
<imageEmbed
  alt="Image"
  size="{size}"
  showBorder={{{show_border}}}
  figureEmbed={{ {{
    preset: "default",
    figure: {figure_js},
    shouldDisplay: {should_display}
  }} }}
  src="{src}"
/>
'''


def replace_standalone_image(m, src_prefix):
    figure = m.group(1).strip()
    raw_src = m.group(2).strip()
    src = add_prefix_if_relative(raw_src, src_prefix)
    figure_js = js_string(figure)

    return f'''
<imageEmbed
  alt="Image"
  size="large"
  showBorder={{false}}
  figureEmbed={{ {{
    preset: "default",
    figure: {figure_js},
    shouldDisplay: true
  }} }}
  src="{src}"
/>
'''

def replace_preset_and_size_image_block(m, src_prefix):
    # Extract preset and size from either order
    preset_kind = m.group('preset1') or m.group('preset2')
    variant = m.group('size1') or m.group('size2')
    figure_raw = m.group('figure').strip()
    raw_src = m.group('src').strip()

    size = {
        "img-small": "small",
        "img-medium": "medium",
        "img-large": "large",
        "small": "small",
        "medium": "medium",
        "large": "large",
        "no-border": "large"
    }.get(variant, "large")

    show_border = "false" if variant == "no-border" else "true"
    src = add_prefix_if_relative(raw_src, src_prefix)
    figure_js = js_string(figure_raw)

    return f'''
<imageEmbed
  alt="Image"
  size="{size}"
  showBorder={{{show_border}}}
  figureEmbed={{ {{
    preset: "{preset_kind}Example",
    figure: {figure_js},
    shouldDisplay: true
  }} }}
  src="{src}"
/>
'''


def replace_email_block(m):
    table = m.group(1)
    body = m.group(2).strip()
    figure_block = m.group(3)

    email_data = parse_email_table(table)
    cleaned_body = clean_email_body(body)

    preset_match = re.match(r'::: (good|bad|ok)', figure_block.strip())
    preset = f"{preset_match.group(1)}Example" if preset_match else "default"

    figure_match = re.search(r'Figure:\s*(.*)', figure_block)
    raw_figure = figure_match.group(1).strip() if figure_match else "Example"

    figure_js = js_string(raw_figure)
    from_js = js_string(email_data['from'])
    to_js = js_string(email_data['to'])
    cc_js = js_string(email_data['cc'])
    bcc_js = js_string(email_data['bcc'])
    subject_js = js_string(email_data['subject'])

    should_display = 'Figure:' in figure_block

    return f'''
<emailEmbed
  from={from_js}
  to={to_js}
  cc={cc_js}
  bcc={bcc_js}
  subject={subject_js}
  body={{<>
    {cleaned_body}
  </>}}
  figureEmbed={{ {{
    preset: "{preset}",
    figure: {figure_js},
    shouldDisplay: {"true" if should_display else "false"}
  }} }}
/>
'''

def replace_email_block_no_rating(m):
    table = m.group(1)
    body = m.group(2).strip()
    figure_text = (m.group(3) or "").strip()

    email_data = parse_email_table(table)
    cleaned_body = clean_email_body(body)

    preset = "default"
    figure_js = js_string(figure_text if figure_text else "Example")
    from_js = js_string(email_data['from'])
    to_js = js_string(email_data['to'])
    cc_js = js_string(email_data['cc'])
    bcc_js = js_string(email_data['bcc'])
    subject_js = js_string(email_data['subject'])

    should_display = bool(figure_text)

    return f'''
<emailEmbed
  from={from_js}
  to={to_js}
  cc={cc_js}
  bcc={bcc_js}
  subject={subject_js}
  body={{<>
    {cleaned_body}
  </>}}
  figureEmbed={{ {{
    preset: "{preset}",
    figure: {figure_js},
    shouldDisplay: {"true" if should_display else "false"}
  }} }}
/>
'''

def replace_simple_figure_block(m):
    preset = m.group(1).strip()
    figure = m.group(2).strip()
    figure_js = js_string(figure)
    return f'''<figureEmbed figureEmbed={{ {{
  preset: "{preset}Example",
  figure: {figure_js},
  shouldDisplay: true
}} }} />\n'''


def process_custom_aside_blocks(content):
    lines = content.splitlines()
    output = []
    i = 0
    in_box = False
    box_type = ""
    buffer = []
    box_indent = 0

    while i < len(lines):
        line = lines[i].rstrip()

        match_start = re.match(r"^(\s*):::\s*(greybox|highlight|china|info|todo|codeauditor|tips|warning)\s*$", line)
        if match_start and not in_box:
            in_box = True
            box_type = match_start.group(2)
            box_indent = len(match_start.group(1))
            buffer = []
            # Add blank line before aside if it's indented (nested in a list)
            if box_indent > 0 and output and output[-1].strip() != '':
                output.append('')
            i += 1
            continue

        if in_box and re.match(r"^\s*:::\s*$", line):

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
                        and (match_l1 := re.match(r"^\s*:::\s*(good|bad|ok)\s*$", lines[i + 1]))
                        and (match_l2 := re.match(r"^\s*Figure:\s*(.*?)\s*$", lines[i + 2]))
                        and re.match(r"^\s*:::\s*$", lines[i + 3])
                    ):
                        preset = f"{match_l1.group(1)}Example"
                        figure = match_l2.group(1).strip()
                        show = True
                        i += 3

            # Remove the indentation from buffer content
            cleaned_buffer = []
            for buf_line in buffer:
                if buf_line.startswith(' ' * box_indent):
                    cleaned_buffer.append(buf_line[box_indent:])
                else:
                    cleaned_buffer.append(buf_line)

            body = '\n'.join(cleaned_buffer)
            body = mdx_safe_template_vars(body)
            body = convert_angle_bracket_links(body)
            body = escape_angle_brackets_except(body, allowed_tags=("mark",))

            figure_js = js_string(figure)
            embed = f'''
<asideEmbed
  variant="{box_type}"
  body={{<>
    {body}
  </>}}
  figureEmbed={{{{
    preset: "{preset}",
    figure: {figure_js},
    shouldDisplay: {"true" if show else "false"}
  }}}}
/>
'''
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


def transform_email_blocks(content: str) -> str:
    # First, handle email templates WITHOUT email-content (body-less templates)
    no_body_pat = re.compile(
        r'::: email-template\s+(.*?)'
        r':::\s*(?=\n)',
        re.DOTALL
    )

    # Then, handle email templates WITH email-content
    with_body_pat = re.compile(
        r'::: email-template\s+(.*?)'
        r'::: email-content\s+(.*?)'
        r':::\s+:::',
        re.DOTALL
    )

    # Process all email templates in order
    all_matches = []

    # Find all matches with body
    for m in with_body_pat.finditer(content):
        all_matches.append(('with_body', m))

    # Find all matches without body
    for m in no_body_pat.finditer(content):
        # Check if this match is not part of a with_body match
        is_part_of_with_body = False
        for match_type, other_m in all_matches:
            if match_type == 'with_body' and m.start() >= other_m.start() and m.end() <= other_m.end():
                is_part_of_with_body = True
                break
        if not is_part_of_with_body:
            all_matches.append(('no_body', m))

    # Sort by start position
    all_matches.sort(key=lambda x: x[1].start())

    out = []
    idx = 0

    for match_type, m in all_matches:
        out.append(content[idx:m.start()])

        table = m.group(1)

        if match_type == 'with_body':
            body = m.group(2).strip()
            should_display_body = True
        else:
            body = ""
            should_display_body = False

        tail = content[m.end():]

        rating_m = re.match(r'\s*(:::\s*(good|bad|ok).*?:::)', tail, re.DOTALL)
        preset = "default"
        figure_text = ""
        consumed = 0
        should_display = False

        if rating_m:
            rating_full = rating_m.group(1)
            rating_kind = rating_m.group(2)
            preset = f"{rating_kind}Example"

            fig_in_rating = re.search(r'Figure:\s*(.*)', rating_full)
            if fig_in_rating:
                figure_text = fig_in_rating.group(1).strip()
                should_display = True
            consumed = rating_m.end()
        else:
            fig_m = re.match(r'\s*\*\*Figure:\s*(.*?)\*\*', tail, re.DOTALL)
            if fig_m:
                figure_text = fig_m.group(1).strip()
                should_display = True
                consumed = fig_m.end()

        email_data = parse_email_table(table)
        cleaned_body = clean_email_body(body) if body else ""

        from_js    = js_string(email_data['from'])
        to_js      = js_string(email_data['to'])
        cc_js      = js_string(email_data['cc'])
        bcc_js     = js_string(email_data['bcc'])
        subject_js = js_string(email_data['subject'])
        figure_js  = js_string(figure_text if figure_text else "Example")

        should_display_body_js = "true" if should_display_body else "false"
        should_display_js = "true" if should_display else "false"

        embed = f'''<emailEmbed
  from={from_js}
  to={to_js}
  cc={cc_js}
  bcc={bcc_js}
  subject={subject_js}
  shouldDisplayBody={{{should_display_body_js}}}
  body={{<>
    {cleaned_body}
  </>}}
  figureEmbed={{{{
    preset: "{preset}",
    figure: {figure_js},
    shouldDisplay: {should_display_js}
  }}}}
/>'''

        out.append(embed)
        idx = m.end() + consumed

    out.append(content[idx:])
    return ''.join(out)


# ----------------------------- #
# Main Transform Function
# ----------------------------- #

def transform_md_to_mdx(file_path, rule_to_categories=None, category_uri_to_path=None, auto_load_categories=True):
    path = Path(file_path)
    if not path.exists():
        print(f"File not found: {file_path}")
        return

    folder_name = path.parent.name
    src_prefix = f"{SRC_PREFIX_BASE}{folder_name}"
    content = path.read_text(encoding='utf-8')

    content = re.sub(r'<!--\s*StartFragment\s*-->', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<!--\s*EndFragment\s*-->', '', content, flags=re.IGNORECASE)

    content = convert_mark_tags_to_md_highlight(content)
    content = mdx_safe_template_vars(content)
    content = re.sub(INTRO_WITH_FM_REGEX, wrap_intro_embed, content, flags=re.IGNORECASE | re.DOTALL)

    content = process_custom_aside_blocks(content)
    content = re.sub(YOUTUBE_BLOCK_REGEX, replace_youtube_block, content, flags=re.MULTILINE)
    content = re.sub(PRESET_AND_SIZE_IMAGE_BLOCK_REGEX, lambda m: replace_preset_and_size_image_block(m, src_prefix), content, flags=re.MULTILINE | re.DOTALL)

    def _replace_image_block_conditional(m):
        if is_inside_any_embed_body(content, m.start(), component_tags=("<emailEmbed", "<asideEmbed", "<introEmbed")):
            return keep_image_block_with_prefixed_src(m, src_prefix)
        return replace_image_block(m, src_prefix)
    content = re.sub(IMAGE_BLOCK_REGEX, _replace_image_block_conditional, content, flags=re.MULTILINE | re.DOTALL)

    content = transform_email_blocks(content)
    content = re.sub(CUSTOM_SIZE_IMAGE_BLOCK_REGEX, lambda m: replace_custom_size_image_block(m, src_prefix), content, flags=re.MULTILINE | re.DOTALL)

    def _replace_standalone_image_conditional(m):
        if is_inside_any_embed_body(content, m.start()):
            return keep_markdown_figure_with_prefix(m, src_prefix)
        return replace_standalone_image(m, src_prefix)
    content = re.sub(STANDALONE_IMAGE_REGEX, _replace_standalone_image_conditional, content)

    def _replace_simple_figure_block_conditional(m):
        if is_inside_any_embed_body(content, m.start(), component_tags=("<emailEmbed", "<asideEmbed", "<introEmbed")):
            body = m.group(2)
            if re.search(r'!\[(?:Figure:\s*)?.*?\]\(.*?\)', body):
                return keep_simple_block_with_prefixed_images(m, src_prefix)
            return m.group(0)
        return replace_simple_figure_block(m)
    content = re.sub(SIMPLE_FIGURE_BLOCK_REGEX, _replace_simple_figure_block_conditional, content, flags=re.MULTILINE | re.DOTALL)


    content = re.sub(RAW_IMAGE_REGEX, lambda m: prefix_raw_image_src(m, src_prefix), content)
    content = re.sub(ASSET_LINK_REGEX, lambda m: replace_asset_link(m, src_prefix), content)
    content = convert_angle_bracket_links(content)


    if path.suffix.lower() == '.mdx':
        output_path = path
    else:
        output_path = path.with_suffix('.mdx')

    output_path.write_text(content, encoding='utf-8')
    print(f"Transformed content saved to: {output_path}")
    
    # Add categories to the newly converted MDX file
    # If mappings not provided but auto_load is enabled, try to load them
    if auto_load_categories and (rule_to_categories is None or category_uri_to_path is None):
        try:
            script_dir = Path(__file__).parent
            repo_root = script_dir.parent.parent
            rule_to_cats_path = repo_root / 'rule-to-categories.json'
            
            if rule_to_cats_path.exists():
                with open(rule_to_cats_path, 'r', encoding='utf-8') as f:
                    rule_to_categories = json.load(f)
                category_uri_to_path = build_category_uri_to_path_map()
                print("[INFO] Auto-loaded category mappings.")
            else:
                print(f"[WARNING] rule-to-categories.json not found, skipping category updates.")
        except Exception as e:
            print(f"[WARNING] Failed to auto-load categories: {e}")
    
    # Add categories if mappings are available
    if rule_to_categories is not None and category_uri_to_path is not None:
        try:
            update_mdx_categories(str(output_path), rule_to_categories, category_uri_to_path)
        except Exception as e:
            print(f"[WARNING] Failed to add categories to {output_path}: {e}")
    

    if path.suffix.lower() == '.md':
        path.unlink()  # delete original .md file

def transform_all_mds(base_dir=DEFAULT_BASE_DIR, file_name=DEFAULT_FILE_NAME, add_categories=True):
    """
    Transform all Markdown (.md) files in each subdirectory of the given base directory.

    :param base_dir: The base directory containing rule folders.
    :param file_name: The specific file name to look for in each folder. If None, process any .md file.
    :param add_categories: If True, load category mappings and add categories to converted MDX files.
    """
    start_time = time.time()
    base_path = Path(base_dir)
    if not base_path.exists():
        print(f"Base path not found: {base_dir}")
        return

    # Load category mappings if requested
    rule_to_categories = None
    category_uri_to_path = None
    if add_categories:
        script_dir = Path(__file__).parent
        repo_root = script_dir.parent.parent
        rule_to_cats_path = repo_root / 'rule-to-categories.json'
        
        if rule_to_cats_path.exists():
            with open(rule_to_cats_path, 'r', encoding='utf-8') as f:
                rule_to_categories = json.load(f)
            print("[INFO] Loaded rule-to-categories mapping.")
            category_uri_to_path = build_category_uri_to_path_map()
            print(f"[INFO] Built category URI to path mapping ({len(category_uri_to_path)} categories).")
        else:
            print(f"[WARNING] rule-to-categories.json not found, skipping category updates.")

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
                md_files = [f for f in rule_dir.glob('*.mdx') if f.name not in IGNORE_FILES]
                if not md_files:
                    md_files = [f for f in rule_dir.glob('*.md') if f.name not in IGNORE_FILES]
                if not md_files:
                    print(f"[WARNING] No .md/mdx files found in: {rule_dir}")
                    continue
                rule_md = md_files[0]  # Process the first .md file found

            print(f"[INFO] Processing: {rule_md}")
            try:
                # Pass auto_load_categories=False since we already loaded them if requested
                transform_md_to_mdx(rule_md, rule_to_categories, category_uri_to_path, auto_load_categories=False)
                count += 1
            except Exception as e:
                print(f"[ERROR] Failed to process {rule_md}: {e}")

    end_time = time.time()
    elapsed = end_time - start_time
    print(f"\n✅ Finished processing {count} rule files in {elapsed:.2f} seconds.")


# ----------------------------- #
# Category Update Functions
# ----------------------------- #

def extract_frontmatter(content):
    """Extract frontmatter from MDX content."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        return match.group(1)
    return None

def parse_frontmatter(fm_text):
    """Parse YAML-like frontmatter into a dictionary, preserving structure."""
    lines = fm_text.split('\n')
    data = {}
    current_list_key = None
    current_list_item = None
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        indent = len(line) - len(line.lstrip())
        base_indent = 0
        
        # Skip empty lines
        if not stripped:
            i += 1
            continue
        
        # Determine base indent for lists (first list item)
        if current_list_key and not current_list_item:
            # Find first list item indent
            for j in range(i, len(lines)):
                if lines[j].strip().startswith('-'):
                    base_indent = len(lines[j]) - len(lines[j].lstrip())
                    break
        
        # Handle list items (indented with -)
        if stripped.startswith('- '):
            if current_list_key:
                list_item = stripped[2:].strip()
                # Handle object items in list (categories with category field, or other objects)
                if ':' in list_item:
                    # Simple key-value on same line
                    key, val = list_item.split(':', 1)
                    key = key.strip()
                    val = val.strip()
                    # Check if next line is indented (nested object)
                    if i + 1 < len(lines):
                        next_line = lines[i + 1]
                        next_indent = len(next_line) - len(next_line.lstrip())
                        if next_indent > base_indent and ':' in next_line.strip():
                            # Start of nested object
                            current_list_item = {key: val}
                            data[current_list_key].append(current_list_item)
                        else:
                            # Simple key-value pair
                            if current_list_key not in data:
                                data[current_list_key] = []
                            if 'category:' in list_item:
                                cat_value = list_item.split(':', 1)[1].strip()
                                data[current_list_key].append({'category': cat_value})
                            else:
                                data[current_list_key].append(list_item)
                    else:
                        # Last line, simple key-value
                        if current_list_key not in data:
                            data[current_list_key] = []
                        if 'category:' in list_item:
                            cat_value = list_item.split(':', 1)[1].strip()
                            data[current_list_key].append({'category': cat_value})
                        else:
                            data[current_list_key].append(list_item)
                else:
                    # Simple string item
                    if current_list_key not in data:
                        data[current_list_key] = []
                    data[current_list_key].append(list_item)
            i += 1
            continue
        
        # Handle nested object properties (indented key-value within list item)
        if current_list_item and indent > base_indent and ':' in stripped:
            key, value = stripped.split(':', 1)
            key = key.strip()
            value = value.strip()
            current_list_item[key] = value
            i += 1
            continue
        
        # Reset list state when we encounter a new top-level key
        current_list_item = None
        current_list_key = None
        
        if ':' in stripped and indent == 0:
            key, value = stripped.split(':', 1)
            key = key.strip()
            value = value.strip()
            
            # Check if next line is a list (indented with -)
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                next_indent = len(next_line) - len(next_line.lstrip())
                if next_indent > 0 and next_line.strip().startswith('-'):
                    current_list_key = key
                    data[key] = []
                    i += 1
                    continue
            
            data[key] = value
        
        i += 1
    
    return data

def format_frontmatter(data):
    """Format dictionary back into YAML-like frontmatter string."""
    lines = []
    keys = list(data.keys())
    
    for i, key in enumerate(keys):
        value = data[key]
        if isinstance(value, list):
            if len(value) == 0:
                lines.append(f"{key}: []")
            else:
                lines.append(f"{key}:")
                for item in value:
                    if isinstance(item, dict):
                        # Handle category objects with nested properties
                        for sub_key, sub_value in item.items():
                            lines.append(f"  - {sub_key}: {sub_value}")
                    else:
                        lines.append(f"  - {item}")
        elif isinstance(value, dict):
            lines.append(f"{key}:")
            for sub_key, sub_value in value.items():
                lines.append(f"  {sub_key}: {sub_value}")
        else:
            # Preserve original formatting for simple values
            lines.append(f"{key}: {value}")
    
    return '\n'.join(lines)

def build_category_uri_to_path_map(categories_root='categories'):
    """Build a mapping from category URI to full category file path."""
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    categories_path = repo_root / categories_root
    pattern = str(categories_path / '**' / '*.mdx')
    mdx_files = glob.glob(pattern, recursive=True)
    
    mdx_files = [f for f in mdx_files if not f.endswith('index.mdx')]
    uri_to_path = {}
    
    for file_path in mdx_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        fm_text = extract_frontmatter(content)
        if not fm_text:
            continue
        
        fm_data = parse_frontmatter(fm_text)
        category_uri = fm_data.get('uri', '')
        
        if category_uri:
            # Convert absolute path to relative path from repo root
            rel_path = Path(file_path).relative_to(repo_root)
            # Normalize to forward slashes for cross-platform compatibility
            rel_path_str = str(rel_path).replace('\\', '/')
            uri_to_path[category_uri] = rel_path_str
    
    return uri_to_path

def update_mdx_categories(mdx_file_path, rule_to_categories, category_uri_to_path):
    """Update or add categories to an MDX file's frontmatter, placing it directly under the title field."""
    path = Path(mdx_file_path)
    if not path.exists():
        print(f"[WARNING] File not found: {mdx_file_path}")
        return False
    
    content = path.read_text(encoding='utf-8')
    
    # Extract frontmatter with better regex to preserve formatting
    fm_match = re.match(r'^(---\s*\n)(.*?)(\n---\s*\n)', content, re.DOTALL)
    if not fm_match:
        print(f"[WARNING] No frontmatter found in: {mdx_file_path}")
        return False
    
    fm_prefix = fm_match.group(1)
    fm_text = fm_match.group(2)
    fm_suffix = fm_match.group(3)
    body = content[fm_match.end():]
    
    # Split frontmatter into lines for precise manipulation
    fm_lines = fm_text.split('\n')
    
    # Get rule URI - try parsing just the uri field
    rule_uri = None
    for line in fm_lines:
        if line.strip().startswith('uri:'):
            rule_uri = line.split(':', 1)[1].strip()
            break
    
    if not rule_uri:
        # Try to get URI from folder name
        rule_uri = path.parent.name
    
    if not rule_uri:
        print(f"[WARNING] Could not determine rule URI for: {mdx_file_path}")
        return False
    
    # Get categories for this rule
    category_uris = rule_to_categories.get(rule_uri, [])
    if not category_uris:
        # No categories to add, skip
        return False
    
    # Extract existing categories and their paths
    existing_category_paths = set()
    categories_start_idx = None
    categories_end_idx = None
    in_categories_block = False
    categories_indent = None
    
    for i, line in enumerate(fm_lines):
        stripped = line.strip()
        indent_i = len(line) - len(line.lstrip())
        if stripped.startswith('categories:') and indent_i == 0:
            categories_start_idx = i
            in_categories_block = True
            categories_indent = indent_i
            continue
        elif in_categories_block:
            # Determine end of categories block: any line with indent <= categories_indent
            # or a new top-level key or list item signals the end
            if not stripped:
                continue
            if indent_i <= (categories_indent or 0):
                categories_end_idx = i
                in_categories_block = False
                continue
            if stripped.startswith('- '):
                # Treat as a categories list item only if it's more indented than the 'categories:' line
                # (expected list items are indented)
                if indent_i > (categories_indent or 0):
                    if stripped.startswith('- category:'):
                        cat_path = stripped.split(':', 1)[1].strip()
                        existing_category_paths.add(cat_path)
                    else:
                        cat_val = stripped[2:].strip()
                        existing_category_paths.add(cat_val)
                else:
                    # A top-level '- ' means categories block ended before this line
                    categories_end_idx = i
                    in_categories_block = False
                    continue
            else:
                # Non-list, still within categories indentation -> treat as continuation of categories item
                # Do nothing for extraction
                pass
    
    if in_categories_block:
        categories_end_idx = len(fm_lines)
    
    # Build new categories list
    new_categories_to_add = []

    # Find title line index and determine where title ends (handle multi-line titles)
    title_idx = None
    title_end_idx = None
    for i, line in enumerate(fm_lines):
        indent_i = len(line) - len(line.lstrip())
        if indent_i == 0 and line.strip().startswith('title:'):
            title_idx = i
            # Extract the title value part (after 'title:')
            title_line = line
            title_parts = line.split(':', 1)
            if len(title_parts) > 1:
                title_value_after_colon = title_parts[1].strip()
            else:
                title_value_after_colon = ''
            
            # In YAML, title can be on one line or span multiple lines
            # If title value ends with a quote or looks complete, it's single line
            # If the line doesn't end properly, it might continue
            title_end_idx = i + 1  # Default: title ends on next line
            
            # Check if title continues on next lines (YAML multi-line values are indented)
            j = i + 1
            while j < len(fm_lines):
                next_line = fm_lines[j]
                stripped_next = next_line.strip()
                
                # Skip empty lines
                if not stripped_next:
                    j += 1
                    continue
                
                # Check indentation - if next line is indented, it might be continuation
                indent = len(next_line) - len(next_line.lstrip())
                
                # If line starts with a valid YAML key (no indent, has colon, valid key name), title ended
                if indent == 0 and ':' in stripped_next:
                    key_part = stripped_next.split(':', 1)[0].strip()
                    # Valid key format (alphanumeric, dash, underscore)
                    if key_part and all(c.isalnum() or c in '-_' for c in key_part.replace(' ', '')):
                        # This is a new key, title ended at previous line
                        title_end_idx = j
                        break
                
                # If not indented and looks like content that should be part of title but isn't,
                # it might be a broken title (like "audience?" on its own line)
                # But we can't reliably detect this, so we'll assume any non-indented line with ':'
                # that looks like a key is a new field
                
                # For indented lines without ':', they could be title continuation
                # But we'll be conservative: only treat as continuation if clearly indented
                if indent > 0 and ':' not in stripped_next:
                    # Might be continuation, continue checking
                    j += 1
                    continue
                
                # If we get here and it's not clearly a continuation, assume title ended
                if indent == 0:
                    title_end_idx = j
                    break
                
                j += 1
            
            # Special case: detect broken titles where continuation appears as unindented text
            # (e.g., "title: Some text" followed by "more text?" on next line)
            if j < len(fm_lines) and title_end_idx == i + 1:
                # Check if title line doesn't end with punctuation and next line looks like continuation
                title_line_ends_with_punct = title_value_after_colon and title_value_after_colon[-1] in '.!?'
                if not title_line_ends_with_punct and j < len(fm_lines):
                    next_non_empty = None
                    for k in range(i + 1, min(j + 3, len(fm_lines))):
                        if fm_lines[k].strip() and not fm_lines[k].strip().startswith('categories:'):
                            next_non_empty = fm_lines[k]
                            break
                    
                    if next_non_empty:
                        next_stripped = next_non_empty.strip()
                        # If next line doesn't look like a YAML key (no colon or invalid key format)
                        # and title doesn't look complete, it might be continuation
                        is_valid_key = False
                        if ':' in next_stripped:
                            key_part = next_stripped.split(':', 1)[0].strip()
                            if key_part:
                                is_valid_key = any(c.isalnum() or c in '-_' for c in key_part)
                        if not is_valid_key:
                            indent_next = len(next_non_empty) - len(next_non_empty.lstrip())
                            # If not indented and looks like text (not a key), might be broken title
                            if indent_next == 0:
                                # Look ahead to find where the next actual key starts
                                for k in range(j, len(fm_lines)):
                                    check_line = fm_lines[k]
                                    if check_line.strip() and ':' in check_line.strip():
                                        key_check = check_line.strip().split(':', 1)[0].strip()
                                        if key_check and all(c.isalnum() or c in '-_' for c in key_check.replace(' ', '')):
                                            title_end_idx = k
                                            break
                                # If we didn't find a clear key, include the continuation line
                                if title_end_idx == i + 1 and j < len(fm_lines):
                                    title_end_idx = j + 1
            
            # If we didn't find a clear end, title ends after the title line itself
            if title_end_idx > len(fm_lines):
                title_end_idx = i + 1
            break
    
    if title_idx is None:
        print(f"[WARNING] Could not find 'title:' field in: {mdx_file_path}")
        return False
    
    # Sync categories: use only the categories from the mapping (remove extras, add missing)
    expected_category_paths = set()
    for category_uri in category_uris:
        category_path = category_uri_to_path.get(category_uri)
        if category_path:
            expected_category_paths.add(category_path)
        elif not category_path:
            print(f"[WARNING] Could not find path for category URI: {category_uri} for rule: {rule_uri}")
    
    # If no categories expected and none exist, nothing to do
    if not expected_category_paths and not existing_category_paths:
        return False
    
    # Determine if update is needed (categories differ from expected or incorrectly placed)
    categories_differ = expected_category_paths != existing_category_paths
    categories_incorrectly_placed = False

    if categories_start_idx is not None:
        indent_categories = len(fm_lines[categories_start_idx]) - len(fm_lines[categories_start_idx].lstrip())
        # Consider incorrect if nested (indented) or not placed immediately after the title block
        if indent_categories > 0 or categories_start_idx != title_end_idx:
            categories_incorrectly_placed = True
    
    # If categories match and are correctly placed, no update needed
    if not categories_differ and not categories_incorrectly_placed:
        return False
    
    # Build new frontmatter lines - preserve everything exactly except categories placement
    new_fm_lines = []
    insert_after_idx = title_end_idx

    # Determine what to skip (the old categories block if it exists)
    skip_range = set()
    if categories_start_idx is not None:
        skip_range = set(range(categories_start_idx, categories_end_idx))

    # Rebuild frontmatter lines and insert categories after the chosen block
    inserted = False
    for i in range(len(fm_lines)):
        if i in skip_range:
            continue
        new_fm_lines.append(fm_lines[i])
        if not inserted and i == insert_after_idx - 1:
            if expected_category_paths:
                new_fm_lines.append('categories:')
                for cat_path in sorted(expected_category_paths):
                    new_fm_lines.append(f"  - category: {cat_path}")
            inserted = True

    # If we need to insert at EOF (e.g., authors at the end)
    if not inserted and insert_after_idx >= len(fm_lines):
        if expected_category_paths:
            new_fm_lines.append('categories:')
            for cat_path in sorted(expected_category_paths):
                new_fm_lines.append(f"  - category: {cat_path}")
    
    # Reconstruct the file
    new_fm_text = '\n'.join(new_fm_lines)
    new_content = fm_prefix + new_fm_text + fm_suffix + body
    
    path.write_text(new_content, encoding='utf-8')
    return True

def update_all_mdx_categories(rules_dir='public/uploads/rules', rule_to_categories_file='rule-to-categories.json'):
    """Update categories in all rule.mdx files."""
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    
    # Load rule-to-categories mapping
    rule_to_cats_path = repo_root / rule_to_categories_file
    if not rule_to_cats_path.exists():
        print(f"[ERROR] rule-to-categories.json not found at: {rule_to_cats_path}")
        return
    
    with open(rule_to_cats_path, 'r', encoding='utf-8') as f:
        rule_to_categories = json.load(f)
    
    # Build category URI to path mapping
    print("[INFO] Building category URI to path mapping...")
    category_uri_to_path = build_category_uri_to_path_map()
    print(f"[INFO] Found {len(category_uri_to_path)} categories.")
    
    # Find all rule.mdx files
    rules_path = repo_root / rules_dir
    if not rules_path.exists():
        print(f"[ERROR] Rules directory not found: {rules_path}")
        return
    
    pattern = str(rules_path / '**' / 'rule.mdx')
    mdx_files = glob.glob(pattern, recursive=True)
    
    print(f"[INFO] Found {len(mdx_files)} rule.mdx files.")
    print("[INFO] Updating categories...")
    
    updated_count = 0
    skipped_count = 0
    
    for mdx_file in mdx_files:
        try:
            updated = update_mdx_categories(mdx_file, rule_to_categories, category_uri_to_path)
            if updated:
                updated_count += 1
                print(f"[INFO] Updated: {mdx_file}")
            else:
                skipped_count += 1
        except Exception as e:
            print(f"[ERROR] Failed to process {mdx_file}: {e}")
    
    print(f"\n✅ Finished updating categories.")
    print(f"   Updated: {updated_count} files")
    print(f"   Skipped: {skipped_count} files")

# ----------------------------- #
# Entry Point
# ----------------------------- #

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--update-categories':
            rules_dir = sys.argv[2] if len(sys.argv) > 2 else 'public/uploads/rules'
            update_all_mdx_categories(rules_dir)
        elif sys.argv[1] == '--add-categories':
            # Add categories flag for MD to MDX conversion
            if len(sys.argv) > 2:
                arg = sys.argv[2]
                path = Path(arg)
                if path.is_file():
                    # For single file, load mappings
                    script_dir = Path(__file__).parent
                    repo_root = script_dir.parent.parent
                    rule_to_cats_path = repo_root / 'rule-to-categories.json'
                    rule_to_categories = None
                    category_uri_to_path = None
                    if rule_to_cats_path.exists():
                        with open(rule_to_cats_path, 'r', encoding='utf-8') as f:
                            rule_to_categories = json.load(f)
                        category_uri_to_path = build_category_uri_to_path_map()
                    transform_md_to_mdx(arg, rule_to_categories, category_uri_to_path)
                elif path.is_dir():
                    file_name = sys.argv[3] if len(sys.argv) > 3 else None
                    transform_all_mds(arg, file_name, add_categories=True)
                else:
                    print(f"Error: The provided path '{arg}' is neither a file nor a directory.")
            else:
                transform_all_mds(add_categories=True)
        else:
            arg = sys.argv[1]
            path = Path(arg)
            if path.is_file():
                # For single file, auto-load categories by default
                transform_md_to_mdx(arg, auto_load_categories=True)
            elif path.is_dir():
                file_name = sys.argv[2] if len(sys.argv) > 2 else None
                # Categories enabled by default
                transform_all_mds(arg, file_name, add_categories=True)
            else:
                print(f"Error: The provided path '{arg}' is neither a file nor a directory.")
    else:
        # Categories enabled by default
        transform_all_mds(add_categories=True)