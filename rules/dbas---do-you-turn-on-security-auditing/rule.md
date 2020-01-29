---
type: rule
archivedreason: 
title: DBAs - Do you turn on security auditing?
guid: fce19814-14c1-4032-9140-4127b0d39727
uri: dbas---do-you-turn-on-security-auditing
created: 2019-11-21T17:55:00.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p>​Configure login security auditing&#58;​<br></p><ul><li>Not on by default</li><li>Configure on the security tab of Server Properties in Enterprise Manager</li><li>Enable for Failure</li><li>View using the Windows Event Viewer​<br></li></ul>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt>​<img src="/PublishingImages/TurnOnSqlSecurityAuditing.png" alt="SQLDatabases_EnableAuditing.png" style="width&#58;682px;height&#58;571px;" /></dt><dd>Figure&#58;&#160;Enable Auditing for SQL Server logins</dd></dl><b style="color&#58;#333333;">Note&#58;</b><span style="color&#58;#333333;">&#160;You can turn on a trace for SQL DDL operations statements.​</span>


