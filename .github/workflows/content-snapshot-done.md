---
description: >
  Agent 4 (Snapshot Done) of the ContentHawk pipeline.
  Triggered when a ContentHawk judge issue is closed or when a snapshot file
  is pushed to TODO/. Parses the Files to Review table and checks whether
  all rows are non-pending and all referenced issues are closed (or all rows
  are skipped). If the snapshot is fully complete, moves it from TODO/ to
  DONE/ via the commit-files safe-output.

on:
  issues:
    types: [closed]
  push:
    branches: [main]
    paths:
      - .github/ContentHawk/TODO/*.md
name: Content Snapshot Cleanup (Agent 3b)

engine:
  id: copilot
  model: gpt-5-mini

permissions: read-all

concurrency:
  group: "contenthawk-snapshot-done"
  cancel-in-progress: false

safe-outputs:
  report-failure-as-issue: false
  create-pull-request:
    max: 1
    title-prefix: "[Content Snapshot Done] "
    protected-files: allowed
    allowed-files:
      - .github/ContentHawk/TODO/*.md
      - .github/ContentHawk/DONE/*.md

steps:
  - name: Guard — only ContentHawk judge issues
    if: github.event_name == 'issues'
    env:
      BODY: ${{ github.event.issue.body }}
    run: |
      if echo "$BODY" | grep -qF "gh-aw-workflow-id: content-judge"; then
        echo "ContentHawk judge issue detected. Proceeding."
      else
        echo "Not a ContentHawk judge issue. Exiting."
        exit 1
      fi

tools:
  github:
    lockdown: false
    toolsets: [issues, search, labels, pull_requests]
    github-token: "${{ secrets.CONTENTHAWK_GITHUB_PAT }}"

post-steps:
  - name: Workflow Summary
    env:
      ISSUE_NUMBER: ${{ github.event.issue.number || '' }}
      EVENT_NAME: ${{ github.event_name }}
    if: always()
    run: |
      echo "## ContentHawk — Agent 4 (Snapshot Done)" >> "$GITHUB_STEP_SUMMARY"
      echo "" >> "$GITHUB_STEP_SUMMARY"

      echo "### Trigger" >> "$GITHUB_STEP_SUMMARY"
      echo "" >> "$GITHUB_STEP_SUMMARY"
      echo "| Field   | Value |" >> "$GITHUB_STEP_SUMMARY"
      echo "|---------|-------|" >> "$GITHUB_STEP_SUMMARY"
      if [ "$EVENT_NAME" = "issues" ]; then
        echo "| Event   | Issue #${ISSUE_NUMBER} closed |" >> "$GITHUB_STEP_SUMMARY"
      else
        echo "| Event   | Push to TODO/ |" >> "$GITHUB_STEP_SUMMARY"
      fi
      echo "" >> "$GITHUB_STEP_SUMMARY"
---

## Important context

This workflow is **Agent 4 (Snapshot Done)** in the ContentHawk pipeline. It runs when a ContentHawk judge issue is closed **or** when a snapshot file is pushed to `TODO/`. It determines whether the associated snapshot is fully complete.

A snapshot is complete when:
1. **No rows** in the Files to Review table have `CheckResult = pending`, **AND**
2. **Either** all rows are `skipped` (no issues exist), **or** every issue referenced in the table (rows with `CheckResult = Issue #<number>`) is closed

If both conditions are met, the agent uses the `commit-files` safe-output to move the snapshot from `TODO/` to `DONE/`.

---

### Step 0 — Determine the snapshot

{{#if github.event.issue.number}}
#### Trigger: Issue closed

The closed issue is #${{ github.event.issue.number }}.

Read the issue's labels. Extract the **label names** — these will be used to match against snapshot filenames.

If the issue has no labels, **stop immediately** with a message:

> Closed issue #${{ github.event.issue.number }} has no labels. Cannot match to a snapshot. Exiting.

Proceed to **Step 1**.
{{/if}}

{{#if github.event.head_commit.id}}
#### Trigger: Push to TODO/

Look at the commits in this push. Identify files matching `.github/ContentHawk/TODO/*_Snapshot_*.md` that were added or modified.

If no matching snapshot files were found, **stop immediately** with a message:

> Push did not include any snapshot files in TODO/. Nothing to do. Exiting.

Before proceeding, verify each snapshot file still exists in `TODO/`. If it has been deleted or moved, skip it — it was likely already processed.

For each remaining snapshot file, extract the **label** from the filename convention `YYYY-MM-DD_Snapshot_<label>.md` — parse `<label>` (everything between `_Snapshot_` and `.md`).

Set **`snapshot_path`** to the full path of the file. **Skip Step 1** and proceed directly to **Step 2**.
{{/if}}

### Step 1 — Find the matching snapshot (issue trigger only)

List the files in `.github/ContentHawk/TODO/`. Look for snapshot files matching the pattern `*_Snapshot_<label>.md` where `<label>` matches one of the labels from the closed issue.

If **no matching snapshot** is found, **stop immediately** with a message:

> No snapshot in TODO/ matches the labels on issue #${{ github.event.issue.number }}. Nothing to do.

If multiple snapshots match (e.g. different dates for the same label), use the **most recent** one (highest date prefix).

Read the full content of the matched snapshot file. Call its path **`snapshot_path`**.

### Step 2 — Parse the Files to Review table

Parse the `## Files to Review` table from the snapshot. For each row, extract the `CheckResult` column value.

Categorise the rows:

* **Pending rows** — `CheckResult` is exactly `pending`
* **Issue rows** — `CheckResult` matches `Issue #<number>` (extract the issue number)
* **Other rows** — any other value (e.g. `skipped`)

If there are **any pending rows**, **stop immediately** with a message:

> Snapshot `<snapshot_path>` still has <N> pending rows. Not ready to move to DONE.

If there are **no issue rows and no pending rows** (all rows are `skipped`), the snapshot is already complete — **skip Step 3** and go directly to **Step 4**.

If there are **issue rows**, proceed to **Step 3** to verify they are all closed.

### Step 3 — Check all referenced issues are closed

For each issue number extracted from the table, use the GitHub tools to check the issue state.

If **any** referenced issue is still open, **stop immediately** with a message:

> Snapshot `<snapshot_path>` is not complete — issue #<number> is still open (<M> of <total> issues closed so far).

### Step 4 — Move snapshot to DONE

The snapshot is complete. Use the `create-pull-request` safe-output to create a PR that moves the snapshot from `<snapshot_path>` to `.github/ContentHawk/DONE/<basename>` with the commit message:

```
content-hawk: move completed snapshot to DONE
```

Output a summary:

> Snapshot `<snapshot_path>` is complete. All rows are resolved (skipped or issues closed). Moved to DONE/.
