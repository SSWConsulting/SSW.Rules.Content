#!/usr/bin/env python3
import os
import sys
import re
from ollama import generate

def generate_seo_description(file_content):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    prompt_file = os.path.join(script_dir, "prompt.txt")
    with open(prompt_file, "r", encoding="utf-8") as pf:
        prompt = pf.read()
    combined_prompt = f"{prompt}\n\n{file_content}"
    response = generate(model="deepseek-r1:14b", prompt=combined_prompt)

    seo_description = response['response']
    
    # Remove <think>...</think> tags from reasoning models
    cleaned = re.sub(r"<think>.*?</think>", "", seo_description, flags=re.DOTALL)
    return cleaned

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
    markdown_files = []
    for root, _, files in os.walk(search_dir):
        for file in files:
            if file.endswith((".md", ".mdx")):
                markdown_files.append(os.path.join(root, file))
    total_files = len(markdown_files)
    processed_files = 0

    for md_file in markdown_files:
        print(f"Processing file: {md_file} 🔍")
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Skip if seoDescription already exists
        if re.search(r"^seoDescription:", content, re.MULTILINE):
            print(f"SEO description already present in {md_file} ✅\n")
        else:
            seo_desc = generate_seo_description(content)
            issues = check_seo_description(seo_desc)
            # Flatten to a single line for YAML
            seo_desc_single = " ".join(seo_desc.split())
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
                print(f"Added SEO description to {md_file} 🎉")
            else:
                with open(log_file, "a", encoding="utf-8") as log:
                    log.write(f"Issues found in {md_file}:\n")
                    log.write(seo_desc + "\n")
                    log.write("Issues: " + ", ".join(issues) + "\n\n")
                print(f"Logged issues for {md_file} ⚠️")
        processed_files += 1
        percent = int(processed_files * 100 / total_files) if total_files else 100
        print(f"{percent}% complete\n")

if __name__ == "__main__":
    main()