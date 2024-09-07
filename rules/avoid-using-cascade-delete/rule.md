---
seoDescription: SQL Server's ON DELETE CASCADE functionality can be dangerous, deleting related records without control, instead delete records in code for better control.
type: rule
archivedreason:
title: Relationships - Do you avoid using Cascade Delete?
guid: 872e3ec0-a2b7-41bd-aea3-e812e2104c4e
uri: avoid-using-cascade-delete
created: 2019-11-13T00:23:04.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related:
  - turn-on-referential-integrity-in-relationships
redirects:
  - relationships-do-you-avoid-using-cascade-delete
---

SQL Servers ON DELETE CASCADE functionality can be very dangerous. We recommend not using it. Imagine someone deletes customer and the orders are deleted. If you need to delete records in related tables, do it in code in the application as it gives you more control.

<!--endintro-->
