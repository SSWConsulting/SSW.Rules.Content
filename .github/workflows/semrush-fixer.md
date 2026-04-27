---
description: >
  SEMrush duplicate SEO field fixer.
  Runs weekly, audits all SEMrush Site Audit issues, prioritises by page count,
  and fixes duplicate seoDescription and title frontmatter on /rules pages.
  Opens one pull request per issue type for human review.
name: SEMrush SEO Fixer

on:
  push:
    branches: [2607-auto-workflow-for-semrush-errors-v3] # TODO: remove before merging to main
  schedule:
    - cron: "0 9 * * 1" # Every Monday at 9:00 AM UTC
  workflow_dispatch:

engine:
  id: copilot
  model: gpt-5-mini

mcp-scripts:
  list-semrush-issues:
    description: >
      Lists all SEMrush Site Audit issue types with page counts.
      Returns JSON array sorted by count descending.
      Items with a "fixable_as" field are ones this agent can fix.
    run: |
      pip install -q requests
      python scripts/semrush/semrush_client.py list-issues

  get-semrush-pages:
    description: >
      Returns JSON array of {url, file_path} for pages flagged with a given issue type.
      issue_type must be "duplicate_meta" or "duplicate_title".
    schema:
      issue_type:
        type: string
        description: The issue type to fetch pages for
        enum: [duplicate_meta, duplicate_title]
    run: |
      python scripts/semrush/semrush_client.py get-pages "$issue_type"

  read-frontmatter:
    description: >
      Reads the title and seoDescription frontmatter fields from a rule.mdx file.
      Returns JSON with "title" and "seoDescription" keys.
    schema:
      file_path:
        type: string
        description: Absolute path to the rule.mdx file
    run: |
      python scripts/semrush/frontmatter_utils.py read "$file_path"

  write-frontmatter:
    description: >
      Writes a new value to one frontmatter field in a rule.mdx file.
      field must be "seoDescription" or "title".
      Returns "OK" on success or exits with code 1 on failure.
    schema:
      file_path:
        type: string
        description: Absolute path to the rule.mdx file
      field:
        type: string
        description: The frontmatter field to update
        enum: [seoDescription, title]
      value:
        type: string
        description: The new value to write
    run: |
      python scripts/semrush/frontmatter_utils.py write "$file_path" "$field" "$value"

permissions: read-all

network:
  allowed:
    - defaults
    - "api.semrush.com"

concurrency:
  group: "semrush-fixer"
  cancel-in-progress: true

safe-outputs:
  create-pull-request:
    title-prefix: "[SEMrush] "
    max: 2

tools:
  github:
    lockdown: false
    toolsets: [repos, pull_requests]
    github-token: "${{ secrets.GITHUB_TOKEN }}"
---

## Context

You are an SEO automation agent for SSW's rules website (ssw.com.au/rules).
Your goal is to fix duplicate SEO frontmatter fields flagged by SEMrush Site Audit.

The repository lives at `${{ github.workspace }}`. All `/rules` pages are MDX files at:
```
public/uploads/rules/<slug>/rule.mdx
```

You have four MCP tools to use:
- `list-semrush-issues` — see all SEMrush issues and their page counts
- `get-semrush-pages` — get the list of affected files for a fixable issue type
- `read-frontmatter` — read current frontmatter values from a file
- `write-frontmatter` — write a new value to a frontmatter field

---

## Step 1 — Audit and prioritise

Call `list-semrush-issues` to see all current problems and their scale.

From the results, identify which issue types are `fixable_as` (only `duplicate_meta` and `duplicate_title` are supported).

**Prioritisation rules:**
- Skip an issue type if `count` is 0.
- If both are worth fixing, process the one with the higher count first.
- Briefly state your decision (what you will fix and why) before starting work.

---

## Step 2 — Fix each issue type

For each issue type you decide to fix, follow this workflow:

### 2a — Get affected pages

Call `get-semrush-pages` with the issue type to get a list of `{url, file_path}` objects.

### 2b — Fix each page

For each page:

1. Call `read-frontmatter` with the `file_path` to get the current `title` and `seoDescription`.
2. Generate a unique replacement value based on the page content and title:
   - **seoDescription**: strictly under 160 characters, no filler openers
     (`Learn` / `Discover` / `Find out` / `In this article` / `This page`),
     no trailing full stop, specific and concrete.
   - **title**: must start with `Do you` and end with `?`, unique, descriptive,
     faithful to the page content. Example: `Do you use pull requests for all code changes?`
3. Call `write-frontmatter` with the file path, field name, and your generated value.
4. If the write fails, try a different value and retry.
5. Keep track of values you have already written — never reuse a value across pages.

### 2c — Commit and open a PR

After all pages for this issue type are processed:

1. Create a branch from `main`:
   - For `duplicate_meta`: `semrush/fix-duplicate-meta`
   - For `duplicate_title`: `semrush/fix-duplicate-titles`
2. Stage and commit only the files you modified:
   ```
   git add -- <file1> <file2> ...
   git commit -m "fix(seo): replace duplicate <field> [SEMrush audit]"
   git push origin <branch>
   ```
3. Check if an open PR already exists for this branch using the GitHub `pull_requests` toolset.
   If one exists, skip PR creation and log a message.
4. If no open PR exists, call `create-pull-request` (safe-output) with:
   - **title**: `Fix duplicate <seoDescription|title> for /rules (<N> pages)`
   - **body**: (see format below)

**PR body format:**

```markdown
Fixes duplicate `<field>` frontmatter on <N> /rules page(s) flagged by SEMrush Site Audit.
Only frontmatter was modified — page body and all other fields are unchanged.
New values were generated by AI.

| File | Old <field> | New <field> |
|------|-------------|-------------|
| `<rel_path>` | <old value> | <new value> |
...

> AI-generated — human review required before merge.
```

---

## Step 3 — Summary

After all issue types are processed, output a summary:
- Which issue types were fixed and how many pages each
- Which were skipped and why
- Any pages that failed and were skipped
