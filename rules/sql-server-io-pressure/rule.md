---
type: rule
archivedreason: 
title: What to do about SQL Server IO Pressure?
guid: 83475165-1eba-47bc-a243-b9d4706ae5d5
uri: sql-server-io-pressure
created: 2023-12-27T07:26:54.0000000Z
authors:
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related: 
  - identify-sql-performance-sql-server
  - identify-sql-performance-azure
  - sql-server-cpu-pressure
  - sql-server-memory-pressure
---
So you've identified that your SQL Server is under IO pressure. What can you do about it?

<!--endintro-->

If disk is being used by SQL Server, try the following:

1. Identify any high IO queries and optimize
2. Check whether more memory might allow caching to dramatically reduce disk IO
3. Identify whether database files under high load can be on separate disks, maybe splitting each file up into several each on a separate disk.

## Identify any high IO queries and optimize

Use the Query Store view Top Resource Consuming Queries in SSMS. Look for high values of Logical Reads, Logical Writes and Physical Reads. These indicate IO intensive queries.

Here's a simple in-depth presentation on techniques to optimize SQL queries and reduce the IO required.

`youtube: https://youtu.be/l18ltcOVN4I?si=Ejf0sGKECfuqFw2L`

## Try adding more memory

This solution is often a quick and easy solution that may be less expensive than more extensive optimization.
If the cost is not overly high, it often provides a better return on investment than spending large amounts of effort on optimization.

## Identify the database files under pressure

Use the following query from the Microsoft Learn article [Troubleshoot slow SQL Server performance caused by I/O issues](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/performance/troubleshoot-sql-io-performance) to identify which database files are under pressure.

```sql
   SELECT   LEFT(mf.physical_name,100),   
         ReadLatency = CASE WHEN num_of_reads = 0 THEN 0 ELSE (io_stall_read_ms / num_of_reads) END, 
         WriteLatency = CASE WHEN num_of_writes = 0 THEN 0 ELSE (io_stall_write_ms / num_of_writes) END, 
         AvgLatency =  CASE WHEN (num_of_reads = 0 AND num_of_writes = 0) THEN 0 
                        ELSE (io_stall / (num_of_reads + num_of_writes)) END,
         LatencyAssessment = CASE WHEN (num_of_reads = 0 AND num_of_writes = 0) THEN 'No data' ELSE 
               CASE WHEN (io_stall / (num_of_reads + num_of_writes)) < 2 THEN 'Excellent' 
                    WHEN (io_stall / (num_of_reads + num_of_writes)) BETWEEN 2 AND 5 THEN 'Very good' 
                    WHEN (io_stall / (num_of_reads + num_of_writes)) BETWEEN 6 AND 15 THEN 'Good' 
                    WHEN (io_stall / (num_of_reads + num_of_writes)) BETWEEN 16 AND 100 THEN 'Poor' 
                    WHEN (io_stall / (num_of_reads + num_of_writes)) BETWEEN 100 AND 500 THEN  'Bad' 
                    ELSE 'Deplorable' END  END, 
         [Avg KBs/Transfer] =  CASE WHEN (num_of_reads = 0 AND num_of_writes = 0) THEN 0 
                    ELSE ((([num_of_bytes_read] + [num_of_bytes_written]) / (num_of_reads + num_of_writes)) / 1024) END, 
         LEFT (mf.physical_name, 2) AS Volume, 
         LEFT(DB_NAME (vfs.database_id),32) AS [Database Name]
       FROM sys.dm_io_virtual_file_stats (NULL,NULL) AS vfs  
       JOIN sys.master_files AS mf ON vfs.database_id = mf.database_id 
         AND vfs.file_id = mf.file_id 
       ORDER BY AvgLatency DESC
```

This then gives somewhere to investigate.

## What the IO related wait types mean

You can find out what types of IO waits are occuring in SQL Server with the following query.

