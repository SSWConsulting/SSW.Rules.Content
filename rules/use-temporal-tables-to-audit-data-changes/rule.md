---
type: rule
archivedreason: 
title: Data - Do you use temporal tables to audit data changes?
guid: 94b69b2e-cb6e-482a-bc6a-f710a7079fec
uri: use-temporal-tables-to-audit-data-changes
created: 2019-11-25T22:35:48.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Christian Morford-Waite
  url: https://ssw.com.au/people/christian-morford-waite
related: []
redirects:
- data-do-you-use-temporal-tables-to-audit-data-changes

---


<p>In many cases, there are legal requirements to audit all updates to financial records. In other cases, you will want to be able to track and undo deletes to your database. Some solutions we have seen in the past are&#58;<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p></p><ol><li>Manually adding triggers on all database tables to log every table</li><li>The business objects or stored procedures all write to 2 tables the main table such as Customer and CustomerAudit</li><li>Using a logging utility to audit database changes</li></ol><p>For ease of reporting and the ability to undo, we recommend that you use a logging utility such as&#160;<a href="https&#58;//www.ssw.com.au/ssw/Redirect/Lumigent/Lumigent.htm">Lumigent Log Explorer</a>. This means that you can devote your development time to areas other than auditing. Also, unlike other utilities which use triggers (such as&#160;<a href="https&#58;//www.ssw.com.au/ssw/Redirect/ApexSQL.htm">ApexSQL Audit</a>), there is no performance overhead because it relies upon log files already created by SQL Server. If required, you can export the log information to SQL Server, so you can perform advanced queries on it. It even allows you to recover previously deleted tables.​<br></p>


