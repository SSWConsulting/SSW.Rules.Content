---
seoDescription: Do you avoid joining too many tables?
type: rule
archivedreason:
title: Do you avoid joining too many tables?
guid: c1f2c427-f53f-4d41-aa33-f835fd8ffb91
uri: sqlperf-too-many-joins
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

Joining too many tables in a single query can cause issues. Find out why.

<!--endintro-->

`youtube: https://www.youtube.com/embed/ntmAmb7vDu4`  
**Video: Avoid too many JOINs for SQL performance | Bryden Oliver (2 min)**

When a query is sent to a database server, the server will then try and optimise that query into the best set of steps that will retrieve the required results.
However the optimisers begin to struggle somewhere between around 4-7 tables being joined in a single query. When they struggle they tend to abandon optimisation and just brute force without using any of the available indexes.
