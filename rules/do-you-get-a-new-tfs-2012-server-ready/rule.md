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


<ol><li>Prepare a new image. We recommend running <strong>Windows 2008 R2 Server x64 </strong>using Hyper-V Manager. Your options are&#58; <ol><li>Manually build a server </li>
<li>Use a&#160;syspreped image (this will be quicker)</li>
<li>System Center Virtual Machine Manager (recommended, quickest)</li></ol></li>
<li>Add the roles <ol><li>Application Server </li>
<li>IIS</li></ol></li>
<li>Install SQL Server 2012 components for reporting and analysis (on the TFS server) <ol><li>Install (but don't configure) <strong>SQL Server 2012 Reporting Services</strong></li>
<li>Install (but don't configure) <strong>SQL Server 2012 Analysis Services</strong></li></ol></li>
<li>You'll also need a SQL Server instance for the TFS databases if you don't already have one <ol><li>Install <strong>SQL Server 2012 x64</strong> default configuration</li></ol></li></ol>
<br><excerpt class='endintro'></excerpt><br>



