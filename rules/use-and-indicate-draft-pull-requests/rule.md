---
seoDescription: Draft Pull Requests enhance collaboration and feedback by indicating work-in-progress, reducing duplication, and maintaining a transparent development pipeline.
type: rule
archivedreason:
title: Pull Requests - Do you use and indicate Draft Pull Requests?
guid: e2b8bcf4-916b-499b-b8f1-ca2a4c80cee9
uri: use-and-indicate-draft-pull-requests
created: 2024-01-11T04:53:25.0000000Z
authors:
  - title: Tino Liu
    url: https://ssw.com.au/people/tino-liu
  - title: Nick Curran
    url: https://ssw.com.au/people/nick-curran
  - title: Daniel Mackay
    url: https://ssw.com.au/people/daniel-mackay
related:
  - over-the-shoulder
  - adding-changes-to-pull-requests
  - do-you-use-co-creation-patterns
  - write-a-good-pull-request
  - co-authored-commits
redirects:
  - create-draft-pull-requests
---

The use of Draft Pull Requests is a handy practice to indicate work in progress promoting early collaboration and continuous feedback.
This approach enhances code quality, reduces duplication, and helps to maintain a transparent and efficient development pipeline. Creating Draft Pull Requests will also trigger GitHub Workflows so developers get early feedback on the quality of their changes.

Draft Pull Requests are less effective if they are not clearly marked as Draft, as is the case on GitHub. To make them clearer, use a naming convention like `🚧 WIP: {{PR Title}}` to clearly show that it is a Draft Pull Request.

### GitHub

::: bad
![Figure: Bad example - The default experience lacks clear indication that this is Draft Pull Request](github-bad-example.png)
:::

::: good
![Figure: Good example - Add prefix with 🚧 emoji to clearly indicate it is a Draft Pull Request](github-good-example.png)
:::

If you want to go one step further, you can add the [WIP App](https://github.com/marketplace/wip) to your repo. The WIP App prevents the merging of Pull Requests with "WIP" in their title. When you are ready to go, you just remove the WIP prefix.

::: good
![Figure: Good example - WIP app catching Draft Pull Request](github-wip.png)
:::

### Azure DevOps

::: good
![Figure: Good example - Clear naming and indication of a draft pull request](devops-good-example.png)
:::
