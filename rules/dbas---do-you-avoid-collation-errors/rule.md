---
type: rule
title: DBAs - Do you avoid collation errors?
uri: dbas---do-you-avoid-collation-errors
created: 2019-11-22T22:54:08.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>​​You don't want this error&#58;<br></p><p class="ssw15-rteElement-GreyBox">&quot;120_ClientInvoice_ClientIDRequired.sql...Column 'dbo.Client.ClientID' is not of same collation as referencing column 'ClientInvoice.ClientID' in foreig...&quot;</p>When you write a stored proc - it must work regardless of the users collation. When you are joining to a temp table - meaning you are joining 2 different databases (eg. Northwind and TempDB) they wont always have the same collation.​<p></p><p>The reality is that you can't tell a user what collation to run their TempDB - we can only specify the collation Northwind should be (we don't even want to specify that - we want that to be their default (as per their server))​​.<br><br></p> </span>

<p class="ssw15-rteElement-P">​Here is what you need to do&#58;​​​<br></p><p class="ssw15-rteElement-CodeArea"> SELECT<br> #ClientSummary.ClientID,<br> DateOfLastReminder = MAX(ClientDiary.DateCreated),<br> DaysSinceLastReminder = DATEDIFF(day,MAX(ClientDiary.DateCreated),getdate())<br> INTO #RecentReminderList<br> FROM<br> ClientDiary INNER JOIN #ClientSummary<br> ON ClientDiary.ClientID = #ClientSummary.ClientID COLLATE<br> database_default<br> WHERE<br> ClientDiary.CategoryID LIKE 'DEBT-%'<br> GROUP BY<br> #ClientSummary.ClientID<br></p>


