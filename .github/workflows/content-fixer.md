---
description: >
  Agent 3 (Fixer) of the ContentHawk pipeline.
  Runs on a cron schedule (or manually) and picks up the first available
  snapshot from the TODO folder. Reads the snapshot to obtain the Label,
  PR Preferences, and Intent, then bundles eligible issues into groups and
  creates one PR per bundle that applies the content fixes and closes the
  linked issues.
  Skips issues already referenced in existing open fixer PRs to avoid
  duplicate work. Exits gracefully if no snapshot file is found in the
  TODO folder.
name: Content Fixer (Agent 3a)

on:

  schedule:
    - cron: "0 0 * * */7"
  skip-if-no-match: 'is:issue is:open in:body "gh-aw-workflow-id: content-judge"'
  workflow_dispatch:
  steps:
    - name: Find first snapshot
      id: snapshot_check
      uses: actions/github-script@v7
      with:
        github-token: ${{ secrets.CONTENTHAWK_GITHUB_PAT }}
        script: |
          let files = [];
          try {
            const { data } = await github.rest.repos.getContent({
              owner: context.repo.owner,
              repo: context.repo.repo,
              path: '.github/ContentHawk/TODO',
            });
            files = data;
          } catch (e) {
            core.setOutput('snapshot_exists', 'false');
            return;
          }
          if (files.length === 0) {
            core.setOutput('snapshot_exists', 'false');
            return;
          }
          core.setOutput('snapshot_exists', 'true');

jobs:
  pre-activation:
    outputs:
      snapshot_exists: ${{ steps.snapshot_check.outputs.snapshot_exists }}

if: needs.pre_activation.outputs.snapshot_exists == 'true'

engine:
  id: copilot
  model: claude-sonnet-4.6

mcp-servers:
  tavily:
    command: npx
    args: ["-y", "tavily-mcp"]
    env:
      TAVILY_API_KEY: "${{ secrets.TAVILY_API_KEY }}"
    allowed: ["tavily_search"]

