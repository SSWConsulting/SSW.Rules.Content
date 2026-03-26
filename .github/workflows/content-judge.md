---
description: >
  Agent 2a (Judge) of the ContentHawk pipeline.
  Discovers the merged snapshot on main by label (filename convention), parses
  the Agent Configuration and Files to Review table, then iterates over every
  pending row in order. For each file it reads the content, judges whether the
  file needs action based on the Intent captured by Agent 1, and opens a
  labelled GitHub issue for files that need fixing.
  After all affordable rows have been processed a post-step dispatches
  Agent 2b (content-judge-pr) which reads the created issues and opens a
  pull request to update the snapshot.
  Stops immediately if the number of open labelled issues already meets
  or exceeds max_open_issues without making any changes.

on:
  workflow_dispatch:
    inputs:
      label_name:
        description: "Label matching the agentic workflow label."
        required: true
      max_open_issues:
        description: "Stop opening new issues once this many issues with the label are already open. Defaults to 30."
        required: false
        default: "30"

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
  group: "contenthawk-judge-${{ inputs.label_name }}"
  cancel-in-progress: false

safe-outputs:
  create-issue:
    labels: ["${{ inputs.label_name }}"]
    title-prefix: "🦅 ContentHawk - Content Audit: "
    max: 30
steps:
  - name: Guard — no open Content Judge PR for this label
    uses: ./.github/actions/guard-open-pr
    with:
      label_name: ${{ inputs.label_name }}
      workflow_id: content-judge-pr
  - name: Generated Skipped Files Output
    run: mkdir -p /tmp/gh-aw && echo "" > /tmp/gh-aw/skipped_files.txt
tools:
  github:
    lockdown: false
    toolsets: [issues, repos, search, labels]
    github-token: "${{ secrets.TINA_GITHUB_PAT }}"
  tavily:
    tools: [search, search_news]

post-steps:
  - name: Workflow Summary
    if: always()
    env:
      INPUT_LABEL_NAME: ${{ inputs.label_name }}
      INPUT_MAX_OPEN_ISSUES: ${{ inputs.max_open_issues }}
    run: |
      echo "## ContentHawk — Agent 2 (Judge)" >> "$GITHUB_STEP_SUMMARY"
      echo "" >> "$GITHUB_STEP_SUMMARY"

      echo "### Inputs" >> "$GITHUB_STEP_SUMMARY"
      echo "" >> "$GITHUB_STEP_SUMMARY"
      echo "| Field            | Value |" >> "$GITHUB_STEP_SUMMARY"
      echo "|------------------|-------|" >> "$GITHUB_STEP_SUMMARY"
      echo "| Label            | \`$INPUT_LABEL_NAME\` |" >> "$GITHUB_STEP_SUMMARY"
      echo "| Max Open Issues  | $INPUT_MAX_OPEN_ISSUES |" >> "$GITHUB_STEP_SUMMARY"
      echo "| Snapshot         | Resolved via \`*_Snapshot_${INPUT_LABEL_NAME}.md\` on \`main\` |" >> "$GITHUB_STEP_SUMMARY"
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

  - name: Ensure skipped files artifact is readable
    if: always()
    run: chmod a+r /tmp/gh-aw/skipped_files.txt 2>/dev/null || true

  - name: Upload Agent Artifacts
    if: always()
    uses: actions/upload-artifact@v7
    with:
      name: ${{ github.run_id }}
      path: /tmp/gh-aw/skipped_files.txt
      if-no-files-found: error
      retention-days: 7

  - name: Trigger Agent 2b (PR Creator)
    if: success()
    env:
      GH_TOKEN: ${{ secrets.TINA_GITHUB_PAT }}
      INPUT_LABEL_NAME: ${{ inputs.label_name }}
      INPUT_JUDGE_RUN_ID: ${{ github.run_id }}
    run: |
      set -euo pipefail
      git fetch origin main --depth 1
      # Snapshot path convention (Agent 1): .github/ContentHawk/TODO/YYYY-MM-DD_Snapshot_<label>.md
      _matches=()
      while IFS= read -r _path; do
        case "$_path" in
          .github/ContentHawk/TODO/[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]_Snapshot_${INPUT_LABEL_NAME}.md)
            _matches+=("$_path") ;;
        esac
      done < <(git ls-tree -r origin/main --name-only | grep '^\.github/ContentHawk/TODO/' || true)
      SNAPSHOT_PATH=$(printf '%s\n' "${_matches[@]:-}" | sort -r | head -1)
      if [ -z "$SNAPSHOT_PATH" ]; then
        echo "::error::No snapshot on main matching <date>_Snapshot_${INPUT_LABEL_NAME}.md under .github/ContentHawk/TODO/"
        exit 1
      fi
      echo "Resolved snapshot: $SNAPSHOT_PATH"
      gh workflow run content-judge-pr.lock.yml \
        -f snapshot_path="$SNAPSHOT_PATH" \
        -f label_name="$INPUT_LABEL_NAME" \
        -f judge_run_id="$INPUT_JUDGE_RUN_ID"
---

## Important context

This workflow looks for a snapshot file on `main` using the label, judges each pending file against the intent, and opens issues for files that need fixing. It does **not** update the snapshot or create a PR.

