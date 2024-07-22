---
seoDescription: How to test the performance of your SQL indexes on SQL Server
type: rule
archivedreason:
title: How to Test Your Indexes in SQL Server?
guid: a0a2192c-3615-424e-9119-9a4db7729d58
uri: sql-indexing-testing
created: 2024-07-22T07:26:54.0000000Z
authors:
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related:
  - sql-indexing-orderby
  - sql-indexing-joins
  - sql-real-world-indexes
  - sql-indexing-where
---

So you've created some indexes. How can you go about verifying that the indexes have actually improved the performance of your queries?

<!--endintro-->

So the previous rule talked about whether or not to INCLUDE extra columns in the index or not. When doing so, it would be great to be able to evaluate different options and identify which provide the best balance.