---
type: rule
archivedreason: 
title: Do you know how to get maximum logging in Report Server?
guid: 548a8189-cfa7-4a5f-bea8-583fe9243118
uri: do-you-keep-track-of-which-reports-are-being-executed
created: 2016-09-12T00:39:48.0000000Z
authors:
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
related: []
redirects:
- do-you-know-how-to-get-maximum-logging-in-report-server

---

By default SSRS will track reporting execution for the last 60 days. This might be OK in most cases, but you may want to adjust the retention days if you want better report usage statistics.

<!--endintro-->

To update the value you can:

1. Connect to the ReportServer database in SQL Management Studio
2. Execute the following script and update the value to the number of days you want to track






``` bash
EXEC SetConfigurationInfo @Name=N'ExecutionLogDaysKept',@Value=N'365'
```





After you have this, you can query the ExecutionLog table to find useful information about report execution like:

* Which users are actively using the reports
* How long reports are executing
* The last time a report was executed
