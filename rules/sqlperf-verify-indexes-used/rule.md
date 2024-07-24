---
seoDescription: Verify SQL indexes are being used
type: rule
archivedreason:
title: Do you know how to verify SQL indexes are being used?
guid: 0df7ba89-a104-4668-b6f0-4ac9e77bbb96
uri: sqlperf-verify-indexes-used
created: 2024-07-23T07:26:54.0000000Z
authors:
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related:
  - sqlperf-reduce-table-size
  - sqlperf-select-required-columns
  - sqlperf-avoid-implicit-type-conversions
  - sqlperf-avoid-looping
  - sqlperf-use-and-instead-of-or
  - sqlperf-minimise-large-writes  
---

So you've created some indexes on your database tables. How can you tell if they are being used by your queries?

<!--endintro-->

You'd be surprised to find out how often the indexes that have been defined on a table are not being used. As such it's worth checking that your indexes are being used.

## Ways to verify

If you know the exact query being run, you can simply run the query in SQL Server Management Studio or Azure Data Studio with "Include Actual Execution Plan" turned on. Then check the execution plan to verify what indexes were used.

The second option is to use the query below. It retrieves the index usage stats. The WHERE clause can be adjusted to ensure you only get the indexes you are interested in.
Then you can run this query, then perform the operations in your application that you think should use the index, and then rerun this query. If the index was used you should see the UserSeeks, UserScans or UserLookups increase between the 2 runs.

```sql
SELECT 
    object_name(s.[object_id]) AS TableName,
    i.name AS IndexName,
    i.index_id AS IndexID,
    us.user_seeks AS UserSeeks,
    us.user_scans AS UserScans,
    us.user_lookups AS UserLookups,
    us.user_updates AS UserUpdates
FROM 
    sys.dm_db_index_usage_stats us
INNER JOIN 
    sys.indexes i ON (us.object_id = i.object_id AND us.index_id = i.index_id)
INNER JOIN 
    sys.objects s ON us.object_id = s.object_id
WHERE 
    s.type = 'U' -- Filter for user tables only
--    AND i.type_desc = 'NONCLUSTERED' -- Filter for non-clustered indexes
--    AND (us.user_seeks = 0 AND us.user_scans = 0) -- Filter for unused indexes
ORDER BY 
    TableName, IndexName;
```

Be aware the statistics in this query are reset when the server is restarted or a user explicitly resets the statistics.
