---
seoDescription: How to index SQL WHERE clauses.
type: rule
archivedreason:
title: Do you know how to index SQL WHERE clauses?
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

## Indexing a single comparison in a WHERE clause

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

```text
(704 rows affected)
Table 'Users'. Scan count 9, logical reads 45184, physical reads 0, page server reads 0, read-ahead reads 0, page server read-ahead reads 0, lob logical reads 0, lob physical reads 0, lob page server reads 0, lob read-ahead reads 0, lob page server read-ahead reads 0.

(704 rows affected)
Table 'Users'. Scan count 1, logical reads 2171, physical reads 0, page server reads 0, read-ahead reads 0, page server read-ahead reads 0, lob logical reads 0, lob physical reads 0, lob page server reads 0, lob read-ahead reads 0, lob page server read-ahead reads 0.

(704 rows affected)
Table 'Users'. Scan count 1, logical reads 6, physical reads 0, page server reads 0, read-ahead reads 0, page server read-ahead reads 0, lob logical reads 0, lob physical reads 0, lob page server reads 0, lob read-ahead reads 0, lob page server read-ahead reads 0.
```

So in this example using no index was more than 20 times worse than the first index. However the second index with the location column included was another 300 times better again. This shows that it's always worth testing whether using an INCLUDE clause on an index is effective.

## Indexing multiple comparisons in a WHERE clause

So if the query becomes a bit more complicated then how would we index that. So for the following:

```sql
SELECT 
 Id, DisplayName, Location
FROM
 dbo.Users
WHERE 
 DisplayName = 'Frank'
 AND Location = 'United States'
```

Based on the index created in the previous section, it looks like the index might be optimal. But if you were to run the following.

```sql
SELECT 
 Id, DisplayName, Location
FROM
 dbo.Users
WHERE 
 DisplayName = 'Frank'
-- AND Location = 'United States'
```

You will see it's not actually optimal. If it were then all the United States records would be grouped together.

```sql
CREATE INDEX IX_DisplayName_Location ON dbo.Users (DisplayName,Location)
```

This is a better index for the query.
However reversing the order of the 2 keys may be better. The key that has more uniqueness is the better one to have first.
This index may be better:

```sql
CREATE INDEX IX_Location_DisplayName ON dbo.Users (Location,DisplayName)
```

To test this then try the following:

```sql
SET STATISTICS IO ON
SELECT 
 Id, DisplayName, Location
FROM
 dbo.Users WITH (Index = 1)
WHERE 
 DisplayName = 'Frank'
 AND Location = 'United States'

SELECT 
 Id, DisplayName, Location
FROM
 dbo.Users WITH (Index = IX_DisplayName_Location)
WHERE 
 DisplayName = 'Frank'
 AND Location = 'United States'

SELECT 
 Id, DisplayName, Location
FROM
  dbo.Users WITH (Index = IX_Location_DisplayName)
WHERE 
 DisplayName = 'Frank'
 AND Location = 'United States'
```

Read the io stats from the messages returned by the query to identify which query performed less logical reads. That is the better index for this query.
