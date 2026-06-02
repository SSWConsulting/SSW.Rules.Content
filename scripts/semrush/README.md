# SEMrush SEO Issue Fixer

Fixes duplicate `seoDescription` and `title` frontmatter on /rules pages flagged by SEMrush Site Audit, using a GitHub Copilot agent (gpt-5-mini) via the `gh-aw` framework. Runs on a weekly schedule and opens pull requests for human review.

## Location

```
scripts/semrush/
├── semrush_client.py    # SEMrush Site Audit API adapter + CLI
├── map_urls_to_files.py # URL → repo file mapper
├── frontmatter_utils.py # Frontmatter reader/writer + CLI
├── requirements.txt
└── README.md

.github/workflows/
├── semrush-fixer.md     # gh-aw agent workflow (source)
└── semrush-fixer.lock.yml  # compiled workflow (generated — do not edit)
```

## How it works

The agent workflow (`semrush-fixer.md`) is compiled by `gh aw compile` into a GitHub Actions workflow (`semrush-fixer.lock.yml`). When triggered, a GitHub Copilot agent:

1. Calls `list-semrush-issues` (MCP script) to see all current SEMrush issues and their scale
2. Decides which fixable issue types to tackle, in priority order by page count
3. For each issue type: fetches affected pages, reads each file, generates a unique replacement, writes it back
4. Commits the changes and opens a PR for review

The agent generates replacement text inline (no separate OpenAI API call). Generation and retries are handled by the model's own reasoning.

## Required secrets

| Secret | Description |
|---|---|
| `COPILOT_GITHUB_TOKEN` | GitHub Copilot token for the `gh-aw` engine |
| `SEMRUSH_API_KEY` | SEMrush API key |
| `SEMRUSH_PROJECT_ID` | SEMrush project ID for ssw.com.au |

Optional:

| Secret / Env var | Description |
|---|---|
| `SEMRUSH_SNAPSHOT_ID` | Pin a specific SEMrush snapshot ID, bypassing the `get_latest_snapshot_id()` lookup |

## Setup

### 1. Install the gh-aw CLI

```bash
gh extension install github/gh-aw
```

### 2. Compile the workflow

```bash
gh aw compile .github/workflows/semrush-fixer.md
```

This generates `.github/workflows/semrush-fixer.lock.yml`. Commit both files.

### 3. Set up secrets

In the repository settings, add: `COPILOT_GITHUB_TOKEN`, `SEMRUSH_API_KEY`, `SEMRUSH_PROJECT_ID`.

### 4. Install Python dependencies (for local testing only)

```bash
cd scripts/semrush
pip install -r requirements.txt
```

## How to run locally (testing Python helpers)

```bash
export SEMRUSH_API_KEY=<key>
export SEMRUSH_PROJECT_ID=<id>

# See all SEMrush issues with counts
python scripts/semrush/semrush_client.py list-issues

# Get pages flagged for duplicate meta descriptions
python scripts/semrush/semrush_client.py get-pages duplicate_meta

# Read frontmatter from a file
python scripts/semrush/frontmatter_utils.py read public/uploads/rules/some-rule/rule.mdx

# Write a new seoDescription
python scripts/semrush/frontmatter_utils.py write public/uploads/rules/some-rule/rule.mdx seoDescription "New description here"
```

## Generation rules (enforced via agent system prompt)

- `seoDescription`: strictly under 160 characters, no filler openers, no trailing full stop, specific and concrete
- `title`: must start with `Do you` and end with `?`, unique, descriptive, faithful to the page content
- Values are never reused within the same run

## What the agent does NOT do

- Does not modify page body content — only the target frontmatter field
- Does not change any frontmatter field other than the one being fixed
- Does not deduplicate against values on other pages (only within the current run)
- Does not handle SEMrush issue types other than duplicate meta descriptions and duplicate titles
