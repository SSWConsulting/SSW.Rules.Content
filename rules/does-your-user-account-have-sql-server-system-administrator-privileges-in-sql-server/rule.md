---
type: rule
title: Does your user account have SQL Server System Administrator privileges in SQL Server?
uri: does-your-user-account-have-sql-server-system-administrator-privileges-in-sql-server
created: 2015-08-12T15:57:43.0000000Z
authors: []

---



<span class='intro'> <p><span style="line-height&#58;20.7999992370605px;">​</span><span style="line-height&#58;20.7999992370605px;">If you're upgrading TFS 2010 to 2012, we recommend that you assign sysadmin privileges to the user account that's doing the upgrade.</span></p> </span>

<p>Some database upgrade steps involve ALTER DATABASE statements and other commands that can't be done by a normal user. If a step fails, you are likely to end up with a corrupted Configuration database (so you have to restore from backup).</p>


