import os
import glob
import re
import json
from pathlib import Path

# ----------------------------- #
# Regex patterns
# ----------------------------- #

YOUTUBE_BLOCK_REGEX = r'`youtube:\s*(https?://[^\s]+)`'
IMAGE_BLOCK_REGEX = r'^(\s*):::\s*(bad|ok|good)\s+(!\[(?:Figure:\s*)?.*?\]\(.*?\))\s+:::'
SIMPLE_FIGURE_BLOCK_REGEX = r'^(\s*):::\s*(good|bad|ok)\s*\n(.*?)\n\1:::'
CUSTOM_SIZE_IMAGE_BLOCK_REGEX = r'^(\s*):::\s*(img-small|img-medium|img-large|no-border|small|medium|large)\s*\n\s*!\[(?:Figure:\s*)?(.*?)\]\((.*?)\)\s*\n\1:::'
PRESET_CUSTOM_SIZE_IMAGE_BLOCK_REGEX = r'^(?P<indent>\s*):::\s*(?:(?P<preset1>good|bad|ok)\s+(?P<size1>img-small|img-medium|img-large|no-border|small|medium|large)|(?P<size2>img-small|img-medium|img-large|no-border|small|medium|large)\s+(?P<preset2>good|bad|ok))\s*\n\s*!\[(?:Figure:\s*)?(.*?)\]\((.*?)\)\s*\n(?P=indent):::'
STANDALONE_IMAGE_REGEX = r'!\[Figure:\s*(.*?)\]\((.*?)\)'

# ----------------------------- #
# Utilities
# ----------------------------- #

def js_string(text: str) -> str:
    return json.dumps(text, ensure_ascii=False)

def mdx_safe_template_vars(text):
    return text.replace("{{", "&#123;&#123;").replace("}}", "&#125;&#125;")

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

def clean_image_src(src):
    return re.sub(r'(\.(?:png|jpg|jpeg|gif))\s.*$', r'\1', src, flags=re.IGNORECASE)

def add_prefix_if_relative(raw_src: str, src_prefix: str) -> str:
    clean = clean_image_src(raw_src)
    if clean.startswith('/') or re.match(r'https?://', clean, flags=re.IGNORECASE):
        return clean
    return f"{src_prefix}/{clean}"

def replace_youtube_block(m):
    url = m.group(1).strip()
    return f'<youtubeEmbed url="{url}" description={{""}} />'

def replace_image_block(m, src_prefix):
    indent = m.group(1)  # Capture indentation
    preset = m.group(2).strip()
    image_line = m.group(3).strip()
    alt_match = re.match(r'!\[(?:Figure:\s*)?(.*?)\]\((.*?)\)', image_line)
    if not alt_match:
        return m.group(0)
    figure = alt_match.group(1).strip()
    raw_src = alt_match.group(2).strip()
    src = add_prefix_if_relative(raw_src, src_prefix)

    # If figure is empty, set shouldDisplay to false
    should_display = "true" if figure else "false"
    figure_js = js_string(figure)

    return f'''{indent}<imageEmbed
{indent}  alt="Image"
{indent}  size="large"
{indent}  showBorder={{false}}
{indent}  figureEmbed={{ {{
{indent}    preset: "{preset}Example",
{indent}    figure: {figure_js},
{indent}    shouldDisplay: {should_display}
{indent}  }} }}
{indent}  src="{src}"
{indent}/>'''

def replace_custom_size_image_block(m, src_prefix):
    indent = m.group(1)  # Capture indentation
    variant = m.group(2).strip()
    figure_raw = m.group(3).strip()
    raw_src = m.group(4).strip()
    src = add_prefix_if_relative(raw_src, src_prefix)

    size = {
        "img-small": "small",
        "img-medium": "medium",
        "img-large": "large",
        "no-border": "large",
        "small": "small",      # Old syntax support
        "medium": "medium",    # Old syntax support
        "large": "large"       # Old syntax support
    }.get(variant, "large")

    show_border = "false" if variant == "no-border" else "true"

    # If figure is empty, set shouldDisplay to false
    should_display = "true" if figure_raw else "false"
    figure_js = js_string(figure_raw)

    return f'''{indent}<imageEmbed
{indent}  alt="Image"
{indent}  size="{size}"
{indent}  showBorder={{{show_border}}}
{indent}  figureEmbed={{ {{
{indent}    preset: "default",
{indent}    figure: {figure_js},
{indent}    shouldDisplay: {should_display}
{indent}  }} }}
{indent}  src="{src}"
{indent}/>'''

