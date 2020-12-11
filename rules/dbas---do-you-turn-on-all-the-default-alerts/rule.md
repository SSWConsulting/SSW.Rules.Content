---
type: rule
archivedreason: 
title: DBAs - Do you turn on all the default alerts?
guid: 2632d756-cb9e-43c9-a0a5-28624ca415e6
uri: dbas---do-you-turn-on-all-the-default-alerts
created: 2019-11-19T18:31:02.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

SQL Alerts are valuable because they can alert administrators of imminent SQL Server failures. e.g. when the msdb log file is full. To enable, you should change the settings under SQL Server Agent.

<!--endintro-->
<dl class="image">&lt;dt&gt;SQL has no default alerts. You will have to create them, and I recommend that you add all the fatal level exceptions to alerts.<br>&lt;/dt&gt;</dl><dl class="image">&lt;dt&gt;<img src="SQLDatabases_DefaultAlerts2005.png" alt="SQLDatabases_DefaultAlerts2005.png"><br>&lt;/dt&gt;<dd>Figure: SQL Alerts - We recommend that you add the fatal exceptions as alerts</dd></dl>
