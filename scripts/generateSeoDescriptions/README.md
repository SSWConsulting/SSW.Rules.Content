# SEO Description Generator

## Summary

This Python script automates the generation of SEO descriptions for Markdown files using the Ollama Python library. It searches for Markdown files in a specified directory, checks if they contain an existing SEO description, and if not, generates one using a specified model.

## Requirements

* Python 3.8+
* Ollama installed and running
* Ollama Python library (`pip install ollama`)

Note: You can use any available model with Ollama. To do so, update the model name in the code where indicated.

## Usage Instructions

1. Ensure you've pulled the desired model. The default is set to use deepseek-r1:14b. To change it, update the line in your code:

    ```
    ollama pull deepseek-r1:14b  # Replace 'deepseek-r1:14b' with your desired model name
    ```

2. Run the script with the directory path as an argument:

    ```
    python ./generateDescriptions.py {{ PATH/TO/MARKDOWN/FILES }}
    ```

3. The script processes each Markdown file:
    * If the file lacks an SEO description, it generates one and inserts it into the YAML front matter.
    * If an SEO description already exists, the file is skipped.
    * Any issues with the generated description are logged in seo_issues.log.

## Prompting

The prompt.txt file stores the prompt for easy editing. The script reads this file to combine with the Markdown content when generating the SEO description.
