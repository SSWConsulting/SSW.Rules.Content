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



  <p>After the database has finished being attached to the web application you will get a log file with information about the import process. </p>
<ol>
    <li>Open up this log fine and pay special attention to any lines with <b>[ERROR]</b>. <br>
    Note #1: The most common reason for errors is that you have forgotten to activate a feature.<br>
    Note #2: If you have your own custom solutions, show this file to your developers to ensure it isn’t your custom solution causing the errors.</li>
    <li>Check your Application Event log after migration for errors related to your SharePoint Web Application, and fix these accordingly.</li>
</ol>
<p> <img src="FixEventLogs.png" alt="" /><br>
<font class="ms-rteCustom-FigureBad" size="+0">figure: the event log should show 0 errors after fixing the errors</font></p>

<br><excerpt class='endintro'></excerpt><br>



