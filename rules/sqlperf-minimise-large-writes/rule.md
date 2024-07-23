---
seoDescription: Large database writes are expensive, so should be avoided?
type: rule
archivedreason:
title: Do you avoid large database writes?
guid: b24619c6-3751-4780-8229-85b9e0121b43
uri: sqlperf-minimise-large-writes
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
  - sqlperf-use-and-instead-of-or
---

It can be very expensive to write large blocks of data into databases. What can you do instead?

<!--endintro-->

When data is written into a database table, any records being modified have to be locked. The more records being modified the more locks that are reuired. If there are enough locks going on, the server may choose to escalate the row locks into page or even table locks. This means that other queries are prevented from touching those records/pages/tables while the write query transaction is not complete.

Most databases have custom Bulk Update libraries which optimise these operations as much as possible, so using these will alleviate these issues somewhat.

The other thing to be aware of is that any indexes or foreign keys that contain the columns being updated by the writes will cause extra locking. This is one of the reasons that indexing is a balancing act between creating too few and too many indexes. Often you want a small number of indexes that improve query performance enough, rather than providing perfect coverage for all expected queries.

This one is often caused by the amount of locking that goes on.
Typically using Bulk Insert libraries you can avoid pain here. Be aware that the more foreign keys attached from or to your table, the worse this will get.
Indexes also have significant effect here.
