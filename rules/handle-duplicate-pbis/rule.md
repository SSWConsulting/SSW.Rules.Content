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
  - title: Luke Cook
    url: https://www.ssw.com.au/people/luke-cook
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
  - title: Tom Iwainski
    url: https://www.ssw.com.au/people/thomas-iwainski
  - title: Jake Bayliss
    url: https://www.ssw.com.au/people/jake-bayliss
related:
  - use-ai-manage-backlog
guid: 85612086-fd82-4d02-abd0-baf0b310004a
---

When working on a GitHub backlog, it's common for multiple Product Backlog Items (PBIs) to be raised about the same issue, especially when several people encounter it independently.

Duplicates clutter the backlog and can lead to wasted effort. A clean backlog is easier to maintain. But it's also important to make sure everyone stays informed on their reported issues.

<!--endintro-->

## Why you should close duplicate PBIs

A cluttered backlog slows progress and makes it hard for the team to focus on what matters most. Keeping duplicates open leads to a messier backlog, which can mean time wasted and discussion fragmented across these issues.

The best practice is to close duplicate PBIs so that there is **only one active PBI per issue**. This ensures all relevant details, conversations, and decisions remain centralized. But while this practice is great for development teams, it can often be seen as hostile toward end-users when they receive a "Closed as duplicate" notification, and never hear from you again. 

### Keep users informed

When a PBI is closed as a duplicate, the person who raised it will **not** automatically receive updates when the main issue is completed. To maintain transparency and show respect for the bug reporter's contribution, it's good practice to keep them informed.

The easiest way to do this is to close the PBI with a friendly comment directing the user to the issue you're keeping, inviting them to subscribe to that thread for updates and discussion.

### How to manage duplicate PBIs

#### 1. Identify the main (active) PBI

Choose the most complete or best-discussed PBI as the primary one to keep open. It should have the clearest description, relevant discussion, and active tracking.

::: good
![Figure: Good example - A clean and well-defined PBI is a good candidate for the main PBI to keep](good-pbi.png "Good bug report")
:::

#### 2. Close and link the duplicate PBIs

Once you've identified the main PBI, close the others as duplicates. In GitHub, there are two standard ways to do this:

* Add a comment in the format of **"Duplicate of #101"**, then close the issue manually, or  
* Use GitHub's **"Close as duplicate"** feature (available when referencing another issue in the comment)

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

#### 3. Notify users who created the duplicates

Since closing their PBI means they won't receive future updates automatically, it's a good idea to invite the users to follow the main issue, if they're interested in tracking progress and adding to the discussion.

::: greybox
Comment on #101:  
> "@jane thanks for reporting this! We've got a few open issues reporting this problem, so we're going to consolidate them into a single issue here - #103. Feel free to subscribe to it to follow along!"
:::
::: good
Figure: Good example - All reporters are acknowledged and invited to join the discussion on the main issue
:::

#### 4. Gold plating - Notify users when the work is complete

For an amazing user or customer experience, don't just rely on them subscribing to the main issue. Instead, get back to them when the work is done, letting them know their contribution has been heard and actioned.

::: greybox
Comment on #101:  
> "Hi @jane 👋
> Good news - this work has been completed! This issue was marked as a duplicate, and the work was tracked in #103.
>
> Thanks for your contribution 🙏"
:::
::: good
Figure: Best example - Users are kept informed that the work is done, even when they didn't subscribe to the main issue
:::

## Automate where possible

If your project frequently encounters duplicates, consider automating this workflow:

* Use GitHub Actions or bots to suggest duplicates automatically based on title or description similarity
* Add a checklist to your **PBI template** reminding team members to search for existing issues before creating new ones
* Automatically notify authors of duplicate issues using our [GitHub workflow](https://github.com/SSWConsulting/SSW.GitHub.Template/blob/main/.github/workflows/duplicate-issue-notifier.yml)

---

### Summary

* Keep one active PBI per issue
* Link duplicates clearly
* Notify all reporters on completion

By consistently managing duplicates this way, your backlog stays clean and nobody is kept in the dark on their reported issues.
