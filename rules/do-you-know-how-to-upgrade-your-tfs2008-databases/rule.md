---
type: rule
archivedreason: 
title: Do you know how to upgrade your TFS2008 databases?
guid: 3edaeb78-d469-41d0-94de-1ba2e848155e
uri: do-you-know-how-to-upgrade-your-tfs2008-databases
created: 2009-11-08T00:23:52.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 3
  title: Eric Phan
related: []

---

Since [we recommend doing a "move based upgrade"](/Pages/MigrationChoices.aspx), we don’t like the "in place upgrade" option, these are the steps:

1. Copy the TFS2008 backups to TFS2010 server (e.g. C:\TfsBackups)
2. Restore all the databases to TFS2010’s instance of SQL 2008
3. Install Team Foundation Server 2010
4. After the install has completed the Team Foundation Server Configuration Wizard will open
5. Select Upgrade | Start Wizard

![](01-TFS Config - Upgrade.png)
6. Click "Next"

![](02-TFS Upgrade Wizard - Upgrade.png)
7. Click "List Available Databases"
8. Select the TfsIntegration database
9. Check "By checking this box, I confirm that I have a current backup"
10. Click "Next"

![](03-TFS Upgrade Wizard - Databases.png)
11. Select "NT AUTHORITY\NETWORK SERVICE" for the System account
12. Click "Next" 

![](04-TFS Upgrade Wizard - Account.png)
13. Click "Next"

![](05-TFS Upgrade Wizard - Application Tier.png)
14. Click "Next"

![](06-TFS Upgrade Wizard - Reporting.png)
15. Click "Next"

![](07-TFS Upgrade Wizard - Reporting - Reporting Services.png)
16. Click "Next"

![](08-TFS Upgrade Wizard - Reporting - Analysis Services.png)
17. Specify the TFSService account
18. Click "Next"

![](09-TFS Upgrade Wizard - Reporting - Report Reader Account.png)
19. Click "Next"

![](10-TFS Upgrade Wizard - Sharepoint.png)
20. Click "Next"

![](11-TFS Upgrade Wizard - Sharepoint - Settings.png)
21. Click "Next"

![](12-TFS Upgrade Wizard - Project Collection.png)
22. Click "Next"

![](13-TFS Upgrade Wizard - Review.png)
23. Click "Configure"

![](14-TFS Upgrade Wizard - Readiness Checks.png)
24. Have coffee (2 hours)

![](ssw-coffee.png)
BTW: A good user interface should have a coffee image 
[TODO: Martin to create new rule in "Rules to better UI"]
[TODO: Martin to add suggestion to TFS]

![](15-TFS Upgrade Wizard - Configure - Upgrade Process.png)
25. Click "Next"

![](16-TFS Upgrade Wizard - Configure - Upgrade Process Success.png)
26. Click "Close"

![](17-TFS Upgrade Wizard - Complete.png)
27. Click "Close"

![](18-TFS Config - Application Server Complete.png)
28. Change the DNS entry for tfs.northwind.com to point to TFS2010 on
    1. Internal DNS
    2. External DNS



| ![](redbull.jpg) | Since you have to deal with your system admins, this job will take the longest. Speed it up by buying a Red Bull for your system admin |
| --- | --- |


<!--endintro-->
