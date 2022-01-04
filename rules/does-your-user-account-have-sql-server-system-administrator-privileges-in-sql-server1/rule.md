---
type: rule
archivedreason: Duplicated of /does-your-user-account-have-sql-server-system-administrator-privileges-in-sql-server
title: Does your user account have SQL Server System Administrator privileges in SQL Server?
guid: 0c942235-1cdb-489a-873b-cae7fdbb0d2d
uri: does-your-user-account-have-sql-server-system-administrator-privileges-in-sql-server1
created: 2015-08-12T15:57:43.0000000Z
authors: []
related: []
redirects:
- does-your-user-account-have-sql-server-system-administrator-privileges-in-sql-server

---

If you're upgrading TFS 2010 to 2012, we recommend that you assign sysadmin privileges to the user account that's doing the upgrade.

<!--endintro-->

Some database upgrade steps involve ALTER DATABASE statements and other commands that can't be done by a normal user. If a step fails, you are likely to end up with a corrupted Configuration database (so you have to restore from backup).
