---
type: rule
title: DBAs - Do you use Performance Alerts?
uri: dbas---do-you-use-performance-alerts
created: 2019-11-22T20:37:16.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>Performance alerts work well for problems that need to be discovered before they occur.</p><p>For example, one problem that you may encounter is database file growth. Since databases are set to grow to a certain percentage, you needed to configure an alert to let you know when my database would draw close to that threshold. you can configure a performance alert that fired off when it reached 80% of that threshold. Here is an example of what you can do&#58;​<br></p> </span>

<p>​​To configure an alert to trigger an application, perform the following steps&#58;<br></p><ol><li>Start the Microsoft Management Console (MMC) Performance snap-in (Start, Programs, Administrative Tools, Performance).</li><li>Expand Performance Logs and Alerts, and select Alerts.</li><li>Right-click in the right pane, and select New Alert Settings.</li><li>Enter a name for the setting that reflects what the alert will monitor, and click OK.</li><li>On the General tab, add the counter the alert will monitor and specify the values that will trigger the action.</li><li>On the Action tab, select the Run this Program checkbox.</li><li>Click the Browse button, and select the name of the application you want to run.</li><li>Click OK.</li></ol><dl class="image"><dt><img src="/PublishingImages/performanceAlert.gif" alt="performanceAlert.gif" /></dt></dl>​You have just configured an application to run in response to an alert. Unfortunately, because the program doesn't interact with the desktop, it runs in the background, visible only in Task Manager. To enable the program to run interactively, perform the following steps&#58;<ol><li>Start the MMC Services snap-in (Start, Programs, Administrative Tools, Services).</li><li>Right-click Performance Logs and Alerts, and select Properties.</li><li>On the Log On tab, specify the &quot;Local System account&quot; and select the &quot;Allow service to interact with desktop&quot; checkbox.​<br></li></ol>


