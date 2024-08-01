---
seoDescription: SQL Server automatic index tuning.
type: rule
archivedreason:
title: Do you know how to use SQL Server's automatic index tuning?
guid: e7094bfc-668d-4928-9963-e6256bb9bec7
uri: sql-automatic-index-tuning
created: 2024-07-26T07:26:54.0000000Z
authors:
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related:
  - sql-indexing-orderby
  - sql-indexing-testing
  - sql-real-world-indexes
  - sql-indexing-where
---

Feel like you don't know enough to manage the indexes on your SQL databases? SQL Server and Azure SQL databases have that covered for you.

<!--endintro-->

In SQL Server 2022 there are lots of features that make day to day database management much easier. These were introduced in SQL Server 2017 and are continually being improved. The Automatic Tuning features can either be used to make recommendations of changes to indexes and query plans, or it can be allowed to take control and make the recommended changes without user intervention.

In small organizations without a dedicated database administrator, turning these features on is strongly recommended. Also for less important servers it can free up the database administrator's time to deal with only the most business critical databases and servers.

See [detailed information on this feature](https://learn.microsoft.com/en-us/sql/relational-databases/automatic-tuning/).