def replace_preset_custom_size_image_block(m, src_prefix):
    # Handle both orders: "::: good img-small" or "::: img-small bad"
    indent = m.group('indent')  # Capture indentation
    if m.group('preset1'):
        preset_kind = m.group('preset1').strip()
        variant = m.group('size1').strip()
        figure_raw = m.group(5).strip()
        raw_src = m.group(6).strip()
    else:
        variant = m.group('size2').strip()
        preset_kind = m.group('preset2').strip()
        figure_raw = m.group(5).strip()
        raw_src = m.group(6).strip()

    size = {
        "img-small": "small",
        "img-medium": "medium",
        "img-large": "large",
        "no-border": "large",
        "small": "small",      # Old syntax support
        "medium": "medium",    # Old syntax support
        "large": "large"       # Old syntax support
    }.get(variant, "large")

    show_border = "false" if variant == "no-border" else "true"
    src = add_prefix_if_relative(raw_src, src_prefix)

    # If figure is empty, set shouldDisplay to false
    should_display = "true" if figure_raw else "false"
    figure_js = js_string(figure_raw)

    return f'''{indent}<imageEmbed
{indent}  alt="Image"
{indent}  size="{size}"
{indent}  showBorder={{{show_border}}}
{indent}  figureEmbed={{ {{
{indent}    preset: "{preset_kind}Example",
{indent}    figure: {figure_js},
{indent}    shouldDisplay: {should_display}
{indent}  }} }}
{indent}  src="{src}"
{indent}/>'''

def replace_simple_figure_block(m, src_prefix):
    indent = m.group(1)  # Capture indentation
    preset = m.group(2).strip()
    body = m.group(3).strip()

    # Check if the body contains an image
    img_match = re.match(r'!\[(?:Figure:\s*)?(.*?)\]\((.*?)\)', body)
    if img_match:
        # It's an image block, convert to imageEmbed
        figure = img_match.group(1).strip()
        raw_src = img_match.group(2).strip()
        src = add_prefix_if_relative(raw_src, src_prefix)

        # If figure is empty, set shouldDisplay to false
        should_display = "true" if figure else "false"
        figure_js = js_string(figure)

        return f'''{indent}<imageEmbed
{indent}  alt="Image"
{indent}  size="large"
{indent}  showBorder={{false}}
{indent}  figureEmbed={{ {{
{indent}    preset: "{preset}Example",
{indent}    figure: {figure_js},
{indent}    shouldDisplay: {should_display}
{indent}  }} }}
{indent}  src="{src}"
{indent}/>'''
    else:
        # It's just text, convert to figureEmbed
        figure_js = js_string(body)
        return f'''{indent}<figureEmbed figureEmbed={{ {{
{indent}  preset: "{preset}Example",
{indent}  figure: {figure_js},
{indent}  shouldDisplay: true
{indent}}} }} />\n'''

def process_custom_aside_blocks(content):
    """Process aside blocks (greybox, info, highlight, etc.) in category files"""
    lines = content.splitlines()
    output = []
    i = 0
    in_box = False
    box_type = ""
    buffer = []
    box_indent = ""  # Track the indentation level of the box

    while i < len(lines):
        line = lines[i].rstrip()

        # Match aside block start with optional indentation
        match_start = re.match(r"^(\s*):::\s*(greybox|highlight|china|info|todo|codeauditor)\s*$", line)
        if match_start and not in_box:
            in_box = True
            box_indent = match_start.group(1)  # Capture the indentation
            box_type = match_start.group(2)
            buffer = []
            i += 1
            continue

        # Match closing ::: at the same indentation level
        if in_box and re.match(rf"^{re.escape(box_indent)}:::\s*$", line):

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
            embed = f'''{box_indent}<asideEmbed
{box_indent}  variant="{box_type}"
{box_indent}  body={{<>
{box_indent}    {body}
{box_indent}  </>}}
{box_indent}  figureEmbed={{{{
{box_indent}    preset: "{preset}",
{box_indent}    figure: {figure_js},
{box_indent}    shouldDisplay: {"true" if show else "false"}
{box_indent}  }}}}
{box_indent}/>'''
            output.append(embed)
            in_box = False
            box_indent = ""  # Reset indentation
            i += 1
            continue

        if in_box:
            buffer.append(line)
        else:
            output.append(line)

        i += 1

    return '\n'.join(output)

