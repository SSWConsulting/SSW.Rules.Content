---
seoDescription: How to test the performance of your SQL indexes on SQL Server
type: rule
archivedreason:
title: Do you know how to test your indexes in SQL Server?
guid: a0a2192c-3615-424e-9119-9a4db7729d58
uri: sql-indexing-testing
created: 2024-07-22T07:26:54.0000000Z
authors:
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related:
  - sql-real-world-indexes
  - sql-indexing-orderby
  - sql-indexing-joins
  - sql-indexing-where
---

So you've created some indexes. How can you go about verifying that the indexes have actually improved the performance of your queries?

<!--endintro-->

So the previous rule talked about whether or not to INCLUDE extra columns in the index or not. When doing so, it would be great to be able to evaluate different options and identify which provide the best balance.

For SQL Server there is what is called a query hint. This particular query hint can be used to force the Query Optimizer to use a particular index on a table.

So if you create an index called IX_Index and you'd like to see if using the index improves a particular query, you can do something like the following. NB: The table itself is designated as Index 1.

```sql
SET STATISTICS IO ON; # Grab the IO statistics for the query
SELECT
  Id, DisplayName
FROM 
  dbo.Users ** WITH (INDEX = 1) # Use the primary key. 

SELECT
  Id, DisplayName
FROM 
  dbo.Users ** WITH (INDEX = IX_Index) # Use the primary key. 
```

You'll get back output like this:

```text
(704 rows affected)
Table 'Users'. Scan count 9, logical reads 45184, physical reads 1, page server reads 0, read-ahead reads 44526, page server read-ahead reads 0, lob logical reads 0, lob physical reads 0, lob page server reads 0, lob read-ahead reads 0, lob page server read-ahead reads 0.

(704 rows affected)
Table 'Users'. Scan count 1, logical reads 2171, physical reads 0, page server reads 0, read-ahead reads 0, page server read-ahead reads 0, lob logical reads 0, lob physical reads 0, lob page server reads 0, lob read-ahead reads 0, lob page server read-ahead reads 0.
```

So the output contains 1 line for each of the 2 queries that got run. The important value is the number of **logical reads** performed. Logical reads are a measure of the number of data pages that were read by the query. **Logical reads** cover every page that was read while **physical reads** only counts pages that had to be read from disk. Because caching can be inconsistent and the hit ratio for the cache will reduce as the data becomes larger, it's always better to know the **logical** reads rather than the **physical** ones.
