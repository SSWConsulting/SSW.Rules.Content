---
type: rule
archivedreason: 
title: DBAs - Do you know the compatibility issues between SQL Server 2000 and 2005?
guid: 4c551f85-4bbe-4b91-9a61-937119cfcb99
uri: dbas---do-you-know-the-compatibility-issues-between-sql-server-2000-and-2005
created: 2019-11-22T21:30:50.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p class="ssw15-rteElement-P">The SQL 2005 generated scripts are not compatible with​&#160;SQL 2000, so use SQL 2000 to generate your scripts if you want to make your scripts work well on both versions.​​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea" style="width&#58;770.031px;">IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[ProcessTarget]') AND type in (N'P', N'PC'))<br>drop procedure [dbo].[ProcessTarget]</p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; script only works on SQL 2005, because 'sys.objects' is only available in this version<br></dd><p class="ssw15-rteElement-CodeArea" style="width&#58;770.031px;">IF EXISTS (SELECT * FROM dbo.sysobjects WHERE id = OBJECT_ID(N'[dbo].[ProcessTarget]') AND OBJECTPROPERTY(id, N'IsProcedure') = 1)<br>drop procedure [dbo].[ProcessTarget]</p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; script works on both SQL 2000 and SQL 2005​<br></dd>


