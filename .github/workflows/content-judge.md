---
description: >
  Agent 2a (Judge) of the ContentHawk pipeline.
  Runs on a cron schedule (or manually) and picks up the first available
  snapshot from the TODO folder. Reads the snapshot to obtain the Label,
  Intent, and Issue Preferences, then iterates over every pending row in
  order. For each file it reads the content, judges whether the file needs
  action based on the Intent captured by Agent 1, and opens a labelled
  GitHub issue for files that need fixing.
  After all affordable rows have been processed a post-step dispatches
  Agent 2b (content-judge-pr) which reads the created issues and opens a
  pull request to update the snapshot.
  Stops immediately if the number of open labelled issues already meets
  or exceeds max_open_issues without making any changes.
name: Content Judge (Agent 2a)
on:
  schedule:
    - cron: "0 * * * */7"
  workflow_dispatch:

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
  group: "contenthawk-judge"
  cancel-in-progress: true

safe-outputs:
  report-failure-as-issue: false
  create-issue:
    title-prefix: "🦅 ContentHawk - Content Audit: "
    max: 30
steps:
  - name: Generated Skipped Files Output
    run: mkdir -p /tmp/gh-aw && echo "" > /tmp/gh-aw/skipped_files.txt && echo "" > /tmp/gh-aw/label_name.txt
tools:
  github:
    lockdown: false
    toolsets: [issues, repos, search, labels, pull_requests]
    github-token: "${{ secrets.CONTENTHAWK_GITHUB_PAT }}"

post-steps:
  - name: Check if work was done
    id: noop-check
    if: always()
    run: |
      if [ -f /tmp/gh-aw/work_done.txt ]; then
        echo "did_work=true" >> "$GITHUB_OUTPUT"
      else
        echo "did_work=false" >> "$GITHUB_OUTPUT"
        echo "Noop run — agent exited before processing any files."
      fi
  - name: Workflow Summary
    if: always()
    run: |
      LABEL_NAME=""
      if [ -f /tmp/gh-aw/label_name.txt ]; then
        LABEL_NAME=$(cat /tmp/gh-aw/label_name.txt | tr -d '[:space:]')
      fi

      echo "## ContentHawk — Agent 2 (Judge)" >> "$GITHUB_STEP_SUMMARY"
      echo "" >> "$GITHUB_STEP_SUMMARY"

      echo "### Run Info" >> "$GITHUB_STEP_SUMMARY"
      echo "" >> "$GITHUB_STEP_SUMMARY"
      echo "| Field              | Value |" >> "$GITHUB_STEP_SUMMARY"
      echo "|--------------------|-------|" >> "$GITHUB_STEP_SUMMARY"
      echo "| Event              | \`${{ github.event_name }}\` |" >> "$GITHUB_STEP_SUMMARY"
      echo "| Label              | \`${LABEL_NAME:-<not resolved>}\` |" >> "$GITHUB_STEP_SUMMARY"
      echo "| Max Open Issues    | 30 |" >> "$GITHUB_STEP_SUMMARY"
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
    if: always() && steps.noop-check.outputs.did_work == 'true'
    run: chmod a+r /tmp/gh-aw/skipped_files.txt 2>/dev/null || true

  - name: Upload Agent Artifacts
    if: always() && steps.noop-check.outputs.did_work == 'true'
    uses: actions/upload-artifact@v7
    with:
      name: ${{ github.run_id }}
      path: /tmp/gh-aw/skipped_files.txt
      if-no-files-found: error
      retention-days: 7

  - name: Trigger Agent 2b (PR Creator)
    if: success() && steps.noop-check.outputs.did_work == 'true'
    env:
      GH_TOKEN: ${{ secrets.CONTENTHAWK_GITHUB_PAT }}
      INPUT_JUDGE_RUN_ID: ${{ github.run_id }}
    run: |
      set -euo pipefail

      # Read the label written by the agent
      LABEL_NAME=""
      if [ -f /tmp/gh-aw/label_name.txt ]; then
        LABEL_NAME=$(cat /tmp/gh-aw/label_name.txt | tr -d '[:space:]')
      fi
      if [ -z "$LABEL_NAME" ]; then
        echo "::error::Agent did not write a label to /tmp/gh-aw/label_name.txt — cannot trigger Agent 2b."
        exit 1
      fi

      git fetch origin main --depth 1
      # Snapshot path convention (Agent 1): .github/ContentHawk/TODO/YYYY-MM-DD_Snapshot_<label>.md
      _matches=()
      while IFS= read -r _path; do
        case "$_path" in
          .github/ContentHawk/TODO/[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]_Snapshot_${LABEL_NAME}.md)
            _matches+=("$_path") ;;
        esac
      done < <(git ls-tree -r origin/main --name-only | grep '^\.github/ContentHawk/TODO/' || true)
      SNAPSHOT_PATH=$(printf '%s\n' "${_matches[@]:-}" | sort -r | head -1)
      if [ -z "$SNAPSHOT_PATH" ]; then
        echo "::error::No snapshot on main matching <date>_Snapshot_${LABEL_NAME}.md under .github/ContentHawk/TODO/"
        exit 1
      fi
      echo "Resolved snapshot: $SNAPSHOT_PATH"
      gh workflow run content-judge-pr.lock.yml \
        -f snapshot_path="$SNAPSHOT_PATH" \
        -f label_name="$LABEL_NAME" \
        -f judge_run_id="$INPUT_JUDGE_RUN_ID"
