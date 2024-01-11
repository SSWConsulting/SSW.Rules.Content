---
type: rule
archivedreason: 
title: Pull Requests - Do you create draft pull requests?
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

Draft pull requests serve as a vital practice, promoting early collaboration and continuous feedback. 
This approach enhances code quality, reduce duplication, and maintain a transparent and efficient development pipeline.

However, the effectiveness of draft pull requests can be hindered by the lack of clarity on certain platforms when presenting them. To enhance the clarity of draft pull requests, you can adopt a naming convention such as: `❌ WIP: {{PR Title}}`. This ensures a clear indication of a draft pull request.

### GitHub

::: bad
![Figure: Bad example - The default experience lacks clear indication](github-bad-example.png)
:::

::: good
![Figure: Good example - Add prefix with ❌ emoji to clearly indicate it is a draft pull request](github-good-example.png)
:::

If you want to go one step further, you can add an app to your repo: [WIP · GitHub Marketplace](https://github.com/SpookyBoogy2016/SSW.Rules.Content/assets/18450582/7c6a9d74-7a87-46a3-a68d-79f8c4096c2e)

::: good
![Figure: Good example - WIP app catching draft pull request](github-wip.png)
:::

### Azure DevOps

::: good
![Figure: Good example - Clear naming and indication of a draft pull request](devops-good-example.png)
:::
