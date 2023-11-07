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
related:
  - useful-information-on-changes
  - close-pbis-with-context
  - use-emojis-in-your-commits
  - which-emojis-to-use-in-scrum
  - use-emojis
  - use-pull-request-templates-to-communicate-expectations
redirects:
  - do-you-know-how-to-write-a-good-pull-request
created: 2020-07-17T01:21:08.000Z
archivedreason: null
guid: d35b49bf-bdd1-48eb-bc1d-944cdc5be4dc
---

As a software developer, you are going to create Pull Requests that you want to be easy for others to review and approve. The quality of a Pull Request (PR) can vary - from cryptic to very well-written.

Including a little bit of context can help your reviewer understand changes quickly so they can review your PR faster, and also give better suggestions.

There are 3 things you can do to improve your Pull Request:

<!--endintro-->

### 1. Write a concise and self-explanatory title

The key to writing a concise Pull Request is to base the PR itself on a PBI / issue.

Good titles cover:

a. What the Pull Request will do

b. How the Pull Request achieved it

c. Use emojis! - follow the [GitMoji.dev](https://gitmoji.dev) standard

Examples:

**PBI title:**  Product Backlog Item 100359: "Desktop App | Exporting occasionally failed"

::: greybox
**Pull Request title:** Fix exporting
:::
::: bad
Bad example - Pull Request title does not tell what issues have been fixed and how.
:::

::: greybox
**Pull Request title:** 🐛 BUG - Fix desktop app exporting - prevent database concurrent access while exporting
:::
::: good
Good example - Pull Request title briefly describes the fix that it has.
:::

Having the **"What"** information allows the reviewers to quickly understand what this is about while having the "How" can help the reviewer to quickly understand how your PR solved the problem. Sometimes we might want to put the **"How"** in the PR body if it is too long or hard to explain in one sentence.

### 2. Write a concise and descriptive body

The Pull Request body is a medium for the developer to tell the reviewers what the changes are about. 

::: info
**Tip:** For straight-forward changes the self-explanatory title might be enough to describe the changes. Include context so the reviewer knows what initiated the changes (e.g. an issue url, email subject, or conversation)
:::

Good descriptions cover:

a. Give context
  - an issue url (or tag the ID, e.g. #123) 
  - email subject, like the rule [Warn then call](https://www.ssw.com.au/rules/warn-then-call/)
  - conversation, using the key phrase "[as per our conversation](https://www.ssw.com.au/rules/as-per-our-conversation-emails/)"

b. Did you do pair or mob programming?
  - [Do you use Co-Creation Patterns?](https://www.ssw.com.au/rules/do-you-use-co-creation-patterns/)
  - Example: Worked with @bob, @mary and @jane

c. What the PR is about and why did you raise it

d. How the PR will achieve the feature / fix the bug / other goals

e. Include a screenshot if it will help the reviewer to understand the changes (e.g. styling changes)

f. Tell he reviewers if there is an area you are uncertain about, e.g.: I'm looking for feedback on this code


::: greybox
**PR title:** Update Rule “meaningful-pbi-titles/rule”

**PR description:**  
:::
::: bad
Figure: Bad example - Cannot tell what was done here.
:::

::: greybox
**PR title:** Update Rule “meaningful-pbi-titles/rule”

**PR description:** Changes made:

1. Added missing video figure to embedded YouTube video
2. Fixed typo:  
From:  
Use emojis. See our rule on emojis in Scrum).  
To:  
Use emojis. See our rule on emojis in Scrum
:::
::: ok
Figure: OK example - What was done is clear, but both editor and reviewer may spend too much time on the description of such simple changes.
:::

Try to make generic comments that objectively summarize your changes. This way the reviewer will know what to expect and confirm the changes by looking at the file diffs.

::: greybox
**PR title:** Update Rule “meaningful-pbi-titles/rule”

**PR description:** Added missing video caption + removed unnecessary brackets
:::
::: ok
Figure: OK example - Clear and concise description, however it's not clear what task triggered the change.
:::

::: greybox
**PR title:** Update Rule “meaningful-pbi-titles/rule”

**PR description:** 
From email, subject: SSW.Rules - Video caption missing
Added missing video caption + removed unnecessary brackets
:::
::: good
Figure: Good example - It's clear what changes are being made and where the task came from.
:::

::: info
**Tip:** If you noticed that a change needed to be made and had no specific task, you can simply mention that in the PR body. Some examples are below of how you could give context for where the task came from:

- Example 1 - Relates to #{{ ISSUE NUMBER }}
- Example 2 - As per my conversation with...
- Example 3 - From email, subject...
- Example 4 - I noticed that...
:::

::: info
There is also well-known Pull Request semantics like [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) on how to write a PR body, but we can still have a great PR without using such preciseness.
:::

**Q: Are you making many small changes?**

A: You should summarize by saying: _“Improved readability”_ OR _“Fixed typos and grammar”_.

**Q: Are the changes big and complex?**

A: You should include a demonstration of the change. E.g. A [screenshot](/screenshots-avoid-walls-of-text) to show text/UI changes, or a [Done video](/record-a-quick-and-dirty-done-video) to demo functionality changes. 

**Q: Are you using a GUI editor (like Netlify or Tina)**

A: If you're using a GUI editor for your PRs, you may need to go to the PR afterward and update the description to include the context

::: bad
![Figure: Bad example - An automatically generated description doesn't give any context to reviewers](cms-bad-example.png)  
:::

::: good
![Figure: Good example - Updating the PR description to follow the repository standard helps you provide context to reviewers](cms-good-example.png)  
:::

### 3. Link the Pull Request to the associated issues / PBIs

::: info
**Warning:** In GitHub, certain keywords will close an issue rather than just associate it, see [avoid linking any Issues that you do not want to close](/avoid-auto-closing-issues/).
:::

Since we already have a great title and body, the last thing to do is to associate the Pull Request to the related PBIs or Issues.

Linking a PBI/Issue to a PR can serve as documentation on which development work that was done. It may help the team in the future to debug when and which changes were introduced and what was the original specification of that piece of work.

::: bad
![Figure: Bad example - Linking a PR to the related issue.](better-pr-link-issues.png)  
:::

::: good
![Figure: Good example - The PR is now associated with the related issue.](better-pr-link-issues-linked.png)
:::

