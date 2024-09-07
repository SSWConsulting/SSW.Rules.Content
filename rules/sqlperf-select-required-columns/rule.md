---
seoDescription: Do you only SELECT the columns you require?
type: rule
archivedreason:
title: Do you only SELECT the columns you require?
guid: db46290f-e1ab-4279-8833-f5a1d54c529f
uri: sqlperf-select-required-columns
created: 2024-07-23T07:26:54.0000000Z
authors:
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related:
  - sqlperf-reduce-table-size
  - sqlperf-verify-indexes-used
  - sqlperf-avoid-implicit-type-conversions
  - sqlperf-avoid-looping
  - sqlperf-use-and-instead-of-or
  - sqlperf-minimise-large-writes
---

It can be expensive retrieving all the columns of a table. Find out why.

<!--endintro-->

Retrieving all the columns in a table is a common pattern.

```sql
SELECT * FROM Users
```

This is not an unusual statement to see. However statements of this type should not be employed inside an application. It's important to minimise the number of columns returned by queries because:

* It takes more network bandwidth to transmit the results
* It takes extra CPU at the database and the caller to encode/decode the response
* In cases where all the columns required are available in an index, retrieving all columns can cause reading an index and then the main table to retrieve the remaining columns
