---
type: rule
archivedreason: 
title: ​DBAs - Do you configure all your SQL Server Services to use a Domain Account rather than a local service account?
guid: 8592bce1-390d-4d01-b459-630c3efea01b
uri: dbas---do-you-configure-all-your-sql-server-services-to-use-a-domain-account-rather-than-a-local-service-account
created: 2019-11-18T19:52:14.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p>Depending on which components you decide to install on your&#160;SQL Server, you may need to configure the following services​&#58;<br><br></p><ul><li>SQL Server<br></li><li>SQL Server Agent<br></li><li>SQL Server Reporting Services</li><li>SQL Server Integration Services<br></li><li>SQL Server Fulltext search</li><li>SQL Server Analysis Services<br></li></ul><p>In the service properties window for these services, ensure that the Service Startup Account is run as &quot;This Account&quot; and not as &quot;Built-in Account&quot;. Otherwise, you won't get all the functionality by default such as the ability to use Replication, Linked Servers or&#160;connect to other machines.<br></p><p>For security, you should not have this domain account​ in the Administrators group.​<br><br></p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt>
      <img src="/PublishingImages/SQLDatabases_RunAsAccount_Bad.png" alt="SQLDatabases_RunAsAccount_Bad.png" />
   </dt><dd>Figure&#58; Bad example -&#160;This service is using a built-in local service account​</dd></dl><dl class="goodImage"><dt>
         <img src="/PublishingImages/SQLDatabases_RunAsAccount.png" alt="SQLDatabases_RunAsAccount.png" />
         <br>
      </dt><dd>​Figure&#58;&#160;Good example -&#160;Run as Account should use a domain account rather than a built-in account​</dd>
</dl>


