---
type: rule
archivedreason: 
title: Do you know how to investigate performance problems in a .NET app?
guid: a7a29113-838b-4dfb-8b97-25d27713c195
uri: do-you-know-how-to-investigate-performance-problems-in-a-net-app
created: 2017-04-20T00:13:21.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Matt Wicks
  url: https://ssw.com.au/people/matt-wicks
related: []
redirects: []

---


Working out why the performance of an application has suddenly degraded can be hard.  This rule covers some investigations steps that can help determine the cause of performance problems.<br>
<br><excerpt class='endintro'></excerpt><br>
<h3>1. Use Application Insights to determine when the application last had acceptable performance​ </h3><p>Follow the <a href=/do-you-know-how-to-find-performance-problems-with-application-insights>Do you know how to find performance problems with Application Insights?​</a> rule to determine when the decrease in performance began to occur. It'​s important to determine if the performance degradation occurred gradually or if there was a dramatic drop-off in performance.<br></p><h3>2. Look for changes that coincide with the performance issue​​<br></h3><p>There are three general cases that can cause performance issues:<br></p><ol><li>A change to software or hardware.  Your deployment tool (such as Octopus) can tell you if there has been a software deployment, and you can work with your network admin to determine if there has been infrastructure changes.<br></li><li>The load factor on the application can change.  Application Insights can help you determine if the load factor on the application has increased.<br></li><li>A hardware issue or network issue can occur that interferes with normal operation.​  The Windows Event ​Log and other sys admin monitoring tools can alert you to infrastructure issues like this.<br></li></ol><h3>3. ​Dealing With Code Related Issues​<br></h3><p>If a software release has caused the performance problems, it is important to work out the code delta between the software release that worked well and the new release with the performance issues.  Your software repository should have the necessary metadata to allow you to trace code deltas between release numbers.  Inspect all the changes that have occurred for obvious performance issues like bad EF code, unnecessary loops and chatty network calls.  See <a href=/where-bottlenecks-can-happen>Do you know where bottlenecks can happen?​</a> for more information on performance issues that can be introduced with code changes.<br></p><h3>4. Dealing with Database Related Issues​​<br></h3><p>Application Insights can help determine which tier of an application is performing poorly, and if it is determined that the performance issue is occurring in the database, SQL Server makes finding these performance issues much easier.</p><p> 
   <b>Tip:</b> Azure SQL can provide performance recommendations based off your application usage and even automatically apply them for you.<br></p><p>Query Store is like having a light-weight version of SQL Profiler running all the time, and is enabled at a database level using the Database Properties dialog:</p><dl class="image"><dt>
      <img src="QueryStore1.png" alt="" style="width:800px;" />
   </dt><dd>Figure: Read Write indicates that the Query Store is setup to help us a few days later</dd></dl><p>Once Query Store has been enabled for a particular database, it needs to run for a number of days to collect performance data.  It is generally a good idea to enable Query Store for important production databases 
   <strong>before</strong> performance problems occur.  Detailed information on regressed queries, overall resource consumption, the worst performing queries, and detailed information such as query plans for a specific SQL statement can then be retrieved using SQL Server Management Studio (SSMS).<br></p><dl class="image"><dt>
      <img src="QueryStore3.png" alt="" />
   </dt><dd>Figure: A couple of days later… Query Store can now be queried to determine which queries are now performing poorly</dd></dl><p>Once Query Store has been collecting performance information on a database for an extended period, a rich collection of information is available.  It is possible to show regressed queries by comparing a Recent time interval (2 weeks in the diagram below) compared to a baseline History period (the Last Year in the diagram below) to see queries that have begun to perform poorly.</p><dl class="image"><dt>
      <img src="QueryStore2.png" alt="" style="width:800px;" />
   </dt><dd>Figure: The query store can show the top 25 regressed queries in the last 2 weeks and give suggestions on how to improve them</dd></dl><p>In the diagram we can see the total duration for a query (top left), the execution plans that have been used on a particular query (top right) and the details of a selected execution plan in the bottom pane.  The actual SQL statement that was executed is also visible, allowing the query to be linked back to a particular EF code statement.</p><p>The Top Resource Consuming Queries tab is extremely valuable for performance tuning a database.  You can see the Top 25 Queries by:<br></p><ul><li>Duration<br></li><li>CPU Time<br></li><li>Execution Count<br></li><li>Logical Reads<br></li><li>Logical Writes<br></li><li>Memory consumption<br></li><li>Physical Reads<br></li></ul><p>All of these readings can be broken down using the  statistical measures of:</p><ul><li>Total<br></li><li>Average<br></li><li>Min<br></li><li>Max<br></li><li>Std Deviation<br></li></ul><p>As with the Regressed Queries tab, the query plan history and details of a particular query plan are available for inspection. ​This provides all the required information to track down the part of the application that is calling the poorly performing SQL, and also provides insight into how to fix the poor performance depending on which SQL step is taking the most time.<br></p><dl class="image"><dt>
      <img src="QueryStore4.png" alt="" style="width:800px;" />
   </dt></dl>


