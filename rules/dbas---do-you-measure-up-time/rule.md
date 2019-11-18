---
type: rule
title: ​DBAs - Do you measure Up-Time?
uri: dbas---do-you-measure-up-time
created: 2019-11-18T18:22:58.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>If you measure up-time you can pro-actively inform your manager how successful you have been as a DBA. You can do this in 2 ways&#58;</p><h3>Option 1&#58; High Tech Solution - using Microsoft Operations Manager (MOM)</h3><p>MOM allows you to monitor and generate reports on the total uptime of your SQL Server and other service level exceptions. You need the following for these reports&#58;</p><ol><li>Microsoft Operations Manager 2005 and SQL Server on the network when performing a network scan</li><li>Downloaded&#160;<a href="https&#58;//www.ssw.com.au/ssw/Redirect/Microsoft/MOMSSQLManagementPack.htm">Microsoft SQL Server Management Pack for Microsoft Operations Manager 2005</a>&#160;for free​<br></li></ol> </span>

<dl class="image"><dt>​<img src="/PublishingImages/SQLDatabases_MOMs.png" alt="SQLDatabases_MOMs.png" style="width&#58;750px;height&#58;641px;" /></dt><dd>Figure&#58;&#160;Show managers what a good job you're doing with Microsoft Operations Manager and associated reporting service reports<br></dd></dl><h3>​Option 2&#58; Low Tech Solution - using a recurring select as a heartbeat</h3><ol><li>Run a query as a ping once every a 5 minutes something that takes about 2 seconds</li><li>SELECT * FROM Orders Five times</li><li>Log it with the time</li><li>Graph - See uptime</li><li>Graph See performance</li></ol><br>


