---
type: rule
archivedreason: 
title: What to do about SQL Server Memory Pressure?
guid: f7e8a48d-375e-4c23-9998-9cd9b8c7980c
uri: sql-server-memory-pressure
created: 2023-12-27T07:26:54.0000000Z
authors:
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related: 
  - identify-sql-performance-sql-server
  - identify-sql-performance-azure
  - sql-server-memory-pressure
  - sql-server-io-pressure
  - sql-server-cpu-pressure
---
So you've identified that your SQL Server is under memory pressure. What can you do about it?

<!--endintro-->

If SQL Server is the primary consumer, then read up on reducing SQL Server memory usage, or whether more memory is appropriate for your workload.

## Identify non SQL engine related usage

Run

```sql
select * from sys.dm_os_memory_clerks where type='MEMORYCLERK_HOST'
```

This isolates a few of the SQL processes that aren't part of the SQL Server engine.
Look for high memory usage for OLE DB providers (MSOLEDBSQL), SQL Native Client (SQLNCLI*) and so on.
This may indicate using some non core features and you should evaluate whether these are necessary. Non core features are things like running .Net CLR code, translating queries to things like OLE DB and other things that aren't strictly database operations.

## Identify SQL engine related usage

Try running the following query. It categorises the various memory allocations SQL Server has made.

```sql
SELECT pages_kb, type, name, virtual_memory_committed_kb, awe_allocated_kb
FROM sys.dm_os_memory_clerks
ORDER BY pages_kb DESC
```

This should allow you to identify what is consuming the most memory.

### MEMORYCLERK_SQLQERESERVATIONS

If the memory clerk MEMORYCLERK_SQLQERESERVATIONS is consuming memory, identify queries that are using huge memory grants and optimize them via indexes, rewrite them (remove ORDER by, for example).
For more information

* [Brent Ozar on Memory Grants](https://www.brentozar.com/blitz/memory-grants/)
* [Microsoft Learn on Troubleshooting Memory Grant Issues](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/performance/troubleshoot-memory-grant-issues)

### OBJECTSTORE_LOCK_MANAGER

The most common example is OBJECTSTORE_LOCK_MANAGER consuming large amounts of memory. This is indicative of a large number of locks being obtained by the server. Often this is due to poor indexing meaning there are locks on far more objects than are required.
Another option is shortening the length of any transactions.

### CACHESTORE_SQLCP

This indicates a large number of ad-hoc query plans are cached. Identify non-parameterized queries whose query plans can't be reused and parameterize them by converting to stored procedures, using sp_executesql, or by using FORCED parameterization. If you have enabled trace flag 174, you may disable it to see if this resolves the problem.

You can use the sys.dm_exec_cached_plans dynamic management view to identify non-parameterized queries. This view returns a row for each query plan that is cached by SQL Server. You can filter the results to show only non-parameterized queries by checking the usecounts column value. If the usecounts column value is 1, the query is non-parameterized 1. Alternatively look for the objtype column containing "Adhoc".

Once you have identified non-parameterized queries whose query plans can’t be reused, you can parameterize them by converting them to use parameterized SQL, use stored procedures, use sp_executesql or use forced parameterization.

### CACHESTORE_OBJCP

If the object plan cache store CACHESTORE_OBJCP is consuming too much memory, identify which stored procedures, functions, or triggers are using large amounts of memory and possibly redesign the application to eliminate the majority of them. Commonly, this may happen due to large amounts of databases or database schemas with hundreds of procedures, functions or triggers in them.

## Release memory inside SQL Server

You can run one or more of the following DBCC commands to free several SQL Server memory caches:

``` sql
DBCC FREESYSTEMCACHE
```

``` sql
DBCC FREESESSIONCACHE
```

``` sql
DBCC FREEPROCCACHE
```

## Restart SQL Server service

In some cases, if you need to deal with critical exhaustion of memory and SQL Server isn't able to process queries, you can consider restarting the service.

## Add more RAM on the physical or virtual server

If the problem continues, you need to investigate further and possibly increase server resources (RAM).
