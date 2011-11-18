---
type: rule
archivedreason: 
title: Do you know that branches are better than Labels?
guid: 6acdf85a-d7d9-4030-b44f-fda34bdc2682
uri: do-you-know-that-branches-are-better-than-labels
created: 2011-11-18T03:52:47.0000000Z
authors:
- id: 22
  title: David Klein
- id: 5
  title: Justin King
- id: 17
  title: Ryan Tee
- id: 6
  title: Tristan Kurniawan
- id: 23
  title: Damian Brady
- id: 24
  title: Adam Stephensen
related: []

---


<p>Although labels are useful they can be changed after they have been created with no way to tell that they have been changed. </p>
<br><excerpt class='endintro'></excerpt><br>
<dl><dt><img border="0" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/tfslabel.jpg" width="610" height="413" alt="" /></dt>
<dd>Figure&#58; Bad example, labels can be edited after the fact (they are mutable)</dd></dl>
<dl><dt><img border="0" src="/Management/RulesToBetterBranchingAndBuilds/PublishingImages/tfslabe2.jpg" alt="" /></dt>
<dd>Figure&#58; Good example, branches give absolute certainty of versions (they are immutable)</dd></dl>
<p><b>Fact #1</b>&#58; Creating a branch of 1GB of source code does not increase the size of your database by 1GB. It just adds a bunch of pointers. Only the differences are actually stored. <br><b>Fact #2</b>&#58; When you delete a branch it is not really “deleted”, you are just ending the history. You can undelete at a later time. </p>
<p><b>Tip</b>&#58; Find deleted items by ticking “Tools | Options | Source Control | Visual Studio Team Foundation Server | Show deleted items in the Source Control Explorer”</p>


