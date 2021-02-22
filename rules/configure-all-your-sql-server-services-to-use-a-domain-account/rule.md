---
type: rule
archivedreason: 
title: ​DBAs - Do you configure all your SQL Server Services to use a Domain Account rather than a local service account?
guid: 8592bce1-390d-4d01-b459-630c3efea01b
uri: configure-all-your-sql-server-services-to-use-a-domain-account
created: 2019-11-18T19:52:14.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- dbas-do-you-configure-all-your-sql-server-services-to-use-a-domain-account-rather-than-a-local-service-account

---

Depending on which components you decide to install on your SQL Server, you may need to configure the following services:

* SQL Server
* SQL Server Agent
* SQL Server Reporting Services
* SQL Server Integration Services
* SQL Server Fulltext search
* SQL Server Analysis Services


In the service properties window for these services, ensure that the Service Startup Account is run as "This Account" and not as "Built-in Account". Otherwise, you won't get all the functionality by default such as the ability to use Replication, Linked Servers or connect to other machines.

For security, you should not have this domain account in the Administrators group.

<!--endintro-->


::: bad  
![Figure: Bad example - This service is using a built-in local service account](SQLDatabases\_RunAsAccount\_Bad.png)  
:::


::: good  
![Figure: Good example - Run as Account should use a domain account rather than a built-in account](SQLDatabases\_RunAsAccount.png)  
:::
