

---
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p>​​Many developers are frightened of making a change to the existing database because they just don't know what applications are using it. This is especially a problem when you are dealing with&#160;databases that you did not create. Here are some approaches to this issue&#58;<br></p> </span>

<ol><li>You could run around the office and find some one and hope they know (unbelievably this seems this the most common method!)</li><li>Trawl through source control, all network locations and all the source code around to check what connection strings are being used</li><li>You can have a zsApplication table and manually populate with application it uses (Recommended). This can be populated with a run of a SQL profiler over a period of a week so all usage is captured. 
      <dl class="image"><dt><img src="/PublishingImages/SQLDatabases_zsApplication.png" alt="SQLDatabases_zsApplication.png" style="width&#58;750px;height&#58;295px;" /></dt><dd>Figure​&#58;&#160;Add a zsApplication table to make applications that use it visible to all developers</dd></dl></li><li>Keep a constantly running login Audit with a SQL Server Profiler Trace that saves to a table​&#160;and make sure all applications have an application name in their connection string. This method is the most comprehensive option but is not recommended because you get a constant performance hit from SQL Profiler running.<br>
   <dl class="image"><dt><span style="color&#58;#555555;font-weight&#58;bold;"><img src="/SiteAssets/design-for-database-change/2020-01-09_18-55-46.png" alt="2020-01-09_18-55-46.png" style="margin&#58;5px;width&#58;808px;" /><br></span></dt><dt><span style="color&#58;#555555;font-weight&#58;bold;">Figure&#58;&#160;SQL Profiler can help you design for change with auditing of Login events by giving you a guide on what applications are connecting to your database</span><br></dt></dl></li></ol>


