---
type: rule
archivedreason: 
title: DBAs - Do you know the compatibility issues between SQL Server 2000 and 2005?
guid: 4c551f85-4bbe-4b91-9a61-937119cfcb99
uri: compatibility-issues-between-sql-server-2000-and-2005
created: 2019-11-22T21:30:50.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- dbas-do-you-know-the-compatibility-issues-between-sql-server-2000-and-2005

---

The SQL 2005 generated scripts are not compatible with SQL 2000, so use SQL 2000 to generate your scripts if you want to make your scripts work well on both versions.

<!--endintro-->

``` sql
IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[ProcessTarget]') AND type in (N'P', N'PC'))
drop procedure [dbo].[ProcessTarget]
```
**Figure: script only works on SQL 2005, because 'sys.objects' is only available in this version** 


``` sql
IF EXISTS (SELECT * FROM dbo.sysobjects WHERE id = OBJECT_ID(N'[dbo].[ProcessTarget]') AND OBJECTPROPERTY(id, N'IsProcedure') = 1)
drop procedure [dbo].[ProcessTarget]
```
**Figure: script works on both SQL 2000 and SQL 2005**
