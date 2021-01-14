---
type: rule
archivedreason: 
title: Do you do a quick test after the upgrade finishes?
guid: e23eb370-ccf0-41a7-b795-b52875370898
uri: do-you-do-a-quick-test-after-the-upgrade-finishes
created: 2015-08-14T11:31:19.0000000Z
authors: []
related: []
redirects:
- do-you-do-a-quick-test-after-the-upgrade-finishes1

---

After upgrading TFS, you should do a quick [smoke test](http://en.wikipedia.org/wiki/Smoke_testing)   to ensure TFS is running as expected.

<!--endintro-->

![](tfs title.png)

**Figure: New TFS Title using our existing url**

a.      Navigate to the web access URL for your new TFS server.

b.     If it loads correctly, click "Browse all..." to check all your Team Projects were migrated across correctly

c.      In Visual Studio, connect to TFS, then:

.                Do a Get Latest on a project or file

Make a change, and ensure you can Check In
