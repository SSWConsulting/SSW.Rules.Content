---
type: rule
title: DBAs - Do you create new databases in the default data directory?
uri: dbas---do-you-create-new-databases-in-the-default-data-directory
created: 2019-11-22T21:21:30.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>When trying to create a database in SQL Server 2005 from an existing create script written for SQL Server 2000, we came across a problem. Our create script was trying to determine the path to save the database file (the path to the default data store) by using the sysdevices table in the Master database; however, the schema for the Master database had changed in 2005 and our script could no longer find the column it relied on to determine this path.</p><p>Rather than creating a new script specific to 2005, we found that by removing the optional FILENAME attribute all together, both SQL Server 2000 and 2005 were happy and the database files were saved into the default data directory which is what we were after.</p><p>The moral of the story is - keep it simple.<br></p> </span>

<p>​When using a create script to create a new database, let SQL Server determine the filename and path from its default settings. This will help make the script simpler, more flexible, and ready to use with utilities such as MS OSQL and&#160;SSW SQL Deploy.</p><p class="ssw15-rteElement-CodeArea">DECLARE @device_directory NVARCHAR(520)<br>SELECT @device_directory = SUBSTRING(phyname, 1,<br> CHARINDEX(N'master.mdf', LOWER(phyname)) - 1)<br>FROM master.dbo.sysdevices<br>WHERE (name = N'master')<br>EXECUTE (N'<br>CREATE DATABASE [DatabaseName]<br> ON PRIMARY <br> (<br> NAME = N''[DatabaseName]'', <br> FILENAME = N''' + @device_directory + N'[DatabaseName].mdf''<br> )<br> LOG ON <br> (<br> NAME = N''[DatabaseName]_log'', <br> FILENAME = N''' + @device_directory + N'[DatabaseName].ldf''<br> ) <br>   COLLATE SQL_Latin1_General_CP1_CI_AS<br> ' <br> )<br>Go</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example - FILENAME Parameter used to specify database path<br></dd><p class="ssw15-rteElement-CodeArea"><br>CREATE DATABASE [DatabaseName]<br>COLLATE SQL_Latin1_General_CP1_CI_AS<br>Go</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example -&#160;Generic CREATE DATABASE used​​<br></dd>


