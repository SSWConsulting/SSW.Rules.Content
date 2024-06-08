---
type: rule
archivedreason: 
title: Do you enable pull requests to ensure code is reviewed?
guid: 1ea236a9-b619-4d78-9bc8-ed3b7e39bf7f
uri: enable-pull-requests-to-ensure-code-is-reviewed
created: 2016-12-12T12:52:43.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ben Cull
  url: https://ssw.com.au/people/ben-cull
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
- title: Seth Daily
  url: https://ssw.com.au/people/seth-daily
related:
- github-content-changes
- use-pull-request-templates-to-communicate-expectations
- over-the-shoulder
- merge-debt
- write-a-good-pull-request
- dont-push-your-pull-requests
- adding-changes-to-pull-requests
- useful-information-on-changes
- do-you-save-failed-experiments-in-abandoned-pull-requests
- when-you-use-mentions-in-a-pbi
- avoid-auto-closing-issues
- use-squash-and-merge-for-open-source-projects
- standard-set-of-pull-request-workflows
- review-prs-when-not-required
- do-you-use-co-creation-patterns
- page-owner
redirects:
- do-you-enable-pull-requests-to-ensure-code-is-reviewed

---

Everybody strives to be perfect, but mistakes are normal, and it is easy for a developer to skim over errors when they've read their own code code hundreds of times!

Pull requests are the best way to ensure that two sets of eyes see every change - so the responsibility is never solely on the person writing the code.

<!--endintro-->

When Pull Requests are enabled, developers must create a branch and make their changes on that branch. Then they submit a Pull Request to merge their changes back into main. Each pull request must be approved by another reviewer.

::: bad  
![Figure: Bad example - Leaving the responsibility to each person to write perfect code](i-will-not-write-bad-code.jpg)  
:::

::: good  
![Figure: Good example - Make Pull Requests required](pull-request-diagram.png)  
:::

![Figure: Pull requests also give version history for rejected code!](github-pullrequest-2.png)  

### Useful resources - learn about Pull Requests

* [Pull Requests in GitHub](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
* [Pull Requests in Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops)

`youtube: https://www.youtube.com/watch?v=2VX1ISk9XH8`
**Video: What is a Pull Request? (3 min)**
