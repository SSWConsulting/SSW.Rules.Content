---
seoDescription: Do you know that AND is much more efficient than OR in a WHERE clause?
type: rule
archivedreason:
title: Do you know that AND is much more efficient than OR in a WHERE clause?
guid: b4be79d9-6bf8-4b31-b222-30faff037d98
uri: sqlperf-use-and-instead-of-or
created: 2024-07-23T07:26:54.0000000Z
authors:
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related:
  - sqlperf-reduce-table-size
  - sqlperf-select-required-columns
  - sqlperf-verify-indexes-used
  - sqlperf-avoid-implicit-type-conversions
  - sqlperf-avoid-looping
  - sqlperf-minimise-large-writes
---

To understand why this is the case it takes a little bit of thought.
<!--endintro-->

 When doing an OR, the server needs to get all the rows that match the first clause in the OR statement. Then it needs to get all the rows that match and then join the 2 results together. If you think about it this is just doing a union and you can generally write a statement with an OR using a UNION instead and the performance will improve. It will however be a bit less readable.

```sql
SELECT Id, Location, DownVotes FROM dbo.Users WHERE location = 'USA' OR DownVotes > 5;

SELECT Id, Location, DownVotes FROM dbo.Users WHERE location = 'USA'
UNION 
SELECT Id, Location, DownVotes FROM dbo.Users WHERE DownVotes > 5
```

Now if you consider an AND, it's the same as an intersection. You can find all the rows that match the first clause, and then immediately check the row matches the second clause before adding it to the results.
