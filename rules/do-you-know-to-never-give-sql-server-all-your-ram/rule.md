---
type: rule
title: Do you know to never give SQL Server all your RAM?
uri: do-you-know-to-never-give-sql-server-all-your-ram
created: 2010-05-25T06:54:56.0000000Z
authors:
- id: 14
  title: Martin Hinshelwood

---



<span class='intro'> Microsoft SQL Server is made to use all the available memory in a server for itself. It will eat all the memory you throw at it. This can be a problem because your other applications may suffer performance problems as all the system memory is gone. To limit this behaviour you can limit the maximum amount of memory SQL is allowed to use. 
 </span>


  <ol>
    <li>Open SQL Server Management Studio<br>
    <img alt="" src="/PublishingImages/SQLServerManagementStudio_small.jpg" /> </li>
    <li>Right click on the server name and select “Properties”<br>
    <img alt="" src="/PublishingImages/Properties_small.jpg" /> </li>
    <li>Select the “Memory” tab <br>
    <img alt="" src="/PublishingImages/MemoryTab_small.jpg" /> </li>
    <li>You will see that the default number is HUGE. Change this to something more realistic. Let SQL use half of the memory in your server.Leave about 1024MB headroom. For example, if you server has 4GB of RAM, give the SQL server a Maximum server memory of 2048mb.<br>
    <img alt="" src="/PublishingImages/DefaultNumber_small.jpg" /> </li>
</ol>
This will prevent SQL from “owning” all of the RAM on your system,leaving some memory left for your other applications to use. 



