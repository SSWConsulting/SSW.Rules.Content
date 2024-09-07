---
seoDescription: Avoid collation errors by specifying database default collation when joining tables or creating temporary tables.
type: rule
archivedreason:
title: DBAs - Do you avoid collation errors?
guid: 90c305f6-40d8-4bab-a049-12108957754f
uri: avoid-collation-errors
created: 2019-11-22T22:54:08.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - dbas-do-you-avoid-collation-errors
---

You don't want this error:

::: greybox
"120_ClientInvoice_ClientIDRequired.sql...Column 'dbo.Client.ClientID' is not of same collation as referencing column 'ClientInvoice.ClientID' in foreig..."  
:::
When you write a stored proc - it must work regardless of the users collation. When you are joining to a temp table - meaning you are joining 2 different databases (eg. Northwind and TempDB) they won't always have the same collation.

The reality is that you can't tell a user what collation to run their TempDB - we can only specify the collation Northwind should be (we don't even want to specify that - we want that to be their default (as per their server)).

<!--endintro-->

Here is what you need to do:

```sql
SELECT
 #ClientSummary.ClientID,
 DateOfLastReminder = MAX(ClientDiary.DateCreated),
 DaysSinceLastReminder = DATEDIFF(day,MAX(ClientDiary.DateCreated),getdate())
 INTO #RecentReminderList
 FROM
 ClientDiary INNER JOIN #ClientSummary
 ON ClientDiary.ClientID = #ClientSummary.ClientID COLLATE
 database_default
 WHERE
 ClientDiary.CategoryID LIKE 'DEBT-%'
 GROUP BY
 #ClientSummary.ClientID
```
