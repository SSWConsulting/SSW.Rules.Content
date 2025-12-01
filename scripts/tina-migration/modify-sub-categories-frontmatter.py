import os
import glob
import re
import json
from pathlib import Path

# ----------------------------- #
# Regex patterns
# ----------------------------- #

YOUTUBE_BLOCK_REGEX = r'`youtube:\s*(https?://[^\s]+)`'
IMAGE_BLOCK_REGEX = r'^\s*:::\s*(bad|ok|good)\s+(!\[(?:Figure:\s*)?.*?\]\(.*?\))\s+:::'
STANDALONE_IMAGE_REGEX = r'!\[Figure:\s*(.*?)\]\((.*?)\)'
CUSTOM_SIZE_IMAGE_BLOCK_REGEX = r'^\s*:::\s*([^\n]+?)\s*\n\s*!\[(?:Figure:\s*)?(.*?)\]\((.*?)\)\s*:::'
PRESET_AND_SIZE_IMAGE_BLOCK_REGEX = r'^\s*:::\s*(?:(?P<preset1>good|bad|ok)\s+(?P<size1>img-small|img-medium|img-large|small|medium|large|no-border)|(?P<size2>img-small|img-medium|img-large|small|medium|large|no-border)\s+(?P<preset2>good|bad|ok))\s*\n\s*!\[Figure:\s*(?P<figure>.*?)\]\((?P<src>.*?)\)\s*:::'
RAW_IMAGE_REGEX = r'!\[(?!Figure:)(.*?)\]\((.*?)\)'
SRC_PREFIX_BASE = '/uploads/categories'

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

def prefix_raw_image_src(m, src_prefix):
    alt_text = m.group(1).strip()
    raw_src = m.group(2).strip()
    clean_src = clean_image_src(raw_src)

    if clean_src.startswith('/') or clean_src.startswith('http'):
        return m.group(0)

    prefixed_src = f"{src_prefix}/{clean_src}"
    return f'![{alt_text}]({prefixed_src})'

def keep_markdown_figure_with_prefix(m, src_prefix: str) -> str:
    figure = m.group(1).strip()
    raw_src = m.group(2).strip()
    src = add_prefix_if_relative(raw_src, src_prefix)
    return f'![Figure: {figure}]({src})'

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

def replace_youtube_block(m):
    url = m.group(1).strip()
    return f'<youtubeEmbed url="{url}" description={{""}} />'

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

    return f'''<imageEmbed
  alt="Image"
  size="large"
  showBorder={{false}}
  figurePreset="{preset}"
  figureText={{{figure_js}}}
  src="{src}"
/>'''

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

    return f'''<imageEmbed
  alt="Image"
  size="{size}"
  showBorder={{{show_border}}}
  figurePreset="{preset}"
  figureText={{{figure_js}}}
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
  figurePreset="{preset}"
  figureText={{{figure_js}}}
  src="{src}"
/>'''

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

    return f'''<imageEmbed
  alt="Image"
  size="{size}"
  showBorder={{{show_border}}}
  figurePreset="{preset}"
  figureText={{{figure_js}}}
  src="{src}"
/>'''

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
            embed = f'''<asideEmbed
  variant="{box_type}"
  body={{<>
    {body}
  </>}}
  figurePreset="default"
  figureText={{{figure_js}}}
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
    # Find all *.md and *.mdx files in subfolders of categories except index.md/index.mdx
    md_pattern = os.path.join(categories_root, '**', '*.md')
    mdx_pattern = os.path.join(categories_root, '**', '*.mdx')
    md_files = glob.glob(md_pattern, recursive=True) + glob.glob(mdx_pattern, recursive=True)
    md_files = [f for f in md_files if not (f.endswith('index.md') or f.endswith('index.mdx'))]
    
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
        
        # Process body content to convert aside blocks, images, and YouTube embeds
        original_body = body

        # Ensure upload directory exists
        upload_dir = project_root / "public/uploads/categories"
        upload_dir.mkdir(parents=True, exist_ok=True)

        # Move all images in the same folder as the MD file
        current_dir = Path(file_path).parent

        for img in current_dir.glob("*"):
            if img.suffix.lower() in [".png", ".jpg", ".jpeg", ".gif"]:
                target = upload_dir / img.name

                # Avoid overwriting existing files
                if not target.exists():
                    print(f"Moving image: {img} → {target}")
                    img.rename(target)

        # Get the category folder name for image src prefix
        category_folder = Path(file_path).parent.name
        src_prefix = SRC_PREFIX_BASE

        # Apply transformations in order
        body = process_custom_aside_blocks(body)
        body = re.sub(YOUTUBE_BLOCK_REGEX, replace_youtube_block, body, flags=re.MULTILINE)

        # Handle preset + size combinations (e.g., "good img-medium" or "img-medium good")
        body = re.sub(PRESET_AND_SIZE_IMAGE_BLOCK_REGEX, lambda m: replace_preset_and_size_image_block(m, src_prefix), body, flags=re.MULTILINE | re.DOTALL)

        # Handle image blocks with ratings (e.g., "::: good ![...] :::")
        def _replace_image_block_conditional(m):
            if is_inside_any_embed_body(body, m.start(), component_tags=("<emailEmbed", "<asideEmbed", "<introEmbed")):
                return keep_image_block_with_prefixed_src(m, src_prefix)
            return replace_image_block(m, src_prefix)
        body = re.sub(IMAGE_BLOCK_REGEX, _replace_image_block_conditional, body, flags=re.MULTILINE | re.DOTALL)

        # Handle custom size image blocks (e.g., "::: img-small\n![...] :::")
        body = re.sub(CUSTOM_SIZE_IMAGE_BLOCK_REGEX, lambda m: replace_custom_size_image_block(m, src_prefix), body, flags=re.MULTILINE | re.DOTALL)

        # Handle standalone Figure images
        def _replace_standalone_image_conditional(m):
            if is_inside_any_embed_body(body, m.start()):
                return keep_markdown_figure_with_prefix(m, src_prefix)
            return replace_standalone_image(m, src_prefix)
        body = re.sub(STANDALONE_IMAGE_REGEX, _replace_standalone_image_conditional, body)

        # Handle raw images (prefix relative paths)
        body = re.sub(RAW_IMAGE_REGEX, lambda m: prefix_raw_image_src(m, src_prefix), body)

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

if __name__ == '__main__':
    modify_category_files()
    print("All category files processed!")