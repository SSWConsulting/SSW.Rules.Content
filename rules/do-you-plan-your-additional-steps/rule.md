---
type: rule
archivedreason: 
title: Do you plan your additional steps?
guid: 4409b758-c749-4129-8d24-6e7ac06e6217
uri: do-you-plan-your-additional-steps
created: 2012-06-02T01:36:29.0000000Z
authors:
- id: 23
  title: Damian Brady
related: []

---

More steps will be required to integrate your SharePoint site and set up your Build servers. 
<!--endintro-->

After a TFS upgrade, you'll need to make sure your other servers are still integrated properly.

1. Check your Build servers. You'll need to upgrade the TFS installation on them and make sure they're set up correctly.
2. Check your SharePoint servers.  You'll need to install the latest SharePoint Extensions and make sure you repair your SharePoint connections in the Configuration Manager of your TFS Server

![](sharepoint_repair.png)
