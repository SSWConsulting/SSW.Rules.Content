---
type: rule
archivedreason: 
title: Do you know you can't think of data the same way?
guid: 96e8212a-a16b-4054-838f-b16722191ec1
uri: do-you-know-you-cant-think-of-data-the-same-way
created: 2009-05-21T23:35:36.0000000Z
authors:
- title: Jay Lin
  url: https://ssw.com.au/people/jay-lin
related: []
redirects: []

---

In SQL Server you have tables to store data.  Then you have Views, Relations and Stored Procedures.

SharePoint gives us Lists where we can store rows and columns of data, but it is not the same as a full database.
   
* There are no joints out of SharePoint – you can do limited operations with lookup fields but they are not the same as joints in SQL Server
* Views in SharePoint are filters, grouping and sort on a single list only.
* Formula fields in SharePoint are only updated when the row is changed.  If you change the lookup value in the lookup list, it will not change any of the items using formula fields that are currently referencing that lookup.
* No stored procedures in SharePoint


Database remains the best at doing database work.  SharePoint is OK at creating quick lists and working with simple lists, but it is not a database server.

<!--endintro-->
