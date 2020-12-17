---
type: rule
archivedreason: 
title: Do you add the Application Name in the SQL Server connection string?
guid: 6c4dd299-6155-4c3f-aa2b-916fc26bec1d
uri: do-you-add-the-application-name-in-the-sql-server-connection-string
created: 2018-04-26T21:01:36.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

You should always add the application name to the connection string so that SQL Server will know which application is connecting, and which database is used by that application. This will also allow SQL Profiler to trace individual applications which helps you monitor performance or resolve conflicts.


<!--endintro-->

&lt;add key="Connection" value="Integrated Security=SSPI;Persist Security Info=False;Initial Catalog=Biotrack01;Data Source=sheep;"/&gt;


::: bad
Bad example - The connection string without Application Name

:::


&lt;add key="Connection" value="Integrated Security=SSPI;Persist Security 
 Info=False;Initial Catalog=Biotrack01;Data Source=sheep; 
 Application Name=Biotracker"/&gt; // Good Code - Application Name is added in the connection string.


::: good
Good example - The connection string with Application Name

:::
