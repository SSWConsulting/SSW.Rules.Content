---
type: rule
archivedreason: 
title: Schema - Do you avoid using indexes on RowGuid column?
guid: 49e77277-e4f8-44a0-bc2c-3d7d487714a0
uri: avoid-using-indexes-on-rowguid-column
created: 2019-11-06T01:32:42.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- schema-do-you-avoid-using-indexes-on-rowguid-column

---

RowGuids (uniqueidentifier) are large fields (16 bytes) and are basically going to ALWAYS be unique.


SQL Server adds a RowGUID column to all tables if you are using Merge Replication (but doesn't add an index).

RowGuids in general slow things down. Some people may consider using a RowGuid as their primary key. This is a bad idea because the index is going to be quite slow.... you are searching a large field. It goes without saying, NEVER have clustered index on a RowGuid column.


<!--endintro-->

Another little annoyance with RowGuids is when you are searching for one. You can't use &gt; or &lt; on a RowGuid column.

**Note: ** There are not many cases where a RowGuid should have an index on it.

Be aware that SQL server adds this column when you perform merge replication. There are not many cases where this should have an index on it.