---

## Important context

This workflow picks up the first available snapshot from the TODO folder, judges each pending file against the intent, and opens issues for files that need fixing. It does **not** update the snapshot or create a PR.

Use the MCP script `list-snapshots` to find snapshot files in the TODO folder. Read and parse the first (oldest) snapshot file to get the intent, label, and pending files. For each pending file, read its content, judge it against the intent (using web search if needed), and create an issue if it needs action. Stop processing more files if the number of open issues with the snapshot's label meets or exceeds 30.

### Step 0 — Discover the first available snapshot

Use the MCP script `list-snapshots` to list all snapshot files in `.github/ContentHawk/TODO/`.

If the result is **empty** (no snapshot files found), **stop immediately** with a message:

> No snapshot files found in `.github/ContentHawk/TODO/`. Nothing to process. Exiting.

Do **not** create any issues. End the workflow here.

If files are found, **choose `snapshot_path`** — use the **first line** of the result (the oldest snapshot, i.e. the one that has been waiting longest). Read the full content of that file from `main`.

### Step 1 — Read and parse the snapshot

#### 1a. Parse the Agent Configuration table

Extract the following fields from the `## Agent Configuration` table:

* **Intent** — what to look for in each file
* **Issue Preferences** — how to write issues (templates, detail level, max per run, etc.)
* **Label** — the label slug stored in the snapshot

Call the extracted label value **`label_name`**. This is the label that will be used throughout the rest of the workflow to find issues, label created issues, and guard headroom.

**Important:** After extracting the label, write it to a file so post-steps can use it:

```
echo "<label_name>" > /tmp/gh-aw/label_name.txt
```

#### 1b. Parse the Files to Review table

Collect every row from the `## Files to Review` table where `CheckResult` is exactly `pending`. Preserve the exact row order from the table — this is the processing order. Call this list `pending_rows`.

If `pending_rows` is empty (all rows already have a non-pending CheckResult), **stop immediately** with a message:

> No pending rows found in snapshot. Nothing to do.

### Step 1c — Check for in-flight Judge PR

Before doing any work, check whether there are any open PRs for this label. Search for open pull requests that have the label `<label_name>` **and** contain the string `gh-aw-workflow-id: content-judge-pr` anywhere in the PR body.

Use the GitHub `search` toolset to find matching PRs:

* Search query: `is:pr is:open label:<label_name> "gh-aw-workflow-id: content-judge-pr"` in this repository.

If **any** matching PR is found, **stop immediately** with a message:

> In-flight Judge PR detected: #\<pr_number\> already exists for label '\<label_name\>'. Skipping this run to avoid duplicate work.

Do **not** create any issues. End the workflow here.

### Step 2 — Check open-issue headroom

Count the number of currently open issues that carry the label `<label_name>`:

list issues with the tool `list_issues` tool from the toolsset. with `state=open`
`labels=<label_name>` and count them.

Let this count be `open_count`. Let `max_open_issues` = 30.

If `open_count >= max_open_issues`, **stop immediately**. Output a message like:

> Issue limit reached: $open_count open issues already exist with label '<label_name>' (max: 30). Run again after issues are closed.

Do **not** create any issues.

### Step 3 — Process pending rows in order

**Before entering the loop**, write the work marker so post-steps know this was not a noop:

```
echo "true" > /tmp/gh-aw/work_done.txt
```

Work through `pending_rows` one at a time, **in order**. For each row:

#### 3a. Re-check headroom

Before processing this row, re-count open issues:

list issues with the tool `list_issues` tool from the toolsset. with `state=open`
`labels=<label_name>` and count them.

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

Create a GitHub issue using the `create-issue` safe-output tool. Add the label `<label_name>` to the issue.


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

After the loop completes, output a summary of the run. Include the total number of issues created, files skipped, and rows still pending (if the headroom limit was reached). Include the **`snapshot_path`** you resolved in Step 0 so logs tie back to the correct file. Skipped files are written to `/tmp/gh-aw/skipped_files.txt` and will be uploaded automatically by the artifact post-step.
