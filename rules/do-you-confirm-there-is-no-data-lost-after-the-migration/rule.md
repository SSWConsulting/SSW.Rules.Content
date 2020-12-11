---
type: rule
archivedreason: 
title: Do you confirm there is no data lost after the migration
guid: 53c410b0-8215-4f20-9870-4484f3408f7c
uri: do-you-confirm-there-is-no-data-lost-after-the-migration
created: 2010-12-23T07:18:06.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins
related: []

---

After you have finished migrating the database, it is extremely important to verify that no data has been lost in the move. The quickest way to do this is to compare the SharePoint 2007 and the SharePoint 2010 server  **All Site Content** pages and confirm that the item numbers match:


![](AllSiteContentCount.png)

**Figure 7 – In the "All Site Content" pages library, ensure the ‘item’ numbers exactly match between SharePoint 2007 and SharePoint 2010**

1. Look at your report from the SharePoint 2007 server
2. On the SharePoint 2010 server, open the site collection you just migrated to
3. Select  **Site Actions | Site Settings**
4. Select  **All Site Content**
5. Compare item numbers with 2007


Repeat this process for all sub-sites of the site collection you migrated.

<!--endintro-->
