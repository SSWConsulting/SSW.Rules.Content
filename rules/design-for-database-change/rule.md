---
seoDescription: Design databases that adapt to change by identifying applications using them with methods like a zsApplication table or SQL Server Profiler.
type: rule
archivedreason:
title: ​DBAs - Do you design for database change?
guid: 0472f4de-45db-4880-8e13-13292e70309d
uri: design-for-database-change
created: 2019-11-18T19:10:50.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - dbas-do-you-design-for-database-change
---

Many developers are frightened of making a change to the existing database because they just don't know what applications are using it. This is especially a problem when you are dealing with databases that you did not create. Here are some approaches to this issue:

<!--endintro-->

1. You could run around the office and find some one and hope they know (unbelievably this seems this the most common method!)
2. Trawl through source control, all network locations and all the source code around to check what connection strings are being used
3. You can have a zsApplication table and manually populate with application it uses (Recommended). This can be populated with a run of a SQL profiler over a period of a week so all usage is captured.

    ![Figure: Add a zsApplication table to make applications that use it visible to all developers](SQLDatabases_zsApplication.png)

4. Keep a constantly running login Audit with a SQL Server Profiler Trace that saves to a table and make sure all applications have an application name in their connection string. This method is the most comprehensive option but is not recommended because you get a constant performance hit from SQL Profiler running.

    ![Figure: SQL Profiler can help you design for change with auditing of Login events by giving you a guide on what applications are connecting to your database](2020-01-09_18-55-46.png)
