---
seoDescription: Do you keep database tables small?
type: rule
archivedreason:
title: Do you keep database tables small?
guid: cd4ffbd0-4a01-4229-9de3-c45207ebb07b
uri: sqlperf-reduce-table-size
created: 2024-07-23T07:26:54.0000000Z
authors:
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related:
  - sqlperf-select-required-columns
  - sqlperf-verify-indexes-used
  - sqlperf-avoid-implicit-type-conversions
  - sqlperf-avoid-looping
  - sqlperf-use-and-instead-of-or
  - sqlperf-minimise-large-writes
---

Reading data from smaller tables is much faster. How can you keep the amount of data stored down.

<!--endintro-->

There are a number of reasons to keep table sizes small.

* Large tables take longer to read and update
* They also take up more space in the databases buffer cache
* They take up extra disk space

There are many solutions to avoiding tables getting too big. If only a small subset of the data is ever queried from, then you can archive unused data out to separate tables. This solution often works for sales based systems where transactions greater than a month old may never be read from again.

Another way to reduce table size is to look carefully at the datatypes for each of the columns in the database. For instance using **nvarchar(500)** for telephone number storage is overdoing it, the 500 could be reduced to somewhere around 25 saving a vast amount of storage for every row in the table. Also looking at the size and accuracy of numeric columns. Often integer percentages are stored in int64s instead of bytes and so on.

Table partitioning is another strategy that can be used to achieve similar improvements. But it is much harder to setup and maintain and is probably best only used if there is a professional Database Administrator available to manage it.
