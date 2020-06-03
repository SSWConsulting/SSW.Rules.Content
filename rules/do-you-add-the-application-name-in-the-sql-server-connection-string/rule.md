---
type: rule
title: Do you add the Application Name in the SQL Server connection string?
uri: do-you-add-the-application-name-in-the-sql-server-connection-string
created: 2018-04-26T21:01:36.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> You should always add the application name to the connection string so that SQL Server will know which application is connecting, and which database is used by that application. This will also allow SQL Profiler to trace individual application which helps you monitor performance or resolve conflicts.<br><br> </span>

<p class="ssw15-rteElement-CodeArea">​&lt;add key=&quot;Connection&quot; value=&quot;Integrated Security=SSPI;Persist Security Info=False;Initial Catalog=Biotrack01;Data Source=sheep;&quot;/&gt;</p><dd class="ssw15-rteElement-FigureBad">Bad example - The connection string without Application Name<br></dd><p class="ssw15-rteElement-CodeArea">&lt;add key=&quot;Connection&quot; value=&quot;Integrated Security=SSPI;Persist Security <br> Info=False;Initial Catalog=Biotrack01;Data Source=sheep; <br> Application Name=Biotracker&quot;/&gt; // Good Code - Application Name is added in the connection string.​<br></p><dd class="ssw15-rteElement-FigureGood">​​Good example - The connection string with Application Name​<br></dd>


