---
seoDescription: Prevent SQL Server from consuming all RAM by limiting maximum server memory to ensure optimal system performance.
type: rule
archivedreason:
title: Do you know to never give SQL Server all your RAM?
guid: f447a60f-e1f8-4b7b-9da9-876267118b66
uri: do-you-know-to-never-give-sql-server-all-your-ram
created: 2010-05-25T06:54:56.0000000Z
authors:
  - title: Martin Hinshelwood
    url: https://ssw.com.au/people/martin-hinshelwood
related: []
redirects: []
---

Microsoft SQL Server is made to use all the available memory in a server for itself. It will eat all the memory you throw at it. This can be a problem because your other applications may suffer performance problems as all the system memory is gone. To limit this behaviour you can limit the maximum amount of memory SQL is allowed to use.

<!--endintro-->

1. Open SQL Server Management Studio

   ![Figure: SQL Server Management Studio - Login Screen](SqlServerAllYourRam_01.png)

3. Right click on the server name and select “Properties”

   ![Figure: SQL Database options and properties menu](SqlServerAllYourRam_02.png)

4. Select the “Memory” tab

   ![Figure: Server Properties showing the ridiculously large value set for the maximum server memory](SqlServerAllYourRam_03.png)

5. You will see that the default number is HUGE. Change this to something more realistic. Let SQL use half of the memory in your server.Leave about 1024MB headroom. For example, if you server has 4GB of RAM, give the SQL server a Maximum server memory of 2048mb.

   ![Figure: Maximum server memory settings in server properties](SqlServerAllYourRam_04.png)

This will prevent SQL from “owning” all of the RAM on your system,leaving some memory left for your other applications to use.
