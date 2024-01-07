---
type: rule
archivedreason: 
title: Do you know when to branch in git?
guid: d023678e-aefe-45e8-a4f3-365d4c0f9c93
uri: do-you-know-when-to-branch-in-git
created: 2016-01-19T22:38:55.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
- title: Danijel Malik
  url: https://ssw.com.au/people/danijel-malik
- title: Edgar Rocha
  url: https://ssw.com.au/people/edgar-rocha
- title: Gabriel George
  url: https://ssw.com.au/people/gabriel-george
related:
- do-you-use-the-best-deployment-tool
redirects: []

---

The best way to handle continuous development and deployment is following [GitHub Flow](https://guides.github.com/introduction/flow/). The basic idea is to always deploy from  **master** , and to create a feature branch for every feature. When the feature is complete, it is merged back to master via a pull request, which provides a trigger for other developers to build.

Using this strategy, **master** is always production-ready and deployable.

<!--endintro-->

![](finishing-a-feature-with-world-class-flow.jpg)  

::: greybox
**Note:** This rule applies to git. For branching advice in TFVC, see [when to branch](/do-you-know-when-to-branch).
:::

`youtube: https://www.youtube.com/embed/9bP4-ly2qtQ?rel=0`

::: bad  
![Figure: Bad example - Committing to master](commit-master-bad.jpg)  
:::

::: good  
![Figure: Good example - Committing to a new branch](commit-branch-good.jpg)  
:::

![Figure: Great diagram from GitHub](github-flow.jpg)  

### The process

#### Assumption

**Set up build system to deploy from the master branch**

Your build systems should always deploy from master, and should automatically deploy on every commit to master.  
Since master is always being deployed, it must always be in a deployable state.

### Step 1 - Create a branch

**a) Create a "feature branch" for every PBI**

When starting a PBI from the task board, create a branch from **master** with a descriptive name for that feature.

```console
git branch start-stuff
```

::: bad  
Figure: Bad example - Branch name is not descriptive
:::

```console
git branch create-basic-web-application
```

::: good
Figure: Good example - Branch name describes the intent of the change
:::

**It is critical that this branch always comes off master, not another feature branch. Master is the only branch that is mandated to be in a deployable state, so any other option is unsafe.**

Obviously, we're creating a lot of branches and merging a lot under this strategy - and that's ok.  Be sure to keep your PBIs small (as per [breaking large tasks into smaller tasks](/estimating-do-you-break-large-tasks-into-smaller-tasks)), and you will not have much merge pain.

The benefit of creating feature branches is to reduce the number of conflicts and churn of unfinished code during development of a feature. It allows features to be developed independently of each other and reduces the amount of expensive "pull latest from the server, and rebuild everything" operations, as well as greatly limiting the impact of commits with unfinished code.

**b) Code away and complete the PBI**

**c) Create a commit - it will contain your changed files on your local PC**

While working, commit frequently to this branch with nice, descriptive messages. For example: _"Added a field to hold the product category to our timesheet read model"_ or _"added a column to the timesheet summary UI for the product category"_.

``` console
git commit -m "Started report change"
```

::: bad
Figure: Bad example - Commit message does not describe what was changed
:::

``` console
git commit -m "Added a product category filter to the timesheet summary report UI"
```

::: good  
Figure: Good example - Commit message describes exactly what was changed
:::

**d) Push your changes to your remote Feature Branch**

### Step 2 - Open a pull request (to merge from your current branch to the master)

When the change is complete, or when you want feedback on anything, open a pull request to merge the branch back to **master**. The pull request is more than just a request to merge, it is a request to have someone review the code and architecture, or image and to discuss any issues. Resolve these issues with more commits in the branch before continuing.

**Tip:** A best practice is to have another developer review your work and then approve.

::: greybox
It is easy to chalk this step up as busy-work, but it is one of the most valuable parts of the strategy.
:::

#### Assumption

Deploy the changes to a staging environment.  This allows the features to be tested before being merged to **master**.

Some prefer to move this step to after the merge, especially when using a release management tool like VSTS Release or Octopus Deploy (see [Do you use the best deployment tool](/do-you-use-the-best-deployment-tool)). If you decide to go this route, remember that **master** should remain deployable and production ready at all times and that all branches come from **master**. If skipping this step, ensure that you have CI on your feature branch to ensure that your branch compiles and passes all tests before merging.

### Step 3 - Merge and Deploy (to master)

Once everyone is happy and everything is tested, complete the pull request, which will merge back to **master**. Ensure you are not using the "Fast Forward" merge option (git), or details about the branch will be lost - it will appear as though all work was done in **master**. Being able to see the feature branches in the git log is very useful.

::: good  
![Figure: Good example - Each change is well described, small and in its own feature branch](GoodGitHistory.png)  
:::

After you completed the pull request, make sure you also delete the branch that you made the pull request of. Deleting your completed branch will not just help yourself in the long run, but also everyone else. Having too many branches especially a stale one will confuse developers on what "may" be in progress, moreover it would cause so much pain to the future developer when they have to do a clean-up and the branch author has left.

::: bad
![Figure: Bad example - Lots of stale branches that could cause confusion or potentially take a long time to resolve conflicts when merging](bad-figure-stale-branches2.png)
:::

Otherwise, you can do it before you complete the pull request by ticking delete branch option.

::: good
![Figure: Good example - Automatically delete the branch after the pull request completion in Azure Devops](delete-branch-in-devops.png)
:::

::: good
![Figure: Good example - Set the whole project to auto-delete branch after merging in GitHub](github-settings.png)
:::

::: greybox
Once merged, **master** should immediately and automatically be deployed (in a perfect world, to production).  
:::
