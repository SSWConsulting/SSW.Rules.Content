#!/bin/bash
set -e

# Process /categories: rename only .md → .mdx (no moving)
# while IFS= read -r file; do
#     new="${file%.md}.mdx"

#     echo "git mv \"$file\" \"$new\""
#     git mv "$file" "$new"
# done < <(git ls-files 'categories/*.md' 'categories/**/*.md')


# Process /rules: move to /public/uploads/rules and rename .md → .mdx
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