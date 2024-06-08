---
type: rule
archivedreason: 
title: Do you do a quick test after the TFS 2015 migration finishes?
guid: e23eb370-ccf0-41a7-b795-b52875370898
uri: do-a-quick-test-after-the-upgrade-finishes-tfs2015-migration
created: 2015-08-14T11:31:19.0000000Z
authors: 
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-do-a-quick-test-after-the-upgrade-finishes1

---

After upgrading TFS, you should do a quick [smoke test](http://en.wikipedia.org/wiki/Smoke_testing) to ensure TFS is running as expected.

<!--endintro-->

![Figure: New TFS Title using our existing url](tfs title.png)

1. Navigate to the web access URL for your new TFS server.
2. If it loads correctly, click "Browse all..." to check all your Team Projects were migrated across correctly

In Visual Studio, connect to TFS, then:

3. Do a Get Latest on a project or file
4. Make a change, and ensure you can Check In
