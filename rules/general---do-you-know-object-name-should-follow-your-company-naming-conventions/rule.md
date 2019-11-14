---
type: rule
title: General - Do you know object name should follow your company Naming Conventions?
uri: general---do-you-know-object-name-should-follow-your-company-naming-conventions
created: 2019-11-14T21:48:00.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <ol><li><a href="https&#58;//www.ssw.com.au/ssw/Standards/DeveloperSQLServer/SQLServerStandard_1_ObjectNaming.aspx">SQL Server Object Naming Standard.aspx</a>&#160;SSW's Standard for naming SQL Server Objects.</li><li><a href="https&#58;//www.ssw.com.au/ssw/Standards/DeveloperSQLServer/SQLServerStandard_2_StoredProcedureNaming.aspx">SQL Server Stored Procedure Naming Standard</a>&#160;SSW's Standard for naming Stored Procedures.</li><li><a href="https&#58;//www.ssw.com.au/ssw/Standards/DeveloperSQLServer/SQLServerStandard_4_IndexesNaming.aspx">SQL Server Indexes Naming Standard</a>&#160;SSW's Standard for naming Indexes.</li><li><a href="https&#58;//www.ssw.com.au/ssw/Standards/DeveloperSQLServer/SQLServerStandard_5_RelationshipNaming.aspx">SQL Server Relationship Naming Standard</a>&#160;SSW's Standard for naming Relationships</li><li>Use decreasing generality for table names ie. Client and ClientInvoice, then ClientInvoiceDetail.</li><li>Don't use underscores, instead use upper and lower case ie. ClientInvoice is preferred over Client_Invoice.</li><li>Table names should not use plurals ie. Client is preferred over Clients.</li><li>Generally don't use abbreviations. But there are a few words that are so commonly used that they can be abbreviated. These are&#58;</li><ul><li>Quantity = Qty</li><li>Amount = Amt</li><li>Password = Pwd</li></ul><li>Prefix all Date fields with 'Date' ie. DateInvoiced. One extra use of this is you can have generic code that enables a Date control on this field.</li><li>Suffix Percent fields with 'Pct' ie. SalesTaxPct.</li><li>Only use alphabet characters. ie. don't use AustraliaListA$. Avoid the following characters in your object names in SQL Server. If you do not do this, you will need to constantly identify those ill-named objects with bracketed or quoted identifiers - otherwise, unintended bugs can arise.&#160;<a href="https&#58;//www.ssw.com.au/ssw/KB/KB.asp?KBID=Q316015">What characters and symbols should I avoid using when naming objects in Access and SQL Server databases</a></li><li>Don't use reserved words on their own. ie. User, Count, Group, etc. They can be used if joined with other words.&#160;<a href="https&#58;//www.ssw.com.au/ssw/KB/KB.asp?KBID=Q931371">What are reserved words for SQL Server 2000?</a>​<br></li></ol><br> </span>




