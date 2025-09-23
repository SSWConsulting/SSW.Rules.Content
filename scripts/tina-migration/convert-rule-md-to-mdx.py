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
import json

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
EMAIL_BLOCK_NO_RATING_REGEX = (
    r'::: email-template\s+(.*?)'
    r'::: email-content\s+(.*?)'
    r':::\s+:::\s*'
    r'(?:\*\*Figure:\s*(.*?)\*\*\s*)?'
)
SIMPLE_FIGURE_BLOCK_REGEX = r':::\s*(good|bad|ok)\s*\n(.*?)\n:::' 
CUSTOM_SIZE_IMAGE_BLOCK_REGEX = r':::\s*(img-small|img-medium|img-large|no-border)\s*\n\s*!\[Figure:\s*(.*?)\]\((.*?)\)\s*:::'
RAW_IMAGE_REGEX = r'!\[(?!Figure:)(.*?)\]\((.*?)\)'
INTRO_WITH_FM_REGEX = r'^(?P<fm>---\s*\n.*?\n---\s*\n)?(?P<intro>.*?)(?:\r?\n)?<!--\s*endintro\s*-->\s*'
PRESET_CUSTOM_SIZE_IMAGE_BLOCK_REGEX = r':::\s*(good|bad|ok)\s+(img-small|img-medium|img-large|no-border)\s*\n\s*!\[Figure:\s*(.*?)\]\((.*?)\)\s*:::'
MARK_TAG_REGEX = r'<\s*mark\b[^>]*>(.*?)<\s*/\s*mark\s*>'

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

    if clean_src.startswith('/') or clean_src.startswith('http'):
        return m.group(0)

    prefixed_src = f"{src_prefix}/{clean_src}"
    return f'![{alt_text}]({prefixed_src})'

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

def is_inside_any_embed_body(s: str, pos: int, component_tags=("<emailEmbed", "<asideEmbed")) -> bool:
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
    if clean.startswith('/') or re.match(r'https?://', clean, flags=re.IGNORECASE):
        return clean
    return f"{src_prefix}/{clean}"


# ----------------------------- #
# Replacements
# ----------------------------- #

def replace_youtube_block(m):
    url = m.group(1).strip()
    desc = m.group(2).strip() if m.group(2) else ""
    desc_js = js_string(desc)
    return f'<youtubeEmbed url="{url}" description={{{desc_js}}} />'

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
    alt_match = re.match(r'!\[Figure:\s*(.*?)\]\((.*?)\)', image_line)
    if not alt_match:
        return m.group(0)
    figure = alt_match.group(1).strip()
    raw_src = alt_match.group(2).strip()
    src = add_prefix_if_relative(raw_src, src_prefix)

    figure_js = js_string(figure)

    return f'''<imageEmbed
  alt="Image"
  size="large"
  showBorder={{false}}
  figureEmbed={{ {{
    preset: "{preset}Example",
    figure: {figure_js},
    shouldDisplay: true
  }} }}
  src="{src}"
/>'''


def replace_custom_size_image_block(m, src_prefix):
    variant = m.group(1).strip()
    figure_raw = m.group(2).strip()
    raw_src = m.group(3).strip()
    src = add_prefix_if_relative(raw_src, src_prefix)

    size = {
        "img-small": "small",
        "img-medium": "medium",
        "img-large": "large",
        "no-border": "large"
    }.get(variant, "large")

    show_border = "false" if variant == "no-border" else "true"
    figure_js = js_string(figure_raw)

    return f'''<imageEmbed
  alt="Image"
  size="{size}"
  showBorder={{{show_border}}}
  figureEmbed={{ {{
    preset: "default",
    figure: {figure_js},
    shouldDisplay: true
  }} }}
  src="{src}"
/>'''


def replace_standalone_image(m, src_prefix):
    figure = m.group(1).strip()
    raw_src = m.group(2).strip()
    src = add_prefix_if_relative(raw_src, src_prefix)
    figure_js = js_string(figure)

    return '\n' + f'''<imageEmbed
  alt="Image"
  size="large"
  showBorder={{false}}
  figureEmbed={{ {{
    preset: "default",
    figure: {figure_js},
    shouldDisplay: true
  }} }}
  src="{src}"
/>'''

