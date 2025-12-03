#!/bin/bash

is_rename=false

for rule_file in $(git diff --name-only $(git merge-base origin/main HEAD) | grep 'rule.mdx'); do
  folder_path=$(dirname $rule_file)
  folder_name=${folder_path#rules/}
  echo "Folder path: $folder_path"
  echo "Folder name: $folder_name"
  
  uri=$(grep -m 1 '^uri:' "${GITHUB_WORKSPACE}/$rule_file" | awk '{print $2}')
  uri=$($uri | tr -d '\r')

  echo "URI: $uri"
  
  if [ "$folder_name" != "$uri" ]; then
    mv "${GITHUB_WORKSPACE}/$folder_path" "${GITHUB_WORKSPACE}/rules/$uri"
    is_rename=true

    if grep -q "^redirects: \[\]$" "${GITHUB_WORKSPACE}/$uri/rule.mdx"; then
      sed -i "/^redirects: \[\]$/d" "${GITHUB_WORKSPACE}/$uri/rule.mdx"
    fi

    if grep -q '^redirects:' "${GITHUB_WORKSPACE}/$uri/rule.mdx"; then
      if grep -q "^ *- $folder_name$" "${GITHUB_WORKSPACE}/$uri/rule.mdx"; then
        echo "Old folder name is already in redirects"
      else
        sed -i "/^redirects:/a \ \ - $folder_name" "${GITHUB_WORKSPACE}/$uri/rule.mdx"
      fi
    else
      sed -i "/uri:.*/a\\redirects:\\n  - $folder_name" "${GITHUB_WORKSPACE}/$uri/rule.mdx"
    fi
  fi
done
echo "rename=$is_rename" >> "$GITHUB_OUTPUT"
