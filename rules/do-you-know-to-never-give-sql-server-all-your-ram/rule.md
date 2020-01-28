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


Microsoft SQL Server is made to use all the available memory in a server for itself. It will eat all the memory you throw at it. This can be a problem because your other applications may suffer performance problems as all the system memory is gone. To limit this behaviour you can limit the maximum amount of memory SQL is allowed to use. 
<br>
<br><excerpt class='endintro'></excerpt><br>

  <ol>
    <li>Open SQL Server Management Studio<dl class="ssw15-rteElement-ImageArea">
    <img src="/PublishingImages/SqlServerAllYourRam_01.png" alt="" style="width&#58;757px;height&#58;427px;" />​​<span style="font-weight&#58;bold;">Figure&#58; SQL Server Nanagement Studio - Login Screen</span></dl></li>
    <li>Right click on the server name and select “Properties”<dl class="ssw15-rteElement-ImageArea">
    <img src="/PublishingImages/SqlServerAllYourRam_02.png" alt="" style="width&#58;759px;height&#58;442px;" /><strong>Figure&#58; SQL Database options and properties menu</strong><br></dl></li>
    <li>Select the “Memory” tab <dl class="ssw15-rteElement-ImageArea">
    <img src="/PublishingImages/SqlServerAllYourRam_03.png" alt="" style="width&#58;757px;height&#58;434px;" /><strong>Figure&#58; Server Properties showing the ridiculously large value set for the maximum server memory​</strong> </dl></li>
    <li>You will see that the default number is HUGE. Change this to something more realistic. Let SQL use half of the memory in your server.Leave about 1024MB headroom. For example, if you server has 4GB of RAM, give the SQL server a Maximum server memory of 2048mb.<dl class="ssw15-rteElement-ImageArea">
    <img src="/PublishingImages/SqlServerAllYourRam_04.png" alt="" style="width&#58;635px;height&#58;523px;" /><strong>Figure&#58; Maximum server memory settings in server properties</strong><br></dl></li>
</ol>
This will prevent SQL from “owning” all of the RAM on your system,leaving some memory left for your other applications to use. 



