# Content style check

Flags common style issues in rule PRs and posts them as a PR comment. It never blocks a PR.

Each warning links to the SSW Rule it comes from. Warnings in lines changed by the PR are listed first, then existing warnings in the same file.

## What it skips

Rules often show bad examples on purpose, so these are never checked:

* Fenced code blocks and inline code
* Greyboxes (`style="greybox"`), bad examples (`figurePrefix="bad"`) and `<emailEmbed>` bodies
* Words in quotes or italics, e.g. `use "email" not *e-mail*` (a mention, not a use)

Captions (`figure="..."`) are always checked.

## Run it locally

```bash
cd scripts/check-content
npm install
node check-content.js ../../public/uploads/rules/some-rule/rule.mdx
npm test
```

Add `--base origin/main` to split warnings into "changed by this branch" and "existing".

## Add a new check

**A word or phrase to avoid** (e.g. "web site" → "website"): add one line to `PITFALLS` in `check-content.js`.

```js
[/\bweb sites?\b/gi, '"website" not "web site"'],
```

**Any other check:**

1. Add an entry to `CHECKS` with a label and the folder name of the SSW Rule it enforces. The rule title in the warning is read from that rule's file
2. Push `[checkName, message]` from `checkLine()` (line-by-line checks) or add issues in `checkFile()` (checks that need the whole file, like headings)
3. Add an example to `test/fixture.mdx`: in the "Should warn" section, and in "Should NOT warn" if it must skip something
4. Update the expected counts in `test/check-content.test.js` and run `npm test`

Before adding a check, run it across all rules to see how noisy it is:

```bash
node check-content.js $(ls ../../public/uploads/rules/*/rule.mdx | paste -sd, -) | grep -c "::warning"
```
