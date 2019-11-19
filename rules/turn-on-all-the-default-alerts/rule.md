---
type: rule
archivedreason: 
title: DBAs - Do you turn on all the default alerts?
guid: 2632d756-cb9e-43c9-a0a5-28624ca415e6
uri: turn-on-all-the-default-alerts
created: 2019-11-19T18:31:02.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- dbas-do-you-turn-on-all-the-default-alerts

---


<p class="ssw15-rteElement-P">Even if you don't have Microsoft Operations Manager, SQL Alerts are valuable because they can alert administrators of imminent SQL Server failures. e.g. when the msdb log file is full. To enable, you should change the settings under SQL Server Agent.​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt>​<img src="/PublishingImages/SQLDatabases_DefaultAlerts2000.png" alt="SQLDatabases_DefaultAlerts2000.png" /></dt><dd>Figure&#58;&#160;Default Alerts in SQL 2000 were disabled after install. Enable them</dd></dl><p>SQL 2005 on the other hand has no default alerts. You will have to create them, and I recommend that you add all the fatal level exceptions to alerts.</p><dl class="image"><dt><img src="/PublishingImages/SQLDatabases_DefaultAlerts2005.png" alt="SQLDatabases_DefaultAlerts2005.png" /></dt><dd>Figure&#58;&#160;SQL 2005 alerts - We recommend that you add the fatal exceptions as alerts​​</dd></dl>


