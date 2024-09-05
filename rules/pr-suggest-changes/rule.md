---
type: rule
seoDescription: Learn the best practices for suggesting changes in a Pull Request using GitHub's 'Suggest a change' feature to streamline the review process.
title: Do you know the best way to suggest changes on a Pull Request?
uri: pr-suggest-changes
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Brady Stroud
    url: https://ssw.com.au/people/brady-stroud
related:
  - github-content-changes
  - change-from-x-to-y
created: 2024-09-05T04:50:21.000Z
archivedreason: null
guid: 8b529efe-d500-42b8-9632-7de23506546a
---

Normally, the best way to provide feedback on content changes is to use the [change X to Y format](/change-from-x-to-y).
When it comes to reviewing Pull Requests (PRs) in GitHub, this is not the case - its  inefficient for the PR owner. They have to manually interpret each suggested change, implement them in the code, and then commit the changes, which can be time-consuming.

<!-- `youtube: TODO`
**Video: TODO** -->

::: bad
![Figure: Bad example - Need to copy+paste changes](bad-pr-suggest-changes.png)
:::

Instead, reviewers should use GitHub's **Add a suggestion** feature. This allows the reviewer to directly suggest changes in the code diff view, and the PR creator can easily accept or reject these changes with a single click. This process is more streamlined and makes it easier to implement suggestions.

::: good
![Figure: Good example - Using the 'Add a suggestion' button](good-suggest-a-change-button.png)
:::

<!--endintro-->

When the PR creator reviews the suggestion, they can either click **'Commit suggestion'** to apply it directly or **'Resolve conversation'** if they choose not to apply it.

::: good
![Figure: Good example - easy to see what has changed + awesome 'Commit Suggestions' button ✨ ](good-pr-suggestions.png)
:::
