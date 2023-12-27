---
type: rule
archivedreason: 
title: What to do about SQL Server IO Pressure?
guid: 83475165-1eba-47bc-a243-b9d4706ae5d5
uri: sql-performance-io-pressure
created: 2023-12-27T07:26:54.0000000Z
authors:
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related: 
  - identify-sql-performance-sql-server
  - identify-sql-performance-azure

---
So you've identified that your SQL Server is under IO pressure. What can you do about it?

<!--endintro-->



If disk is being used by SQL Server, try the following:
1. Identify any high IO queries and optimize
2. Check whether more memory might allow caching to dramatically reduce disk IO
3. Identify whether database files under high load can be on separate disks, maybe splitting each file up into several each on a separate disk.

