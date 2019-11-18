---
type: rule
title: ​DBAs - Do you configure all your SQL Server Services to use a Domain Account rather than a local service account?
uri: dbas---do-you-configure-all-your-sql-server-services-to-use-a-domain-account-rather-than-a-local-service-account
created: 2019-11-18T19:52:14.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>SQL Server 2000 and 2005 have several different services that support them.</p><ul><li>SQL Server</li><li>SQL Server Agent</li><li>SQL Server Reporting Services</li><li>SQL Server Integration Services</li><li>SQL Server Fulltext search</li><li>SQL Server Analysis Services</li></ul><p>In the service properties window for these services, ensure that the Service Startup Account is run as &quot;This Account&quot; and not as &quot;Built-in Account&quot; (SQL 2005) or &quot;Service Account&quot; (SQL 2000). Otherwise, you won't get all the functionality by default such as the ability to use Replication, Linked Servers, connect to other machines or use SQL Server mail.</p><p>For security you should not have this domain acccount in the Administrators group.​<br><br></p> </span>

<dl class="badImage"><dt>
      <img src="/PublishingImages/SQLDatabases_RunAsAccount_Bad.png" alt="SQLDatabases_RunAsAccount_Bad.png" />
   </dt><dd>Figure&#58; Bad example -&#160;This service is using a built-in local service account​</dd></dl><dl class="goodImage"><dt>
         <img src="/PublishingImages/SQLDatabases_RunAsAccount.png" alt="SQLDatabases_RunAsAccount.png" />
         <br>
      </dt><dd>​Figure&#58;&#160;Good example -&#160;Run as Account should use a domain account rather than a built-in account​</dd>
</dl>


