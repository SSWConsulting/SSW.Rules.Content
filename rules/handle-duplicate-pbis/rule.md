---
type: rule
tips: ""
title: Do you know how to handle duplicate PBIs in your backlog?
seoDescription: Learn the best way to handle duplicate PBIs in GitHub backlogs
  to keep your project clean, organized, and user-focused.
uri: handle-duplicate-pbis
authors:
  - title: Zach Keeping
    url: https://www.ssw.com.au/people/zach-keeping/
guid: 85612086-fd82-4d02-abd0-baf0b310004a
---
When working on a GitHub backlog, it’s common for multiple Product Backlog Items (PBIs) to be raised about the same issue, especially when several people encounter it independently.

If left unmanaged, these duplicates clutter the backlog, confuse priorities, and lead to wasted effort. A clean backlog is easier to maintain, track, and report on.  

<!--endintro-->

### Why you should close duplicate PBIs

A cluttered backlog slows progress and makes it hard for the team to focus on what matters most. Keeping duplicates open leads to double work, inconsistent updates, and fragmented discussion across issues.

The best practice is to close duplicate PBIs so that there is **only one active PBI per issue**. This ensures all relevant details, conversations, and notifications remain centralized — while still ensuring everyone who reported the issue stays informed.

- - -

### Keep reporters informed

When a PBI is closed as a duplicate, the person who raised it will not automatically receive updates when the main issue is completed. To maintain transparency and show respect for the reporter’s contribution, always ensure they are kept informed.

The simplest way to do this is to **@mention the reporter** in the main (active) PBI when closing the duplicate. This ensures they receive notifications about progress and resolution.

- - -

### How to manage duplicate PBIs

#### 1. Identify the main (active) PBI

Choose the most complete or best-discussed PBI as the primary one to keep open.
It should have the clearest description, relevant discussion, and active tracking.

::: good
![Figure: Good example - A clean and well-defined PBI is a good candidate for the main PBI to keep.](screenshot-2025-10-14-at-2.52.18 pm.png "Good bug report")
:::


#### 2. Close and link the duplicate PBIs

Once you’ve identified the main PBI, close the others as duplicates.
In GitHub, there are two standard ways to do this:

* Add a comment in the format of **"Duplicate of #101"**, then close the issue manually, or  
* Use GitHub’s **"Close as duplicate"** feature (available when referencing another issue in the comment)

Both methods automatically link the issue to the active PBI and make the relationship clear to other users.

::: greybox
Comment: "Duplicate."
:::

::: bad
Figure: Bad example – The issue is closed abruptly without context, which confuses the reporter
:::

::: greybox
Comment: "Duplicate of #101 - follow here for further updates"
:::
::: good
Figure: Good example – Using the built-in GitHub duplicate workflow keeps issues linked and easy to trace
:::

::: good
![Figure: Good example - Using the built-in "Close as duplicate" button is an easy way to close an item while linking to the main PBI. It can be helpful to leave comment here for additional context.](screenshot-2025-10-14-at-2.20.29 pm.png "Close as duplicate button")
:::

#### 3. Notify the users who created the duplicates

Since closing their PBI means they won’t receive future updates automatically, it’s essential to @mention those users in the main PBI so they know when the issue is resolved.

::: greybox
Comment on #101:  

> "@jane @sam closing your related issues (#102, #103) as duplicates. You’ll be notified here when this issue is resolved."
:::

::: good
Figure: Good example - All reporters are acknowledged and notified when the main PBI is completed
:::

- - -

### Automate where possible

If your project frequently encounters duplicates, consider automating this workflow:

* Use GitHub Actions or bots to suggest duplicates automatically based on title or description similarity.
* Add a checklist to your **PBI template** reminding team members to search for existing issues before creating new ones.

- - -

### Summary

✅ Keep one active PBI per issue\
✅ Link duplicates clearly\
✅ Notify all reporters on completion

By consistently managing duplicates this way, your backlog stays clean, your team stays aligned, and every contributor feels informed and valued.
