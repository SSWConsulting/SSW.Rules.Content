# SSW.Rules.Content agent guide

## Repository

This is a content-only repository. Rules and categories are MDX consumed by the separate [SSW.Rules engine](https://github.com/SSWConsulting/SSW.Rules); there is no root build or test command.

* Rules: `public/uploads/rules/[uri]/rule.mdx`
* Images: beside the rule that uses them
* Top categories: `categories/[top-category]/index.mdx`
* Categories: `categories/[top-category]/[category].mdx`
* Validation utilities: `scripts/`

Use the current schemas and scripts as the source of truth. Before introducing unfamiliar MDX, inspect a recent working rule that uses the same component.

## Writing rules

* The rule folder name must exactly match its `uri`.
* Titles are questions. Start content headings at `##`; the page title supplies the only H1.
* Start with the pain or context, then add exactly one `<endIntro />` before the main content.
* Use present tense, active voice, and an objective, company-agnostic perspective.
* Explain why the practice matters. Link to product documentation for implementation details that will become stale.
* Prefer concrete good/bad examples when they materially clarify the advice. Every image or example box needs a descriptive `figure`.
* Use asterisks for unordered lists and specify a language on fenced code blocks.
* Link to another rule as `[descriptive title](/[uri])`.
* SSW URLs must use `https://www.ssw.com.au/...`; the URL linter flags the bare domain.
* Put images in the rule folder, use descriptive kebab-case names and lowercase extensions, and embed them with `<imageEmbed>` rather than Markdown image syntax.

Categories contain descriptive body content only and do not use `<endIntro />`.

## Rule frontmatter

For a new rule, copy [the rule template](template/rule.mdx) and replace every placeholder. The frontmatter validator requires non-empty `title`, `guid`, `uri`, `seoDescription`, and `authors`; new rules also follow the repository convention shown here:

```yaml
---
type: rule
title: Do you use a question for every rule title?
seoDescription: Explain the rule in a concise, search-friendly sentence.
guid: 00000000-0000-0000-0000-000000000000
uri: use-question-rule-titles
created: 2026-01-01T00:00:00.000Z
authors:
  - title: Person Name
    url: https://www.ssw.com.au/people/person-name
related: []
categories:
  - category: categories/communication/rules-to-better-technical-documentation.mdx
archivedreason: null
isArchived: false
---
```

* Generate a real UUID and use a real ISO 8601 creation timestamp.
* `related` entries, when present, are objects containing the full repository path:

  ```yaml
  related:
    - rule: public/uploads/rules/related-rule/rule.mdx
  ```

* `categories` entries contain full `categories/.../*.mdx` paths.
* Omit optional fields that have no value. Do not invent or manually change `createdBy*` or `lastUpdated*` fields.

## MDX components

Before adding or modifying custom MDX, read [the SSW Rules custom MDX reference](template/custom-mdx.md). Copy the structure of a recent working example and preserve the exact prop names.

* `<boxEmbed>`: `style`, rich-text `body`, `figurePrefix`, and `figure`. Supported styles are `greybox`, `info`, `warning`, `tips`, `highlight`, `china`, `codeauditor`, `yakshaver`, and `todo`.
* `<imageEmbed>`: `src`, descriptive `alt`, `size` (`small`, `medium`, or `large`), `showBorder`, `figurePrefix`, and `figure`.
* `<emailEmbed>`: `from`, `to`, optional `cc`/`bcc`, `subject`, `shouldDisplayBody`, rich-text `body`, `figurePrefix`, and `figure`.
* `<youtubeEmbed>`: `url` accepts a YouTube URL or video ID; `description` should contain the video title and duration.
* Figure prefixes are `bad`, `ok`, `good`, and `none`.

Wrap rich component content in `body={<> ... </>}`. Avoid raw `{...}` in prose because MDX treats it as an expression.

## Archiving

When archiving a rule:

* Set `isArchived: true`.
* Add a concise `archivedreason`.
* If the guidance moved or is covered elsewhere, link to the active rule using a Markdown link whose target is `/rules/[uri]`.
* Remove links from active rules back to the archived rule.

```yaml
isArchived: true
archivedreason: Merged into [Do you know how to decide what to test?](/rules/how-to-decide-what-to-test)
```

Archive reasons use `/rules/[uri]`, unlike links in rule bodies. Do not put an absolute `https://www.ssw.com.au/rules/...` URL inside an archive-reason Markdown link: one rule-list rendering path can linkify the absolute URL twice.

## Categories

For a new or recategorized rule:

1. Browse `categories/[top-category]/` and choose the most relevant category.
2. Add its full path to the rule's `categories` array.
3. Ensure the category's `index` contains `- rule: public/uploads/rules/[uri]/rule.mdx`.
4. Remove stale index entries when a rule leaves a category.

The category-sync validator can update the reciprocal category indexes.

## Validation

Validate only the files relevant to the change. Install script-local dependencies when their `node_modules` directory is absent.

Frontmatter (this command runs from the validator directory, so content paths need `../../`):

```bash
(cd scripts/frontmatter-validator && npm install --silent && node frontmatter-validator.js '../../public/uploads/rules/[uri]/rule.mdx,../../categories/[top-category]/[category].mdx')
```

MDX compilation and repository-specific fixes:

```bash
npm --prefix scripts/check-mdx install --silent
node scripts/check-mdx/check-mdx.js 'public/uploads/rules/[uri]/rule.mdx'
```

Markdown:

```bash
npx --yes markdownlint-cli 'public/uploads/rules/[uri]/rule.mdx' --config .markdownlint/config.json
```

For new, moved, or recategorized rules:

```bash
npm --prefix scripts/category-sync-validator install --silent
node scripts/category-sync-validator/category-sync-validator.js 'public/uploads/rules/[uri]/rule.mdx,categories/[top-category]/[category].mdx'
```

For changed rule files, also run:

```bash
node scripts/find-rules-missing-endintro/find-rules-missing-endintro.js 'public/uploads/rules/[uri]/rule.mdx'
```

Before handing off, ensure the relevant commands pass, reciprocal category references agree, internal links resolve, `git diff --check` passes, and unrelated worktree changes remain untouched.
