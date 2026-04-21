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

steps: 
  - name: Guard — no open Content Judge PR for this label
    uses: ./.github/actions/guard-open-pr
    with:
      label_name: ${{ inputs.label_name }}
      workflow_id: content-judge-pr
  - name: Download skipped file list
    run: gh run download $JUDGE_RUN_ID -n $JUDGE_RUN_ID -D /tmp/gh-aw
    env:
      JUDGE_RUN_ID: ${{ inputs.judge_run_id }}
      GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}

engine:
  id: copilot
  model: gpt-5-mini

permissions: read-all

concurrency:
  group: "contenthawk-judge-pr-${{ inputs.label_name }}"
  cancel-in-progress: true

safe-outputs:
  report-failure-as-issue: false
  create-pull-request:
    title-prefix: "[Content Judge] "
    labels: ["${{ inputs.label_name }}"]
    protected-files: allowed
    allowed-files:
      - .github/ContentHawk/TODO/*.md
      - .github/ContentHawk/DONE/*.md
    max: 1

tools:
  github:
    lockdown: false
    toolsets: [issues, repos, pull_requests, search, labels]
    github-token: "${{ secrets.CONTENTHAWK_GITHUB_PAT }}"

post-steps:
  - name: Workflow Summary
    if: always()
    env:
      INPUT_SNAPSHOT_PATH: ${{ inputs.snapshot_path }}
      INPUT_LABEL_NAME: ${{ inputs.label_name }}
      INPUT_JUDGE_RUN_ID: ${{ inputs.judge_run_id }}
    run: |
      echo "## ContentHawk — Agent 2b (PR Creator)" >> "$GITHUB_STEP_SUMMARY"
      echo "" >> "$GITHUB_STEP_SUMMARY"

      echo "### Inputs" >> "$GITHUB_STEP_SUMMARY"
      echo "" >> "$GITHUB_STEP_SUMMARY"
      echo "| Field            | Value |" >> "$GITHUB_STEP_SUMMARY"
      echo "|------------------|-------|" >> "$GITHUB_STEP_SUMMARY"
      echo "| Snapshot Path    | $INPUT_SNAPSHOT_PATH |" >> "$GITHUB_STEP_SUMMARY"
      echo "| Label            | \`$INPUT_LABEL_NAME\` |" >> "$GITHUB_STEP_SUMMARY"
      echo "| Judge Run ID     | $INPUT_JUDGE_RUN_ID |" >> "$GITHUB_STEP_SUMMARY"
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
- **Agent 2a (Judge)**: Reads the merged snapshot, judges each pending file against the intent, and opens issues for files that need fixing. Triggers this workflow via a post-step when it completes.
- **Agent 2b (this workflow)**: Reads the issues created by Agent 2a, matches them to the snapshot's Files to Review table, updates the snapshot with issue numbers and checked dates, and opens a PR.
- **Agent 3 (Fixer)**: Reads issues with the intent label and raises PRs to resolve them.

The snapshot file is **self-contained** — it stores every configuration value Agent 1 received.

---

### Step 1 — Read and parse the snapshot

Read the full content of the file at `${{ inputs.snapshot_path }}` from the `main` branch.

#### 1a. Parse the Agent Configuration table

Extract the following fields from the `## Agent Configuration` table:

- **Intent** — what the judge was looking for in each file
- **Label** — the label slug stored in the snapshot

**Validation**: Assert that the `Label` value extracted from the snapshot matches `${{ inputs.label_name }}` exactly (ignoring surrounding backticks). If they do not match, **stop immediately** with an error:

> Snapshot label '<snapshot_label>' does not match the input label '${{ inputs.label_name }}'. Aborting.

#### 1b. Parse the Files to Review table

Collect every row from the `## Files to Review` table. Preserve the exact row order from the table. Separate them into:
- `pending_rows` — rows where `CheckResult` is exactly `pending`
- `other_rows` — rows that already have a non-pending `CheckResult`

If `pending_rows` is empty (all rows already have a non-pending CheckResult), **stop immediately** with a message:

> No pending rows found in snapshot. Nothing to do.

### Step 2 — Resolve issues from the judge run

Search GitHub for all issues created by Agent 2a during the judge run. Use the hidden `gh-aw-workflow-id` marker that the gh-aw runtime automatically embeds in the body of every issue created by Agent 2a:

```
repo:${{ github.repository }} is:issue is:open "contenthawk-run-id: ${{ inputs.judge_run_id }}" in:body
```

For each issue returned:
1. Parse the `### File` section of the issue body to extract the file path.
2. Find the matching row in `pending_rows` where `Path` equals that extracted path.
3. Record the match: `{ path: <Path>, number: <issue number> }`.

Build a `matched_issues` list from all successful matches. If an issue cannot be matched to any `pending_rows` entry, log a warning but continue.

If no issues are found at all, log a message:

> No issues found for judge run ${{ inputs.judge_run_id }}. The judge may have skipped all files.

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
ContentHawk/judge/${{ inputs.label_name }}${{ github.run_id }}
```

Commit the updated snapshot file from Step 3 to this branch. The commit message must be:

```
content-hawk[judge]: update snapshot for ${{ inputs.label_name }}
```

Then open a pull request using the `create-pull-request` safe-output tool:

**Title**: `[Content Judge] ${{ inputs.label_name }} — <N> issues matched, <P> still pending`

> Note: the `title-prefix` safe-output setting will prepend `[Content Judge] ` automatically — so only pass `${{ inputs.label_name }} — <N> issues matched, <P> still pending` as the title value.

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

`${{ inputs.label_name }}`

### Judge Run

[Agent 2a Run #${{ inputs.judge_run_id }}](${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ inputs.judge_run_id }})

### Snapshot file

`${{ inputs.snapshot_path }}`

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

After the PR is created, apply the label `${{ inputs.label_name }}` to the PR using the `add-labels` tool.
