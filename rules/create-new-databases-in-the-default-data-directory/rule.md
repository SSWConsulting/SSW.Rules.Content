---
type: rule
archivedreason: 
title: DBAs - Do you create new databases in the default data directory?
guid: 9bc0d25e-9ea7-4abc-9f9c-b59099a00a78
uri: create-new-databases-in-the-default-data-directory
created: 2019-11-22T21:21:30.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- dbas-do-you-create-new-databases-in-the-default-data-directory

---

When trying to create a database in SQL Server 2005 from an existing create script written for SQL Server 2000, we came across a problem. Our create script was trying to determine the path to save the database file (the path to the default data store) by using the sysdevices table in the Master database; however, the schema for the Master database had changed in 2005 and our script could no longer find the column it relied on to determine this path.

Rather than creating a new script specific to 2005, we found that by removing the optional FILENAME attribute altogether, both SQL Server 2000 and 2005 were happy and the database files were saved into the default data directory which is what we were after.

The moral of the story is - keep it simple.

<!--endintro-->

When using a create script to create a new database, let SQL Server determine the filename and path from its default settings. This will help make the script simpler, more flexible, and ready to use with utilities such as MS OSQL and SSW SQL Deploy.



```sql
DECLARE @device_directory NVARCHAR(520)
SELECT @device_directory = SUBSTRING(phyname, 1,
 CHARINDEX(N'master.mdf', LOWER(phyname)) - 1)
FROM master.dbo.sysdevices
WHERE (name = N'master')
EXECUTE (N'
CREATE DATABASE [DatabaseName]
 ON PRIMARY 
 (
 NAME = N''[DatabaseName]'', 
 FILENAME = N''' + @device_directory + N'[DatabaseName].mdf''
 )
 LOG ON 
 (
 NAME = N''[DatabaseName]_log'', 
 FILENAME = N''' + @device_directory + N'[DatabaseName].ldf''
 ) 		COLLATE SQL_Latin1_General_CP1_CI_AS
 ' 
 )
Go
```

::: bad
Figure: Bad Example - FILENAME Parameter used to specify database path

:::

```sql
CREATE DATABASE [DatabaseName]
COLLATE SQL_Latin1_General_CP1_CI_AS
Go
```

::: good
Figure: Good Example - Generic CREATE DATABASE used

:::
