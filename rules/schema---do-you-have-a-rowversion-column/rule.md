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



<span class='intro'> <p class="ssw15-rteElement-P">​​​SQL Server rowversions&#160;are a data type available which are&#160;binary numbers that indicate the relative sequence in which data modifications took place in a database.​ See the MSDN article on rowversions here&#58;&#160;<a href="https&#58;//docs.microsoft.com/en-us/sql/t-sql/data-types/rowversion-transact-sql?view=sql-server-ver15">rowversion (Transact-SQL)​</a><br></p> </span>

<p class="ssw15-rteElement-P">​​All tables should have a rowversion&#160;column called &quot;RecordVersion&quot; to aid concurrency checking. A rowversion&#160;improves update performance because only one column needs to be checked when performing a concurrency check (instead of checking all columns in a table for changes).​​</p><dl class="ssw15-rteElement-ImageArea"><img src="/PublishingImages/NoRowversionOnTable.png" alt="" style="margin&#58;5px;" /></dl><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example - No rowversion available in this table​<br></dd><p class="ssw15-rteElement-P">​<br></p><p class="ssw15-rteElement-CodeArea">​CREATE TABLE MyTest (myKey int PRIMARY KEY&#160;<br>&#160;&#160;&#160;&#160;,myValue int, RV rowversion);&#160;<br>GO<br>&#160;<br>INSERT INTO MyTest (myKey, myValue) VALUES (1, 0);&#160;&#160;<br>INSERT INTO MyTest (myKey, myValue) VALUES (2, 0);&#160;<br>INSERT INTO MyTest (myKey, myValue) VALUES (3, 0);&#160;<br>UPDATE MyTest SET myValue = 1 WHERE myKey = 2<br>&#160;<br>SELECT * FROM MyTest ORDER BY RV DESC<br></p><dd class="ssw15-rteElement-FigureGood">​​Figure&#58; Good Example - A create statement which builds a table with a rowversion<br></dd><p class="ssw15-rteElement-P"><br></p><dl class="ssw15-rteElement-ImageArea"><img src="/PublishingImages/RecordsWithRowversion.jpg" alt="" style="margin&#58;5px;" /></dl><dd class="ssw15-rteElement-FigureGood">​Figure&#58; Good Example - A set of records with a rowversion available</dd><p class="ssw15-rteElement-P">​<br></p>


