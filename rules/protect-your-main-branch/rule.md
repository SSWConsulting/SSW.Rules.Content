---
type: rule
title: Do you protect your main branch? aka branch protection
uri: protect-your-main-branch
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
  - title: Gordon Beeming
    url: https://www.ssw.com.au/people/gordon-beeming/
  - title: Jernej Kavka
    url: https://ssw.com.au/people/jernej-kavka
related: []
redirects:
  - do-you-protect-your-master-branch
  - protect-your-master-branch
created: 2017-09-12T22:35:37.000Z
archivedreason: null
guid: 93bfec41-6b37-4413-a660-931fffa88d44
---

Branch protection is a feature in version control software that allows teams to define rules and restrictions around who can make changes to specific branches, what types of changes are allowed, and if there are conditions that have to be met.

<!--endintro-->

This can include:

- Number of reviewers
- Linked work items e.g. PBIs (super useful to track back to why the code was changed)
- Any feedback has been addressed/resolved
- Enforcing specific merge types
- Checking that builds pass
- Checking other services e.g. code quality like SonarQube
- Automatically adding specific people to review the code

::: bad  
![Figure: Bad example – No protection – anyone can make unreviewed changes](protect-branch-bad-1.jpg)  
:::

::: good  
![Figure: Good example – The branch protected](protect-branch-good-1.jpg)  
:::
