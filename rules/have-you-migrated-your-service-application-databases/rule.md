---
type: rule
archivedreason: 
title: Have you migrated your service application databases
guid: c7079a95-c46a-46f0-b737-37a3aa44b164
uri: have-you-migrated-your-service-application-databases
created: 2013-04-26T00:12:43.0000000Z
authors:
- id: 28
  title: Daragh Bannigan
- id: 9
  title: William Yin
related: []

---

Depends on your SharePoint farm environments, you may need to upgrade some service applications databases.


<!--endintro-->

In our case, we have upgraded the below several service application databases:

* Secure Store
* User Profiles
* Managed Metadata
* Business Connectivity Services


Steps:

1. Backup databases of SharePoint 2010 or 2013 Service Application.

2. Restore and attach databases to SharePoint 2013 or 2016 SQL server.

3. Create service application in SharePoint 2013 or 2016 Central Admin site with the restored database.

4. Test.

5. Done.
