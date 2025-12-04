---
seoDescription: Learn how to lock your SharePoint Content Database before making a backup and prevent unwanted edits or check-ins during migration.
type: rule
archivedreason:
title: Do you lock the SharePoint Content Database before making a backup?
guid: 8dad04d4-ba19-4338-b35a-4eaad6b34fbc
uri: do-you-lock-the-sharepoint-content-database-before-making-a-backup
created: 2010-12-23T06:55:11.0000000Z
authors:
  - title: Daniel Šmon
    url: https://ssw.com.au/people/daniel-smon
    img: https://github.com/SSWConsulting/SSW.People.Profiles/raw/main/Daniel-Smon/Images/Daniel-Smon-Profile.jpg
  - title: William Yin
    url: https://ssw.com.au/people/william-yin
  - title: Matthew Hodgkins
    url: https://ssw.com.au/people/matthew-hodgkins
related: []
redirects: []
---

Even though you have advised staff members a migration is taking place – you can guarantee someone will try to check-in or edit documents. The best way to prevent this is to put your content database into read-only mode, locking the content database.

<!--endintro-->

There are two options to lock the content database.

Option 1 ( **Recommended** ):

1. Open **SharePoint Central Administration** site, navigate to "**Application Management** " | "**Site Collections** " | " **Configure quotas and locks** ".
    ![](quotas-and-locks.jpg)
2. Select the "site collection" which you would like to lock.

3. Choose "Read-only (blocks additions, updates, and deletions)", then click "OK".
    ![](read-only-status.jpg) Note: Read more at [Manage the lock status for site collections in SharePoint 2013](https://technet.microsoft.com/en-us/library/cc263238%28v=office.15%29.aspx?f=255&MSPPError=-2147217396&WT.mc_id=DP-MVP-33518)
    Option 2 ( **not recommended** ):

4. On your database server open **SQL Server Management Studio**

5. Right click on the content database associated with the site collection you're migrating | **Properties**

6. Choose **Options** | Scroll to the bottom of the options list

7. For the **Database Read-Only** choose True

![Figure - Database Properties | Options | Database-Read Only](LocLSQLDB.jpg)

5. Now it’s safe to take a backup of your content database

**NOTE:** When some SharePoint timer services are run it may cause the site to display errors when the database is in read-only mode
