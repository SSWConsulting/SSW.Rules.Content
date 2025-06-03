import os
import re
from pathlib import Path
import time

# ----------------------------- #
# Regex patterns
# ----------------------------- #

YOUTUBE_BLOCK_REGEX = r'`youtube:\s*(https?://[^\s]+)`\s*\n\*\*(.*?)\*\*'
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

# ----------------------------- #
# Utilities
# ----------------------------- #

def escape_single_quotes(text):
    return text.replace("'", "\\'")

def mdx_safe_template_vars(text):
    return text.replace("{{", "&#123;&#123;").replace("}}", "&#125;&#125;")

def parse_email_table(table_text):
    result = {'to': '', 'cc': '', 'bcc': '', 'subject': ''}
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
    return re.sub(r'^###', '##', cleaned, flags=re.MULTILINE)

def clean_image_src(src):
    return re.sub(r'(\.(?:png|jpg|jpeg|gif))\s.*$', r'\1', src, flags=re.IGNORECASE)

# ----------------------------- #
# Replacements
# ----------------------------- #

def replace_youtube_block(m):
    url = m.group(1).strip()
    desc = m.group(2).strip()
    return f'<youtubeEmbed url="{url}" description="{desc}" />'

def replace_image_block(m):
    preset = m.group(1).strip()
    image_line = m.group(2).strip()
    alt_match = re.match(r'!\[Figure:\s*(.*?)\]\((.*?)\)', image_line)
    if not alt_match:
        return m.group(0)
    figure = alt_match.group(1).strip()
    raw_src = alt_match.group(2).strip()
    src = clean_image_src(raw_src)

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

def replace_custom_size_image_block(m):
    variant = m.group(1).strip()
    figure = escape_single_quotes(m.group(2).strip())
    raw_src = m.group(3).strip()
    src = clean_image_src(raw_src)

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

def replace_standalone_image(m):
    figure = m.group(1).strip()
    raw_src = m.group(2).strip()
    src = clean_image_src(raw_src)

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

def transform_rule_md_to_mdx(file_path='../../rules/rule/rule.md'):
    path = Path(file_path)
    if not path.exists():
        print(f"File not found: {file_path}")
        return

    content = path.read_text(encoding='utf-8')

    content = process_custom_aside_blocks(content)

    content = re.sub(r'^\s*<!--endintro-->\s*\n?', '', content, flags=re.MULTILINE)

    content = re.sub(YOUTUBE_BLOCK_REGEX, replace_youtube_block, content, flags=re.MULTILINE)
    content = re.sub(IMAGE_BLOCK_REGEX, replace_image_block, content, flags=re.DOTALL)
    content = re.sub(CUSTOM_SIZE_IMAGE_BLOCK_REGEX, replace_custom_size_image_block, content, flags=re.DOTALL)
    content = re.sub(STANDALONE_IMAGE_REGEX, replace_standalone_image, content)
    content = re.sub(EMAIL_BLOCK_REGEX, replace_email_block, content, flags=re.DOTALL)
    content = re.sub(SIMPLE_FIGURE_BLOCK_REGEX, replace_simple_figure_block, content, flags=re.DOTALL)


    output_path = path.with_suffix('.mdx')
    output_path.write_text(content, encoding='utf-8')

    print(f"Transformed content saved to: {output_path}")

def transform_all_rules(base_dir='../../rules'):
    start_time = time.time()

    base_path = Path(base_dir)
    if not base_path.exists():
        print(f"Base path not found: {base_dir}")
        return

    count = 0

    for rule_dir in base_path.iterdir():
        if rule_dir.is_dir():
            rule_md = rule_dir / 'rule.md'
            if rule_md.exists():
                print(f"[INFO] Processing: {rule_md}")
                try:
                    content = rule_md.read_text(encoding='utf-8')

                    # === TRANSFORM PIPELINE ===
                    content = process_custom_aside_blocks(content)
                    content = re.sub(r'^\s*<!--endintro-->\s*\n?', '', content, flags=re.MULTILINE)
                    content = re.sub(YOUTUBE_BLOCK_REGEX, replace_youtube_block, content, flags=re.MULTILINE)
                    content = re.sub(IMAGE_BLOCK_REGEX, replace_image_block, content, flags=re.DOTALL)
                    content = re.sub(CUSTOM_SIZE_IMAGE_BLOCK_REGEX, replace_custom_size_image_block, content, flags=re.DOTALL)
                    content = re.sub(STANDALONE_IMAGE_REGEX, replace_standalone_image, content)
                    content = re.sub(EMAIL_BLOCK_REGEX, replace_email_block, content, flags=re.DOTALL)
                    content = re.sub(SIMPLE_FIGURE_BLOCK_REGEX, replace_simple_figure_block, content, flags=re.DOTALL)

                    # === SAVE AS rule.mdx ===
                    output_path = rule_md.with_suffix('.mdx')
                    output_path.write_text(content, encoding='utf-8')
                    rule_md.unlink()  # delete original .md file

                    print(f"[SUCCESS] Converted and replaced: {output_path}")
                    count += 1

                except Exception as e:
                    print(f"[ERROR] Failed to process {rule_md}: {e}")

    end_time = time.time()
    elapsed = end_time - start_time
    print(f"\n✅ Finished processing {count} rule.md files in {elapsed:.2f} seconds.")

# ----------------------------- #
# Entry Point
# ----------------------------- #

if __name__ == '__main__':
    transform_all_rules()
