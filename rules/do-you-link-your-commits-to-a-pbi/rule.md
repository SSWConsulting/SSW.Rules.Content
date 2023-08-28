---
type: rule
archivedreason: 
title: Do you link your commits to a PBI?
guid: 0e206ce8-deed-4b09-902d-ecec0499586b
uri: do-you-link-your-commits-to-a-pbi
created: 2019-03-13T01:00:33.0000000Z
authors:
- title: Adam Cogan
  url: /people/adam-cogan
- title: Andreas Lengkeek
  url: /people/andreas-lengkeek
- title: Barry Sanders
  url: /people/barry-sanders
- title: Jernej Kavka
  url: /people/jernej-kavka
- title: Patricia Barros
  url: /people/patricia-barros
related: []
redirects: []

---

In order to get better clarity on what work is done, it's a good idea to connect your PBI's and tasks to the commits, branches and pull requests that relate to the item. All commits, branches and pull requests should be linked to a PBI.


::: bad  
![Bad Example: No linked commit's, branches or pull requests](no-linked-commit.png)  
:::


::: good  
![Good Example: Git branch linked to PBI in TFS](link-branch-to-pbi.png)  
:::

<!--endintro-->

Note: If you create your branches through Azure DevOps then you can link them during creation.


::: good  
![Good Example: Using Azure DevOps to link PBI during creation](link-pbi-during-creation.png)  
:::

Here is a handy resource for linking work items:

https://devblogs.microsoft.com/devops/linking-work-items-to-git-branches-commits-and-pull-requests/

Note: You can setup Branch Policies on your main branches to enforce this behaviour.


::: good  
![Good Example: Branch Policy on the master branch to enforce linked work items on pull requests](add-branch-policy-for-linked-items.png)  
:::
