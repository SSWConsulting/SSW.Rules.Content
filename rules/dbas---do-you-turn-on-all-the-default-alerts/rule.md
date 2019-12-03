---
type: rule
title: DBAs - Do you turn on all the default alerts?
uri: dbas---do-you-turn-on-all-the-default-alerts
created: 2019-11-19T18:31:02.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p class="ssw15-rteElement-P">SQL Alerts are valuable because they can alert administrators of imminent SQL Server failures. e.g. when the msdb log file is full. To enable, you should change the settings under SQL Server Agent.​<br></p> </span>

<dl class="image"><dt>SQL has no default alerts. You will have to create them, and I recommend that you add all the fatal level exceptions to alerts.<br></dt></dl><dl class="image"><dt><img src="/PublishingImages/SQLDatabases_DefaultAlerts2005.png" alt="SQLDatabases_DefaultAlerts2005.png" /><br></dt><dd>Figure&#58;&#160;SQL Alerts - We recommend that you add the fatal exceptions as alerts​​</dd></dl>


