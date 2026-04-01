---
description: >
  Agent 1 (Detective) of the ContentHawk pipeline.
  Scans content files based on user-provided search scope, extracts category
  and date metadata from each file, sorts them by the user's processing
  priority, and commits a markdown snapshot tracking file to a new branch,
  then opens a pull request.
  The snapshot is a markdown table listing every file with its metadata so
  Agent 2 can iterate over rows to find issues and Agent 3 can raise PRs
  grouped by the intent label.
  Also creates a custom GitHub label derived from the user's intent for
  Agent 2 to inject into issues and Agent 3 to bundle PRs.
  Stops immediately if an open catalog-tracking PR already exists for this
  intent to avoid duplicates.
name: Content Campaign (Agent 1)

on:
  workflow_dispatch:
    inputs:
      search_scope:
        description: "Which content files to scan and how to filter them (e.g. '.NET rules under content/rules that are not archived', 'all public pages in content folder')."
        required: true
      processing_priority:
        description: "How to sort the file list for processing order (e.g. 'first sort by created date ascending, then by lastUpdated descending')."
        required: true
      intent:
        description: "What Agent 2 should look for and act on (e.g. 'archive all legacy rules and populate archive reason including modern rule reference')."
        required: true
      issue_preferences:
        description: "Preferences for how Agent 2 creates issues (e.g. 'use template .github/ISSUE_TEMPLATE/content-review.md, max 20 issues per run')."
        required: true
      pr_preferences:
        description: "Preferences for how Agent 3 creates PRs (e.g. 'use template .github/PULL_REQUEST_TEMPLATE/content-fix.md, bundle up to 5 related issues per PR')."
        required: true
      label_name:
        description: "GitHub label slug to tie the pipeline together (e.g. 'archive-legacy-rules'). Agent 2 applies it to issues, Agent 3 queries by it."
        required: true

engine:
  id: copilot
  model: gpt-5-mini

mcp-servers:
  tavily:
    command: npx
    args: ["-y", "tavily-mcp"]
    env:
      TAVILY_API_KEY: "${{ secrets.TAVILY_API_KEY }}"
    allowed: ["tavily_search" ]

permissions: read-all

network:
  allowed:
    - defaults
    - "*.tavily.com"

