---
type: rule
archivedreason: 
title: Do you setup SharePoint backups in the correct order?
guid: bd877a4f-5a2c-46e0-95db-07d432c0ab07
uri: do-you-setup-sharepoint-backups-in-the-correct-order
created: 2011-06-15T00:50:23.0000000Z
authors:
- title: Matthew Hodgkins
  url: https://ssw.com.au/people/matthew-hodgkins
related: []
redirects: []

---

DPM is great for backing up SharePoint data, but when you select to back up the SharePoint role of a server, DPM will only backup the SharePoint\_Config database and the content databases, which is less than ideal.   
<!--endintro-->
 To back up the SharePoint Server properly in DPM: 




1. Create a new Protection Group, for our example we will call it  **SharePoint Protection**
2. In the new Protection Group, add protection for the for the SharePoint role on your SharePoint server:

![Notice that SharePoint protection only selects the SharePoint_Config and Content databases.](dpm-spcorrectorder-1.png)
**Notice that SharePoint protection only selects the SharePoint\_Config and Content databases.**
3. Now browse to the SQL Server and add the entire SharePoint SQL Instance to the  **SharePoint Protection** group. You will notice that you are unable to select some of the databases, as they are already being protected by SharePoint role protection.

![Ensure you back up the remaining databases in the SharePoint SQL Instance](dpm-spcorrectorder-2.png)
**Ensure you back up the remaining databases in the SharePoint SQL Instance**



After following these steps you will have full protection of your SharePoint databases.
