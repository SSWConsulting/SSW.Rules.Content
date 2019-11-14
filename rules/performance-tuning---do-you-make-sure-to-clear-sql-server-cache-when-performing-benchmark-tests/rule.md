

---
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p>When you are tuning SQL statements you tend to play in SQL management studio for a while. During this time SQL caches your query's and execution plans.<br>All well and good but when you are trying to speed up a existing query that is taking some time then you may not be making a difference even though your execution times are way down.</p><p>You really need to clear SQL's cache (or buffer) every time you test the speed of a query. This prevents the data and/or execution plans from being cached, thus corrupting the next test.</p><p>To clear SQL Server's cache, run&#160;<strong>DBCC DROPCLEANBUFFERS</strong>, which clears all data from the cache. Then run&#160;<strong>DBCC FREEPROCCACHE</strong>, which clears the stored procedure cache.​<br></p> </span>

<dl class="image"><dt>​​<img src="/PublishingImages/ClearSQLServerCache_BenchmarkTests.jpeg" alt="ClearSQLServerCache_BenchmarkTests.jpeg" style="width&#58;750px;" /></dt><dd>Figure&#58; First call is after clearing the cache. The second one is without clearing the cache. (26 seconds vs 2 seconds)</dd></dl>


