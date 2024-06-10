# SEO Description Generator

## Summary

This bash script automates the generation of SEO descriptions for Markdown files using the Ollama CLI. It searches for Markdown files in a specified directory, checks if they contain an existing SEO description, and if not, generates one using the Llama 3 LLM.

## Requirements

* Bash shell
* Ollama CLI tool (`ollama`) installed and configured

## Usage Instructions

2. Run the script providing the directory path as an argument:

```bash
bash ./generate_seo_descriptions.sh </path/to/markdown/files>
```

3. The script will process each Markdown file in the directory:

* If the file does not contain an existing SEO description, it will generate one using the Ollama CLI and add it to the YAML front matter of the file.
* If the file already contains an SEO description, it will skip it.

5. Review the output to see which files had SEO descriptions added.

## Prompting

The prompt.txt file is where the prompt is stored for easy editing. The script will read the prompt from this file.