mcp-scripts:
  list-snapshots:
    description: >
      Lists all snapshot files in the TODO folder, sorted oldest-first
      so the first line is the next snapshot to process.
    run: |
      ls .github/ContentHawk/TODO/*_Snapshot_*.md 2>/dev/null | sort

permissions: read-all

network:
  allowed:
    - defaults
    - "*.tavily.com"

concurrency:
  group: "contenthawk-fixer"
  cancel-in-progress: true

safe-outputs:
  report-failure-as-issue: false
  create-pull-request:
    title-prefix: "[Content Fixer] "
    max: 5

tools:
  github:
    lockdown: false
    toolsets: [issues, repos, pull_requests, search, labels]
    github-token: "${{ secrets.CONTENTHAWK_GITHUB_PAT }}"

post-steps:
  - name: Workflow Summary
    if: always()
    run: |
      echo "## ContentHawk — Agent 3 (Fixer)" >> "$GITHUB_STEP_SUMMARY"
      echo "" >> "$GITHUB_STEP_SUMMARY"

      echo "### Trigger" >> "$GITHUB_STEP_SUMMARY"
      echo "" >> "$GITHUB_STEP_SUMMARY"
      echo "| Field              | Value |" >> "$GITHUB_STEP_SUMMARY"
      echo "|--------------------|-------|" >> "$GITHUB_STEP_SUMMARY"
      echo "| Event              | \`${{ github.event_name }}\` |" >> "$GITHUB_STEP_SUMMARY"
      echo "" >> "$GITHUB_STEP_SUMMARY"

      echo "### Agent Output" >> "$GITHUB_STEP_SUMMARY"
      echo "" >> "$GITHUB_STEP_SUMMARY"
      if [ -d /tmp/gh-aw ]; then
        echo "\`\`\`" >> "$GITHUB_STEP_SUMMARY"
        find /tmp/gh-aw -type f | head -30 >> "$GITHUB_STEP_SUMMARY"
        echo "\`\`\`" >> "$GITHUB_STEP_SUMMARY"
      else
        echo "_No agent output directory found._" >> "$GITHUB_STEP_SUMMARY"
      fi
---

## Important context

This workflow is **Agent 3 (Fixer)** in a multi-agent pipeline called **ContentHawk**:

- **Agent 1 (Detective)**: Catalogs content files, creates a snapshot tracking file on a branch, and opens a PR. That PR is reviewed and merged into `main` before Agent 2a runs.
- **Agent 2a (Judge)**: Reads the merged snapshot, judges each pending file against the intent, and opens issues for files that need fixing. Triggers Agent 2b via a post-step when it completes.
- **Agent 2b (PR Creator)**: Reads the issues created by Agent 2a, updates the snapshot with issue numbers, and opens a PR.
- **Agent 3 (this workflow)**: Runs on a schedule, picks up the first available snapshot from the TODO folder, reads open issues for that snapshot's label, bundles them according to PR Preferences, applies content fixes, and opens PRs that close the bundled issues.

The snapshot file is **self-contained** — it stores every configuration value Agent 1 received, including the PR Preferences that control how Agent 3 bundles and creates PRs.

## How this workflow is triggered

This workflow runs on a **cron schedule** (every 6 hours) and can also be triggered manually via `workflow_dispatch`. It does **not** accept any inputs — instead, it discovers the next snapshot to process from the TODO folder automatically.

---

Do **not** create any PRs. End the workflow here.

If files are found, **choose `snapshot_path`** — use the **first line** of the result (the oldest snapshot, i.e. the one that has been waiting longest). Read the full content of that file from `main`.

### Step 1 — Read and parse the snapshot

#### 1a. Parse the Agent Configuration table

Extract the following fields from the `## Agent Configuration` table:

- **Intent** — what the judge was looking for in each file (Agent 3 uses this to understand what fixes to apply)
- **PR Preferences** — how to bundle and create PRs (e.g. "bundle up to 5 related issues per PR")
- **Label** — the label slug stored in the snapshot

Call the extracted label value **`label_name`**. This is the label that will be used throughout the rest of the workflow to find issues, label PRs, and guard concurrency.

#### 1b. Parse the Files to Review table

Read the `## Files to Review` table. You do **not** need to process this table directly — Agent 3 works from issues, not from snapshot rows. However, the table is useful context: rows with a `CheckResult` of `Issue #<number>` are the ones Agent 2a flagged, and their issues are what Agent 3 will fix.

### Step 2 — Collect eligible issues

#### 2a. Extract issue numbers from the snapshot

Parse the `## Files to Review` table (read in Step 1b). For each row where the `CheckResult` column matches `Issue #<number>`, extract the issue number. Collect all extracted issue numbers into a list called `snapshot_issue_numbers`.

If `snapshot_issue_numbers` is empty, **stop immediately** with a message:

> No issues found in the snapshot file. Nothing to fix. Exiting.

#### 2b. Filter out issues already referenced in open pull requests

For each issue number in `snapshot_issue_numbers`, use the GitHub `pull_requests` toolset to search for **open** pull requests in this repository whose body contains `#<number>` (e.g. `#42` for issue 42).

If **any** open PR is found that references the issue number in its body, **remove that issue number** from `snapshot_issue_numbers` — it is already being addressed by an in-flight PR.

If `snapshot_issue_numbers` is empty after filtering, **stop immediately** with a message:

> All issues in the snapshot are already referenced in open pull requests. Nothing to fix. Exiting.

#### 2c. Fetch issue details and filter to open issues

For each issue number in `snapshot_issue_numbers`, fetch the issue from GitHub. Only include issues that are **open** — closed issues have already been resolved and should be skipped. For each open issue, record:

- `number` — the issue number
- `title` — the issue title
- `body` — the full issue body

Call this list `eligible_issues`.

If `eligible_issues` is empty, **stop immediately** with a message:

> All issues listed in the snapshot are already closed. Nothing to fix. Exiting.

### Step 3 — Bundle issues

Read the **PR Preferences** extracted in Step 1a. Use them to determine bundling rules:

- **Bundle size** — the maximum number of issues per PR. Look for language like "bundle up to N issues per PR" or "max N per PR". If the PR Preferences do not specify a number, default to **5 issues per bundle**.
- **Grouping strategy** — the PR Preferences may specify how to group issues (e.g. "by category", "by file path similarity", "by topic"). If no grouping strategy is specified, group issues by file path similarity (files in the same directory or with related names go together).

Follow this procedure:

1. For each issue in `eligible_issues`, parse the `### File` section of the issue body to extract the file path.
2. Group issues by relatedness according to the grouping strategy. Issues affecting files in the same directory or with overlapping topics should be in the same bundle.
3. Split each group into sub-bundles of at most `bundle_size` issues.
4. Produce a `bundles` list where each bundle is a list of `{ number, title, path, finding, suggestions }` objects.

If the PR Preferences contain **any other instructions** about PR creation (e.g. a PR template path, specific formatting, draft vs. ready), note them for Step 4.

### Step 4 — Fix content and create PRs

Work through `bundles` one at a time. For each bundle:

#### 4a. Create a working branch

Create a new branch from `main` named:

```
ContentHawk/fixer/<label_name>/<bundle-index>
```

Where `<label_name>` is the label extracted from the snapshot and `<bundle-index>` is a 1-based index (e.g. `1`, `2`, `3`).

#### 4b. Apply fixes to each file in the bundle

For each issue in the bundle:

1. Read the file at the `path` extracted from the issue body.
2. Understand the **finding** and **suggestions** from the issue body.
3. Apply the fix to the file content based on the **Intent** from Step 1a and the **suggestions** from the issue.
4. If the fix requires external research (e.g. finding the current best practice, the modern replacement for a deprecated technology, or validating a URL), use the Tavily search tool to gather accurate information before making the change.
5. Write the updated file content.

**Important guidelines for applying fixes:**

- Make the minimum change necessary to address the finding. Do not rewrite entire files.
- Preserve the file's existing structure, formatting, and front-matter.
- If a suggestion involves updating a date field (e.g. `lastUpdated`), set it to today's date in the format the file already uses.
- If you cannot confidently fix a file (e.g. the suggestion is ambiguous, the file structure is unexpected, or the fix would require domain expertise you lack), **skip that file** and note it in the PR body. Do not make speculative changes.

#### 4c. Commit all changes

Commit all modified files to the branch with the message:

```
content-hawk[fixer]: fix <N> issues for <label_name>
```

Where `<N>` is the number of files actually modified in this bundle.

#### 4d. Open a pull request

Open a PR using the `create-pull-request` safe-output tool. Add the label `<label_name>` to the PR.

**Title**: `<label_name> — fix <N> issues (<brief-description>)`

> Note: the `title-prefix` safe-output setting will prepend `[Content Fixer] ` automatically — so only pass `<label_name> — fix <N> issues (<brief-description>)` as the title value. The `<brief-description>` should summarise the bundle (e.g. "outdated .NET references", "deprecated API mentions").

**Base branch**: `main`

**Body**:

```markdown
## ContentHawk — Agent 3 (Fixer) Results

### Summary

| Metric              | Count |
|---------------------|-------|
| Issues fixed        | <N>   |
| Issues skipped      | <S>   |

### Intent

<Intent from the snapshot>

### Label

`<label_name>`

### Snapshot

`<snapshot_path resolved in Step 0>`

### Issues resolved

<For each issue in the bundle that was successfully fixed, write one line:>
Closes #<number>

<If any issues in the bundle were skipped (could not be fixed), list them separately:>

### Issues skipped (could not be fixed)

<For each skipped issue, write: `- #<number> — <reason>`>
<If none were skipped, omit this section.>

### Changes made

<For each file modified, write a brief summary of what was changed and why.>

---

contenthawk-fixer-run-id: ${{ github.run_id }}
```

The `Closes #<number>` lines in the body will automatically link and close the issues when the PR is merged.

### Step 5 — Summary

After all bundles have been processed, output a summary of the entire run:

- Snapshot processed: `<snapshot_path>`
- Label: `<label_name>`
- Total PRs created
- Total issues fixed across all PRs
- Total issues skipped (could not be fixed)
- Total issues still open (not included in any bundle, e.g. because of bundle-size limits)
