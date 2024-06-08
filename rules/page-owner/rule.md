---
type: rule
title: Do you have a page owner for each webpage?
uri: page-owner
authors:
  - title: Seth Daily
    url: https://www.ssw.com.au/people/seth-daily
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
related:
  - using-markdown-to-store-your-content
  - do-you-know-the-best-practices-for-frontmatter-in-markdown
  - standard-set-of-pull-request-workflows
created: 2023-11-28T00:00:00.000Z
guid: 4bdc5e9f-bdd9-4e8a-a5e2-3cfa637e4a56
---

Managing webpages can be challenging, especially in projects with many contributors. When editing a page, a common problem is not knowing who the original author was. This is bad, because it's important not to change something that was there for a reason!

<!--endintro-->

The best way to solve this is by having a page owner for each webpage.

### Why?

A designated page owner ensures someone is responsible for the accuracy of the page content. It avoids confusion about who to approach for major changes, and it allows the page owner to keep an eye on changes.

### Steps

1. Markdown files - Add an 'owner' field in the frontmatter metadata for each page.
2. New pages - The field should be required when creating a page.
3. Pull requests - Automatically add the page owner as a reviewer for any pull requests that modify their page.

**Tip: this can be done automatically with a GitHub Action (or similar automation)**

✅ The "owner" (person responsible) is aware of and can approve any changes

✅ People know who to consult about changes to the page

🤔 We don't use `CODEOWNERS` for this because we don't want to block pull requests for minor edits

❌ When trying to work out who is the page owner, version history is not good enough - often the creator of a page is not the actual author e.g. a dev makes the page for a Marketing person

::: bad
![Figure: Bad example - No owner field. Impossible to see who wrote this page!](no-author-bad.png)
:::

::: good
![Figure: Good example - Frontmatter with an 'author' field.](page-owner-good.jpg)
:::
