---
type: rule
archivedreason: 
title: Do you have a rollback plan?
guid: f7bc73a3-32c9-450a-9eb4-ac056e93f7bb
uri: do-you-have-a-rollback-plan1
created: 2015-08-12T15:35:42.0000000Z
authors: []
related: []
redirects:
- do-you-have-a-rollback-plan

---

Always [plan for a catastrophic disaster](http&#58;//www.ssw.com.au/SSW/Standards/Rules/RulesToBetterNetworks.aspx#assumeCatastrophic). This means backing up your environment, and making sure you have a working plan to recover from that backup should you need to.

<!--endintro-->

If you are doing an in-place upgrade and need to roll back, we'd advise using the TFS upgrade wizard, or the TFS Administration Console to create a backup of your project collections. You can find instructions over on MSDN in the article [Back up and restore TFS](https&#58;//msdn.microsoft.com/en-us/library/bb552295.aspx).

If you are running in a virtual environment, you can also use server snapshots to back up your TFS system. This is only a viable option if your TFS installation contains everything on a single server (including SQL), and you shut down the server before taking a snapshot. It is not sufficient to create a regular SQL database backup and snapshot the server!

Ideally, you should test your rollback plan to make sure that you can recover successfully. The easiest way to do this is to recover to an isolated virtual environment.
