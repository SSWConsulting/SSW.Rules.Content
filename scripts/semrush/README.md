# SEMrush Duplicate Meta Description Fixer

Pulls duplicate meta description issues from a SEMrush Site Audit, maps the affected pages to files in this repo, generates unique replacement descriptions using the OpenAI API, writes the updated `seoDescription` frontmatter field back to each file, and automatically opens a GitHub pull request for review.

## Location

```
scripts/semrush/
├── semrush_client.py           # SEMrush Site Audit API adapter
├── map_urls_to_files.py        # URL → repo file mapper
├── generate_seo_description.py # AI description generator (OpenAI)
├── fix_duplicate_meta.py       # Frontmatter reader/writer
├── github_pr.py                # Branch, commit, push, PR creation + duplicate guard
├── run_duplicate_meta_fix.py   # Entry point (orchestrator)
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
# Dry run — logs what would change, no files written, no PR created
python scripts/semrush/run_duplicate_meta_fix.py --dry-run

# Test a small batch without creating a PR
python scripts/semrush/run_duplicate_meta_fix.py --dry-run --limit 5

# Full run: write files AND automatically create a GitHub PR
python scripts/semrush/run_duplicate_meta_fix.py

# Write files but skip the PR (for manual review before committing)
python scripts/semrush/run_duplicate_meta_fix.py --skip-pr
```

Set env vars inline on Windows PowerShell:

```powershell
$env:SEMRUSH_API_KEY="<key>"
$env:SEMRUSH_PROJECT_ID="<id>"
$env:OPENAI_API_KEY="<key>"
python scripts/semrush/run_duplicate_meta_fix.py --dry-run --limit 5
```

Or on bash/macOS/Linux:

```bash
export SEMRUSH_API_KEY=<key>
export SEMRUSH_PROJECT_ID=<id>
export OPENAI_API_KEY=<key>
python scripts/semrush/run_duplicate_meta_fix.py --dry-run --limit 5
```

## What it does

1. **Checks** for an already-open PR on `semrush/fix-duplicate-meta` — exits early if one exists.
2. **Fetches** the latest Site Audit snapshot from SEMrush and retrieves all pages flagged with duplicate meta descriptions (issue #15).
3. **Filters** to URLs matching `https://[www.]ssw.com.au/rules/{slug}` only.
4. **Maps** each URL to `public/uploads/rules/{slug}/rule.mdx` on disk.
5. **Reads** the current `title` and `seoDescription` from the file's frontmatter.
6. **Generates** a replacement description using the OpenAI API (`gpt-4o-mini`, Responses API), using the page title, current description, and a body excerpt as context. Enforces:
   * Under 160 characters
   * No filler phrases
   * Unique within the current batch
   * Automatic retry with the over-length draft if the first attempt is too long
7. **Writes** only the `seoDescription` frontmatter line. Everything else (title, body, other fields) is unchanged.
8. **Creates** a branch (`semrush/fix-duplicate-meta`), commits only the changed files, pushes, and opens a GitHub pull request for human review.

## PR automation

The full run (`python run_duplicate_meta_fix.py`) will:

* Create or reset the branch `semrush/fix-duplicate-meta` from `main`
* Stage and commit only the files that were actually updated
* Push to `origin`
* Open a PR titled `[SEMrush] Fix duplicate meta descriptions for /rules`

The PR body lists every changed file, explains how descriptions were generated, and includes a checklist for reviewers.

**Duplicate PR guard:** if an open PR already exists on `semrush/fix-duplicate-meta`, the script exits immediately without writing any files or creating a duplicate PR. Close or merge the existing PR first.

## What it does NOT do

* Does not change `title` or any other frontmatter field
* Does not modify page body content
* Does not commit or push to Git
* Does not create a PR (that step is manual or handled by a separate pipeline)
* Does not handle issue types other than `duplicate_meta_descriptions`

## After running

The PR is created automatically. Once it's open:

```bash
# Validate frontmatter on the changed files (copy paths from PR description)
cd scripts/frontmatter-validator && npm install
node frontmatter-validator.js '<comma-separated file paths>'
```

Review each description in the PR diff, edit anything that looks off directly on the branch, then merge.

## Known limitations and follow-up work

### Current limitations

* Only handles `seoDescription` field; does not detect or fix other SEO issues.
* Does not deduplicate against descriptions already present on *other* pages (only within the current batch).
* No retry logic on transient SEMrush/OpenAI API failures.
* Does not integrate with ContentHawk or the existing PR automation pipeline.
* Python only; no npm script alias (there is no root `package.json` in this content repo).
* `semrush/fix-duplicate-meta` is a single shared branch — running the script twice in a row without merging the first PR will be caught by the duplicate guard and exit cleanly.

### For GitHub Actions / recurring runs

To run this automatically on a schedule, you would need a workflow file that:

1. Provides secrets: `SEMRUSH_API_KEY`, `SEMRUSH_PROJECT_ID`, `OPENAI_API_KEY`
2. Uses a PAT (Personal Access Token) with `repo` and `pull_requests` scopes for the `gh` CLI — store it as `GH_TOKEN` or `CONTENTHAWK_GITHUB_PAT` (already used in this repo)
3. Runs: `pip install -r scripts/semrush/requirements.txt && python scripts/semrush/run_duplicate_meta_fix.py`

The duplicate PR guard means it is safe to run on a schedule — it will exit without creating a duplicate if the previous PR is still open.
