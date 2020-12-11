---
type: rule
archivedreason: 
title: Do you lock the SharePoint Content Database before making a backup?
guid: 8dad04d4-ba19-4338-b35a-4eaad6b34fbc
uri: do-you-lock-the-sharepoint-content-database-before-making-a-backup
created: 2010-12-23T06:55:11.0000000Z
authors:
- id: 36
  title: Daniel Šmon
- id: 9
  title: William Yin
- id: 21
  title: Matthew Hodgkins
related: []

---

Even though you have advised staff members a migration is taking place – you can guarantee someone will try to check-in or edit documents. The best way to prevent this is to put your content database into read-only mode, locking the content database.
<!--endintro-->

There are two options to lock the content database.

Option 1 ( **Recommended** ):

1.  Open  **SharePoint Central Administration** site, navigate to "**Application Management** " | "**Site Collections** " | " **Configure quotas and locks** ".
<dl class="ssw15-rteElement-ImageArea">   <img src="quotas-and-locks.jpg" alt="quotas-and-locks.jpg" data-pin-nopin="true" style="width:800px;"></dl>
2. Select the "site collection" which you would like to lock.

3. Choose "Read-only (blocks additions, updates, and deletions)", then click "OK".
<dl class="ssw15-rteElement-ImageArea">   <img src="read-only-status.jpg" alt="read-only-status.jpg">
<dd>Note: Read more at <a href="https://technet.microsoft.com/en-us/library/cc263238%28v=office.15%29.aspx?f=255&MSPPError=-2147217396">Manage the lock status for site collections in SharePoint 2013</a></dd></dl>
Option 2 ( **not recommended** ):

1.    On your database server open      **SQL Server Management Studio**

2.    Right click on the content database associated with the site collection you're migrating | **Properties**

3.    Choose      **Options** | Scroll to the bottom of the options list

4.    For the      **Database Read-Only** choose True
<dl class="image">&lt;dt&gt;
      <img src="LocLSQLDB.jpg" alt="">
   &lt;/dt&gt;<dd>Figure - Database Properties | Options | Database-Read Only</dd></dl>
5.    Now it’s safe to take a backup of your content database

**NOTE:** When some SharePoint timer services are run it may cause the site to display errors when the database is in read-only mode
