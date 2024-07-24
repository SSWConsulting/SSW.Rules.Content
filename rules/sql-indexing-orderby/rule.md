---
seoDescription: How to index SQL ORDER BY clauses.
type: rule
archivedreason:
title: Do you know how to index SQL ORDER BY clauses?
guid: 0c72c6f6-3a18-42a4-a733-5d5147d89506
uri: sql-indexing-orderby
created: 2024-07-22T07:26:54.0000000Z
authors:
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related:
  - sql-indexing-joins
  - sql-indexing-testing
  - sql-real-world-indexes
  - sql-indexing-where
---

So you've identified that you need to improve the performance of a SQL ORDER BY clause. How can you create an index to improve the performance?

<!--endintro-->

When creating indexes for your SQL tables, creating indexes to improve the performance of ORDER BY clauses is by far the easiest index to create.

## Creating the index

Basically just take the columns from the ORDER BY and drop them into the index definition in the same order.

So for example if you want to optimize the following query by providing an appropriate index:

```sql
SELECT
  DisplayName, Location, FullName
FROM
  dbo.Users
ORDER BY
  DisplayName, Location
```

The corresponding index definition would look like:

```sql
CREATE INDEX IX_DisplayName_Location ON dbo.Users (DisplayName, Location)
```

## Including extra columns

One other thing you can do when creating indexes is to include extra columns not related to the order of the rows in the index. So in the example above, the FullName column appears in the list of columns requested by the query.

If you don't include FullName in the index at all, then the database engine then has to go back to the orginal table to retrieve the values for that column.

You can include the FullName column in the index by adding an INCLUDE clause to the index definition.

```sql
CREATE INDEX IX_DisplayName_Location ON dbo.Users (DisplayName, Location) INCLUDE (FullName)
```

Be aware that including columns in an index does make the index bigger. So deciding whether to include extra columns or not is a tradeoff between disk space, the extra time it takes to write the index, the extra disk io required when reading back the index, against the improvement achieved for the queries in question.

If queries consistently want the same small subset of the columns on a table then this will generally be a good optimization.

Also, it is often better to include the **included** columns at the end of the index key as there is very little benefit unless the size of the **included** columns is quite large (think large fixed length strings).