safe-outputs:
  report-failure-as-issue: false
  create-pull-request:
    protected-files: allowed
    allowed-files:
      - .github/ContentHawk/TODO/*.md
    title-prefix: "[Content Catalog] "
    max: 1
  add-labels:
    target: "*"
    max: 1

steps:
  - name: Guard — label must not already exist
    uses: actions/github-script@v7
    with:
      script: |
        try {
          await github.rest.issues.getLabel({
            owner: context.repo.owner,
            repo: context.repo.repo,
            name: '${{ inputs.label_name }}'
          });
          core.setFailed(
            `Label '${{ inputs.label_name }}' already exists in this repository. ` +
            `Choose a different label_name or delete the existing label first.`
          );
        } catch (error) {
          if (error.status === 404) {
            core.info(`Label '${{ inputs.label_name }}' does not exist yet. Proceeding.`);
          } else {
            core.setFailed(`Failed to check label: ${error.message}`);
          }
        }
tools:
  github:
    toolsets: [default]
    github-token: "${{ secrets.CONTENTHAWK_GITHUB_PAT }}"
  tavily:
    tools: [search, search_news]

post-steps:
  - name: Workflow Summary
    if: always()
    env:
      INPUT_SEARCH_SCOPE: ${{ inputs.search_scope }}
      INPUT_PROCESSING_PRIORITY: ${{ inputs.processing_priority }}
      INPUT_INTENT: ${{ inputs.intent }}
      INPUT_LABEL_NAME: ${{ inputs.label_name }}
    run: |
      echo "## ContentHawk — Agent 1 (Detective)" >> "$GITHUB_STEP_SUMMARY"
      echo "" >> "$GITHUB_STEP_SUMMARY"

      # Show the inputs that were provided
      echo "### Inputs" >> "$GITHUB_STEP_SUMMARY"
      echo "" >> "$GITHUB_STEP_SUMMARY"
      echo "| Field               | Value |" >> "$GITHUB_STEP_SUMMARY"
      echo "|---------------------|-------|" >> "$GITHUB_STEP_SUMMARY"
      echo "| Search Scope        | $INPUT_SEARCH_SCOPE |" >> "$GITHUB_STEP_SUMMARY"
      echo "| Processing Priority | $INPUT_PROCESSING_PRIORITY |" >> "$GITHUB_STEP_SUMMARY"
      echo "| Intent              | $INPUT_INTENT |" >> "$GITHUB_STEP_SUMMARY"
      echo "| Label               | \`$INPUT_LABEL_NAME\` |" >> "$GITHUB_STEP_SUMMARY"
      echo "" >> "$GITHUB_STEP_SUMMARY"

      # List any files the agent created or modified
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

This workflow is **Agent 1 (Detective)** in a three-agent pipeline called **ContentHawk**:

- **Agent 1 (this workflow)**: Catalogs content files and creates a snapshot tracking file. Creates a label for the intent.
- **Agent 2**: Reads the snapshot, checks each file against the intent, and opens GitHub issues for files that match. Uses the label and issue preferences captured here.
- **Agent 3**: Reads issues with the intent label and raises PRs to resolve them. Uses the PR preferences captured here.

The snapshot file you create must contain **all the information** Agent 2 and Agent 3 need — every user prompt is persisted into the snapshot so downstream agents are self-contained.

## Inputs provided by the user

All six prompts are captured and must be written into the snapshot file:

| Prompt              | Value                                | Used by        |
|---------------------|--------------------------------------|----------------|
| Search Scope        | `${{ inputs.search_scope }}`         | Agent 1        |
| Processing Priority | `${{ inputs.processing_priority }}`  | Agent 1        |
| Intent              | `${{ inputs.intent }}`               | Agents 1, 2, 3 |
| Issue Preferences   | `${{ inputs.issue_preferences }}`    | Agent 2        |
| PR Preferences      | `${{ inputs.pr_preferences }}`       | Agent 3        |
| Label Name          | `${{ inputs.label_name }}`           | Agents 1, 2, 3 |

---


### Step 1 — Create the intent label

Create a GitHub label named exactly `${{ inputs.label_name }}` with a distinguishing color and the intent as its description. Use the `--force` flag so re-runs update rather than fail:

```bash
gh label create "${{ inputs.label_name }}" --color "D93F0B" --description "${{ inputs.intent }}" --force
```

### Step 2 — Discover, filter, and sort content files

The user's search scope is:

```
${{ inputs.search_scope }}
```

Follow this procedure exactly:

#### 2a. List candidate files

Parse the search scope to identify the **directory/file-type scope** (which directories and extensions to scan). List every file that matches.

#### 2b. Read and filter each candidate — MANDATORY

The search scope may also contain **content-level criteria** (conditions about a file's contents, front-matter values, or metadata — e.g. "files that contain lorem ipsum", "non-archived files", "files tagged with X").

For **every** candidate file from 2a you **must**:

1. Read the file's full content.
2. Evaluate it against **every** content-level criterion in the search scope.
3. If the file **fails any criterion**, **exclude it** — do NOT add it to the snapshot.

**Do NOT skip this step.** A file that lives in the right directory but fails a content-level criterion must be excluded. If the search scope says "files that contain lorem ipsum", every file without the text "lorem ipsum" must be dropped. If it says "non-archived", every file with an archived flag must be dropped. When in doubt, exclude.

**Verification**: Before adding any file to `passed_files`, also confirm it is relevant to the user's intent:

```
${{ inputs.intent }}
```

If a file passes the search scope criteria but is clearly unrelated to the intent, exclude it.

**Using Web Search for Relevance Validation**: During verification, if you need to confirm whether content is relevant to the intent (e.g., checking if a technology mentioned in the file is deprecated, outdated, or has been replaced), use the Tavily search tool. For example:
- If the intent involves archiving legacy documentation, search for the technology/framework to check deprecation status
- If the intent involves updating outdated content, search for the topic to verify current recommendations
- Formulate queries like "[technology] deprecated", "[technology] end of life", or "[topic] current best practices"

Search results should inform your decision about whether the file is relevant to the user's intent. If search results indicate the content is obsolete or unrelated to current recommendations, exclude the file.

Build a `passed_files` list containing only files that satisfy **all** criteria. Files that fail go into an internal `excluded_files` list (you do not need to write this list anywhere, but you must track it to ensure they are not in the snapshot).

#### 2c. Extract metadata from passed files

For each file in `passed_files`:

1. **CategoryList** — look for any categorisation mechanism (front-matter tags, categories, labels, folder structure). If found, extract as a comma-separated string. Otherwise use `uncategorized`.
2. **Created** — a date field representing original creation/publication (e.g. `date`, `created`, `publishedAt`). Format `YYYY-MM-DD`. If absent, use `-`.
3. **LastUpdated** — a date field representing last modification (e.g. `lastUpdated`, `updatedAt`, `modified`, `lastChecked`). If absent, use `-`.

#### 2d. Sort

Sort `passed_files` according to the user's processing priority:

```
${{ inputs.processing_priority }}
```

Interpret this as a sort specification. For example, "first sort by created then lastUpdated" means sort primarily by Created date, then break ties with LastUpdated date. Apply ascending order unless the user explicitly says descending. Rows with `-` dates sort last.

**The snapshot table must contain ONLY the files in `passed_files` after this step. No other files.**

### Step 3 — Write the snapshot tracking file

Determine today's date in `YYYY-MM-DD` format. Create the file:

```
.github/ContentHawk/TODO/<todays-date>_Snapshot_${{ inputs.label_name }}.md
```

For example: `.github/ContentHawk/TODO/2026-03-05_Snapshot_archive-legacy-rules.md`

The file must follow this **exact** structure:

```markdown
# Content Campaign

## Agent Configuration

| Field               | Value                                           |
|---------------------|-------------------------------------------------|
| Intent              | ${{ inputs.intent }}                            |
| Search Scope        | ${{ inputs.search_scope }}                      |
| Processing Priority | ${{ inputs.processing_priority }}               |
| Issue Preferences   | ${{ inputs.issue_preferences }}                 |
| PR Preferences      | ${{ inputs.pr_preferences }}                    |
| Label               | `${{ inputs.label_name }}`                      |
| Created             | <today's date in YYYY-MM-DD>                    |

## Files to Review

| Path        | CategoryList   | Created    | LastUpdated   | CheckedDate | CheckResult |
|-------------|----------------|------------|---------------|-------------|-------------|
| <file-path> | <CategoryList> | <Created>  | <LastUpdated> | -           | pending     |
```

Rules for the table:

- One row per non-skipped file from Step 2.
- Rows are in the sort order determined by the processing priority (NOT alphabetical unless that is what the user requested).
- `CheckedDate` is always `-` (Agent 2 fills this in later).
- `CheckResult` is always `pending` (Agent 2 updates this later).

### Step 4 — Open the pull request

Create a pull request with the title `[Content Catalog] {description}` where {description} is a very brief description of the intent from a branch named `ContentHawk/TODO/${{ inputs.label_name }}` into `main`.

Use this PR body:

```markdown
## Intent

${{ inputs.intent }}

## Search Scope

${{ inputs.search_scope }}

## Processing Priority

${{ inputs.processing_priority }}

## Label for flagged issues

`${{ inputs.label_name }}`

## Issue Preferences (for Agent 2)

${{ inputs.issue_preferences }}

## PR Preferences (for Agent 3)

${{ inputs.pr_preferences }}

## Snapshot file

The full file list with metadata is in `.github/ContentHawk/TODO/<todays-date>_Snapshot_${{ inputs.label_name }}.md` on this branch.

- **Agent 2** will iterate over the table rows in order, check each file against the intent, update `CheckedDate` and `CheckResult`, and open issues with the `${{ inputs.label_name }}` label.
- **Agent 3** will read issues labelled `${{ inputs.label_name }}` and raise PRs to resolve them.
```

After the PR is created, **add the label** `${{ inputs.label_name }}` to the PR. This is the user's custom intent label (created in Step 1) and is separate from the `catalog-tracking` label that is applied automatically. Use the add-labels tool to apply it to the PR.
