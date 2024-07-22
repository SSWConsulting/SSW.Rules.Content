---
seoDescription: How to index SQL WHERE clauses.
type: rule
archivedreason:
title: How to Index SQL WHERE Clauses?
guid: 65a83a45-bcdb-4eff-ad50-cca61011ab1a
uri: sql-indexing-where
created: 2024-07-22T07:26:54.0000000Z
authors:
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related:
  - sql-indexing-orderby
  - sql-indexing-joins
  - sql-real-world-indexes
  - sql-indexing-testing
---

So you've identified that a WHERE clause is causing query performance issues. How can you create an index to alleviate the problem?

<!--endintro-->


-- Here's our query
So let's say we have the following query:
```sql
SELECT 
	Id, DisplayName, Location
FROM
	dbo.Users
WHERE 
	DisplayName = 'Frank'
```

We want to quickly be able to skip to data matching the DisplayName, so we should create an index on that column.

```sql
CREATE INDEX IX_DisplayName ON dbo.Users (DisplayName)
```

But the original query was also reading the location column. It may be worth verifying whether including the location column is valuable.

```sql
CREATE INDEX IX_DisplayName_Includes ON dbo.Users (DisplayName) INCLUDE (Location)
```

Having created 2 options, it's important to evaluate which of the options works better.

So test the query as shown.
```sql
SET STATISTICS IO ON;
SELECT 
	Id, DisplayName, Location
FROM
	dbo.Users WITH (Index = 1) -- use the primary key for a baseline
WHERE 
	DisplayName = 'Frank'

SELECT 
	Id, DisplayName, Location
FROM
	dbo.Users WITH (Index = IX_DisplayName)
WHERE 
	DisplayName = 'Frank'

SELECT 
	Id, DisplayName, Location
FROM
	dbo.Users WITH (Index = IX_DisplayName_Includes)
WHERE 
	DisplayName = 'Frank'
```

This returns data like the following.
```
(704 rows affected)
Table 'Users'. Scan count 9, logical reads 45184, physical reads 0, page server reads 0, read-ahead reads 0, page server read-ahead reads 0, lob logical reads 0, lob physical reads 0, lob page server reads 0, lob read-ahead reads 0, lob page server read-ahead reads 0.

(704 rows affected)
Table 'Users'. Scan count 1, logical reads 2171, physical reads 0, page server reads 0, read-ahead reads 0, page server read-ahead reads 0, lob logical reads 0, lob physical reads 0, lob page server reads 0, lob read-ahead reads 0, lob page server read-ahead reads 0.

(704 rows affected)
Table 'Users'. Scan count 1, logical reads 6, physical reads 0, page server reads 0, read-ahead reads 0, page server read-ahead reads 0, lob logical reads 0, lob physical reads 0, lob page server reads 0, lob read-ahead reads 0, lob page server read-ahead reads 0.
```

So in this example using no index was more than 20 times worse than the first index. However the second index with the location column included was another 300 times better again. This shows that it's always worth testing whether using an INCLUDE clause on an index is effective.