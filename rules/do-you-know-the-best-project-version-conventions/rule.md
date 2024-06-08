---
type: rule
archivedreason: 
title: Do you know the best Project/Version conventions?
guid: 40607b1c-4874-4421-8ea0-4820f19b5ef1
uri: do-you-know-the-best-project-version-conventions
created: 2011-11-18T03:52:36.0000000Z
authors:
- title: David Klein
  url: https://ssw.com.au/people/david-klein
  noimage: true
- title: Justin King
  url: https://ssw.com.au/people/justin-king
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
  noimage: true
- title: Tristan Kurniawan
  url: https://ssw.com.au/people/tristan-kurniawan
related: []
redirects: []

---

Having a good folder structure in version control allows everyone to know where everything is without even having to look.

<!--endintro-->

::: greybox
/northwind
 /trunk
 /branches (or shelvesets)
  /experiemental-feature1
 /releases (or tags)
  /1.0.0.356
:::
::: bad
Figure: Bad example - SVN conventions are a dated and ignore releases, hotfixes and Service Packs  
:::

Trunk is the old way, Main is the new way as per the branching guidance, and it is the way that Microsoft does things.

::: good
![Figure: Good example - This makes a lot more sense](BranchGuidance.jpg)
:::

**More Information:**

![Figure: A good format for all your Products/Projects makes it easy to know where things are and what they are for](GoodFormatForInfo.jpg)
