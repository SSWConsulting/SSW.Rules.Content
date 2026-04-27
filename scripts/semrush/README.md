# SEMrush SEO Issue Fixers

Pulls duplicate SEO issues from a SEMrush Site Audit, maps the affected pages to files in this repo, generates unique replacements using the OpenAI API, writes the updated frontmatter back to each file, and automatically opens a GitHub pull request for review.

Two fixers are included — one for `seoDescription` and one for `title`.

## Location

```
scripts/semrush/
├── semrush_client.py           # SEMrush Site Audit API adapter
├── map_urls_to_files.py        # URL → repo file mapper
├── fix_duplicate_meta.py       # Frontmatter reader/writer
├── generate_seo_description.py # AI description generator (OpenAI)
├── generate_title.py           # AI title generator (OpenAI)
├── github_pr.py                # Branch, commit, push, PR creation + duplicate guard
├── run_duplicate_meta_fix.py   # Entry point: duplicate seoDescription fixer
├── run_duplicate_title_fix.py  # Entry point: duplicate title fixer
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

Both scripts share the same flags: `--dry-run`, `--skip-pr`, `--limit N`, `--urls-file PATH`, `--list-issues`.

### Duplicate meta descriptions

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

### Duplicate titles

```bash
python scripts/semrush/run_duplicate_title_fix.py --dry-run
python scripts/semrush/run_duplicate_title_fix.py --dry-run --limit 5
python scripts/semrush/run_duplicate_title_fix.py
python scripts/semrush/run_duplicate_title_fix.py --skip-pr
```

## What each fixer does

### Duplicate meta description fixer (`run_duplicate_meta_fix.py`)

1. **Checks** for an already-open PR on `semrush/fix-duplicate-meta` — exits early if one exists.
2. **Fetches** the latest Site Audit snapshot from SEMrush and retrieves all pages flagged with duplicate meta descriptions (issue #15).
3. **Filters** to URLs matching `https://[www.]ssw.com.au/rules/{slug}` only.
4. **Maps** each URL to `public/uploads/rules/{slug}/rule.mdx` on disk.
5. **Reads** the current `title` and `seoDescription` from the file's frontmatter.
6. **Generates** a replacement description using the OpenAI API (`gpt-4o-mini`), using the page title, current description, and a body excerpt as context. Enforces:
   * Under 160 characters
   * No filler phrases
   * Unique within the current batch
   * Automatic retry with the over-length draft if the first attempt is too long
7. **Writes** only the `seoDescription` frontmatter line. Everything else (title, body, other fields) is unchanged.
8. **Creates** a branch (`semrush/fix-duplicate-meta`), commits only the changed files, pushes, and opens a GitHub PR with an old → new description table for human review.

### Duplicate title fixer (`run_duplicate_title_fix.py`)

1. **Checks** for an already-open PR on `semrush/fix-duplicate-titles` — exits early if one exists.
2. **Fetches** pages flagged with duplicate title tags (issue #13) from SEMrush.
3. **Filters and maps** URLs to `rule.mdx` files, same as above.
4. **Groups** files that share the same `title` value.
5. **Generates** distinct replacement titles for each group using the OpenAI API, ensuring no two pages in the batch share a title.
6. **Writes** only the `title` frontmatter line. Everything else is unchanged.
7. **Creates** a branch (`semrush/fix-duplicate-titles`), commits, pushes, and opens a GitHub PR with an old → new title table for human review.

## GitHub Actions workflow

Both fixers run automatically via `.github/workflows/semrush-fix-duplicate-meta.yml` as two parallel jobs:

* **Schedule:** every Monday at 9:00 AM UTC
* **Manual trigger:** available from the Actions tab (`workflow_dispatch`)

Required secrets: `SEMRUSH_API_KEY`, `SEMRUSH_PROJECT_ID`, `OPENAI_API_KEY`. The workflow uses `GITHUB_TOKEN` for git push and PR creation — no PAT required.

The duplicate PR guard on each script means it is safe to run on a schedule — if the previous PR is still open, the script exits without writing any files or creating a duplicate.

## What the fixers do NOT do

* Do not modify page body content — only the relevant frontmatter field is touched
* Do not change any frontmatter field other than the one being fixed
* Do not deduplicate against values already present on *other* pages (only within the current batch)
* Do not retry on transient SEMrush/OpenAI API failures
* Do not handle SEMrush issue types other than duplicate meta descriptions and duplicate titles