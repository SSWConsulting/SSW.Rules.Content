---
type: rule
archivedreason: 
title: Do you know how to upgrade your TFS2008 databases?
guid: 3edaeb78-d469-41d0-94de-1ba2e848155e
uri: do-you-know-how-to-upgrade-your-tfs2008-databases
created: 2009-11-08T00:23:52.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
related: []
redirects: []

---

Since [we recommend doing a "move based upgrade"](/Pages/MigrationChoices.aspx), we don’t like the "in place upgrade" option, these are the steps:

1. Copy the TFS2008 backups to TFS2010 server (e.g. C:\TfsBackups)
2. Restore all the databases to TFS2010’s instance of SQL 2008
3. Install Team Foundation Server 2010
4. After the install has completed the Team Foundation Server Configuration Wizard will open
5. Select Upgrade | Start Wizard
![TFS Config - Upgrade](01-TFS Config - Upgrade.png)
6. Click "Next"
![](02-TFS Upgrade Wizard - Upgrade.png)
7. Click "List Available Databases"
8. Select the TfsIntegration database
9. Check "By checking this box, I confirm that I have a current backup"
10. Click "Next"
![](03-TFS Upgrade Wizard - Databases.png)
11. Select "NT AUTHORITY\NETWORK SERVICE" for the System account
12. Click "Next" 
![TFS Upgrade Wizard - Account](04-TFS Upgrade Wizard - Account.png)
13. Click "Next"
![TFS Upgrade Wizard - Application Tier](05-TFS Upgrade Wizard - Application Tier.png)
14. Click "Next"
![TFS Upgrade Wizard - Reporting](06-TFS Upgrade Wizard - Reporting.png)
15. Click "Next"
![TFS Upgrade Wizard - Reporting - Reporting Services](07-TFS Upgrade Wizard - Reporting - Reporting Services.png)
16. Click "Next"
![TFS Upgrade Wizard - Reporting - Analysis Services](08-TFS Upgrade Wizard - Reporting - Analysis Services.png)
17. Specify the TFSService account
18. Click "Next"
![TFS Upgrade Wizard - Reporting - Report Reader Account](09-TFS Upgrade Wizard - Reporting - Report Reader Account.png)
19. Click "Next"
![TFS Upgrade Wizard - Sharepoint](10-TFS Upgrade Wizard - Sharepoint.png)
20. Click "Next"
![TFS Upgrade Wizard - Sharepoint - Settings](11-TFS Upgrade Wizard - Sharepoint - Settings.png)
21. Click "Next"
![TFS Upgrade Wizard - Project Collection](12-TFS Upgrade Wizard - Project Collection.png)
22. Click "Next"
![TFS Upgrade Wizard - Review](13-TFS Upgrade Wizard - Review.png)
23. Click "Configure"
![TFS Upgrade Wizard - Readiness Checks](14-TFS Upgrade Wizard - Readiness Checks.png)
24. Have coffee (2 hours)
![Coffee](ssw-coffee.png)
BTW: A good user interface should have a coffee image 
[TODO: Martin to create new rule in "Rules to better UI"]
[TODO: Martin to add suggestion to TFS]
![TFS Upgrade Wizard - Configure - Upgrade Process](15-TFS Upgrade Wizard - Configure - Upgrade Process.png)
25. Click "Next"
![TFS Upgrade Wizard - Configure - Upgrade Process Success](16-TFS Upgrade Wizard - Configure - Upgrade Process Success.png)
26. Click "Close"
![TFS Upgrade Wizard - Complete](17-TFS Upgrade Wizard - Complete.png)
27. Click "Close"
![TFS Config - Application Server Complete](18-TFS Config - Application Server Complete.png)
28. Change the DNS entry for tfs.northwind.com to point to TFS2010 on
    1. Internal DNS
    2. External DNS



| ![Red Bull Can](redbull.jpg) | Since you have to deal with your system admins, this job will take the longest. Speed it up by buying a Red Bull for your system admin |
| --- | --- |


<!--endintro-->
