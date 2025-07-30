---
seoDescription: Create a comprehensive SQL Server maintenance plan that includes database integrity checks, shrinking, reorganizing and rebuilding indexes, updating statistics, cleaning up old history, automatic backups, system database backups, and regular check-ins for successful execution.
type: rule
archivedreason:
title: Backup - Do you set up a complete Maintenance Plan?
guid: 74d963fc-ec96-4be6-84af-c0e12905d1b1
uri: setup-a-complete-maintenance-plan
created: 2019-11-20T18:33:22.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - backup-do-you-set-up-a-complete-maintenance-plan
---

It is surprising how many IT staff create backup plans and then leave it at that. To have a complete maintenance plan, you should also consider the following:

1. Checking database integrity
2. Shrinking Databases
3. Reorganizing Indexes
4. Rebuilding Indexes
5. Updating Statistics
6. Cleaning up old maintenance histories
7. Performing automatic backups
8. Backing up System databases
9. Last but not least - you should regularly check that the maintenance plans have been running successfully. Otherwise, all your backup and maintenance efforts are pointless

<!--endintro-->

This can be found under **Management | Maintenance Plans** within the database tee in SQL Server.

![Figure: SQL Server - A Complete Weekly Maintenance Plan](SqlMaintenancePlan.png)
