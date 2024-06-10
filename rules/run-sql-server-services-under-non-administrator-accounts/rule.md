---
seoDescription: Run SQL Server services under non-Administrator accounts to ensure security and prevent unauthorized access.
type: rule
archivedreason:
title: ​DBAs - Do you run SQL Server Services under non-Administrator accounts?
guid: 315c44af-d43f-4880-9b9a-6bcafab9ed00
uri: run-sql-server-services-under-non-administrator-accounts
created: 2019-11-18T23:40:32.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - dbas-do-you-run-sql-server-services-under-non-administrator-accounts
---

You should always run all SQL Server services with the lowest possible privileges allowed in case the account is compromised. SQL Server setup makes the whole process of granting privileges a whole lot easier because it automatically creates groups with all the necessary permissions for you!

<!--endintro-->

![Figure: SQL Server now creates groups for all the SQL Server services with the bare minimum permissions for you](SQLDatabases_RunAsAccount_GroupsCreated.png)

If you are running any SQL Server Service in a user account that has administrator privileges a user that compromises the account could do anything that administrator could do - including playing around with the registry with procedures like xp_regdeletevalue. So, if you use an Administrator account, you're in effect giving away the keys to the house. Is this something you want to do?
