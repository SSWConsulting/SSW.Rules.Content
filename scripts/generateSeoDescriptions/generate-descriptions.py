#!/usr/bin/env python3
import os
import sys
import re
from ollama import generate
from tqdm import tqdm  # Progress bar


def generate_seo_description(file_content):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    prompt_file = os.path.join(script_dir, "prompt.txt")
    with open(prompt_file, "r", encoding="utf-8") as pf:
        prompt = pf.read()
    combined_prompt = f"{prompt}\n\n{file_content}"
    response = generate(model="deepseek-r1:14b", prompt=combined_prompt)

    seo_description = response["response"]

    # Remove <think>...</think> tags from reasoning models
    cleaned = re.sub(r"<think>.*?</think>", "", seo_description, flags=re.DOTALL)
    return cleaned.strip()


def check_seo_description(seo_description):
    issues = []
    if len(seo_description) > 300:
        issues.append("Exceeds 300 characters")
    for phrase in ["Here is", "generated SEO", "SEO description", "I've generated"]:
        if re.search(phrase, seo_description, re.IGNORECASE):
            issues.append(f"Contains the phrase '{phrase}'")
    if re.search(r"[*_:]", seo_description):
        issues.append("Contains odd characters *, _, or :")
    return issues


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <search_dir> 🛠️")
        sys.exit(1)

    search_dir = sys.argv[1]
    script_dir = os.path.dirname(os.path.realpath(__file__))
    log_file = os.path.join(script_dir, "seo_issues.log")

    # Gather markdown files (.md and .mdx)
    markdown_files = [
        os.path.join(root, file)
        for root, _, files in os.walk(search_dir)
        for file in files
        if file.endswith((".md", ".mdx"))
    ]

    total_files = len(markdown_files)
    if total_files == 0:
        print("No Markdown files found. 📭")
        sys.exit(0)

    with tqdm(total=total_files, desc="Processing", unit="file") as pbar:
        for md_file in markdown_files:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Skip if seoDescription already exists
            if re.search(r"^seoDescription:", content, re.MULTILINE):
                pbar.update(1)
                continue

            seo_desc = generate_seo_description(content)
            issues = check_seo_description(seo_desc)
            seo_desc_single = " ".join(seo_desc.split())  # Flatten for YAML

            if not issues:
                lines = content.splitlines()
                new_lines = []
                inserted = False

                for line in lines:
                    new_lines.append(line)
                    if not inserted and line.strip() == "---":
                        new_lines.append(f"seoDescription: {seo_desc_single}")
                        inserted = True

                new_content = "\n".join(new_lines)
                with open(md_file, "w", encoding="utf-8") as f:
                    f.write(new_content)

            else:
                with open(log_file, "a", encoding="utf-8") as log:
                    log.write(f"Issues found in {md_file}:\n")
                    log.write(seo_desc + "\n")
                    log.write("Issues: " + ", ".join(issues) + "\n\n")

            pbar.update(1)  # Update progress bar

    print("✅ SEO description updates complete!")


if __name__ == "__main__":
    main()
