---
type: rule
archivedreason: 
title: DBAs - Do you know all the log files?
guid: ca665fb5-1f57-410e-8a68-c61b2a773407
uri: know-all-the-log-files
created: 2019-11-21T17:47:35.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- dbas-do-you-know-all-the-log-files

---

SQL Server stores vital error and performance information in several different logs. You should be aware of all of them:

1. SQL Server Error Logs
    * Configure how many you want to keep
    * You should Back up your SQL Server error logs with your other scripts
    * Sp\_cycle\_errorlog
2. SQL Server Agent Error Log
    * Recycles after every service restart
3. Job History Logs
    * Agent properties, Job System tab
    * Probably too low by default
4. DBMaint history logs
5. (Event Viewer) - Issues



<!--endintro-->
