---
type: rule
archivedreason: 
title: Schema - Do you have a rowversion column?
guid: fda895fe-2c8c-4e8d-9db7-ced3717bae64
uri: have-a-rowversion-column
created: 2019-11-06T17:27:42.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Alex Breskin
  url: https://ssw.com.au/people/alex-breskin
- title: Christian Morford-Waite
  url: https://ssw.com.au/people/christian-morford-waite
related: []
redirects:
- schema-do-you-have-a-rowversion-column

---

SQL Server rowversions are a data type available which are binary numbers that indicate the relative sequence in which data modifications took place in a database. See the MSDN article on rowversions here: [rowversion (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/data-types/rowversion-transact-sql?view=sql-server-ver15)

<!--endintro-->

All tables should have a rowversion column called "RecordVersion" to aid concurrency checking. A rowversion improves update performance because only one column needs to be checked when performing a concurrency check (instead of checking all columns in a table for changes).
![](NoRowversionOnTable.png)

::: bad
Figure: Bad Example - No rowversion available in this table
:::

```sql
CREATE TABLE MyTest (myKey int PRIMARY KEY 
    ,myValue int, RecordVersion rowversion); 
GO
 
INSERT INTO MyTest (myKey, myValue) VALUES (1, 0);  
INSERT INTO MyTest (myKey, myValue) VALUES (2, 0); 
INSERT INTO MyTest (myKey, myValue) VALUES (3, 0); 
UPDATE MyTest SET myValue = 1 WHERE myKey = 2
 
SELECT * FROM MyTest ORDER BY RecordVersion DESC
```

::: good
Figure: Good Example - A create statement which builds a table with a rowversion

:::

![](RecordsWithRowversion.jpg)

::: good
Figure: Good Example - A set of records with a rowversion available  
:::
