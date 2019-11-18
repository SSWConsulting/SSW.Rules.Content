---
type: rule
archivedreason: 
title: ​DBAs - Do you name your SQL Server Domain Account as 'SQLServerMachineName' so it is easily identified when performing network operations?
guid: 8656c69b-74d5-4de0-976f-2369e68eaa88
uri: dbas---do-you-name-your-sql-server-domain-account-as-sqlservermachinename-so-it-is-easily-identified-when-performing-network-operations
created: 2019-11-18T23:37:45.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p class="ssw15-rteElement-P">When you create the domain accounts under which SQL Server services run, you should name this domain account as &quot;SQLServerMachineName&quot;.&#160;</p><p class="ssw15-rteElement-P">E.g. <b>SSW2000\SQLServerDragon</b><br></p><p class="ssw15-rteElement-P">If one of the SQL Server services updates a file on the network, then you can then determine which server wrote to the file.​<br></p>
<br><excerpt class='endintro'></excerpt><br>



