---
type: rule
archivedreason: 
title: Export Method - Do you know how to export the solution if you don’t have the original installer or source code? (optional)
guid: 82c0d0bb-4774-4244-9022-3d835cf79b95
uri: export-method---do-you-know-how-to-export-the-solution-if-you-dont-have-the-original-installer-or-source-code-optional
created: 2010-12-23T03:04:11.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 21
  title: Matthew Hodgkins
- id: 9
  title: William Yin
related: []

---

(Not recommended)
 In unusual cases where you don’t have source code (for your own customizations) or the setup files (from 3rd party vendor) of the SharePoint solutions that have been deployed in the SharePoint 2007 server, there is a way to export the solution files.

1. Download  **Solution Exporter** from [Mark Wagner's Cogitation Blog](http&#58;//blog.crsw.com/2007/11/01/how-to-create-a-sharepoint-solution-for-an-infopath-form/) and run it on the SharePoint 2007 server. This allows you to export the installed solutions from the source SharePoint server.
2. Export all of the solutions out of the SharePoint farm.
3. Copy the  **C:\SharePointCustomizations** folder to the destination SharePoint 2010 server.




<!--endintro-->
