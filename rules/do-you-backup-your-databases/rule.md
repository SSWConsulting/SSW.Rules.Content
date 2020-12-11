---
type: rule
archivedreason: 
title: Do you backup your databases?
guid: 51ffe26f-c0cf-418e-be78-e7e742be6e99
uri: do-you-backup-your-databases
created: 2009-11-07T23:06:18.0000000Z
authors: []
related: []

---

Run your daily backups to provide a safety net should things go wrong.

1. Confirm that the TFS2008 databases were backed up last night. 
a. TfsActivityLogging
b. TfsBuild
c. TfsIntegration
d. TfsVersionControl
e. TfsWarehouse 
f. TfsWorkItemTracking
g. TfsWorkItemTrackingAttachments
 **Figure: If you can’t see the physical .bak file for all these, chase up your DBA**
2. Create a backup of the TFS2008 databases by running your Daily Backup maintenance plan on TFS2008 

![Before starting, kick off the daily backups](RunDailyBackup.png)



<!--endintro-->
