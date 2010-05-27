---
type: rule
archivedreason: 
title: Do you know to never give SQL Server all your RAM?
guid: f447a60f-e1f8-4b7b-9da9-876267118b66
uri: do-you-know-to-never-give-sql-server-all-your-ram
created: 2010-05-25T06:54:56.0000000Z
authors:
- id: 14
  title: Martin Hinshelwood
related: []

---


This field should not be null (Remove me when you edit this field).
<br><excerpt class='endintro'></excerpt><br>

  <ol>
    <li>Open SQL Server Management Studio<br>
    <img alt="" src="/Standards/ITAndNetworking/RulesToBetterSQLServerAdministration/PublishingImages/SQLServerManagementStudio_small.jpg" /> </li>
    <li>Right click on the server name and select “Properties”<br>
    <img alt="" src="/Standards/ITAndNetworking/RulesToBetterSQLServerAdministration/PublishingImages/Properties_small.jpg" /> </li>
    <li>Select the “Memory” tab <br>
    <img alt="" src="/Standards/ITAndNetworking/RulesToBetterSQLServerAdministration/PublishingImages/MemoryTab_small.jpg" /> </li>
    <li>You will see that the default number is HUGE. Change this to something more realistic. Let SQL use half of the memory in your server.Leave about 1024MB headroom. For example, if you server has 4GB of RAM, give the SQL server a Maximum server memory of 2048mb.<br>
    <img alt="" src="/Standards/ITAndNetworking/RulesToBetterSQLServerAdministration/PublishingImages/DefaultNumber_small.jpg" /> </li>
</ol>
This will prevent SQL from “owning” all of the RAM on your system,leaving some memory left for your other applications to use. 



