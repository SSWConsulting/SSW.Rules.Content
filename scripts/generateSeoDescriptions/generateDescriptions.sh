#!/bin/bash

# Function to generate SEO description using ollama run llama3
generate_seo_description() {
  local file_content="$1"
  local prompt_file="$(dirname "${BASH_SOURCE[0]}")/prompt.txt"
  local prompt=$(cat "$prompt_file")
  local seo_description=$(echo "$file_content" | ollama run llama3 "$prompt")

  echo $seo_description
}

# Function to check SEO description validity
check_seo_description() {
  local seo_description="$1"
  local issues=()

  # Check if description is more than 300 characters
  if [ ${#seo_description} -gt 300 ]; then
    issues+=("Exceeds 300 characters")
  fi

  # Check if description includes "Here is the ..."
  if echo "$seo_description" | grep -q "Here is the ..."; then
    issues+=("Contains the phrase 'Here is the ...'")
  fi

    # Check if the AI included formalities
  if echo "$seo_description" | grep -q "I've generated"; then
    issues+=("Contains 'I've generated'")
  fi

  # Check if description includes odd characters * or _
  if echo "$seo_description" | grep -q "[*_]"; then
    issues+=("Contains odd characters * or _")
  fi

  if [ ${#issues[@]} -gt 0 ]; then
    echo "${issues[@]}"
  else
    echo "No issues"
  fi
}

# Directory to search for markdown files
search_dir="$1"

# Log file for issues
log_file="$(dirname "${BASH_SOURCE[0]}")/seo_issues.log"

# Iterate over each markdown file in the directory
find "$search_dir" -name "*.md" -o -name "*.mdx" | while read -r markdown_file; do
  echo "Processing file: $markdown_file"

  # Read the content of the markdown file
  file_content=$(cat "$markdown_file")

  # Check if the file contains an seoDescription field
  if ! grep -q '^seoDescription:' "$markdown_file"; then
    # Generate SEO description
    seo_description=$(generate_seo_description "$file_content")

    # Check SEO description validity
    issues=$(check_seo_description "$seo_description")

    if [ "$issues" == "No issues" ]; then
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
      # Log issues
      echo "$markdown_file:" >> "$log_file"
      echo "$seo_description" >> "$log_file"
      echo "Issues: $issues" >> "$log_file"
      echo "" >> "$log_file"
      echo "Logged issues for $markdown_file"
    fi
  else
    echo "SEO description already present in $markdown_file"
  fi
  echo ""
done
