---
type: rule
title: Pull Request - Do you do over the shoulder reviews?
uri: over-the-shoulder-prs
authors:
  - title: Brook Jeynes
    url: https://www.ssw.com.au/people/brook-jeynes
related:
  - do-you-know-the-3-steps-to-a-pbi
  - do-you-use-co-creation-patterns
created: 2023-05-15T21:36:54.519Z
guid: f20af960-7a60-499c-980b-bd5bb6a0af91
---
An "over-the-shoulder" review is one of the best ways to avoid merge debt. When a pull request (PR) is ready to be reviewed, get someone with you either in-person or on call, and go through the PR together. This not only allows you to demo the content of the PR but also talk with the person taking feedback when needed.

It is the developer's responsibility to get a PR reviewed and action feedback ASAP. When a PR is created but left open for a long time, it becomes stale. Stale PRs equate to merge debt because the longer the PR stays open, the more changes occur on the main branch and the harder it is to merge back in.

Merge debt refers to the amount of work a PR has to undergo before it can be merged into the main branch. If the PR is brand new, the amount of work required to merge is near to none, but as the PR stays open, the more work gets done on the main branch, leading to more work needing to be done to ensure the PR is up-to-date and able to be merged.

Merge debt can be avoided by:

* Ensuring PRs don't stay open for too long
* Conducting daily reviews on repos to ensure all PRs that can be merged are merged
* Ensuring that once a PR is ready to be merged, an "over-the-shoulder" review occurs.

::: bad
![Figure: Bad example - Pressing commit and forgetting about it. PR has been left open for a over 2 weeks](https://github.com/SSWConsulting/SSW.Website-v3/assets/25432120/5a67d6ed-a301-4d72-af00-8da4277c1b75)
:::

::: good
![Figure: Good example - Pressing commit and calling up an engineer to check through it](screenshot-2023-06-12-at-07.41.59.png)
:::