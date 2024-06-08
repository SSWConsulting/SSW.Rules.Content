---
type: rule
archivedreason: 
title: Schema - Do you always use Varchar?
guid: aedc3260-9b29-4115-9536-43c57d1e13b1
uri: always-use-varchar
created: 2019-11-05T22:48:11.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- schema-do-you-always-use-varchar

---



Use `VARCHAR` instead of `CHAR`, unless your data is almost always of a fixed length, or is very short. For example, a Social Security/Tax File number which is always 9 characters. These situations are rare.

SQL Server fits a whole row on a single page, and will never try to save space by splitting a row across two pages.

Running `DBCC SHOWCONTIG` against tables shows that a table with fixed length columns takes up less pages of storage space to store rows of data.

General rule is that the shorter the row length, the more rows you will fit on a page, and the smaller a table will be.

It allows you to save disk space and it means that any retrieval operation such as `SELECT COUNT(*) FROM`, runs much quicker against the smaller table.

<!--endintro-->
