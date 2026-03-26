---
description: >
  Agent 3 (Fixer) of the ContentHawk pipeline.
  Searches for open issues with the intent label, reads the snapshot to
  obtain PR Preferences and Intent, then bundles eligible issues into
  groups and creates one PR per bundle that applies the content fixes and
  closes the linked issues.
  Skips issues already referenced in existing open fixer PRs to avoid
  duplicate work. Stops immediately if the number of eligible issues is
  below the configured minimum threshold.

on:
  workflow_dispatch:
    inputs:
      label_name:
        description: "GitHub label slug that ties this pipeline together (e.g. 'archive-legacy-rules'). Must match the Label field in the snapshot."
        required: true
      min_issues_to_bundle:
        description: "Minimum number of eligible open issues required before Agent 3 will create PRs. Defaults to 10."
        required: false
        default: "10"

engine:
  id: copilot
  model: gpt-5-mini

mcp-servers:
  tavily:
    command: npx
    args: ["-y", "tavily-mcp"]
    env:
      TAVILY_API_KEY: "${{ secrets.TAVILY_API_KEY }}"
    allowed: ["tavily_search"]

mcp-scripts:
  list-snapshots:
    env:
      INPUT_LABEL_NAME: ${{ inputs.label_name }}
    description: >
      Lists all snapshot files produced by Agent 1
    run: |
      ls .github/ContentHawk/TODO/*_Snapshot_${INPUT_LABEL_NAME}.md 2>/dev/null | sort -r

permissions: read-all

network:
  allowed:
    - defaults
    - "*.tavily.com"

concurrency:
  group: "contenthawk-fixer-${{ inputs.label_name }}"
  cancel-in-progress: false

safe-outputs:
  create-pull-request:
    title-prefix: "[Content Fixer] "
    labels: ["${{ inputs.label_name }}"]
    max: 5

tools:
  github:
    lockdown: false
    toolsets: [issues, repos, pull_requests, search, labels]
    github-token: "${{ secrets.TINA_GITHUB_PAT }}"
  tavily:
    tools: [search, search_news]

post-steps:
  - name: Workflow Summary
    if: always()
    env:
      INPUT_LABEL_NAME: ${{ inputs.label_name }}
      INPUT_MIN_ISSUES: ${{ inputs.min_issues_to_bundle }}
    run: |
      echo "## ContentHawk — Agent 3 (Fixer)" >> "$GITHUB_STEP_SUMMARY"
      echo "" >> "$GITHUB_STEP_SUMMARY"

      echo "### Inputs" >> "$GITHUB_STEP_SUMMARY"
      echo "" >> "$GITHUB_STEP_SUMMARY"
      echo "| Field              | Value |" >> "$GITHUB_STEP_SUMMARY"
      echo "|--------------------|-------|" >> "$GITHUB_STEP_SUMMARY"
      echo "| Label              | \`$INPUT_LABEL_NAME\` |" >> "$GITHUB_STEP_SUMMARY"
      echo "| Min Issues         | $INPUT_MIN_ISSUES |" >> "$GITHUB_STEP_SUMMARY"
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

  - name: Upload Agent Artifacts
    if: always()
    uses: actions/upload-artifact@v4
    with:
      name: contenthawk-agent3-results
      path: /tmp/gh-aw/
      retention-days: 7
---

## Important context

This workflow is **Agent 3 (Fixer)** in a multi-agent pipeline called **ContentHawk**:

- **Agent 1 (Detective)**: Catalogs content files, creates a snapshot tracking file on a branch, and opens a PR. That PR is reviewed and merged into `main` before Agent 2a runs.
- **Agent 2a (Judge)**: Reads the merged snapshot, judges each pending file against the intent, and opens issues for files that need fixing. Triggers Agent 2b via a post-step when it completes.
- **Agent 2b (PR Creator)**: Reads the issues created by Agent 2a, updates the snapshot with issue numbers, and opens a PR.
- **Agent 3 (this workflow)**: Reads open issues with the intent label, bundles them according to PR Preferences from the snapshot, applies content fixes to the actual files, and opens PRs that close the bundled issues.

The snapshot file is **self-contained** — it stores every configuration value Agent 1 received, including the PR Preferences that control how Agent 3 bundles and creates PRs.

## Inputs provided by the user

| Input              | Value                                    | Used for                                           |
|--------------------|------------------------------------------|----------------------------------------------------|
| Label Name         | `${{ inputs.label_name }}`               | Finding issues, labelling PRs, concurrency guard    |
| Min Issues         | `${{ inputs.min_issues_to_bundle }}`     | Threshold before creating PRs                       |

---

### Step 0 — Guard: check eligible issue count

Before doing any work, use the GitHub toolset to list all open issues that carry the label `${{ inputs.label_name }}`. Count the results to get `open_count`. Let `min_issues` = `${{ inputs.min_issues_to_bundle }}` (parsed as an integer).

If `open_count < min_issues`, **stop immediately**. Output a message like:

> Not enough issues to bundle: $open_count open issues with label '${{ inputs.label_name }}' (minimum: $min_issues). Waiting for more issues before creating fix PRs.

Do **not** read the snapshot or create any PRs. End the workflow here.

### Step 1 — Discover, then read and parse the snapshot

#### 1.0 — Resolve the snapshot file on `main`

Use the MCP script `list-snapshots` to find snapshot files on `main` that match the label naming convention.

1. If the result is empty (no snapshot files found), **stop immediately** with an error:

   > No snapshot file on main for label '${{ inputs.label_name }}'. Expected path pattern: `.github/ContentHawk/TODO/<date>_Snapshot_${{ inputs.label_name }}.md`. Aborting.

2. **Choose `snapshot_path`** — use the **first line** of the result (the latest date). If there are multiple lines, the first is already the correct one (latest date).
3. Call that path **`snapshot_path`**. Read the full content of that file from `main`.

#### 1a. Parse the Agent Configuration table

Extract the following fields from the `## Agent Configuration` table:

- **Intent** — what the judge was looking for in each file (Agent 3 uses this to understand what fixes to apply)
- **PR Preferences** — how to bundle and create PRs (e.g. "bundle up to 5 related issues per PR")
- **Label** — the label slug stored in the snapshot

**Validation**: Assert that the `Label` value extracted from the snapshot matches `${{ inputs.label_name }}` exactly (ignoring surrounding backticks). If they do not match, **stop immediately** with an error:

> Snapshot label '<snapshot_label>' does not match the input label '${{ inputs.label_name }}'. Aborting.

#### 1b. Parse the Files to Review table

Read the `## Files to Review` table. You do **not** need to process this table directly — Agent 3 works from issues, not from snapshot rows. However, the table is useful context: rows with a `CheckResult` of `Issue #<number>` are the ones Agent 2a flagged, and their issues are what Agent 3 will fix.

### Step 2 — Collect eligible issues (deduplication)

#### 2a. Fetch all open issues with the label

List every open issue that carries the label `${{ inputs.label_name }}`. For each issue, record:

- `number` — the issue number
- `title` — the issue title
- `body` — the full issue body

Call this list `all_open_issues`.

#### 2b. Fetch existing fixer PRs and build claimed-issues set

Search for all **open** pull requests that carry the label `${{ inputs.label_name }}` and whose title contains `[Content Fixer]`:

For each such PR, parse the PR body to find every reference of the form `Closes #<number>` or `Fixes #<number>`. Collect all referenced issue numbers into a `claimed_issues` set. These issues are already being handled by an existing fixer PR and must be excluded.

#### 2c. Filter to eligible issues

Build `eligible_issues` = issues from `all_open_issues` whose `number` is **not** in `claimed_issues`.

If `eligible_issues` is empty, **stop immediately** with a message:

> All open issues with label '${{ inputs.label_name }}' are already claimed by existing fixer PRs. Nothing to do.

If `eligible_issues` count is less than `min_issues`, **stop immediately** with a message:

> Only <count> eligible issues remain after deduplication (minimum: $min_issues). Waiting for more issues.

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
ContentHawk/fixer/${{ inputs.label_name }}/<bundle-index>
```

Where `<bundle-index>` is a 1-based index (e.g. `1`, `2`, `3`).

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
content-hawk[fixer]: fix <N> issues for ${{ inputs.label_name }}
```

Where `<N>` is the number of files actually modified in this bundle.

#### 4d. Open a pull request

Open a PR using the `create-pull-request` safe-output tool:

**Title**: `${{ inputs.label_name }} — fix <N> issues (<brief-description>)`

> Note: the `title-prefix` safe-output setting will prepend `[Content Fixer] ` automatically — so only pass `${{ inputs.label_name }} — fix <N> issues (<brief-description>)` as the title value. The `<brief-description>` should summarise the bundle (e.g. "outdated .NET references", "deprecated API mentions").

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

`${{ inputs.label_name }}`

### Snapshot

`<snapshot_path resolved in Step 1.0>`

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

- Total PRs created
- Total issues fixed across all PRs
- Total issues skipped (could not be fixed)
- Total issues still open (not included in any bundle, e.g. because of bundle-size limits)
- Total issues already claimed by existing fixer PRs (from Step 2b)
