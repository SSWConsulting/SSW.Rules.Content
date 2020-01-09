---
type: rule
archivedreason: 
title: DBAs - Do you use Database Mail (not SQL Mail)?
guid: aae96599-6401-4eb3-af17-68640cdd0435
uri: use-database-mail-not-sql-mail
created: 2019-11-19T17:57:28.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- dbas-do-you-use-database-mail-not-sql-mail
- dbas-do-you-use-database-mail-(not-sql-mail)

---


<p>​​SQL Server includes Database Mail (it was a new feature released back in 2005 as&#160;a replacement for SQL Mail). Database Mail is a great feature as it allows&#58;<br></p><ul><li>HTML messages natively supported - so there's no need to use 3rd party dlls anymore</li><li>Communication direct with SMTP server -&#160;There's no need for outlook or MAPI profiles on server<br></li><li>Multiple profiles and accounts supported to specify multiple SMTP servers or different email infrastructure situations</li><li>SQL Server queues messages even when the external mailing process fails</li><li>High security - users and roles have to be granted permission to send mail</li><li>Logging and auditing</li><li>Attachment size regulations and file extension requirements <br><br></li></ul>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt>​<img src="/PublishingImages/SQLDatabases_SQLMail.png" alt="SQLDatabases_SQLMail.png" style="width&#58;750px;height&#58;509px;" /></dt><dd>F​​igure&#58; Bad example -&#160;Using SQL Mail</dd></dl><p class="ssw15-rteElement-CodeArea">EXEC master.dbo.xp_smtp_sendmail<br>@FROM = N'your@email.com',<br>@FROM_NAME = N'Sophie Belle',<br>@TO = 'recipient@email.com',<br>@subject = 'Vendor List',<br>@message = 'The list of vendors is attached.',<br>@type = N'text/html',<br>@server = N'mail.company.com.au'</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example - Avoid using SQL Mail - &#160;you need to have Outlook on the server and there is no built-in logging<br></dd><dl class="goodImage"><dt><img src="/PublishingImages/SQLDatabases_DBMail.png" alt="SQLDatabases_DBMail.png" style="width&#58;750px;" /></dt><dd>Figure&#58; Good example -&#160; Use Database Mail</dd></dl>
<p class="ssw15-rteElement-CodeArea">USE msdb<br>Execute dbo.sp_send_dbmail<br>@profile_name = 'UTS',<br>@recipients = 'your@email.com,<br>@body = 'The list of vendors is attached.',<br>@query = 'USE AdventureWorks; SELECT VendorID, Name FROM Purchasing.Vendor',<br>@subject = 'Vendor List',<br>@attach_query_result_as_file = 1</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example -&#160;Use database mail for scalability, built-in logging and HTML capability<br></dd><p>&#160;​<br></p>


