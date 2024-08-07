---
seoDescription: Do you avoid implicit data type conversions in SQL queries?
type: rule
archivedreason:
title: Do you avoid implicit data type conversions in SQL queries?
guid: 20eee575-a2ea-4283-9462-681f6ffc85d5
uri: sqlperf-avoid-implicit-type-conversions
created: 2024-07-23T07:26:54.0000000Z
authors:
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related:
  - sqlperf-reduce-table-size
  - sqlperf-select-required-columns
  - sqlperf-verify-indexes-used
  - sqlperf-avoid-implicit-type-conversions
  - sqlperf-use-and-instead-of-or
  - sqlperf-minimise-large-writes
---

Specifying the wrong data types in SQL queries can make the server scan your whole table. That can take ages.

<!--endintro-->

It doesn't seem right that getting the data type wrong can result in the database having to walk an entire table, but if we think about the following 2 queries.

```sql
SELECT * FROM dbo.VotesString WHERE PostId = '9999997'
SELECT * FROM dbo.VotesString WHERE PostId = 9999997
```

**Note** In the VotesString table, the PostId is a string column, and there is an index on it.

So the first query can seek straight to the correct row, and return it straight back. Almost no effort.

But the second case where we are comparing the PostId as an integer, there are multiple integer representations of the same value. For instance '009999997' or in exponential form. Hence the server has to walk through every row of that column and try to cast the string to an integer and then perform the comparison.

So the rule of thumb is always make sure any comparisons have the same data types.
