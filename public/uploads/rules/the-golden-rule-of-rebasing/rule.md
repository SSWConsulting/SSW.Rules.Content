---
seoDescription: Never rebase master onto a feature branch to avoid confusing project history and ensuring clean collaboration.
type: rule
archivedreason:
title: Do you know The Golden Rule of Rebasing?
guid: 9302157e-0ca6-48d3-9f59-46af0c035b9c
uri: the-golden-rule-of-rebasing
created: 2016-02-15T20:11:38.0000000Z
authors:
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
related: []
redirects:
  - do-you-know-the-golden-rule-of-rebasing
---

Rebasing is great for ensuring a clean project history... but it can be dangerous in inexperienced hands.

<!--endintro-->

**The golden rule of git rebase is to never use it on public branches.** (ie. never rebase master).

You should never rebase master onto a feature branch. This would move all of the commits in master onto the tip of the feature branch (not the other way around).

Since rebasing results in brand new commits, Git will think that your master branch’s history has diverged from everybody else’s. If you were to Push this to the server... [expect lots of pain to fix it up](https://www.atlassian.com/git/tutorials/merging-vs-rebasing/the-golden-rule-of-rebasing)!

::: bad  
![Figure: Bad Example: Rebasing master onto a feature branch can cause project history to become confused.](rebase3.png)  
:::

![Figure: To get it wrong in Visual Studio you would need to change the current branch to master and then choose rebase. While this is possible, the VS team have done a good job making it hard to do the wrong thing](rebase4.png)

::: good  
![Figure: Good Example - Rebase your Feature branch onto Master](rebase5.png)  
:::
