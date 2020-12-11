---
type: rule
archivedreason: 
title: Do you check for errors after the migration process?
guid: 4434740d-dcb7-47f0-9d02-6631d00def9d
uri: do-you-check-for-errors-after-the-migration-process
created: 2010-12-23T07:11:10.0000000Z
authors: []
related: []

---

After the database has finished being attached to the web application you will get a log file with information about the import process.

1. Open up this log fine and pay special attention to any lines with  **[ERROR]** . 
<br>    Note #1: The most common reason for errors is that you have forgotten to activate a feature.
<br>    Note #2: If you have your own custom solutions, show this file to your developers to ensure it isn’t your custom solution causing the errors.
2. Check your Application Event log after migration for errors related to your SharePoint Web Application, and fix these accordingly.



![](FixEventLogs.png)
<font class="ms-rteCustom-FigureBad">figure: the event log should show 0 errors after fixing the errors</font>

<!--endintro-->
