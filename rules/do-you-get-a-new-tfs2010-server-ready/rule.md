---
type: rule
archivedreason: 
title: Do you get a new TFS2010 Server ready?
guid: 682d55b3-af4d-439b-94ae-fdd57cef0eef
uri: do-you-get-a-new-tfs2010-server-ready
created: 2009-11-02T23:10:40.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 3
  title: Eric Phan
related: []

---

1. Prepare a new image. We recommend running  **Windows 2008 R2 Server x64**using Hyper-V Manager. Your options are:
    1. Manually build a server
    2. A syspreped image (this will be quicker)
    3. System Center Virtual Machine Manager (recommended, quickest)
2. Add the roles
    1. Application Server
    2. IIS
3. Install  **SQL Server 2008 x64** default configuration
4. Install  **SQL Server 2008 SP1**
5. Run [www.ssw.com.au/ssw/Diagnostics/](http&#58;//www.ssw.com.au/ssw/Diagnostics/) and get all green ticks


<!--endintro-->
