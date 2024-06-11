---
seoDescription: SharePoint 2010 migration experts guide you through restoring your content database, ensuring a seamless transition from SharePoint 2007.
type: rule
title: Do you know how to restore your content database to SharePoint 2010?
uri: do-you-know-how-to-restore-your-content-database-to-sharepoint-2010
authors:
  - title: Matthew Hodgkins
    url: https://ssw.com.au/people/matthew-hodgkins
related: []
redirects: []
created: 2010-12-23T07:23:48.000Z
archivedreason: null
guid: ae0f46a9-3029-4d8d-b206-e7841812cd78
---

This is the meat of the migration process. First we need to detach the current content database from the Web Application:

1. On the SharePoint 2010 server, open **SharePoint Central Administration | Application Management | Manage Content Databases**
2. Set the **Database Status** to **offline** | tick **Remove content database**
3. Open **SQL Server Management Studio** and delete the database you just removed from the web application

Now we need to attach the database backup we took of our SharePoint 2007 server:

<!--endintro-->

1. In **SQL Server Management Studio** right click on **Databases | Restore Database...**

![Figure: Select “Restore Database](RestoreDatabase.png)

- Follow the prompts to restore your database

2. Take the database out of read only mode (it will be in read only mode because we backed it up in read only mode)

Now we need to attach the content database to the web application:

1. Open up the **SharePoint 2010 Management Shell** with administrative permissions.
2. Run the following command to attach the database to the web application (replacing the red text to match your environment)

```shell
stsadm –o addcontentdb –url http://sp2010rc/ –databaseserver <DatabaseServerName> –databasename <ContentDatabaseName>
```

3. After the database has been restored you will get a status message telling you how the upgrade went, with the path to a log file. Send this file to the SharePoint developers to determine if any issues occurred during the migration
