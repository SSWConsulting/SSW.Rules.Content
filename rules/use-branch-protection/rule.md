---
type: rule
title: Do you use branch protection?
uri: use-branch-protection
authors:
  - title: Brady Stroud
    url: https://www.github.com/bradystroud
related: []
redirects: []
created: 2021-03-08T15:13:00.000Z
archivedreason: null
guid: 615dd407-2877-4c2d-b31a-60d75d42da3d
---
Branch protection is a feature in version control software that allows teams to define rules and restrictions around who can make changes to specific branches, and what types of changes are allowed. 

Disabling the **Allow force pushes** and **Allow Deletions** settings on your main branch will protect the branch from accidentally being deleted and the history being rewritten.

Using force push is dangerous and should be used with extreme caution, as it will override other contributor's changes with your own — and it won't stop to check if it will override any changes pushed up to remote in the process.

<!--endintro-->

1. Go to your repo | Settings | Branches 
2. If it doesn't already exist, create a branch protection rule on the 'main' or 'master' branch
3. Ensure 'Allow force pushes' and 'Allow Deletions' are disabled
4. Save changes

::: bad
![Bad example: Main branch not protected](image001.jpg)
:::

::: good
![Good Example: Main branch is protected](branchProtection.png)
:::

See the GitHub docs [Managing a branch protection rule](https://docs.github.com/en/github/administering-a-repository/managing-a-branch-protection-rule)

You can use required status checks if you need to check that your code changes will build. Status checks are GitHub Actions that are required to succeed before the PR can be merged, so developers can't merge failing code. You can enable required status checks in the same location as **Allow force pushes** and **Allow Deletions**.

::: good
![Figure: Developers can't merge until all checks have passed](requiredChecks.png)
:::

See the GitHub docs [Require status checks before merging](https://docs.github.com/en/github/administering-a-repository/defining-the-mergeability-of-pull-requests/about-protected-branches#require-status-checks-before-merging)