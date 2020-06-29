---
type: rule
title: DBAs - Do you turn on security auditing?
uri: dbas---do-you-turn-on-security-auditing
created: 2019-11-21T17:55:00.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>​​Configure login security auditing&#58;​<br></p><ul><li>Not on by default</li><li>Configure on the security tab of Server Properties in SQL Server Management Studio<br></li><li>Enable for Failure</li><li>View using the Windows Event Viewer​<br></li></ul> </span>

<dl class="image"><dt>​<img src="TurnOnSqlSecurityAuditing.png" alt="SQLDatabases_EnableAuditing.png" style="width&#58;682px;height&#58;571px;" /></dt><dd>Figure&#58;&#160;Enable Auditing for SQL Server logins</dd></dl><b style="color&#58;#333333;">Note&#58;</b><span style="color&#58;#333333;">&#160;You can turn on a trace for SQL DDL operations statements.​</span>


