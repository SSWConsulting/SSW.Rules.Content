---
seoDescription: Learn why and how to use .gitignore to manage clean repositories. Understand key patterns and explore gitignore templates for different projects.
type: rule
title: Do you use a .gitignore file to keep your Git repository clean?
uri: use-gitignore-for-clean-repo
authors:
  - title: Ben Neoh
    url: https://www.ssw.com.au/people/ben-neoh/
created: 2024-09-19T13:42:55.753Z
guid: 1e89d2a8-3718-4920-934a-c28f1d4cb497
related: 
- do-you-know-the-benefits-of-using-source-control
- do-you-know-these-important-git-commands
---

The .gitignore file tells Git which files to ignore and not track in your repository. Every Git project should have a .gitignore file to keep unnecessary files out of the repo. For example, cache files should not be included in the main repository.
<!--endintro-->

### Why Use .gitignore?

When working on projects, you often generate files that should not be committed to the version control system. These might include:

* Temporary files generated during development (e.g., .log, .tmp)
* Configuration files with sensitive data (e.g., .env)
* Build outputs (e.g., bin/, obj/ folders for .NET projects)
* Dependency caches (e.g., /node_module folder for javacript projects)
* Personal IDE config (e.g., .vscode sometimes you might want to share IDE config intentionally)
  
A .gitignore file tells Git which files or folders to ignore. This keeps your repository clean and ensures that only important files are tracked, improving efficiency.

### Common Syntax Patterns for .gitignore

Here are some useful patterns you might need in a .gitignore file:

 "\*" - (e.g. \*.log This will ignore all files ending in .log anywhere in the repository.)

 "\*\*" - (e.g. \**/lib/name.file This pattern will ignore name.file in any lib/ directory within the repository, no matter its depth.)

 " /{{name}}/ " - (e.g. /build/ This will ignore the build/ directory only at the root level.)

For more details and advanced patterns, refer to the [w3schools Gitignore tutorial](https://www.w3schools.com/git/git_ignore.asp?remote=github).

### How to setup .gitignore?

1. Create a .gitignore File:
In your project’s root directory, create a file named .gitignore if it doesn't already exist.

2. Add Files or Directories to Ignore:
Open the .gitignore file and list the files or directories you want Git to ignore. Each entry should be on a new line. For example:

```gitignore
bash
node_modules/
.env
*.log
```

**Figure: Example of gitnore file**

### Additional Tips

1. Use Pre-made Templates(You don’t need to write a .gitignore from scratch! ):
    * Use templates based on your programming language or framework. gitignore template from [github](https://github.com/github/gitignore)
    * Use a generator like [gitignore.io](https://www.toptal.com/developers/gitignore) to create a .gitignore file tailored to your project.
    * Use command dotnet new gitignore to create gitignore file for dotnet application. More details on [create dotnet gitignore](https://dev.to/rafalpienkowski/easy-to-create-gitignore-for-the-dotnet-developers-1h42)

2. Use Comments:
You can add comments in the .gitignore file to explain why certain files or directories are being ignored. Use # for comments. For example:

```gitignore
# Ignore environment variables for security
.env

# Ignore node_modules folder to avoid unnecessary files in the repo
node_modules/
```

**Figure: Example of gitignore file with comment**
