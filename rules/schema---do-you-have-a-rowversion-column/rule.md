---
type: rule
title: Schema - Do you have a rowversion column?
uri: schema---do-you-have-a-rowversion-column
created: 2019-11-06T17:27:42.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 96
  title: Alex Breskin
- id: 99
  title: Christian Morford-Waite

---



<span class='intro'> <p class="ssw15-rteElement-P">​The SQL Server timestamp data type has nothing to do with times or dates. SQL Server timestamps are binary numbers that indicate the relative sequence in which data modifications took place in a database.​<br></p> </span>

<p class="ssw15-rteElement-P">​​All tables should have a timestamp column to aid concurrency checking. A timestamp improves update performance because only one column needs to be checked when performing a concurrency check (instead of checking all columns in a table for changes).</p><p class="ssw15-rteElement-P">Be aware that when replicating with a SQL Server CE Pocket PC device using SQL server, a timestamp column is added automatically.​​​​<br></p>


