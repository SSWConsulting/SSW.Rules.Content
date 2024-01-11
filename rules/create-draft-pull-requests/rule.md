---
type: rule
archivedreason: 
title: Pull Requests - Do you use draft pull requests?
guid: e2b8bcf4-916b-499b-b8f1-ca2a4c80cee9
uri: create-draft-pull-requests
created: TODO
authors:
- title: Tino Liu
  url: https://ssw.com.au/people/tino-liu
related:
- github-content-changes
- use-pull-request-templates-to-communicate-expectations
- over-the-shoulder
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

---

The use of draft pull requests is a handy practice to indicate work in progress promoting early collaboration and continuous feedback.
This approach enhances code quality, reduces duplication, and helps to maintain a transparent and efficient development pipeline.

Draft pull requests are less effective if they are not clearly marked as Draft, as is the case on GitHub. To make them clearer, use a naming convention like `❌ WIP: {{PR Title}}` to clearly show that it is a draft pull request.

### GitHub

::: bad
![Figure: Bad example - The default experience lacks clear indication that this is draft pull request](github-bad-example.png)
:::

::: good
![Figure: Good example - Add prefix with ❌ emoji to clearly indicate it is a draft pull request](github-good-example.png)
:::

If you want to go one step further, you can add the [WIP App](https://github.com/marketplace/wip) to your repo. The WIP App prevents the merging of Pull Requests with "WIP" in their title.

::: good
![Figure: Good example - WIP app catching draft pull request](github-wip.png)
:::

### Azure DevOps

::: good
![Figure: Good example - Clear naming and indication of a draft pull request](devops-good-example.png)
:::
