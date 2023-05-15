---
type: rule
title: Over the shoulder PRs
uri: over-the-shoulder-prs
authors:
  - title: Brook Jeynes
    url: https://www.ssw.com.au/people/brook-jeynes
created: 2023-05-15T21:36:54.519Z
guid: f20af960-7a60-499c-980b-bd5bb6a0af91
---
A PBI isn't considered complete until the PR has been accepted and merged into 
main. It is the developers responsibility to get a PR reviewed before closing the PBI. When a PR is created but left open for a long time, it becomes stale. Stale PRs lead to merge debt because the longer the PR stays open, the more changes occur on main. 

Merge debt refers to the amount of work a PR has to undergo before it can be merged
into main. If the PR is brand new, the amount of work required here is near to none, but as the PR stays open, the more work gets done on main, leading to more work needing to be done to ensure the PR is up-to-date and able to be merged.

Merge debt can be avoided by:
- Ensuring PRs don't stay open too long
- Conduct daily reviews on repos ensuring all PRs that can be merged are merged
- Ensuring once a PR is ready to be merged, and "over the shoulder" review occurs. 

An "over the shoulder" review is one of the best ways of avoiding merge debt. When a PR is ready to be reviewed, get someone with you either in-person or on call, and go through the PR together. This not only allows you to demo the content of the PR but also talk with the person taking feedback when needed


::: bad
![Figure: Bad example - PR has been left open for a over 2 weeks](https://github.com/SSWConsulting/SSW.Website-v3/assets/25432120/5a67d6ed-a301-4d72-af00-8da4277c1b75)
:::