---
type: rule
archivedreason: 
title: Do you know how to ensure your build succeeded?
guid: 0bc29011-9fd4-46e2-bb2c-77c1d1df725b
uri: do-you-know-how-to-ensure-your-build-succeeded
created: 2013-01-21T17:20:24.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

When checking code into TFS, a build should be triggered as per the rule [Do you know the minimum builds to create on any branch?](http://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterVersionControlwithTFS%28AKASourceControl%29.aspx#MinimumBuilds)

You should not just trigger a build and walk away however – make sure that build succeeded!

<!--endintro-->

The first way is from within Visual Studio.


::: good  
![Figure: Good Example – Check your build has passed from Team Explorer | Builds](builds-success-good.jpg)  
:::

The second is by always having the TFS Build Notification tool always running. Through it you can subscribe to any builds you are interested in, when they start, end and their status.


::: good  
![Figure: Better Example – Check your build(s) are continually passing by having the TFS Build Notification tool always running - Start | All Programs | Visual Studio 2012 | Team Foundation Server Tools | Build Notifications](builds-success-better.jpg)  
:::
