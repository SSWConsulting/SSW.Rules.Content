---
type: rule
archivedreason: 
title: General - Do you know object name should follow your company Naming Conventions?
guid: fa1bf3c6-8189-4541-b1ae-9c2abfea5297
uri: general-do-you-know-object-name-should-follow-your-company-naming-conventions
created: 2019-11-14T21:48:00.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- object-name-should-follow-your-company-naming-conventions

---

1. [SQL Server Object Naming Standard](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=93beacde-8efd-4084-8d48-66c87e91c221) SSW's Standard for naming SQL Server Objects.
2. [SQL Server Stored Procedure Naming Standard](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=c7421f43-0f83-4bd8-adba-6924b29c83cf) SSW's Standard for naming Stored Procedures.
3. [SQL Server Indexes Naming Standard](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=356a81d0-09f5-42ba-b257-5657f85fd939) SSW's Standard for naming Indexes.
4. [SQL Server Relationship Naming Standard](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=b2ebc7fb-471a-44b6-85ee-6c4a055341a0) SSW's Standard for naming Relationships
5. Use decreasing generality for table names ie. Client and ClientInvoice, then ClientInvoiceDetail.
6. Don't use underscores, instead use upper and lower case ie. ClientInvoice is preferred over Client\_Invoice.
7. Table names should use pluralisation ie. Clients is preferred over Client.
8. Generally, do not use abbreviations. But there are a few words that are so commonly used that they can be abbreviated. These are:
    * Quantity = Qty
    * Amount = Amt
    * Password = Pwd
9. Prefix all Date fields with 'Date' ie. DateInvoiced. One extra use of this is you can have generic code that enables a Date control on this field.
10. Suffix Percent fields with 'Pct' ie. SalesTaxPct.
11. Only use alphabet characters. ie. don't use AustraliaListA$. Avoid the following characters in your object names in SQL Server. If you do not do this, you will need to constantly identify those ill-named objects with bracketed or quoted identifiers - otherwise, unintended bugs can arise.
12. Don't use reserved words on their own. ie. User, Count, Group, etc. They can be used if joined with other words. [Reserved Keywords (Transact-SQL)](https&#58;//docs.microsoft.com/en-us/sql/t-sql/language-elements/reserved-keywords-transact-sql?view=sql-server-ver15)



<!--endintro-->
