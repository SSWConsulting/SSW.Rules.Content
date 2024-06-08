---
type: rule
archivedreason: No longer relevant. See [https://www.ssw.com.au/rules/rules-to-better-version-control-with-git](/rules/rules-to-better-version-control-with-git)
title: Do You Choose TFS-Git Over Team Foundation Source Control?
guid: 9a1642c8-3164-49b4-bd21-d81a014df14f
uri: do-you-choose-tfs-git-over-team-foundation-source-control
created: 2014-05-22T19:47:49.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []

---

Only a madman would write software today without using source control.

Apart from being the easiest way to back-up your code, and having the ability to go back to a previous state, source control provides a huge number of benefits, especially when integrated with Continuous Integration servers, and Continuous Deployment solutions.

<!--endintro-->

But which source control solution should I choose?

::: bad  
![Figure: Bad Example - Unless you have time-travelled back to 1999, you should not be using Visual Source Safe](git-1.jpg)  
:::

::: bad  
![Figure: Bad Example – Git is great, but learning to use ‘pure’ git from the command line can be intimidating for developers not used to working in a console](git2.jpg)  
:::

::: bad  
![Figure: Bad Example - Team Foundation Source Control – Server Workspaces. This is the source control that we have been using in TFS for years. It’s great, even on large code bases, except for when you are not connected to the TFS server. (Image from        http://bit.ly/why-tfs-git)](git3.jpg)  
:::

::: bad  
![Figure: Bad Example – Team Foundation Source Control – Local Workspaces. It’s great for when you are not connected to the TFS Server, except for when your code-base is very large. (Image from        http://bit.ly/why-tfs-git)](git4.jpg)  
:::

::: good  
![Good Example – TFS Git works fantastically offline and with large code-bases. Visual Studio has support for the basic operations so developers can ease their way into working with git. Once users become familiar with it, it also allows for far more control and flexibility. Note: My Work and Code Review are not currently compatible with TFS Git, and you will need to fall back to the Git command line for more complex source control commands](git5.jpg)  
:::
**Resources:** [Taking your version control to a next level with TFS and Git](http://bit.ly/why-tfs-git)by Alexander Vanwynsberghe.
