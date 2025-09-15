---
seoDescription: SQL Server administrators enable default alerts to stay informed of imminent failures and optimize database performance.
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

SQL Alerts are valuable because they can alert administrators of imminent SQL Server failures. e.g. when the msdb log file is full. To enable, you should change the settings under SQL Server Agent.

<!--endintro-->

SQL has no default alerts. You will have to create them, and I recommend that you add all the fatal level exceptions to alerts.

![Figure: SQL Alerts - We recommend that you add the fatal exceptions as alerts](SQLDatabases_DefaultAlerts2005.png)
