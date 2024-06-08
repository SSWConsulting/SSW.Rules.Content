---
type: rule
archivedreason: 
title: General - Do you know object name should follow your company naming conventions?
guid: fa1bf3c6-8189-4541-b1ae-9c2abfea5297
uri: object-name-should-follow-your-company-naming-conventions
created: 2019-11-14T21:48:00.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- general-do-you-know-object-name-should-follow-your-company-naming-conventions

---

Follow naming conventions:

<!--endintro-->

1. [SQL Server Object Naming Standard](/use-a-sql-server-object-naming-standard)
2. [SQL Server Stored Procedure Naming Standard](/use-a-sql-server-stored-procedure-naming-standard)
3. [SQL Server Indexes Naming Standard](/use-a-sql-server-indexes-naming-standard)
4. [SQL Server Relationship Naming Standard](/use-a-sql-server-relationship-naming-standard)
5. Use decreasing generality for table names ie. `Client` and `ClientInvoice`, then `ClientInvoiceDetail`.
6. Don't use underscores, instead use upper and lower case ie. `ClientInvoice` is preferred over `Client_Invoice`.
7. Table names should use plural ie. `Clients` is preferred over `Client`.
8. Generally, do not use abbreviations. But there are a few words that are so commonly used that they can be abbreviated. These are:
    * Quantity = `Qty`
    * Amount = `Amt`
    * Password = `Pwd`
9. Prefix all date fields with 'Date' ie. `DateInvoiced`. One extra use of this is you can have generic code that enables a date control on this field.
10. Suffix Percent fields with 'Pct' ie. `SalesTaxPct`.
11. Only use alphabet characters. ie. don't use `AustraliaListA$`. Avoid the following characters in your object names in SQL Server. If you do not do this, you will need to constantly identify those ill-named objects with bracketed or quoted identifiers - otherwise, unintended bugs can arise.
12. Don't use reserved words on their own. ie. `User`, `Count`, `Group`, etc. They can be used if joined with other words. See [Reserved Keywords (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/reserved-keywords-transact-sql?view=sql-server-ver15)
