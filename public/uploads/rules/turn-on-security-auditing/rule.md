---
seoDescription: Configure SQL Server login security auditing to ensure database integrity and monitor suspicious activity efficiently.
type: rule
archivedreason:
title: DBAs - Do you turn on security auditing?
guid: fce19814-14c1-4032-9140-4127b0d39727
uri: turn-on-security-auditing
created: 2019-11-21T17:55:00.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - dbas-do-you-turn-on-security-auditing
---

Configure login security auditing:

- Not on by default
- Configure on the security tab of Server Properties in SQL Server Management Studio
- Enable for Failure
- View using the Windows Event Viewer

<!--endintro-->

![Figure: Enable Auditing for SQL Server logins](TurnOnSqlSecurityAuditing.png)  
**Note:** You can turn on a trace for SQL DDL operations statements.
