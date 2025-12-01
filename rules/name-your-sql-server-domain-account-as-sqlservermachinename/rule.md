---
seoDescription: SQL Server domain account best practices suggest naming it after the machine name to easily identify file updates.
type: rule
archivedreason:
title: ​DBAs - Do you name your SQL Server Domain Account as 'SQLServerMachineName' so it is easily identified when performing network operations?
guid: 8656c69b-74d5-4de0-976f-2369e68eaa88
uri: name-your-sql-server-domain-account-as-sqlservermachinename
created: 2019-11-18T23:37:45.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - dbas-do-you-name-your-sql-server-domain-account-as-sqlservermachinename-so-it-is-easily-identified-when-performing-network-operations
---

When you create the domain accounts under which SQL Server services run, you should name this domain account as "SQLServerMachineName".

E.g. **SSW2000\SQLServerDragon**

If one of the SQL Server services updates a file on the network, then you can then determine which server wrote to the file.

<!--endintro-->
