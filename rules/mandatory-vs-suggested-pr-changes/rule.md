---
seoDescription: Master effective pull request reviews by categorizing feedback into ‘Change,’ ‘Consider,’ and ‘PBI’ for clear, actionable guidance. Improve collaboration and streamline approvals with structured, prioritized comments
type: rule
title: Do you know how to indicate mandatory vs suggested PR changes?
uri: mandatory-vs-suggested-pr-changes
authors:
  - title: Daniel Mackay
    url: https://www.ssw.com.au/people/daniel-mackay
  - title: Matt Goldman
    url: https://www.ssw.com.au/people/goldie
related:
  - todo-tasks
created: 2024-10-28T17:00:00.000Z
guid: 6F5AE6FC-F29A-4938-B012-FDE7F669998C
---

When reviewing another developer's pull request, review comments can fall into a mix of categories. Some changes might be required, while others might be optional. Do you know the best way to tell the requester which is which?

<!--endintro-->

## Types of Pull Request Feedback

When reviewing pull requests, comments can often be divided into two categories:

* **Change** - you must change this if you want me to approve
* **Consider** – consider this suggestion, but don’t feel obliged to change (i.e. I would do this, but I won’t block you on it)
* **PBI** – Important, but create a PBI to fix this in future

By prefixing the comment with one of the categories above, the reviewer can make it clear to the author if they must make the change or not.

When adding 'PBI' comments, a "good Samaritan" approach is to create the PBI and link to it (add a [TODO task](https://www.ssw.com.au/rules/todo-tasks/)). Alternatively if you just leave the comment and want the requester to do it, they should do the same (add a TODO with a link to the PBI) before you approve it.

## Pull Request Comment Examples

::: greybox  
This could be refactored to be better
:::  
::: bad  
Figure: Bad example - not clear if the author should make the change or not
:::

::: greybox  
Change – check for null reference and throw if found
:::  
::: good  
Figure: Good example - clear that the change should be made before the PR will be approved
:::

::: greybox  
Consider – break long method into several smaller ones
:::  
::: good  
Figure: Good example - the reviewer has left a suggestion, but it's up to the author do change or not
:::

::: greybox  
PBI – Consolidate these xUnit ‘Fact’ tests to use ‘InlineData’
:::  
::: good  
Figure: Good example - This change doesn't need to be done now, but should be added to the backlog with a comment in the code
:::
