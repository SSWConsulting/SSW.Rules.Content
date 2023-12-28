---
type: rule
archivedreason: 
title: Identifying the cause of SQL Server performance problems
guid: 46f8cae3-7aa0-4313-9ac2-8e9d84ef236c
uri: identify-sql-performance-sql-server
created: 2023-12-27T07:26:54.0000000Z
authors:
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related: 
  - identify-sql-performance-azure
  - identify-sql-performance-sql-server
  - sql-server-cpu-pressure
  - sql-server-io-pressure
  - sql-server-memory-pressure
---
## Identifying CPU Pressure
When looking at SQL Server, you often get performance issues, but how can you figure out what might be the cause?

<!--endintro-->

To figure out whether the SQL Server itself is experiencing CPU pressure, fire up Task manager and take a look at the CPU usage. If the CPU is high and SQL Server is not the primary consumer, evaluate whether you can separate the CPU consuming workload from your SQL Server by moving one onto another server.

A good way to identify if SQL Server is experiencing CPU Pressure internally is to try the following SQL

``` sql
DECLARE @BatchRequests bigint;
DECLARE @Compilations bigint;
DECLARE @Recompiles bigint;

select @BatchRequests = [Batch Requests/sec], @Compilations = [SQL Compilations/sec], @Recompiles = [SQL Re-Compilations/sec] from 
(select cntr_value, counter_name from sys.dm_os_performance_counters 
where counter_name in ('Batch Requests/sec', 'SQL Compilations/sec' , 'SQL Re-Compilations/sec') ) as SourceTable PIVOT
(max(cntr_value) for counter_name in ([Batch Requests/sec], [SQL Compilations/sec], [SQL Re-Compilations/sec])) as pivottable

WAITFOR DELAY '00:01:00';

select ([Batch Requests/sec] - @BatchRequests) / 60 as BatchesPerSec, ([SQL Compilations/sec] - @Compilations) / 60 AS CompilationsPerSec, ([SQL Re-Compilations/sec] - @Recompiles) / 60 as RecompilesPerSec from 
(select cntr_value, counter_name from sys.dm_os_performance_counters 
where counter_name in ('Batch Requests/sec', 'SQL Compilations/sec' , 'SQL Re-Compilations/sec') ) as SourceTable PIVOT
(max(cntr_value) for counter_name in ([Batch Requests/sec], [SQL Compilations/sec], [SQL Re-Compilations/sec])) as pivottable
```

The BatchesPerSec should be under 1000. Compilations should be less than 10% of the BatchesPerSec and the RecompilesPerSec should be less then 10% of the CompilationsPerSec.

[LINK to what to do about CPU Pressure rule]

## Identifying Memory Pressure
Open Task manager, select Performance > Memory to check whether all the memory is being used.

Use Perfmon and monitor these counters:
- Process\Working Set - to check individual apps' memory usage.
- Memory\Available MBytes - to check overall memory usage.

If any of these are using all of the memory then SQL Server may be experiencing memory pressure.
If the memory is not being used by SQL Server, then evaluate whether SQL Server and the other workload should be on separate servers.
Otherwise: [LINK to what to do about memory Pressure rule]

## Identifying IO Pressure

Open Task Manager, select Performance > Disk (*) to check for disks being pushed to their limits.

Monitor the following using perfmon:
- LogicalDisk\Disk Bytes/sec
- LogicalDisk\Avg. Disk sec/Transfer

If any disks are being pushed to their limits, is SQL Server performing the IO. If not, can the application doing all the disk access be on a separate server to your SQL Server.

Otherwise : [LINK to what to do about IO Pressure rule]