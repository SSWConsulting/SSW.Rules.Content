---
type: rule
archivedreason: 
title: Performance Tuning - Do you make sure to clear SQL server cache when performing benchmark tests?
guid: e63b4ecc-b474-48a4-be95-9a777980bd36
uri: be-sure-to-clear-sql-server-cache-when-performing-benchmark-tests
created: 2019-11-14T23:15:10.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- performance-tuning-do-you-make-sure-to-clear-sql-server-cache-when-performing-benchmark-tests

---

When you are tuning SQL statements you tend to play in SQL management studio for a while. During this time SQL caches your query's and execution plans.

<!--endintro-->

All well and good but when you are trying to speed up an existing query that is taking some time then you may not be making a difference even though your execution times are way down.

You really need to clear SQL's cache (or buffer) every time you test the speed of a query. This prevents the data and/or execution plans from being cached, thus corrupting the next test.

To clear SQL Server's cache, run `DBCC DROPCLEANBUFFERS`, which clears all data from the cache. Then run  `DBCC FREEPROCCACHE`, which clears the stored procedure cache.

![Figure: First call is after clearing the cache, the second one is without clearing the cache (26 seconds vs 2 seconds)](ClearSQLServerCache\_BenchmarkTests.jpeg)
