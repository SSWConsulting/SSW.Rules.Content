---
type: rule
archivedreason: 
title: Do you have a standard set of pull request workflows?
guid: 660b3dce-0c6b-412e-839e-15083f829454
uri: standard-set-of-pull-request-workflows
created: 2020-08-12T01:21:08.0000000Z
authors:
- title: Gordon Beeming
  url: https://ssw.com.au/people/gordon-beeming
related: 
- merge-debt
redirects: []

---

Getting started with a new repository can be daunting, especially if you are new to the project. Having a standard set of pull request workflows can help you get started and make sure you are following the same process as everyone else on the team.

A few standard workflows helps developers see a consistent process across all repositories. This makes it easier for developers to get started with a new repository and makes it easier for developers to move between repositories as the feedback they get from each pull request is consistent.

<!--endintro-->

Below are a few standard workflows that you can use in your repositories.

### PR - t-shirt size the pr

This workflow uses the [microsoft/PR-Metrics](https://github.com/microsoft/PR-Metrics) action to update each pull request with information that helps ensure engineers keep PRs to an appropriate size with appropriate test coverage, while informing reviewers of the expected time commitment for a thorough review of the code.

![Figure: PR Metrics gives warnings with suggested actions](pr-metrics.jpg)

You can find the workflow at [SSWConsulting/SSW.GitHub.Template/.github/workflows/pr-metrics.yml](https://github.com/SSWConsulting/SSW.GitHub.Template/blob/main/.github/workflows/pr-metrics.yml)

### PR - Manage Stale PRs

This workflow creates adds labels to pull requests as they age.

![Figure: It's easy to see at a glance when PRs have been around for a while](pr-age-labels.jpg)

The workflow will also ping the author of the pull request after around 36 hours and remind them about [merge debt](/merge-debt/)

![Figure: A gentle reminder helps remind developers the next day that their pull request needs attention](pr-merge-debt-reminder.jpg)

You can find the workflow at [SSWConsulting/SSW.GitHub.Template/.github/workflows/pr-manage-stale.yml](https://github.com/SSWConsulting/SSW.GitHub.Template/blob/main/.github/workflows/pr-manage-stale.yml)
