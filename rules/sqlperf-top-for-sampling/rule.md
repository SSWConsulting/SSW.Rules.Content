---
seoDescription: Do you use TOP for sampling in your queries?
type: rule
archivedreason:
title: Do you use TOP for sampling in your queries?
guid: a11ed36c-da5e-49dc-bddc-9deffa03b858
uri: sqlperf-top-for-sampling
created: 2024-07-25T07:26:54.0000000Z
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

Top is an efficient way of identifying what a tables structure and data look like.

<!--endintro-->

Retrieving all the data in a table is a common pattern especially when someone is looking into a production incident. If the table in question is a large table, grabbing all the rows back may make the problem worse.

```sql
SELECT * FROM Users
```

Using TOP to reduce the number of rows being returned makes this a much less expensive operation.

```sql
SELECT TOP 20 FROM Users
```

TOP works with filtering and joining, so you can use it to get a sample of only the rows you are interested in.
