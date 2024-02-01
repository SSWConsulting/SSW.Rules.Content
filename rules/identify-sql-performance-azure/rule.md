---
type: rule
archivedreason: 
title: Identifying the cause of Azure SQL Database performance problems
guid: 0c3cca32-b436-4e65-8d06-0263d35f283e
uri: identify-sql-performance-azure
created: 2023-12-27T07:26:54.0000000Z
authors:
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related: 
  - identify-sql-performance-sql-server
  - identify-sql-performance-azure
  - sql-server-cpu-pressure
  - sql-server-io-pressure
  - sql-server-memory-pressure
---
When looking at Azure SQL Dataabase, you often get performance issues, but how can you figure out what might be the cause?

<!--endintro-->

The first step when working with Azure SQL is to identify whether the problem is a single poorly optimised query, or whether you are reaching a limit of the server. In Azure SQL Database you choose a level of performance expressed in DTUs (Database Transaction Units). These are just a way of expressing a fixed amount of available CPU, Disk IO and memory. If you are finding that you are hitting a bandwidth limit against only one of those, you can tune your queries to use more of the other parameters while reducing the one that is being throttled. For example, you can often choose a technique that uses less CPU, but requires more memory.

To identify where the bottleneck lies, try the following SQL query. Note the historical data is only retained for about an hour, so you do need to execute the query shortly after the issue occurs.

``` sql
SELECT * FROM sys.dm_db_resource_stats ORDER BY end_time DESC;
```

The results are expressed as percentages of the maximum allowed for the service tier you are running on. So it's very easy to pick out which limit is being reached.

There is a roughly equivalent call available for Azure Managed Instance. Try:

``` sql
SELECT * FROM sys.server_resource_stats ORDER BY end_time DESC;
```

From the returned statistics you should be able to determine whether SQL Server is under CPU, IO, Network or memory pressure.
