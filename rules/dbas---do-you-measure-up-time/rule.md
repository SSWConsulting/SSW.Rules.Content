

---
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p>​If you measure up-time you can pro-actively inform your manager how successful you have been as a DBA. You can do this in 2 ways&#58;<br></p><h3>Option 1&#58; High Tech Solution - using System Center Operations Manager (SCOM)</h3><p>SCOM allows you to monitor and generate reports on the total uptime of your SQL Server and other service level exceptions. You need the following for these reports&#58;<br></p><ol><li>System Center Operations Manager&#160;and SQL Server on the network when performing a network scan<br></li><li>Microsoft System Center Management Pack for SQL Server<br></li></ol> </span>

<dl class="image"><dt>​<span style="color&#58;#cc4141;font-family&#58;&quot;segoe ui&quot;, &quot;trebuchet ms&quot;, tahoma, arial, verdana, sans-serif;font-size&#58;18px;">​Option 2&#58; Low Tech So</span><span style="color&#58;#cc4141;font-family&#58;&quot;segoe ui&quot;, &quot;trebuchet ms&quot;, tahoma, arial, verdana, sans-serif;font-size&#58;18px;">lution - using a recurring select as a heartbeat</span></dt></dl><ol><li>Run a query as a ping once every&#160;5 minutes something that takes about 2 seconds</li><li>SELECT * FROM Orders Five times</li><li>Log it with the time</li><li>Graph - See uptime</li><li>Graph -&#160;​See performance</li></ol><br>


