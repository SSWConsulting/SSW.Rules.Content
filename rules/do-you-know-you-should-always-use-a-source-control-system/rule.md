---
seoDescription: Use a source control system to track and collaborate on code changes, reducing bug introduction and fixing time.
type: rule
title: Do you know you should always use a source control system?
uri: do-you-know-you-should-always-use-a-source-control-system
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related:
  - spec-do-you-use-user-stories
redirects: []
created: 2009-03-17T07:15:10.000Z
archivedreason: null
guid: 0490d3ad-83bc-481b-b611-97a6f001f056
---

You should always use a source control system!

It is not for a backup, it is because changing code can introduce new bugs. Often these bugs are non-obvious and appear in a part of the system, far removed from your changes. They are especially useful when another developer made the breaking change.

<!--endintro-->

So source code tracking allows you to see what changed recently to introduce a new bug. This dramatically reduces the time it takes to find and fix a newly introduced error.

### Integrate your source control with your bug tracking tool

Source control works best when integrated with a task tracking system. SSW uses and recommends Microsoft Team Foundation Server which allows you to check in changes and link to the work item (Bug or Task)... all from within Visual Studio.

**Tip:** If your systems are not integrated automatically, you can still integrate manually by convention. Just quoting the work item or bug ID in comments, whenever a source code change is committed.

Whatever you use, your toolchain/process/IDE should fulfil the following user stories:

::: greybox
**As a developer** working on a code file

**I want to** easily view a file’s change history and navigate to the work items that were associated with the changes

**So that I can** fix a recently introduced bug quickly
:::

::: greybox
**As a senior software developer**

**I want to** browse work items of junior developers, and have it linking/showing the code

**So that I can** easily review their recent code
:::
