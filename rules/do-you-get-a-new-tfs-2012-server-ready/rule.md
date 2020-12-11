---
type: rule
archivedreason: 
title: Do you get a new TFS 2012 Server ready?
guid: 40f7b3c9-03f1-48b4-8a5a-548e7cdb5b1b
uri: do-you-get-a-new-tfs-2012-server-ready
created: 2012-06-02T01:36:32.0000000Z
authors:
- id: 23
  title: Damian Brady
related: []

---

1. Prepare a new image. We recommend running  **Windows 2008 R2 Server x64**using Hyper-V Manager. Your options are:
    1. Manually build a server
    2. Use a syspreped image (this will be quicker)
    3. System Center Virtual Machine Manager (recommended, quickest)
2. Add the roles
    1. Application Server
    2. IIS
3. Install SQL Server 2012 components for reporting and analysis (on the TFS server)
    1. Install (but don't configure)  **SQL Server 2012 Reporting Services**
    2. Install (but don't configure)  **SQL Server 2012 Analysis Services**
4. You'll also need a SQL Server instance for the TFS databases if you don't already have one
    1. Install  **SQL Server 2012 x64** default configuration


<!--endintro-->
