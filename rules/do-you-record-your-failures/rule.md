---
seoDescription: Recording every attempt, even if it doesn't yield the desired results, helps prove R&D efforts and provides valuable experimentation history.
type: rule
archivedreason:
title: Do you document your failures for R&D?
guid: 1de870f1-0278-4c11-8a25-8ec13bf8bdad
uri: do-you-record-your-failures
created: 2019-03-13T04:50:25.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Andreas Lengkeek
    url: https://ssw.com.au/people/andreas-lengkeek
  - title: Barry Sanders
    url: https://ssw.com.au/people/barry-sanders
  - title: Jernej Kavka
    url: https://ssw.com.au/people/jernej-kavka
  - title: Patricia Barros
    url: https://ssw.com.au/people/patricia-barros
related:
  - do-you-know-how-painful-rd-is
  - do-you-record-your-research-under-the-pbi
redirects: []
---

Australian R&D laws require you to show the separate attempts you make when developing a feature that counts towards R&D.

For this reason, you should make sure to commit in between **every attempt** you make even if it does not have the desired affect to record the history of experimentation.

<!--endintro-->

## Example scenario

A developer is improving load times while migrating an MVC app to Angular. They create a new feature branch and begin development on their local machine.

Once they are done the developer commits all the changes they made and push it the remote repository. Using this method, the developer loses the history of experimentation and it will be difficult to prove for R&D.

::: bad
![Figure: Bad example - Only the final solution is committed. Experimentation history not recorded](single-commit-not-showing-experimentation-2.png)
:::

For the same scenario the developer makes sure to commit every separate attempt to reduce load times for their web application. This way, everybody knows what kinds of experimentation was done to solve this problem.

::: good
![Figure: Good example - Each attempt has a new commit and is not lost when retrieving history](commit-failed-experiments.png)
:::

## Save failed experiments using abandoned pull requests

Assume you are creating a cool new feature. First you will create a new branch, create some commits, check it works, and submit a pull request. However, if you are not happy with the feature then don’t just delete the branch as normal. Instead, create a pull request anyway and set the status to Abandoned. Now, you can continue to delete your branch as normal.

This makes sure that we have a historical log of work completed, and still keeps a clean repository.

::: good
![Figure: Good example - Setup pull request for feature branch so that we have a history of the commits](create-pr-for-failed-branch.png)
:::

::: good
![Figure: Good example - PR is abandoned with a deleted branch](abandoned-pr-for-branch.png)
:::
