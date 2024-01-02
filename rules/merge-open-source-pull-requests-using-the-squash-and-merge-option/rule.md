---
type: rule
archivedreason: 
title: Do you merge open source pull requests using the squash and merge option?
guid: fdf79da7-2c24-42e1-bf2e-9f88fd034eb7
uri: use-squash-and-merge-for-open-source-projects
created: 2023-09-07T04:49:00.0000000Z
authors:
- title: Gordon Beeming
  url: https://ssw.com.au/people/gordon-beeming
- title: Brady Stroud
  url: https://ssw.com.au/people/brady-stroud
- title: William Liebenberg
  url: https://ssw.com.au/people/william-liebenberg
related: 
- use-pull-request-templates-to-communicate-expectations
redirects: []

---

When you are working on an open source project, you will often get pull requests from contributors. When you merge these pull requests, you should use the squash and merge option. This will squash all the commits into one commit and then merge it into the target branch. This is a good practice because it keeps the commit history clean and easy to read. It also makes it easier for other developers to understand what changes were made in each pull request.

<!--endintro-->

### Commit Message

Like any commit message, the PR commit message should be short and descriptive. The easiest way to achieve this is to combine the PR title and commit details.

::: bad  
![Figure: Bad example - This merge will be missing important information from the commit message](confirm-squash-and-merge-with-no-details.jpg)  
:::

::: good  
![Figure: Good example - This merge will include all the commit messages as part of the PR commit message](confirm-squash-and-merge.jpg)  
:::

In order to get GitHub to use your commit details by default you need to change the configuration for the repository. 

![Figure: Repo Settings | Pull Requests | Allow squash merging, and change the value to **Default to pull request title and commit details**](squash-merge-settings.jpg)  

### Limit merge types

You should limit the merge types that are allowed on your repository. This makes it easy for everyone to know the expected merge type of the repository when the PR is merged.

![Figure: Repo Settings | Pull Requests, Remove **Allow merge commits** and **Allow rebase merging** to force all PRs to be squash merged](limit-merge-types.jpg)  


### Automatically delete head branches

After a branch is merged into the target branch, you'd not want to continue development on the previous branch as the changes were squashed in. It's always a good idea to create a new branch after a PR is merged from the target branch if you have additional changes. To make this easier, you can configure GitHub to automatically delete the branch after the PR is merged.

![Figure: Repo Settings | Pull Requests, Enable **Automatically delete head branches** to avoid stale branches](automatically-delete-head-branches.jpg)  


### Other configuration

If you find that pull requests are often approved but for some reason not merged in, you may want to enable `auto-merge`. This will automatically merge the PR when all the required checks have passed.

![Figure: Repo Settings | Pull Requests, Enable **Allow auto-merge**](auto-merge.jpg)  

You may want to enable **Always suggest updating pull request branches**, this can be done from Repo Settings | Pull Requests, this provides contributors with an easy way to update their branch from the target branch without performing the merge themselves on their local machine. 

![Figure: Providing contributors with an easy mechanism to update their branch helps reduce conflicts if they need to make more changes](update-branch.jpg)  

