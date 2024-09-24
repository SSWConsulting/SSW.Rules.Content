#!/bin/bash


slugify () {
    echo "$1" | iconv -c -t ascii//TRANSLIT | sed -E 's/[~^]+//g' | sed -E 's/[^a-zA-Z0-9]+/-/g' | sed -E 's/^-+|-+$//g' | tr A-Z a-z
}

title=$1
uri=$(slugify "$1")
date_created=$(date -u +%FT%TZ)
guid=$(uuidgen)

echo "Creating rule: $uri"


if [ -z "$1" ]; then
    echo "ERR: No rule name provided"
    exit 1
fi


rule_dir="../rules/$uri/"
if [ -d $rule_dir ]; then
    echo "ERR: Rule already exists"
    exit 1
fi

mkdir $rule_dir
echo "Created directory $rule_dir"

sed -e "s/{{title}}/$title/g" -e "s/{{uri}}/$uri/g" -e "s/{{date_created}}/$date_created/g" -e "s/{{guid}}/$guid/g" rule.md > $rule_dir/rule.md
echo "Created rule $title"


# TODO: update category index with this rule
