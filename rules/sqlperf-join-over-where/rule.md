---
seoDescription: Do you use JOIN instead of WHERE?
type: rule
archivedreason:
title: Do you use JOIN instead of WHERE?
guid: 0cfb92ec-6948-4a54-bcc6-b7005be34d26
uri: sqlperf-join-over-where
created: 2024-07-25T07:26:54.0000000Z
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

It's better to join tables together using a JOIN clause instead of a WHERE clause.
<!--endintro-->
There are several good reasons to use JOINs rather than WHERE clauses to join tables.
The first is that it keeps the joining of tables separate from the filtering. So it means when you see a WHERE clause you know it is being used to further filter data.

The second reason is that modern SQL optimisation engines optimise JOINs better than WHERE clauses. So your query will generally run faster with a JOIN.

Finally it's easier to express the various types of joins better with a JOIN as you can state INNER, OUTER and so on depending on how you'd like to join. This achieves the equivalent of intersections, unions and so on very clearly.
