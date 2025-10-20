---
type: rule
tips: ""
title: Do you know how to handle duplicate PBIs in your backlog?
seoDescription: Learn the best way to handle duplicate PBIs in GitHub backlogs
  to keep your project clean, organized, and user-focused.
uri: handle-duplicate-pbis
authors:
  - title: Zach Keeping
    url: https://www.ssw.com.au/people/zach-keeping
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
  - title: Luke Cook
    url: https://www.ssw.com.au/people/luke-cook
  - title: Ulysses Maclaren
    url: https://www.ssw.com.au/people/ulysses-maclaren
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
  - title: Levi Jackson
    url: https://www.ssw.com.au/people/levi-jackson
  - title: Jim Zheng
    url: https://www.ssw.com.au/people/jim-zheng
  - title: Luke Mao
    url: https://www.ssw.com.au/people/luke-mao
  - title: Tom Iwainski
    url: https://www.ssw.com.au/people/thomas-iwainski
  - title: Aman Kumar
    url: https://www.ssw.com.au/people/aman-kumar
  - title: Jake Bayliss
    url: https://www.ssw.com.au/people/jake-bayliss
  - title: Josh Berman
    url: https://www.ssw.com.au/people/josh-berman
related:
  - use-ai-manage-backlog
guid: 85612086-fd82-4d02-abd0-baf0b310004a
---

When working on a GitHub backlog, it’s common for multiple Product Backlog Items (PBIs) to be raised about the same issue, especially when several people encounter it independently.

Duplicates clutter the backlog and can lead to wasted effort. A clean backlog is easier to maintain. But it's also important to make sure everyone stays informed on their reported issues.

<!--endintro-->

## Why you should close duplicate PBIs

A cluttered backlog slows progress and makes it hard for the team to focus on what matters most. Keeping duplicates open leads to a messier and harder to manage backlog, which can mean time wasted and discussion fragmented across these issues.

The best practice is to close duplicate PBIs so that there is **only one active PBI per issue**. This ensures all relevant details, conversations, and notifications remain centralized, while still ensuring everyone who reported the issue stays informed.

### Keep bug reporters informed

When a PBI is closed as a duplicate, the person who raised it will **not** automatically receive updates when the main issue is completed. To maintain transparency and show respect for the bug reporter’s contribution, always ensure they are kept informed.

The simplest way to do this is to **@mention the reporting user** in the main (active) PBI when closing the duplicate. This ensures they receive notifications about progress and resolution.

## How to manage duplicate PBIs

### 1. Identify the main (active) PBI

Choose the most complete or best-discussed PBI as the primary one to keep open. It should have the clearest description, relevant discussion, and active tracking.

::: good
![Figure: Good example - A clean and well-defined PBI is a good candidate for the main PBI to keep](good-pbi.png "Good bug report")
:::

### 2. Close and link the duplicate PBIs

Once you’ve identified the main PBI, close the others as duplicates. In GitHub, there are two standard ways to do this:

* Add a comment in the format of **"Duplicate of #101"**, then close the issue manually, or  
* Use GitHub’s **"Close as duplicate"** feature (available when referencing another issue in the comment)

Both methods automatically link the issue to the active PBI and make the relationship clear to other users.

::: greybox
**Comment:** "Duplicate"
:::
::: bad
Figure: Bad example - The issue is closed abruptly without context, which confuses the reporter
:::

::: greybox
**Comment:** "Duplicate of #101 - follow here for further updates"
:::
::: good
Figure: Good example - Using the built-in GitHub duplicate workflow keeps issues linked and easy to trace
:::

::: good
![Figure: Good example - Using the built-in "Close as duplicate of..." button is an easy way to close an item while linking to the main PBI. It can be helpful to leave comment here for additional context](close-as-duplicate-button.png "Close as duplicate button")
:::

### 3. Notify the users who created the duplicates

Since closing their PBI means they won’t receive future updates automatically, it’s essential to @mention those users in the main PBI so they know when the issue is resolved.

::: greybox
Comment on #101:  
> "@jane @sam closing your related issues (#102, #103) as duplicates. You’ll be notified here when this issue is resolved."
:::
::: good
Figure: Good example - All reporters are acknowledged and notified when the main PBI is completed
:::

## Automate where possible

If your project frequently encounters duplicates, consider automating this workflow:

* Use GitHub Actions or bots to suggest duplicates automatically based on title or description similarity
* Add a checklist to your **PBI template** reminding team members to search for existing issues before creating new ones

---

### Summary

* Keep one active PBI per issue
* Link duplicates clearly
* Notify all reporters on completion

By consistently managing duplicates this way, your backlog stays clean and nobody is kept in the dark on their reported issues.
