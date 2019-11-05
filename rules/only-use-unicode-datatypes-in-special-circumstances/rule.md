---
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


Columns defined using the nchar, nvarchar and ntext datatypes can store any character defined by the Unicode Standard, which includes all of the characters defined in the various English and Non-English character sets. These datatypes take twice as much storage space per characters as non-Unicode data types.<br>
<br><excerpt class='endintro'></excerpt><br>
<p>​It is not the disk space costs that are the concern. It is the 8060 limit, please refer to&#160;<a href="https&#58;//docs.microsoft.com/en-us/sql/sql-server/maximum-capacity-specifications-for-sql-server?redirectedfrom=MSDN&amp;view=sql-server-ver15">Maximum Capacity Specifications for SQL Server​</a>&#160;for details.</p><p>​If your database stores only English characters, this is a waste of space. Don't use Unicode double-byte datatypes such as nchar, nvarchar and ntext unless you are doing multilingual applications.<br></p>


