---
type: rule
title: Do you limit who gets admin access to repositories?
uri: limit-admin-access
authors:
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
  - title: Brady Stroud
    url: https://www.github.com/bradystroud
related:
  - use-teams
redirects: []
created: 2021-03-08T15:13:00.000Z
archivedreason: null
guid: 4e1f6b92-6549-49f6-bddb-0228707bc316
---
Increasing a member's permissions also increases the amount of damage they can do. As a good rule of thumb, only give members the access that they need to complete their work. 
e.g. You do not want developers to have force-push permissions on the main branch, as they might accidentally delete branches and code by mistake!

::: greybox
💡 Tip: GitHub has a role called "Maintainer" which is like an Admin but without the destructive powers
:::

::: greybox
⚠️ Note: If you are still using Azure DevOps, force-push permissions into a repo is only allowed for Project Administrators, so pick your administrators well.
:::

See GitHub docs [Repository permission levels for an organization](https://docs.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization)

::: bad
![Bad Example: All members are Admins](tooManyAdmins.png)
:::

::: good
![Good Example: Most users have push access, some can maintain the repo](notManyAdmins.png)
:::