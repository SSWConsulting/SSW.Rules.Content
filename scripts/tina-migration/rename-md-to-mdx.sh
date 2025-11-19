#!/bin/bash
set -e

# Move all files under /rules to /public/uploads/rules
# Rename only .md → .mdx

while IFS= read -r file; do
    # Compute new path
    if [[ "$file" == rules/* ]]; then
        new="public/uploads/rules/${file#rules/}"
        
        # If it's a markdown file, change extension
        if [[ "$new" == *.md ]]; then
            new="${new%.md}.mdx"
        fi

        # Ensure target directory exists
        mkdir -p "$(dirname "$new")"

        echo "git mv \"$file\" \"$new\""
        git mv "$file" "$new"
    fi
done < <(git ls-files 'rules/**')