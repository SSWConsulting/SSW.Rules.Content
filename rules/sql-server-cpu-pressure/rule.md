---
type: rule
archivedreason: 
title: What to do about SQL Server CPU Pressure?
guid: 870f4673-3a45-48d9-b73d-14921a77bc70
uri: sql-server-cpu-pressure
created: 2023-12-27T07:26:54.0000000Z
authors:
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related: 
  - identify-sql-performance-sql-server
  - identify-sql-performance-azure
  - sql-server-memory-pressure
  - sql-server-io-pressure
---
So you've identified that your SQL Server is under CPU pressure. What can you do about it?

<!--endintro-->

Here's a simple in-depth presentation covering things that can help reduce CPU pressure.

1. Throw hardware at the problem
2. Update the index statistics
3. Identify high CPU queries
4. Identify poor queries (reading too much data either columns or rows)
5. Identify missing indexes

## Add more CPUs

In many situations, the problem is poorly specifying the hardware configuration for your SQL Server. It's worth thinking about whether increasing the server specifications is the easiest solution, or whether optimising the applications are a better choice.

## Update index statistics

This can be achieved by

``` sql
exec sp_updatestats
```

Be aware that this can be expensive and as such using it all the time to avoid problems is not a great solution. But as a one off to verify whether your problem is a statistics issue, this is perfect.

## Identifying high CPU queries

The following sql identifies high CPU queries running right now.

```sql
SELECT TOP 10 s.session_id,
           r.status,
           r.cpu_time,
           r.logical_reads,
           r.reads,
           r.writes,
           r.total_elapsed_time / (1000 * 60) 'Elaps M',
           SUBSTRING(st.TEXT, (r.statement_start_offset / 2) + 1,
           ((CASE r.statement_end_offset
                WHEN -1 THEN DATALENGTH(st.TEXT)
                ELSE r.statement_end_offset
            END - r.statement_start_offset) / 2) + 1) AS statement_text,
           COALESCE(QUOTENAME(DB_NAME(st.dbid)) + N'.' + QUOTENAME(OBJECT_SCHEMA_NAME(st.objectid, st.dbid)) 
           + N'.' + QUOTENAME(OBJECT_NAME(st.objectid, st.dbid)), '') AS command_text,
           r.command,
           s.login_name,
           s.host_name,
           s.program_name,
           s.last_request_end_time,
           s.login_time,
           r.open_transaction_count
FROM sys.dm_exec_sessions AS s
JOIN sys.dm_exec_requests AS r ON r.session_id = s.session_id CROSS APPLY sys.Dm_exec_sql_text(r.sql_handle) AS st
WHERE r.session_id != @@SPID
ORDER BY r.cpu_time DESC
```

If queries aren't driving the CPU currently, try the following query.

``` sql
SELECT TOP 10 st.text AS batch_text,
    SUBSTRING(st.TEXT, (qs.statement_start_offset / 2) + 1, ((CASE qs.statement_end_offset WHEN - 1 THEN DATALENGTH(st.TEXT) ELSE qs.statement_end_offset END - qs.statement_start_offset) / 2) + 1) AS statement_text,
    (qs.total_worker_time / 1000) / qs.execution_count AS avg_cpu_time_ms,
    (qs.total_elapsed_time / 1000) / qs.execution_count AS avg_elapsed_time_ms,
    (qs.total_logical_reads / qs.execution_count) AS avg_logical_reads,
    (qs.total_worker_time / 1000) AS cumulative_cpu_time_all_executions_ms,
    (qs.total_elapsed_time / 1000) AS cumulative_elapsed_time_all_executions_ms
FROM sys.dm_exec_query_stats qs
CROSS APPLY sys.dm_exec_sql_text(sql_handle) st
ORDER BY (qs.total_worker_time / qs.execution_count) DESC
```

## Identify missing indexes

Indexes can dramatically improve query performance. SQL Server has inbuilt mechanisms to try and identify indexes that would aid a particular query. Running the following SQL identifies the 50 queries consuming the most CPU where SQL Server has identified that there is potentially a missing index.

``` sql
SELECT
    qs_cpu.total_worker_time / 1000 AS total_cpu_time_ms,
    q.[text],
    p.query_plan,
    qs_cpu.execution_count,
    q.dbid,
    q.objectid,
    q.encrypted AS text_encrypted
FROM
    (SELECT TOP 50 qs.plan_handle,
     qs.total_worker_time,
     qs.execution_count FROM sys.dm_exec_query_stats qs ORDER BY qs.total_worker_time DESC) AS qs_cpu
CROSS APPLY sys.dm_exec_sql_text(plan_handle) AS q
CROSS APPLY sys.dm_exec_query_plan(plan_handle) p
WHERE p.query_plan.exist('declare namespace 
        qplan = "http://schemas.microsoft.com/sqlserver/2004/07/showplan";
        //qplan:MissingIndexes')=1
```

This is super useful for giving suggestions. Otherwise, you may need to manually identify potential indexes and test those.

`youtube: https://youtu.be/l18ltcOVN4I?si=Ejf0sGKECfuqFw2L`

## Identifying parameter-sensitive problems

Try running

``` sql
DBCC FREEPROCCACHE
```

This will empty the plan cache. If this resolves the issue, then it's probably a parameter-sensitive problem.

*Note* DBCC is an acronym for Database Console Command and identifies things that do not denote structured queries.
