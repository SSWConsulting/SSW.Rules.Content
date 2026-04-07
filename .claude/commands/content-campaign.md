---
description: "Collect inputs and trigger the ContentHawk Content Campaign GitHub Actions workflow."
allowed-tools: Bash
---

# ContentHawk — Trigger Content Campaign Workflow

Your job is to collect the required inputs from the user and then trigger the `content-campaign.md` GitHub Actions workflow via `gh workflow run`.

> **IMPORTANT — Do not stop early.** Collect all inputs, then trigger the workflow in a single run. Do not stop after collecting inputs to wait for further confirmation unless you are missing required information.

## Collect inputs

Ask the user for the following inputs (all required). Present them as a numbered list and wait for answers before proceeding:

1. **Search Scope** — Which content files to scan and how to filter them (e.g. ".NET rules under the windows forms category that are not archived", "all rules in the accessibility category").
2. **Processing Priority** — How to sort the file list (e.g. "sort by created date ascending, then by lastUpdated descending").
3. **Intent** — What downstream agents should look for and act on (e.g. "archive all legacy rules and populate archive reason").
4. **Issue Preferences** — How Agent 2 should create issues (e.g. "max 20 issues per run").
5. **PR Preferences** — How Agent 3 should create PRs (e.g. "bundle up to 5 related issues per PR").
6. **Label Name** — A GitHub label slug to tie the pipeline together (e.g. "archive-legacy-rules"). Must be kebab-case.

If the user provides all inputs in their initial message (e.g. as a description of what they want), extract them. For any missing inputs, ask before proceeding.

## Trigger the workflow

Once you have all six inputs, trigger the workflow:

```bash
gh workflow run content-campaign.md \
  -f search_scope='<search_scope>' \
  -f processing_priority='<processing_priority>' \
  -f intent='<intent>' \
  -f issue_preferences='<issue_preferences>' \
  -f pr_preferences='<pr_preferences>' \
  -f label_name='<label_name>'
```

Replace each `<placeholder>` with the user's actual input. Make sure to properly escape any single quotes in the values.

## Watch the workflow run

After triggering, immediately get the run ID and watch it:

```bash
# Wait a few seconds for the run to register, then get the latest run ID
sleep 5
RUN_ID=$(gh run list --workflow=content-campaign.md --limit=1 --json databaseId --jq '.[0].databaseId')
gh run watch "$RUN_ID"
```

This will stream live status updates until the workflow completes or fails.

## After the workflow completes

1. If the workflow **succeeded**, find the PR it created and show the user the link:

   ```bash
   gh pr list --label '<label_name>' --json url --jq '.[0].url'
   ```

2. If the workflow **failed**, show the user the failure logs:

   ```bash
   gh run view "$RUN_ID" --log-failed
   ```

3. Remind them that once the PR is merged or ready, **Agent 2 (content-check)** can be run to process the snapshot.