def replace_preset_custom_size_image_block(m, src_prefix):
    preset_kind = m.group(1).strip()        # good / bad / ok
    variant = m.group(2).strip()            # img-small / img-medium / img-large / no-border
    figure_raw = m.group(3).strip()
    raw_src = m.group(4).strip()

    size = {
        "img-small": "small",
        "img-medium": "medium",
        "img-large": "large",
        "no-border": "large"
    }.get(variant, "large")

    show_border = "false" if variant == "no-border" else "true"
    src = add_prefix_if_relative(raw_src, src_prefix)
    figure_js = js_string(figure_raw)

    return f'''<imageEmbed
  alt="Image"
  size="{size}"
  showBorder={{{show_border}}}
  figureEmbed={{ {{
    preset: "{preset_kind}Example",
    figure: {figure_js},
    shouldDisplay: true
  }} }}
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
    raw_figure = figure_match.group(1).strip() if figure_match else "Example"

    figure_js = js_string(raw_figure)
    from_js = js_string(email_data['from'])
    to_js = js_string(email_data['to'])
    cc_js = js_string(email_data['cc'])
    bcc_js = js_string(email_data['bcc'])
    subject_js = js_string(email_data['subject'])

    should_display = 'Figure:' in figure_block

    return f'''<emailEmbed
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
/>'''

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

    return f'''<emailEmbed
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
/>'''

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

            body = '\n'.join(buffer)
            body = mdx_safe_template_vars(body)
            body = convert_angle_bracket_links(body)
            body = escape_angle_brackets_except(body, allowed_tags=("mark",))

            figure_js = js_string(figure)
            embed = f'''<asideEmbed
  variant="{box_type}"
  body={{<>
    {body}
  </>}}
  figureEmbed={{{{
    preset: "{preset}",
    figure: {figure_js},
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


def transform_email_blocks(content: str) -> str:
    base_pat = re.compile(
        r'::: email-template\s+(.*?)'
        r'::: email-content\s+(.*?)'
        r':::\s+:::',
        re.DOTALL
    )

    out = []
    idx = 0

    for m in base_pat.finditer(content):
        out.append(content[idx:m.start()])

        table = m.group(1)
        body  = m.group(2).strip()

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
        cleaned_body = clean_email_body(body)

        from_js    = js_string(email_data['from'])
        to_js      = js_string(email_data['to'])
        cc_js      = js_string(email_data['cc'])
        bcc_js     = js_string(email_data['bcc'])
        subject_js = js_string(email_data['subject'])
        figure_js  = js_string(figure_text if figure_text else "Example")

        embed = f'''<emailEmbed
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
/>'''

        out.append(embed)
        idx = m.end() + consumed

    out.append(content[idx:])
    return ''.join(out)


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

    content = re.sub(r'<!--\s*StartFragment\s*-->', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<!--\s*EndFragment\s*-->', '', content, flags=re.IGNORECASE)

    content = convert_mark_tags_to_md_highlight(content)
    content = mdx_safe_template_vars(content)
    content = re.sub(INTRO_WITH_FM_REGEX, wrap_intro_embed, content, flags=re.IGNORECASE | re.DOTALL)

    content = process_custom_aside_blocks(content)
    content = re.sub(YOUTUBE_BLOCK_REGEX, replace_youtube_block, content, flags=re.MULTILINE)
    content = re.sub(PRESET_CUSTOM_SIZE_IMAGE_BLOCK_REGEX, lambda m: replace_preset_custom_size_image_block(m, src_prefix), content, flags=re.DOTALL)
    content = re.sub(IMAGE_BLOCK_REGEX, lambda m: replace_image_block(m, src_prefix), content, flags=re.DOTALL)
    content = transform_email_blocks(content)
    content = re.sub(CUSTOM_SIZE_IMAGE_BLOCK_REGEX, lambda m: replace_custom_size_image_block(m, src_prefix), content, flags=re.DOTALL)
    # content = re.sub(STANDALONE_IMAGE_REGEX, lambda m: replace_standalone_image(m, src_prefix), content)

    def _replace_standalone_image_conditional(m):
        if is_inside_any_embed_body(content, m.start()):
            return keep_markdown_figure_with_prefix(m, src_prefix)
        return replace_standalone_image(m, src_prefix)
    content = re.sub(STANDALONE_IMAGE_REGEX, _replace_standalone_image_conditional, content)

    content = re.sub(SIMPLE_FIGURE_BLOCK_REGEX, replace_simple_figure_block, content, flags=re.DOTALL)
    content = re.sub(RAW_IMAGE_REGEX, lambda m: prefix_raw_image_src(m, src_prefix), content)

    content = convert_angle_bracket_links(content)

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