```sql

SELECT r.session_id, r.wait_type, r.wait_time as wait_time_ms
                                       FROM sys.dm_exec_requests r JOIN sys.dm_exec_sessions s
                                        ON r.session_id = s.session_id
                                       WHERE wait_type in (
                                        'PAGEIOLATCH_EX', 
                                        'PAGEIOLATCH_SH', 
                                        'PAGEIOLATCH_UP',
                                        'WRITELOG',
                                        'ASYNC_IO_COMPLETION',
                                        'IO_COMPLETION',
                                        'BACKUPIO')
                                       AND is_user_process = 1
```

If these waits exceed 10-15 milliseconds consistently, I/O is considered a bottleneck.

### PAGEIOLATCH_EX

Occurs when a task is waiting on a latch for a data or index page (buffer) in an I/O request. The latch request is in the Exclusive mode. An Exclusive mode is used when the buffer is being written to disk. Long waits may indicate problems with the disk subsystem.

### PAGEIOLATCH_SH

Occurs when a task is waiting on a latch for a data or index page (buffer) in an I/O request. The latch request is in the Shared mode. The Shared mode is used when the buffer is being read from the disk. Long waits may indicate problems with the disk subsystem.

### PAGEIOLATCH_UP

Occurs when a task is waiting on a latch for a buffer in an I/O request. The latch request is in the Update mode. Long waits may indicate problems with the disk subsystem.

### WRITELOG

Occurs when a task is waiting for a transaction log flush to complete. A flush occurs when the Log Manager writes its temporary contents to disk. Common operations that cause log flushes are transaction commits and checkpoints.

Common reasons for long waits on WRITELOG are:

##### Transaction log disk latency

This is the most common cause of WRITELOG waits. Generally, the recommendation is to keep the data and log files on separate volumes. Transaction log writes are sequential writes while reading or writing data from a data file is random. Mixing data and log files on one drive volume (especially conventional spinning disk drives) will cause excessive disk head movement.

##### Too many VLFs

Too many virtual log files (VLFs) can cause WRITELOG waits. Too many VLFs can cause other types of issues, such as long recovery.

##### Too many small transactions

While large transactions can lead to blocking, too many small transactions can lead to another set of issues. If you don't explicitly begin a transaction, any insert, delete, or update will result in a transaction (we call this auto transaction). If you do 1,000 inserts in a loop, there will be 1,000 transactions generated. Each transaction in this example needs to commit, which results in a transaction log flush and 1,000 transaction flushes. When possible, group individual update, delete, or insert into a bigger transaction to reduce transaction log flushes and increase performance. This operation can lead to fewer WRITELOG waits.

##### Scheduling issues cause Log Writer threads to not get scheduled fast enough

Prior to SQL Server 2016, a single Log Writer thread performed all log writes. If there were issues with thread scheduling (for example, high CPU), both the Log Writer thread and log flushes could get delayed. In SQL Server 2016, up to four Log Writer threads were added to increase the log-writing throughput. See SQL 2016 - It Just Runs Faster: Multiple Log Writer Workers. In SQL Server 2019, up to eight Log Writer threads were added, which improves throughput even more. Also, in SQL Server 2019, each regular worker thread can do log writes directly instead of posting to the Log writer thread. With these improvements, WRITELOG waits would rarely be triggered by scheduling issues.

### ASYNC_IO_COMPLETION

Occurs when some of the following I/O activities happen:

* The Bulk Insert Provider ("Insert Bulk") uses this wait type when performing I/O.
* Reading Undo file in LogShipping and directing Async I/O for Log Shipping.
* Reading the actual data from the data files during a data backup.

### IO_COMPLETION

Occurs while waiting for I/O operations to complete. This wait type generally involves I/Os not related to data pages (buffers). Examples include:

* Reading and writing of sort/hash results from/to disk during a spill (check performance of tempdb storage).
* Reading and writing eager spools to disk (check tempdb storage).
* Reading log blocks from the transaction log (during any operation that causes the log to be read from disk for example, recovery).
* Reading a page from disk when database isn't set up yet.
* Copying pages to a database snapshot (Copy-on-Write).
* Closing database file and file uncompression.

### BACKUPIO

Occurs when a backup task is waiting for data, or is waiting for a buffer to store data. This type isn't typical, except when a task is waiting for a tape mount.
