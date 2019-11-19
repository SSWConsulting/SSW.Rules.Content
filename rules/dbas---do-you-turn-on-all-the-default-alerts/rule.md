

---
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p class="ssw15-rteElement-P">​​Even if you don't have Microsoft Operations Manager, SQL Alerts are valuable because they can alert administrators of imminent SQL Server failures. e.g. when the msdb log file is full. To enable, you should change the settings under SQL Server Agent.​<br></p> </span>

<dl class="image"><dt>​<img src="/PublishingImages/SQLDatabases_DefaultAlerts2000.png" alt="SQLDatabases_DefaultAlerts2000.png" /></dt><dd>Figure&#58;&#160;Default Alerts in SQL 2000 were disabled after install. Enable them</dd></dl><p>SQL 2005 on the other hand has no default alerts. You will have to create them, and I recommend that you add all the fatal level exceptions to alerts.</p><dl class="image"><dt><img src="/PublishingImages/SQLDatabases_DefaultAlerts2005.png" alt="SQLDatabases_DefaultAlerts2005.png" /></dt><dd>Figure&#58;&#160;SQL 2005 alerts - We recommend that you add the fatal exceptions as alerts​​</dd></dl>


