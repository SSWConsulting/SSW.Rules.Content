---
uri: general---do-you-know-object-name-should-follow-your-company-naming-conventions
title: General - Do you know object name should follow your company Naming Conventions?
created: 2019-11-14 21:48:00
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <ol><li>​​<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=93beacde-8efd-4084-8d48-66c87e91c221">SQL Server Object Naming Standard</a>&#160;SSW's Standard for naming SQL Server Objects.</li><li><a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=c7421f43-0f83-4bd8-adba-6924b29c83cf">SQL Server Stored Procedure Naming Standard</a>&#160;SSW's Standard for naming Stored Procedures.<br></li><li><a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=356a81d0-09f5-42ba-b257-5657f85fd939">SQL Server Indexes Naming S​tandard</a>&#160;SSW's Standard for naming Indexes.</li><li><a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=b2ebc7fb-471a-44b6-85ee-6c4a055341a0">SQL Server Relationship Naming Standard</a>&#160;SSW's Standard for naming Relationships</li><li>Use decreasing generality for table names ie. Client and ClientInvoice, then ClientInvoiceDetail.</li><li>Don't use underscores, instead use upper and lower case ie. ClientInvoice is preferred over Client_Invoice.</li><li>Table names should use pluralisation&#160;ie. Clients is preferred over Client.<br></li><li>Generally, do not use abbreviations. But there are a few words that are so commonly used that they can be abbreviated. These are&#58;</li><ul><li>Quantity = Qty<br></li><li>Amount = Amt<br></li><li>Password = Pwd</li></ul><li>Prefix all Date fields with 'Date' ie. DateInvoiced. One extra use of this is you can have generic code that enables a Date control on this field.</li><li>Suffix Percent fields with 'Pct' ie. SalesTaxPct.<br></li><li>Only use alphabet characters. ie. don't use AustraliaListA$. Avoid the following characters in your object names in SQL Server. If you do not do this, you will need to constantly identify those ill-named objects with bracketed or quoted identifiers - otherwise, unintended bugs can arise.</li><li>Don't use reserved words on their own. ie. User, Count, Group, etc. They can be used if joined with other words.&#160;<a href="https&#58;//docs.microsoft.com/en-us/sql/t-sql/language-elements/reserved-keywords-transact-sql?view=sql-server-ver15">Reserved Keywords (Transact-SQL)</a></li></ol><br> </span>