Use the MCP script `list-snapshots` to find snapshot files on `main` that match the label naming convention. Read and parse the latest snapshot file to get the intent and pending files. For each pending file, read its content, judge it against the intent (using web search if needed), and create an issue if it needs action. Stop processing more files if the number of open issues with this label meets or exceeds the `max_open_issues` threshold.

### Step 1 — Discover, then read and parse the snapshot

#### 1.0 — Resolve the snapshot file on `main`

**Your task:**

1. If the file is empty (no snapshot files found), **stop immediately** with an error:

   > No snapshot file on main for label '${{ inputs.label_name }}'. Expected path pattern: `.github/ContentHawk/TODO/<date>_Snapshot_${{ inputs.label_name }}.md`. Aborting.

2. **Choose `snapshot_path`** — use the **first line** of the file (the latest date). If there are multiple lines, the first is already the correct one (latest date).
3. Call that path **`snapshot_path`**. Read the full content of that file from `main`.

#### 1a. Parse the Agent Configuration table

Extract the following fields from the `## Agent Configuration` table:

* **Intent** — what to look for in each file
* **Issue Preferences** — how to write issues (templates, detail level, max per run, etc.)
* **Label** — the label slug stored in the snapshot

**Validation**: Assert that the `Label` value extracted from the snapshot matches `${{ inputs.label_name }}` exactly (ignoring surrounding backticks). If they do not match, **stop immediately** with an error:

> Snapshot label '<snapshot_label>' does not match the input label '${{ inputs.label_name }}'. Aborting.

#### 1b. Parse the Files to Review table

Collect every row from the `## Files to Review` table where `CheckResult` is exactly `pending`. Preserve the exact row order from the table — this is the processing order. Call this list `pending_rows`.

If `pending_rows` is empty (all rows already have a non-pending CheckResult), **stop immediately** with a message:

> No pending rows found in snapshot. Nothing to do.

### Step 2 — Check open-issue headroom

Count the number of currently open issues that carry the label `${{ inputs.label_name }}`:

list issues with the tool `list_issues` tool from the toolsset. with `state=open`
`labels=${{ inputs.label_name }}` and count them. 

Let this count be `open_count`. Let `max_open_issues` = `${{ inputs.max_open_issues }}` (parsed as an integer).

If `open_count >= max_open_issues`, **stop immediately**. Output a message like:

> Issue limit reached: $open_count open issues already exist with label '${{ inputs.label_name }}' (max: $max_open_issues). Run again after issues are closed.

Do **not** create any issues.

### Step 3 — Process pending rows in order

Work through `pending_rows` one at a time, **in order**. For each row:

#### 3a. Re-check headroom

Before processing this row, re-count open issues:

list issues with the tool `list_issues` tool from the toolsset. with `state=open`
`labels=${{ inputs.label_name }}` and count them. 

If the count meets or exceeds `max_open_issues` **stop the loop**. Log a message noting the headroom limit was reached and how many rows remain unprocessed.

#### 3b. Read the content file

Read the full content of the file at the `Path` value from the row. If the file does not exist in the repository, log a warning and continue to the next row.

#### 3c. Judge the file

Evaluate the file's content against the **Intent** extracted in Step 1a. Your judgment must determine:

1. **`needs_action`** (`true` or `false`) — does this file require attention based on the intent?
2. **`issue_summary`** — if `needs_action` is true: a concise description of the specific problem (≤ 10 words, used directly in the issue title). Make it specific to this file, not generic.
3. **`issue_body`** — if `needs_action` is true: a fuller description for the issue body (see Step 3d for required sections). Respect any formatting or template instructions from **Issue Preferences**.

**Using web search during judgment**: If evaluating the file requires external context (e.g. checking whether a technology is deprecated, whether a recommended practice has changed, whether a link or reference is still valid), use the Tavily search tool:

* Formulate targeted queries like `"[technology] deprecated 2025"`, `"[tool] end of life"`, `"[topic] current best practices"`
* Let search results inform whether the file's content is outdated, inaccurate, or in need of the action described in the intent
* If search results are inconclusive, default to `needs_action = false` (do not create spurious issues)

#### 3d. Create an issue (if `needs_action = true`)

Create a GitHub issue using the `create-issue` safe-output tool:


**Title**: `🦅 ContentHawk - Content Audit: <issue_summary>`

> Note: the `title-prefix` safe-output setting will prepend `🦅 ContentHawk - Content Audit: ` automatically — so only pass the `<issue_summary>` part as the title value.

**Body** (use these exact sections, honouring any formatting instructions from Issue Preferences):

```markdown
### File

`<Path>`

### Finding

<A clear explanation of why this file needs attention, based on your analysis. Be specific — reference the actual content that triggered the finding.>

### Suggestions

<Concrete, actionable suggestions for how to resolve the issue. If you used web search, include relevant references.>

---

contenthawk-run-id: ${{ github.run_id }}
```

Log the issue creation. Continue to the next row.

#### 3e. Skip the file (if `needs_action = false`)

  if you find a file that does not need action, use the following command to append the file path to a list of skipped files for this run.

```
echo "- <Path>" >> /tmp/gh-aw/skipped_files.txt
```

### Step 4 — Summary

After the loop completes, output a summary of the run. Include the total number of issues created, files skipped, and rows still pending (if the headroom limit was reached). Include the **`snapshot_path`** you resolved in Step 1.0 so logs tie back to the correct file. Skipped files are written to `/tmp/gh-aw/skipped_files.txt` and will be uploaded automatically by the artifact post-step.
