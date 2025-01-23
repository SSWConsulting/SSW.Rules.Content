---
seoDescription: Learn how to use labels for GitHub issues and streamline your open-source project's workflow.
type: rule
title: Do you know how to use labels for GitHub Issues?
uri: do-you-know-how-to-use-tags-for-github-issues
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Andreas Lengkeek
    url: https://ssw.com.au/people/andreas-lengkeek
  - title: Steven Qiang
    url: https://ssw.com.au/people/steven-qiang
related: []
redirects:
  - do-you-know-how-to-use-labels-for-github-issues
created: 2019-11-15T04:19:40.000Z
archivedreason: null
guid: c530e5c8-1fca-4a4b-bc17-fb0ba65b8625
---

It is important that you, especially a developer, knows how to use labels for GitHub issues when using an open source project on GitHub, as it would help compact issues and make the issue management workflow more efficient. Essentially, having such a predictable workflow will let the community feel professional.

<!--endintro-->

Every new repository comes in with some default labels out of the box that you could use to label your issues to help create a standard workflow in a repository. A list of the default labels and their general uses can be found here: [GitHub - Managing Labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels)

Depending on the project, there is often a need to create labels on top of the default labels. For instance, when you are using an internal project management solution (such as Azure DevOps) for an open source project, a new label "added to backlog" is created and applied to applicable issues specifically for demonstrating that an issue has been added to the Azure DevOps backlog and is being worked on for the community. This way you can give the community an understanding of the current goals of the project and a higher feeling of interactivity with your development team.

::: bad
![Figure: Bad example - It is hard to understand what issues are being worked on](issues_bad_example.png)
:::

::: good
![Figure: Good example - It is very simple to understand if an issue has received attention](issues_good_example.png)
:::

## Review and clean up labels

You should review the labels regularly and clean up outdated or irrelevant labels to keep the backlog clean and organized. A good use of labels can improve project clarity, enhance communication among team members, and streamline issue prioritization. In contrast, poor management of labels can lead to confusion, misaligned priorities in workflow.

When using [YakShaver](https://yakshaver.ai) to create work items, they will be tagged with `Needs Refinement`, this reminds developers to review the issue to ensure that the details are correct. Once the review has been test passed, ensure that this label is removed, so that other team members know that it ready to be worked on.

::: bad
![Figure: Bad example - The `Needs Refinement` labels are still on closed issues](label_bad_example.png)
:::

::: good
![Figure: Good example - Labels are relevant](label_good_example.png)
:::

### When to review a label

* **When the label is no longer relevant** - For example, removing a "blocked" label after resolving dependencies or unblocking an issue
* **If it misrepresents the current state** - For instance, removing "need refinement" after the details has been added
* **When the issue is closed** - Ensure the labels are consistent before closing the issue to maintain an accurate project history
* **If the label is unused or duplicated** - Remove labels that are not actively used or merge duplicates (e.g. having both label "bug-fix" and "bug")
* **When team conventions change** - If the team revises its workflow or labeling strategy, update labels to align with the new conventions
