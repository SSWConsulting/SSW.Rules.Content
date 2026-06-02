---
description: >
  Agent 2b (PR Creator) of the ContentHawk pipeline.
  Triggered by Agent 2a after it finishes creating issues. Reads the snapshot
  file from main, searches for all issues created by Agent 2a in the given
  judge run, matches them to rows in the Files to Review table, and updates
  each matched row with the issue number and checked date.
  Commits the updated snapshot to a new branch and opens a pull request back
  to main.
  Stops immediately if a judge PR already exists for this label to avoid
  duplicates.
name: Content Judge PR (Agent 2b)
on:
  workflow_dispatch:
    inputs:
      snapshot_path:
        description: "Repo-relative path to the snapshot file on main (e.g. '.github/ContentHawk/TODO/2026-03-05_Snapshot_archive-legacy-rules.md')."
        required: true
      label_name:
        description: "GitHub label slug that ties this pipeline together (e.g. 'archive-legacy-rules'). Must match the Label field in the snapshot."
        required: true
      judge_run_id:
        description: "The workflow run ID of the Agent 2a (Judge) run that created the issues. Used to filter issues to this specific run."
        required: true
  workflow_run:
    workflows: ["Content Judge (Agent 2a)"]
    types: [completed]
    branches:
      - main

steps:
  - name: Resolve run context
    id: resolve-context
    env:
      GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      JUDGE_RUN_ID: ${{ github.event.workflow_run.id || inputs.judge_run_id }}
    run: |
      set -euo pipefail
      mkdir -p /tmp/gh-aw

      gh run download "$JUDGE_RUN_ID" -n "$JUDGE_RUN_ID" -D /tmp/gh-aw || {
        echo "No artifact for run $JUDGE_RUN_ID — Agent 2a was a noop, skipping."
        exit 1
      }

      LABEL_NAME=$(cat /tmp/gh-aw/label_name.txt 2>/dev/null | tr -d '[:space:]')
      if [ -z "$LABEL_NAME" ]; then
        echo "::error::label_name.txt is empty in artifact — cannot proceed."
        exit 1
      fi

      SNAPSHOT_PATH=$(ls .github/ContentHawk/TODO/*_Snapshot_${LABEL_NAME}.md 2>/dev/null | sort -r | head -1)

      if [ -z "$SNAPSHOT_PATH" ]; then
        echo "::error::No snapshot found for label $LABEL_NAME"
        exit 1
      fi

      echo "label_name=$LABEL_NAME" >> "$GITHUB_OUTPUT"
      echo "judge_run_id=$JUDGE_RUN_ID" >> "$GITHUB_OUTPUT"
      echo "snapshot_path=$SNAPSHOT_PATH" >> "$GITHUB_OUTPUT"

      cat > /tmp/gh-aw/run_context.env << EOF
      export JUDGE_RUN_ID="$JUDGE_RUN_ID"
      export LABEL_NAME="$LABEL_NAME"
      export SNAPSHOT_PATH="$SNAPSHOT_PATH"
      EOF

      echo "Resolved: JUDGE_RUN_ID=$JUDGE_RUN_ID LABEL_NAME=$LABEL_NAME SNAPSHOT_PATH=$SNAPSHOT_PATH"

  - name: Guard — no open Content Judge PR for this label
    uses: ./.github/actions/guard-open-pr
    with:
      label_name: ${{ steps.resolve-context.outputs.label_name }}
      workflow_id: content-judge-pr

engine:
  id: copilot
  model: gpt-5-mini

permissions: read-all

concurrency:
  group: "contenthawk-judge-pr-${{ inputs.label_name || github.event.workflow_run.id }}"
  cancel-in-progress: true

safe-outputs:
  report-failure-as-issue: false
  create-pull-request:
    title-prefix: "[Content Judge] "
    protected-files: allowed
    allowed-files:
      - .github/ContentHawk/TODO/*.md
      - .github/ContentHawk/DONE/*.md
    max: 1

tools:
  github:
    lockdown: false
    toolsets: [issues, repos, pull_requests, search, labels]
    github-token: "${{ secrets.GITHUB_TOKEN }}"

post-steps:
  - name: Workflow Summary
    if: always()
    env:
      RESOLVED_SNAPSHOT_PATH: ${{ steps.resolve-context.outputs.snapshot_path }}
      RESOLVED_LABEL_NAME: ${{ steps.resolve-context.outputs.label_name }}
      RESOLVED_JUDGE_RUN_ID: ${{ steps.resolve-context.outputs.judge_run_id }}
    run: |
      echo "## ContentHawk — Agent 2b (PR Creator)" >> "$GITHUB_STEP_SUMMARY"
      echo "" >> "$GITHUB_STEP_SUMMARY"

      echo "### Run Context" >> "$GITHUB_STEP_SUMMARY"
      echo "" >> "$GITHUB_STEP_SUMMARY"
      echo "| Field            | Value |" >> "$GITHUB_STEP_SUMMARY"
      echo "|------------------|-------|" >> "$GITHUB_STEP_SUMMARY"
      echo "| Trigger          | \`${{ github.event_name }}\` |" >> "$GITHUB_STEP_SUMMARY"
      echo "| Snapshot Path    | ${RESOLVED_SNAPSHOT_PATH:-<not resolved>} |" >> "$GITHUB_STEP_SUMMARY"
      echo "| Label            | \`${RESOLVED_LABEL_NAME:-<not resolved>}\` |" >> "$GITHUB_STEP_SUMMARY"
      echo "| Judge Run ID     | ${RESOLVED_JUDGE_RUN_ID:-<not resolved>} |" >> "$GITHUB_STEP_SUMMARY"
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

This workflow is **Agent 2b (PR Creator)** in a multi-agent pipeline called **ContentHawk**:

- **Agent 1 (Detective)**: Catalogs content files, creates a snapshot tracking file on a branch, and opens a PR. That PR is reviewed and merged into `main` before Agent 2a runs.
- **Agent 2a (Judge)**: Reads the merged snapshot, judges each pending file against the intent, and opens issues for files that need fixing. Completes successfully, which automatically triggers this workflow via `workflow_run`.
- **Agent 2b (this workflow)**: Reads the issues created by Agent 2a, matches them to the snapshot's Files to Review table, updates the snapshot with issue numbers and checked dates, and opens a PR.
- **Agent 3 (Fixer)**: Reads issues with the intent label and raises PRs to resolve them.

The snapshot file is **self-contained** — it stores every configuration value Agent 1 received.

---

### Step 0 — Load run context

Source the run context file written by the pre-step:

```bash
source /tmp/gh-aw/run_context.env
```

This provides three variables used throughout all steps below:
- `$SNAPSHOT_PATH` — repo-relative path to the snapshot file on `main`
- `$LABEL_NAME` — the label slug tying this pipeline run together
- `$JUDGE_RUN_ID` — the Agent 2a run ID whose issues this workflow will process

### Step 1 — Read and parse the snapshot

Read the full content of the file at `$SNAPSHOT_PATH` from the `main` branch.

#### 1a. Parse the Agent Configuration table

Extract the following fields from the `## Agent Configuration` table:

- **Intent** — what the judge was looking for in each file
- **Label** — the label slug stored in the snapshot

**Validation**: Assert that the `Label` value extracted from the snapshot matches `$LABEL_NAME` exactly (ignoring surrounding backticks). If they do not match, **stop immediately** with an error:

> Snapshot label '<snapshot_label>' does not match the resolved label '$LABEL_NAME'. Aborting.

#### 1b. Parse the Files to Review table

Collect every row from the `## Files to Review` table. Preserve the exact row order from the table. Separate them into:
- `pending_rows` — rows where `CheckResult` is exactly `pending`
- `other_rows` — rows that already have a non-pending `CheckResult`

If `pending_rows` is empty (all rows already have a non-pending CheckResult), **stop immediately** with a message:

> No pending rows found in snapshot. Nothing to do.

### Step 2 — Resolve issues from the judge run

Search GitHub for all issues created by Agent 2a during the judge run. Use the hidden `gh-aw-workflow-id` marker that the gh-aw runtime automatically embeds in the body of every issue created by Agent 2a:

```
repo:${{ github.repository }} is:issue is:open "contenthawk-run-id: $JUDGE_RUN_ID" in:body
```

For each issue returned:
1. Parse the `### File` section of the issue body to extract the file path.
2. Find the matching row in `pending_rows` where `Path` equals that extracted path.
3. Record the match: `{ path: <Path>, number: <issue number> }`.

Build a `matched_issues` list from all successful matches. If an issue cannot be matched to any `pending_rows` entry, log a warning but continue.

If no issues are found at all, log a message:

> No issues found for judge run $JUDGE_RUN_ID. The judge may have skipped all files.

Continue to Step 3 — the snapshot still needs to be committed even if no issues were created (rows remain `pending`).

### Step 3 — Update the snapshot


run the following command to get a list of files that were skipped by Agent 2a and stored in the artifact and store the result in a variable called `skipped_files`:

```

cat /tmp/gh-aw/skipped_files.txt || echo "No skipped files artifact found."

```

For each file in `skipped_files`, add the following to the matching row:

- For each matched row, update:
  - `CheckResult` → `skipped`
  - `CheckedDate` → `<today's date in YYYY-MM-DD>`

For each issue in `matched_issues`, add the following to the matching row:

- For each matched row, update:
  - `CheckResult` → `Issue #<number>`
  - `CheckedDate` → `<today's date in YYYY-MM-DD>`

All other columns (`Path`, `CategoryList`, `Created`, `LastUpdated`) must be preserved **verbatim**, character-for-character.

Rows in `pending_rows` that do **not** have a matching issue remain unchanged — keep `CheckResult = pending` and `CheckedDate = -` exactly as they were.

The `## Agent Configuration` table must be preserved entirely unchanged.

### Step 4 — Open a pull request with the updated snapshot

Create a new branch from `main` named:

```
ContentHawk/judge/$LABEL_NAME-${{ github.run_id }}
```

Commit the updated snapshot file from Step 3 to this branch. The commit message must be:

```
content-hawk[judge]: update snapshot for $LABEL_NAME
```

Then open a pull request using the `create-pull-request` safe-output tool:

**Title**: `$LABEL_NAME — <N> issues matched, <P> still pending`

> Note: the `title-prefix` safe-output setting will prepend `[Content Judge] ` automatically — so only pass `$LABEL_NAME — <N> issues matched, <P> still pending` as the title value.

**Base branch**: `main`

**Body**:

```markdown
## ContentHawk — Agent 2b (PR Creator) Results

### Summary

| Metric                | Count |
|-----------------------|-------|
| Issues matched        | <N>   |
| Rows still pending    | <P>   |
| Skipped files         | <S>   |

### Label

`$LABEL_NAME`

### Judge Run

[Agent 2a Run #$JUDGE_RUN_ID](${{ github.server_url }}/${{ github.repository }}/actions/runs/$JUDGE_RUN_ID)

### Snapshot file

`$SNAPSHOT_PATH`

### Issues matched

<Iterate over the `matched_issues` list. For each entry, write one bullet:
`- #<number> (<path>)`
If `matched_issues` is empty, write: _No issues were matched this run._>

### Next steps

- Merge this PR to update the snapshot on `main`.
- If rows are still pending, re-run Agent 2a after closing enough issues to drop below the limit.
- Once all rows are processed, Agent 3 can start resolving the open issues.

---
```

After the PR is created, apply the label `$LABEL_NAME` to the PR using the `add-labels` tool.
