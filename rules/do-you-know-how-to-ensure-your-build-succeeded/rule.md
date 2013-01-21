---
type: rule
archivedreason: 
title: Do you know how to ensure your build succeeded?
guid: 0bc29011-9fd4-46e2-bb2c-77c1d1df725b
uri: do-you-know-how-to-ensure-your-build-succeeded
created: 2013-01-21T17:20:24.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p>When checking code into TFS, a build should be triggered as per the rule <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSourceControlwithTFS.aspx#MinimumBuilds">Do you know the minimum builds to create on any branch?</a></p><p>You should not just trigger a build and walk away however – make sure that build succeeded!</p>
<br><excerpt class='endintro'></excerpt><br>
<p>The first way is from within Visual Studio.</p><dl class="goodImage"><dt><img src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/builds-success-good.jpg" alt="" /></dt><dd>Figure&#58; Good Example – Check your build has passed from Team Explorer | Builds</dd></dl><p>The second is by always having the TFS Build Notification tool always running. Through it you can subscribe to any builds you are interested in, when they start, end and their status.</p><dl class="goodImage"><dt><img src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/builds-success-better.jpg" alt="" /></dt><dd>Figure&#58; Better Example – Check your build(s) are continually passing by having the TFS Build Notification tool always running (Start | All Programs | Visual Studio 2012 | Team Foundation Server Tools | Build Notifications</dd></dl>


