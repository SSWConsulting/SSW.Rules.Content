---
seoDescription: Indexing SQL database JOINs.
type: rule
archivedreason:
title: Do you know how to index SQL JOINs?
guid: 303d37d9-2b0b-42a4-824e-1801a4babe7a
uri: sql-indexing-joins
created: 2024-07-24T07:26:54.0000000Z
authors:
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related:
  - sql-indexing-orderby
  - sql-indexing-testing
  - sql-real-world-indexes
  - sql-indexing-where
---

So you've identified that you need to improve the performance of a SQL JOIN. How can you create an index to improve the performance?

<!--endintro-->

Joins behave just like a where clause. So for this statement:

```sql
SELECT 
 u.DisplayName,
 c.CreationDate,
FROM
 dbo.Users u
 INNER JOIN dbo.Comments c ON u.Id = c.UserId
Where
 u.DisplayName = 'Jernej Kavka'
```

The following index would provide a performance increase.

```sql
CREATE INDEX IX_UserId_INCLUDES_CreationDate on dbo.Comments (UserId, CreationDate)
```

Note the fact that rather than including CreationDate in an included column it's been included in the indexed columns. That's because dates are a nice small column type, so the extra storage in the index tree nodes is negligible.
