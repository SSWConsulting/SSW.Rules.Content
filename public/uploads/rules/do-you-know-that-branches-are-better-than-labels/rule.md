---
seoDescription: Discover how branches can provide a more reliable and immutable versioning system compared to labels, ensuring absolute certainty of changes and making it easier to track and manage source code.
type: rule
archivedreason:
title: Do you know that branches are better than Labels?
guid: 6acdf85a-d7d9-4030-b44f-fda34bdc2682
uri: do-you-know-that-branches-are-better-than-labels
created: 2011-11-18T03:52:47.0000000Z
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
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []
---

Although labels are useful they can be changed after they have been created with no way to tell that they have been changed.

<!--endintro-->

::: bad  
![Figure: Bad example, labels can be edited after the fact (they are mutable)](TFSLabel.png)  
:::

::: good  
![Figure: Good example, branches give absolute certainty of versions (they are immutable)](tfslabe2.jpg)  
:::

**Fact #1** : Creating a branch of 1GB of source code does not increase the size of your database by 1GB. It just adds a bunch of pointers. Only the differences are actually stored.
**Fact #2** : When you delete a branch it is not really “deleted”, you are just ending the history. You can undelete at a later time.

**Tip** : Find deleted items by ticking “Tools | Options | Source Control | Visual Studio Team Foundation Server | Show deleted items in the Source Control Explorer”
