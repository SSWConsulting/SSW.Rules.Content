---
seoDescription: Do you avoid looping in database queries?
type: rule
archivedreason:
title: Do you avoid looping in database queries?
guid: d17571ce-30ca-4007-8b92-b2a7e467fc2b
uri: sqlperf-avoid-looping
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

It's very inefficient to loop in database queries. You should avoid it wherever possible.

<!--endintro-->
