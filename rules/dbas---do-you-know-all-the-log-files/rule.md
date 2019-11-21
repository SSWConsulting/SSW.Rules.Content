---
type: rule
archivedreason: 
title: DBAs - Do you know all the log files?
guid: ca665fb5-1f57-410e-8a68-c61b2a773407
uri: dbas---do-you-know-all-the-log-files
created: 2019-11-21T17:47:35.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p>SQL Server stores vital error and performance information in several different logs. You should be aware of all of them&#58;</p><ol><li>SQL Server Error Logs</li><ul><li>Configure how many you want to keep</li><li>You should Back up your SQL Server error logs with your other scripts</li><li>Sp_cycle_errorlog</li></ul><li>SQL Server Agent Error Log</li><ul><li>Recycles after every service restart</li></ul><li>Job History Logs</li><ul><li>Agent properties, Job System tab</li><li>Probably too low by default</li></ul><li>DBMaint history logs</li><li>(Event Viewer) - Issues​<br></li></ol><br>
<br><excerpt class='endintro'></excerpt><br>



