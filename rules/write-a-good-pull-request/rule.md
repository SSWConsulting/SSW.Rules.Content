---
type: rule
title: Do you know how to write a great Pull Request (PR)?
uri: write-a-good-pull-request
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Chris Clement
    url: https://ssw.com.au/people/chris-clement
  - title: Matt Goldman
    url: https://ssw.com.au/people/matt-goldman
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
  - title: Gordon Beeming
    url: https://ssw.com.au/people/gordon-beeming
  - title: Seth Daily
    url: https://ssw.com.au/people/seth-daily
related:
  - useful-information-on-changes
  - close-pbis-with-context
  - use-pull-request-templates-to-communicate-expectations
  - use-emojis-in-your-commits
  - which-emojis-to-use-in-scrum
  - reply-done-and-delete-the-email
redirects:
  - do-you-know-how-to-write-a-good-pull-request
created: 2020-07-17T01:21:08.000Z
archivedreason: null
guid: d35b49bf-bdd1-48eb-bc1d-944cdc5be4dc

---

As a software developer, you are going to create Pull Requests (PRs) that you want to be easy for others to review and approve. The quality of a Pull Request can vary - from cryptic to well-written.

Including a little bit of context helps your reviewer understand changes quickly so they can review your PR faster and give better suggestions.

There are 2 essential things you should have when writing a Pull Request:

<!--endintro-->

## 1. Concise and self-explanatory title

Good **PR titles** provide a clear, concise summary of the change, helping reviewers quickly understand its purpose and priority.

* What the PR will do
* How the PR achieves it
* Emojis! Follow the [GitMoji.dev](https://gitmoji.dev) standard

The key to writing a concise Pull Request is to base the PR itself on a PBI / Issue (assuming they are well written).

::: greybox
**PBI title:** Product Backlog Item 100359: "Desktop App | Exporting occasionally failed"

**Pull Request title:** Fix exporting
:::
::: bad
Bad example - Pull Request title does not tell what issues have been fixed and how
:::

::: greybox
**PBI title:** Product Backlog Item 100359: "Desktop App | Exporting occasionally failed"

**Pull Request title:** 🐛 BUG - Fix desktop app exporting - prevent database concurrent access while exporting
:::
::: good
Good example - Pull Request title briefly describes the fix that it has
:::

Having the **"What"** information allows the reviewers to quickly understand what this is about while having the **"How"** can help the reviewer to quickly understand how your PR solved the problem. Sometimes we might want to put the **"How"** in the PR descriptions (see below) if it is too long or hard to explain in one sentence.

## 2. Clear and informative description that gives all the context

The Pull Request description is a medium for the developer to tell the reviewers what the changes are about.

Good **PR descriptions** provide background information helps others quickly understand the problem, solution, and rationale. This minimizes confusion, accelerates reviews, and improves overall code quality.

::: info
**Tip:** For rare straight-forward changes the self-explanatory title might be enough. You should still include context so the reviewer knows what initiated the changes (examples below)
:::

Examples of sentences to have in a good PR description:

* "Relates to **#{{ ISSUE NUMBER or URL }}**" (⚠️ see [avoid linking to Issues you do **not** want to close](/avoid-auto-closing-issues/))
* "From email subject: **{{ EMAIL SUBJECT }}**" (similar to the rule on [warn then call](/warn-then-call))
* "As per my conversation with **{{ NAME(S) }}**" (similar to "[as per our conversation](/as-per-our-conversation-emails)" rule)
* "Worked with **{{ @MENTION(S) }}**" (as per [pair or mob programming](/do-you-use-co-creation-patterns) rule)
* "This PR is to **{{ ACHIEVE THE FEATURE / FIX THE BUG / OTHER GOAL(S) }}**" (anything that was not possible to explain in the title)
* See **"{{ SCREENSHOT / DONE VIDEO }}** for more details" (to help the reviewer to understand the changes. E.g. Styling changes)

If you noticed that a change needed to be made and had no specific task/issue, use:
  
* "I/We noticed a problem: **{{ DETAILS }}**"

If there is an area you are uncertain about, add:

* "I'm looking for feedback on this code"

If the PR is closing an email task after merged, remember to refer back to it:

* "Done - see email: **{{ EMAIL SUBJECT }}**

::: info
Linking the source to a PR serves as documentation on which development work that was done. It helps in the future to debug when and which changes were introduced and the original specification of that piece of work.
:::

::: greybox
**PR title:** Update Rule “meaningful-pbi-titles/rule”

**PR description:**
:::
::: bad
Figure: Bad example - Cannot tell what was done here
:::

::: greybox
**PR title:** Update Rule “meaningful-pbi-titles/rule”

**PR description:** Added missing video caption + removed unnecessary brackets
:::
::: ok
Figure: OK example - Clear and concise description, however it's not clear what task triggered the change
:::

::: greybox
**PR title:** Update Rule “meaningful-pbi-titles/rule”

**PR description:**
From email subject by @bob: **SSW.Rules - Video caption missing**
Added missing video caption + removed unnecessary brackets
:::
::: good
Figure: Good example - It's clear what changes are being made and where the task came from
:::

::: info
There is also well-known Pull Request semantics like [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) on how to write a PR body, but we can still have a great PR without using such preciseness.
:::

### How to approach making a Pull Request

`youtube: https://www.youtube.com/watch?v=d8yGY6KsYys&t=29s`

**Video: 5 Tips For Better Pull Requests (11 min)**

#### FAQs

**Q: Are you making many small changes?**

**A:** You should summarize by saying: *“Improved readability”* OR *“Fixed typos and grammar”*.

**Q: Are the changes big and complex?**

**A:** You should include a demonstration of the change.  
E.g. A [screenshot](/screenshots-avoid-walls-of-text) to show text/UI changes, or a [Done video](/record-a-quick-and-dirty-done-video) to demo functionality changes.

**Q: Are you using a CMS editor (like Netlify or Tina)**

**A:** CMS editors may automatically add a placeholder description. If you're using a CMS to make your changes, you may need to go to the PR afterward and update the description to include the context.

::: info
**Tip:** Ensure devs follow these tips by using a template. [Learn more and check out a template example](/use-pull-request-templates-to-communicate-expectations).
:::
