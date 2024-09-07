---
seoDescription: Use Unicode datatypes (nchar, nvarchar) only in special circumstances to avoid wasting space, especially for non-multilingual applications.
type: rule
archivedreason:
title: Schema - Do you only use Unicode datatypes (nchar, nvarchar and ntext) in special circumstances?
guid: 23e8abdb-2a84-45b6-89b2-de974601b35b
uri: only-use-unicode-datatypes-in-special-circumstances
created: 2019-11-05T22:41:29.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - schema-do-you-only-use-unicode-datatypes-nchar-nvarchar-and-ntext-in-special-circumstances
  - schema-do-you-only-use-unicode-datatypes-(nchar-nvarchar-and-ntext)-in-special-circumstances
---

Columns defined using the nchar and nvarchar datatypes can store any character defined by the Unicode Standard, which includes all of the characters defined in the various English and Non-English character sets. These datatypes take twice as much storage space per characters as non-Unicode data types.

<!--endintro-->

It is not the disk space costs that are the concern. It is the 8060 limit, please refer to [Maximum Capacity Specifications for SQL Server](https://docs.microsoft.com/en-us/sql/sql-server/maximum-capacity-specifications-for-sql-server?redirectedfrom=MSDN&view=sql-server-ver15) for details.

If your database stores only English characters, this is a waste of space. Don't use Unicode double-byte datatypes such as nchar and nvarchar unless you are doing multilingual applications.

If you need to store more that 255 Characters, use Varchar(max) or nvarchar(max).
