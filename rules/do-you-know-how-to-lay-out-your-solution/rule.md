---
seoDescription: Know how to lay out your solution structure for a well-organized and maintainable .NET project.
type: rule
archivedreason: Same as https://www.ssw.com.au/rules/do-you-have-a-consistent-net-solution-structure/
title: Do you know how to lay out your solution?
guid: fe6fa29b-60dd-49db-8836-c06ee3ff7ef1
uri: do-you-know-how-to-lay-out-your-solution
created: 2011-11-18T03:52:49.0000000Z
authors:
  - title: Justin King
    url: https://ssw.com.au/people/justin-king
  - title: Tristan Kurniawan
    url: https://ssw.com.au/people/tristan-kurniawan
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
related:
  - do-you-have-a-consistent-net-solution-structure
redirects: []
---

Whenever we setup a new Team Project we implement a basic version control structure. We put "readme.txt" files in the folder structure explaining the different levels, and a solution file called `[Client].[Product].sln?` located at `?/[Client]/[Product]/DEV/` within version control.

<!--endintro-->

::: bad  
![Figure: Bad Example, how would anyone know how to sort this mess out?](MessySolution.jpg)  
:::

::: good  
![Figure: Good Example, The ideal solution.](IdealSolution.jpg)  
:::
