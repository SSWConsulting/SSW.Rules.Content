# SEMrush SEO Issue Fixer

Pulls duplicate SEO issues from a SEMrush Site Audit and fixes them using an AI agent (OpenAI tool use). The agent fetches flagged pages, reads each file, generates unique replacements, writes the updated frontmatter, and opens a GitHub pull request for review — all driven by the model's own reasoning rather than a fixed script.

## Location

```
scripts/semrush/
├── semrush_client.py   # SEMrush Site Audit API adapter
├── map_urls_to_files.py # URL → repo file mapper
├── fix_duplicate_meta.py # Frontmatter reader/writer
├── github_pr.py        # Branch, commit, push, PR creation + duplicate guard
├── run_agent.py        # Entry point: LLM-driven tool use (gpt-4o)
├── requirements.txt
└── README.md
```

## Required environment variables

| Variable | Description |
|---|---|
| `SEMRUSH_API_KEY` | Your SEMrush API key (found in SEMrush → Account → API keys) |
| `SEMRUSH_PROJECT_ID` | The SEMrush project ID for ssw.com.au (visible in the project URL) |
| `OPENAI_API_KEY` | OpenAI API key |

Optional:

| Variable | Description |
|---|---|
| `AGENT_MODEL` | OpenAI model to use (default: `gpt-4o`) |
| `REPO_ROOT` | Absolute path to the repo root. Defaults to two levels above this script (`../../`). |

## Setup

```bash
# 1. Install Python dependencies
cd scripts/semrush
pip install -r requirements.txt

# 2. Authenticate the GitHub CLI (required for PR creation)
gh auth login
```

The `gh` CLI must be installed and authenticated before running the full workflow.
Install it from <https://cli.github.com/>

## How to run

```bash
# Dry run — fix both issue types, no files written, no PR created
python scripts/semrush/run_agent.py --dry-run

# Test with a small batch
python scripts/semrush/run_agent.py --dry-run --limit 3

# Fix only one issue type
python scripts/semrush/run_agent.py --issue duplicate_meta
python scripts/semrush/run_agent.py --issue duplicate_title

# Full run: fix both issue types and open PRs
python scripts/semrush/run_agent.py
```

Override the model (default: `gpt-4o`):

```bash
AGENT_MODEL=gpt-4o-mini python scripts/semrush/run_agent.py --dry-run --limit 3
```

Set env vars inline on Windows PowerShell:

```powershell
$env:SEMRUSH_API_KEY="<key>"
$env:SEMRUSH_PROJECT_ID="<id>"
$env:OPENAI_API_KEY="<key>"
python scripts/semrush/run_agent.py --dry-run --limit 3
```

Or on bash/macOS/Linux:

```bash
export SEMRUSH_API_KEY=<key>
export SEMRUSH_PROJECT_ID=<id>
export OPENAI_API_KEY=<key>
python scripts/semrush/run_agent.py --dry-run --limit 3
```

## How it works

`run_agent.py` exposes four tools to the model and gives it a high-level goal. The model decides the order of calls, inspects results, and retries when a tool rejects a value.

**Tools:**

| Tool | What it does |
|---|---|
| `fetch_flagged_pages(issue_type)` | Calls SEMrush API, maps URLs to `rule.mdx` file paths |
| `read_rule_file(file_path)` | Returns title, seoDescription, and body excerpt |
| `write_frontmatter_field(file_path, field, value, old_value)` | Validates (length, uniqueness) and writes; returns an error the model must reason about |
| `open_pull_request(issue_type)` | Commits changed files and opens a GitHub PR with an old → new table |

**Agent workflow per issue type:**
1. Calls `fetch_flagged_pages` to get affected pages
2. For each page: calls `read_rule_file`, generates a replacement, calls `write_frontmatter_field`
3. If the tool rejects the value (too long, duplicate), the model reads the error and retries with a different value
4. After all pages are processed, calls `open_pull_request`

**Generation rules enforced via the system prompt:**
- `seoDescription`: under 160 characters, no filler openers, no trailing full stop, specific and concrete
- `title`: unique, descriptive, faithful to the page content
- Values already written in the session are rejected by the tool — the model must generate something different

## GitHub Actions workflow

The agent runs automatically via `.github/workflows/semrush-fix-duplicate-meta.yml`:

* **Schedule:** every Monday at 9:00 AM UTC
* **Manual trigger:** available from the Actions tab (`workflow_dispatch`)

Required secrets: `SEMRUSH_API_KEY`, `SEMRUSH_PROJECT_ID`, `OPENAI_API_KEY`. The workflow uses `GITHUB_TOKEN` for git push and PR creation — no PAT required.

The duplicate PR guard means it is safe to run on a schedule — if a previous PR is still open, the agent exits without writing files or creating a duplicate.

## PR format

Each issue type gets a separate PR with a markdown table:

| File | Old description / Old title | New description / New title |
|------|-----------------------------|-----------------------------|
| `` `rules/.../rule.mdx` `` | original value | AI-generated replacement |

## What the agent does NOT do

* Does not modify page body content — only the relevant frontmatter field is touched
* Does not change any frontmatter field other than the one being fixed
* Does not deduplicate against values already present on *other* pages (only within the current run)
* Does not retry on transient SEMrush/OpenAI API failures
* Does not handle SEMrush issue types other than duplicate meta descriptions and duplicate titles

## After running

The PR is created automatically. Once it's open:

```bash
# Validate frontmatter on the changed files (copy paths from PR description)
cd scripts/frontmatter-validator && npm install
node frontmatter-validator.js '<comma-separated file paths>'
```

Review each value in the PR diff, edit anything that looks off directly on the branch, then merge.