def modify_category_files(categories_root=None):
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    # Go up two levels to get to the project root (from scripts/tina-migration/ to project root)
    project_root = script_dir.parent.parent

    # Default categories_root to the categories folder in the project root
    if categories_root is None:
        categories_root = project_root / 'categories'
    else:
        # If provided, make it relative to project root
        categories_root = project_root / categories_root
    # Find all *.md and *.mdx files in subfolders of categories except index.md
    md_pattern = os.path.join(categories_root, '**', '*.md')
    mdx_pattern = os.path.join(categories_root, '**', '*.mdx')
    md_files = glob.glob(md_pattern, recursive=True) + glob.glob(mdx_pattern, recursive=True)
    md_files = [f for f in md_files if not f.endswith('index.md') and not f.endswith('index.mdx')]
    
    for file_path in md_files:
        print(f"Processing: {file_path}")
        
        # Read the entire file content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split into frontmatter and body
        fm_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
        if not fm_match:
            print(f"No frontmatter found in {file_path}, skipping")
            continue
            
        fm_content, body = fm_match.groups()
        
        # Check if this is a category file
        if 'type: category' not in fm_content:
            print(f"Skipping (not a category file): {file_path}")
            continue
        
        # Track if we need to update the file
        needs_update = False
        new_fm_lines = fm_content.split('\n')
        
        # Add _template if missing (insert after first line)
        if not any(line.startswith('_template:') for line in new_fm_lines):
            new_fm_lines.insert(0, '_template: category')
            needs_update = True
        
        # Process index field if it exists
        index_pos = None
        for i, line in enumerate(new_fm_lines):
            if line.startswith('index:'):
                index_pos = i
                break
        
        if index_pos is not None:
            # Process index items
            new_index_lines = []
            index_modified = False
            i = index_pos
            while i < len(new_fm_lines):
                line = new_fm_lines[i]
                if i == index_pos:  # The 'index:' line
                    new_index_lines.append(line)
                    i += 1
                    continue

                # Check if this is an empty line
                if line.strip() == '':
                    # Skip empty lines and continue
                    new_index_lines.append(line)
                    i += 1
                    continue

                # Check if this is a comment line
                if re.match(r'^\s*#', line):
                    # Skip comment lines and continue
                    new_index_lines.append(line)
                    i += 1
                    continue

                # Check if this is an index item
                if re.match(r'^\s*-', line):
                    item = line.strip()[2:]  # Remove '- '
                    if not (item.startswith('rule:') or ':' in item):
                        # Convert to new format
                        indent = re.match(r'^\s*', line).group()
                        clean_item = item.replace('.md', '').strip("'\"")
                        new_line = f"{indent}- rule: public/uploads/rules/{clean_item}/rule.mdx"
                        new_index_lines.append(new_line)
                        index_modified = True
                        needs_update = True
                    else:
                        new_index_lines.append(line)
                    i += 1
                else:
                    break

            # Replace the index section if we made changes to the index
            if index_modified:
                new_fm_lines = new_fm_lines[:index_pos] + new_index_lines + new_fm_lines[i:]
                needs_update = True
        
        # Process body content to convert YouTube embeds, aside blocks, and image blocks
        original_body = body

        # Get the folder name for image src prefix
        folder_name = Path(file_path).parent.name
        src_prefix = f"/categories/{folder_name}"

        # Process in order
        body = re.sub(YOUTUBE_BLOCK_REGEX, replace_youtube_block, body, flags=re.MULTILINE)
        body = process_custom_aside_blocks(body)
        body = re.sub(PRESET_CUSTOM_SIZE_IMAGE_BLOCK_REGEX, lambda m: replace_preset_custom_size_image_block(m, src_prefix), body, flags=re.MULTILINE | re.DOTALL)
        body = re.sub(IMAGE_BLOCK_REGEX, lambda m: replace_image_block(m, src_prefix), body, flags=re.MULTILINE | re.DOTALL)
        body = re.sub(CUSTOM_SIZE_IMAGE_BLOCK_REGEX, lambda m: replace_custom_size_image_block(m, src_prefix), body, flags=re.MULTILINE | re.DOTALL)
        body = re.sub(SIMPLE_FIGURE_BLOCK_REGEX, lambda m: replace_simple_figure_block(m, src_prefix), body, flags=re.MULTILINE | re.DOTALL)

        # Check if body was modified
        if body != original_body:
            needs_update = True

        # Write back if changes were made
        if needs_update:
            new_fm_content = '\n'.join(new_fm_lines)
            new_content = f"---\n{new_fm_content}\n---\n{body}"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Successfully updated: {file_path}")

        # Always rename .md to .mdx (even if no content changes)
        new_file_path = Path(file_path).with_suffix('.mdx')
        if file_path.endswith('.md'):
            # Delete existing .mdx file if it exists
            if new_file_path.exists():
                new_file_path.unlink()

            os.rename(file_path, new_file_path)
            print(f"Renamed to: {new_file_path}\n")
        else:
            print(f"Already .mdx: {file_path}\n")

if __name__ == '__main__':
    modify_category_files()
    print("All category files processed!")