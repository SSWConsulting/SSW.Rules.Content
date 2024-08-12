---
seoDescription: Learn how to use cloc to measure code line metrics including number file count, blank lines, comment lines, and physical lines of code across multiple programming languages.
type: rule
title: Do you know how to get code line metrics?
uri: get-code-line-metrics
authors:
  - title: Luke Mao
    url: https://www.ssw.com.au/people/luke-mao
created: 2024-08-12T12:31:00.000Z
guid: c72d02f4-8990-4f54-964f-17e558d833ae
---

When working on software projects, it’s important to keep track of your codebase's size and structure. Code line metrics help you understand the scope of the code, identify potential areas for refactoring, and maintain a healthy balance between files, blank lines comments, and code. Without these metrics, your project can become difficult to manage, and you may struggle to track progress or maintain code quality.

<!--endintro-->

### Using cloc to Measure Code Line Metrics

The tool [cloc](https://github.com/AlDanial/cloc) is a straightforward yet powerful way to count number of files, blank lines, comment lines, and physical lines of source code across various programming languages. Here’s how you can use it effectively:

#### 1. **Install cloc**

- You can install cloc on most operating systems using package managers:
  - **Windows**: Use [chocolatey](https://chocolatey.org/): `choco install cloc`
  - **macOS**: Use [Homebrew](https://brew.sh/): `brew install cloc`
  - **Linux**: Install via your package manager, e.g., `sudo apt-get install cloc` for Debian-based distributions.

#### 2. **Run cloc on Your Codebase**

- For a git repository (using a specific commit):

  ```bash
  cloc {{ COMMIT_HASH }}
  ```

- For a specific file or folder:

  ```bash
  cloc /path/to/your/file_or_folder
  ```

#### 3. **Understand the Output**

- **File Count:** The number of files in your project, helping you understand its size and complexity.
- **Blank Lines:** These can indicate the organization of your code, providing insights into its readability.
- **Comment Lines:** The number of lines that contain comments, helping you gauge how well-documented your code is.
- **Physical Lines of Code (LOC):** This counts the actual code lines, excluding blank lines and comments.

#### 4. **Incorporate cloc in Your CI/CD Pipeline**

- Regularly running cloc as part of your continuous integration process can help track changes in your codebase over time. This allows you to monitor code growth and ensure that the proportion of comments and blank lines remains healthy.

### Benefits of Tracking Code Metrics

Tracking code metrics with cloc helps in maintaining clean and well-documented code. It provides insights that can lead to:

- **Improved Code Quality:** By identifying parts of the code that are poorly documented or unnecessarily complex.
- **Better Project Management:** Enabling project leads to assess the size and complexity of the codebase and plan accordingly.
- **Code Review Efficiency:** Assisting in identifying files that have changed significantly and might require more thorough reviews.

By integrating cloc into your workflow, you can ensure that your codebase remains manageable, maintainable, and well-documented as your project evolves.
