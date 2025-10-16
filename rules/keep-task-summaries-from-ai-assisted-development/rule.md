---
type: rule
tips: ""
title: Do you keep task summaries from AI-assisted development?
seoDescription: Learn how to organize and preserve task summaries from GitHub
  Copilot CLI sessions. This standard ensures AI-assisted development work is
  properly documented and easily discoverable for future reference.
uri: keep-task-summaries-from-ai-assisted-development
authors:
  - title: Gordon Beeming
    url: https://ssw.com.au/people/gordon-beeming
  - title: Lewis Toh
    url: https://ssw.com.au/people/lewis-toh
related:
  - leave-explanatory-notes-for-non-standard-code
  - use-a-project-portal-for-your-team-and-client
created: 2025-10-16T16:49:00.000Z
guid: 86655840-0d01-4fb1-aba8-fabd54e1e916
---

When using AI assistants (like GitHub Copilot, Claude, ChatGPT, or Cursor) for development tasks, they often generate valuable documentation summaries explaining the changes made, architectural decisions, and implementation details. Properly organizing these AI-generated documentation ensures that:
- Significant changes are properly documented
- Documentation noise is minimized
- Task summaries are easily discoverable

<!--endintro-->

### The Problem with Unorganized Documentation

When AI tools generate documentation during development sessions, developers often:

- Save files with random names like `summary.md`, `changes.md`, or `notes.md`
- Scatter documentation files throughout the repository
- Create redundant documentation for minor changes
- Lose track of which documentation relates to which task

### The Problem with Over-Documentation

Creating documentation for every small change leads to:

::: greybox
**docs/**
- `fix-typo-in-readme.md`
- `update-variable-name.md`
- `correct-spacing.md`
- `fix-null-check.md`
- `add-missing-semicolon.md`
:::
::: bad
Bad Example - Too many documentation files for trivial changes creates noise and makes important documentation harder to find
:::

## The Solution: Structured AI Task Documentation

Implement a standardized approach by adding guidelines to your AI assistant instructions. This ensures your AI tools only create documentation when appropriate and use a consistent naming convention.

### 1. Add to Your AI Assistant Instructions

Add the following section to your AI assistant configuration (e.g., `.github/copilot-instructions.md`, `.cursorrules`, `.ai/instructions.md`, or your preferred location):
```markdown
## AI Task Documentation

When creating documentation files (MD files) during AI-assisted development, follow these guidelines to avoid unnecessary documentation noise:

### When to Create New Documentation

**DO create new documentation for**:
- Significant architectural changes or new features
- Major refactorings that affect multiple modules
- New patterns or conventions being established
- Implementation guides that will be referenced by others
- Complex changes that need detailed explanation for future reference

**DO NOT create new documentation for**:
- Minor bug fixes or corrections
- Small adjustments to existing code
- Clarifications or improvements to existing implementations
- Changes that can be adequately explained in commit messages

**When unsure**: Ask if documentation should be created before writing it. It's better to update existing documentation than create redundant files.

### Documentation File Naming Format
All documentation files created during AI-assisted tasks should be saved to `docs/ai-tasks/` with the following format:

yyyyMMdd-II-XX-description.md

Where:
- `yyyyMMdd` = Current date (e.g., 20251002)
- `II` = Author's initials from git config (e.g., GB for Gordon Beeming)
- `XX` = Sequential number starting at 01 for the day (01, 02, 03, etc.)
- `description` = Kebab-case description of the task/document

### Examples
- `20251002-GB-01-graceful-row-failure-implementation-summary.md`
- `20251002-GB-02-graceful-row-failure-refactoring-guide.md`
- `20251002-GB-03-graceful-row-failure-changes-summary.md`

### Process
1. **Determine if documentation is needed** - Is this a significant change?
2. Get current date in yyyyMMdd format
3. Get author initials from git config or developer identity
4. Check existing files in `docs/ai-tasks/` for today's date to determine next sequence number
5. Check if existing documentation should be **updated** instead of creating new
6. Create file with proper naming format only if needed
7. If multiple related documents, use sequential numbers to maintain order

### Updating Existing Documentation

Prefer updating existing documentation when:
- The change is related to a recent task documented today
- It's a bug fix or improvement to something recently implemented
- It adds clarification or correction to existing docs
- The change is minor and fits within the scope of existing documentation
```

### 2. Create the Documentation Directory

Set up the directory structure in your repository:
```bash
mkdir -p docs/ai-tasks
```

### 3. Add to .gitignore (Optional)

If you prefer to keep task summaries local and not commit them:
```gitignore
# Optional: Exclude AI task documentation from version control
docs/ai-tasks/
```

::: info
**Tip:** Most teams should commit this documentation to share context across the team. Only exclude it if your team uses a separate documentation system.
:::

## Benefits

This standardized approach provides:

✅ **Clarity:** Clear guidelines on when documentation should be created  
✅ **Discoverability:** Consistent naming makes finding relevant documentation easy  
✅ **Organization:** All task summaries in one dedicated location  
✅ **Traceability:** Date and author initials provide clear audit trail  
✅ **Signal-to-noise ratio:** Only significant changes are documented  
✅ **Chronological ordering:** Sequential numbering maintains task order  
✅ **Tool-agnostic:** Works with any AI assistant or development tool

### Example Result

::: greybox
**docs/ai-tasks/**
- `20250102-GB-01-implement-authentication-module.md`
- `20250102-GB-02-add-role-based-authorization.md`
- `20250115-DM-01-refactor-database-layer-for-multi-tenancy.md`
- `20250115-DM-02-add-tenant-isolation-integration-tests.md`
:::
::: good
Good Example - Clear, organized, and meaningful documentation that's easy to navigate and understand
:::

## Conclusion

By configuring your AI assistants with these instructions, you ensure that AI-generated documentation enhances your project rather than cluttering it. The structured approach makes it easy for team members to find relevant task summaries while maintaining a clean and organized repository.
