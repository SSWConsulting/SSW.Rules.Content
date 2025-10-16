---
type: rule
tips: ""
title: Do you configure AI assistants to keep all working files inside the
  repository directory?
seoDescription: Learn how to configure AI coding assistants to keep all work
  within repository boundaries. This standard ensures temporary files, scripts,
  and AI-generated content remain visible and properly managed within your
  project.
uri: ai-assistants-work-in-repository-directory
authors:
  - title: Gordon Beeming
    url: https://ssw.com.au/people/gordon-beeming
  - title: Lewis Toh
    url: https://ssw.com.au/people/lewis-toh
related:
  - keep-task-summaries-from-ai-assisted-development
created: 2025-10-16T17:01:00.000Z
guid: 86655840-0d01-4fb1-aba8-fabd54e1e916
---

When AI assistants (e.g. GitHub Copilot, Claude, ChatGPT) perform development tasks, they sometimes create temporary files, scripts, or intermediate outputs. By default, they might use system temp directories like `/tmp`, `/var/tmp`, or the user's home directory. This creates several problems: files become hard to find, they're outside version control, and cleanup becomes unpredictable.

Configuring AI assistants to work exclusively within the repository boundaries ensures all work is visible, properly managed, and easy to clean up.

<!--endintro-->

:::info
Note: This rule applies to **temporary or working files** created during AI-assisted tasks. See [Do you keep task summaries from AI-assisted development?](/keep-task-summaries-from-ai-assisted-development) if you want to store files permanently from AI output (e.g. documentation)
:::

### The Problem with System Directories

When AI assistants use **system temp directories**, you lose visibility:

::: greybox
* `/tmp/ai-test-12345.sh`
* `/var/tmp/analysis-output.json`
* `~/ai-workspace/temp-queries.sql`
:::
::: bad
Bad Example - Files scattered across the system are hard to find, review, and clean up
:::

### Issues with External Files

Using directories outside the repository causes:

1. **Cleanup challenges** - Files left behind after tasks complete
2. **Security risks** - Sensitive data might be written to shared system directories
3. **Review difficulties** - Harder to review AI-generated code before committing

## The Solution: Repository-Bounded Work

Configure your AI assistants' instruction to keep all work within the repository directory by introducing guidelines

### 1. Add to your AI Assistant Instructions

Add the following section to your AI assistant configuration (e.g. `.github/copilot-instructions.md`, `.cursorrules`, `.ai/instructions.md`):
```markdown
## Working Directory and File Management

### Repository Boundaries
All work, including temporary files, must be done within the repository boundaries:

**DO**:
- Create temporary files/directories within the repository root
- Use `/tmp/` directory at repository root for temporary work files
- Add temporary directories to `.gitignore` if they shouldn't be committed
- Clean up temporary files after completing tasks

**DO NOT**:
- Create files outside the repository directory
- Work in system temp directories or home directory
- Leave temporary files scattered throughout the repository

### Temporary Files
- Use `/tmp/` at the repository root for scratch work
- This directory is already in `.gitignore`
- Always clean up temporary files when done
- Document any temporary files that need to persist
```

### 2. Create the Temporary Directory

Set up the directory structure in your repository:
```bash
mkdir -p tmp
```

### 3. Update .gitignore

Ensure your `.gitignore` includes the temporary directory:
```gitignore
# Temporary work files from AI assistants
/tmp/
```

::: good
Good Example - Clear structure for temporary files that stays within the repository
:::

## Benefits

This approach provides:

✅ **Visibility:** All files are within the repository and easy to find\
✅ **Version Control Ready:** Can selectively commit useful artifacts\
✅ **Easy Cleanup:** Simple to remove all temporary files at once\
✅ **Security:** `.gitignore` prevents accidental commits of sensitive temp files\
✅ **Tool-agnostic:** Works with any AI assistant or development tool

### Example Workflow

::: greybox
**Task:** Generate a database migration script
```bash
# AI assistant creates work files in repository
/work/
├── tmp/
│   ├── migration-analysis.md
│   ├── test-queries.sql
│   └── rollback-script.sql
├── src/
└── docs/

# Easy to review
$ cat tmp/migration-analysis.md
$ cat tmp/test-queries.sql

# Easy to clean up when done
$ rm -rf tmp/*
```

:::
::: good
Good Example - All temporary files are in one predictable location within the repository
:::

## Conclusion

By configuring AI assistants to work exclusively within repository boundaries, you maintain full visibility and control over AI-generated files. This prevents file sprawl and makes it easier to review and manage all work produced during AI-assisted development sessions.
