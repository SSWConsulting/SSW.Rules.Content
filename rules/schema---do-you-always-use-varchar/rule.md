---
uri: schema---do-you-always-use-varchar
title: Schema - Do you always use Varchar?
created: 2019-11-05 22:48:11
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p class="ssw15-rteElement-P">​​​Use VARCHAR instead of CHAR, unless your data is almost always of a fixed length, or is very short. For example, a Social Security/Tax File number which is always 9 characters. These situations are rare.&#160;</p><p class="ssw15-rteElement-P">SQL Server fits a whole row on a single page, and will never try to save space by splitting a row across two pages.&#160;</p><p class="ssw15-rteElement-P">Running DBCC SHOWCONTIG against tables shows that a table with fixed length columns takes up less pages of storage space to store rows of data.&#160;</p><p class="ssw15-rteElement-P">General rule is that the shorter the row length, the more rows you will fit on a page, and the smaller a table will be.&#160;<br></p><p class="ssw15-rteElement-P">It allows you to save disk space and it means that any retrieval operation such as SELECT COUNT(*) FROM, runs much quicker against the smaller table.​​<br></p> </span>




