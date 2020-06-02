---
uri: schema---do-you-only-use-unicode-datatypes-nchar-nvarchar-and-ntext-in-special-circumstances
title: Schema - Do you only use Unicode datatypes (nchar, nvarchar and ntext) in special circumstances?
created: 2019-11-05 22:41:29
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> Columns defined using the nchar and nvarchar&#160;datatypes can store any character defined by the Unicode Standard, which includes all of the characters defined in the various English and Non-English character sets. These datatypes take twice as much storage space per characters as non-Unicode data types.<br> </span>

<p>​It is not the disk space costs that are the concern. It is the 8060 limit, please refer to&#160;<a href="https&#58;//docs.microsoft.com/en-us/sql/sql-server/maximum-capacity-specifications-for-sql-server?redirectedfrom=MSDN&amp;view=sql-server-ver15">Maximum Capacity Specifications for SQL Server​</a>&#160;for details.</p><p>​If your database stores only English characters, this is a waste of space. Don't use Unicode double-byte datatypes such as nchar and&#160;nvarchar&#160;unless you are doing multilingual applications.<br></p><p>If you need to store more that 255 Characters, use Varchar(max) or nvarchar(max).<br></p>


