---
type: rule
archivedreason: 
title: Do you know how to lay out your solution?
guid: fe6fa29b-60dd-49db-8836-c06ee3ff7ef1
uri: do-you-know-how-to-lay-out-your-solution
created: 2011-11-18T03:52:49.0000000Z
authors:
- title: Justin King
  url: /people/justin-king
- title: Tristan Kurniawan
  url: /people/tristan-kurniawan
- title: Adam Stephensen
  url: /people/adam-stephensen
related: []
redirects: []

---

Whenever we setup a new Team Project we implement a basic version control structure. We put "readme.txt" files in the folder structure explaining the different levels, and a solution file called [Client].[Product].sln?located at ?/[Client]/[Product]/DEV/ within version control.


::: bad  
![Figure: Bad Example, how would anyone know how to sort this mess out?](MessySolution.jpg)  
:::

<!--endintro-->


::: good  
![Figure: Good Example, The ideal solution.](IdealSolution.jpg)  
:::

For more implementation details see:     
[http://blog.hinshelwood.com/archive/2010/05/17/guidance-how-to-layout-you-files-for-an-ideal-solution.aspx](http://www.ssw.com.au/ssw/redirect/LayoutSolution.htm)

### Related rule

* [Do you have a consistent .NET Solution Structure?](/do-you-have-a-consistent-net-solution-structure)
