#!/bin/bash

# Function to generate SEO description using ollama run llama3
generate_seo_description() {
  local file_content="$1"
  local seo_description=$(echo "$file_content" | ollama run llama3 "SEO Description requirements - short 1 sentence. Generate an SEO description from the following content. Only output the generated description, NOTHING else:")

  echo $seo_description
}

# Directory to search for markdown files
search_dir="./rules"

# Iterate over each markdown file in the directory
find "$search_dir" -name "*.md" | while read -r markdown_file; do
  echo "Processing file: $markdown_file"

  # Read the content of the markdown file
  file_content=$(cat "$markdown_file")

  # Check if the file contains an seoDescription field
  if ! grep -q '^seoDescription:' "$markdown_file"; then
    # Generate SEO description
    seo_description=$(generate_seo_description "$file_content")

    # Add the seoDescription to the YAML front matter
    awk -v desc="$seo_description" '
      BEGIN { found = 0 }
      /^---$/ { 
        if (found == 0) { 
          found = 1; 
          print; 
          print "seoDescription: \"" desc "\""; 
          next 
        }
      }
      { print }
    ' "$markdown_file" > "${markdown_file}.tmp"

    # Replace the original file with the updated file
    mv "${markdown_file}.tmp" "$markdown_file"
    
    echo "Added SEO description to $markdown_file"
  else
    echo "SEO description already present in $markdown_file"
  fi
  echo ""
done