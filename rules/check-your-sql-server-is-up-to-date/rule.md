---
type: rule
archivedreason: 
title: DBAs - Do you check your SQL Server is up-to-date?
guid: 04b490b1-cf6f-448f-97b6-1a9ca0f8cb6d
uri: check-your-sql-server-is-up-to-date
created: 2019-11-18T18:33:24.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- dbas-do-you-check-your-sql-server-is-up-to-date

---


Most patches are for security. SQL Slammer showed that it's no good waiting a month before you decide to install a service pack. I would say wait one week and then install the service pack (maximum delay should be 2 weeks)<br><br><ul><li><strong>Option 1&#58;</strong>&#160;Manually check using&#160;<a href="https&#58;//www.ssw.com.au/ssw/KB/KB.asp?KBID=Q746022">@@version</a></li><li><strong>Option 2</strong>&#58; Run&#160;<a href="https&#58;//www.ssw.com.au/ssw/Diagnostics">SSW Diagnostics</a>&#160;and get all green ticks (Recommended)​</li></ul>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt>​<img src="/PublishingImages/SQLDatabases_RunDiagnostics.png" alt="SQLDatabases_RunDiagnostics.png" /></dt><dd>Figure&#58;&#160;Use diagnostics to ensure your SQL is up-to-date</dd></dl><b>​Note&#58;&#160;</b>To check all servers on my network we&#160;use&#160;<a href="https&#58;//www.ssw.com.au/ssw/Standards/DeveloperGeneral/networkTools.aspx#NetPing">Net Ping​</a>.<br><p></p>


