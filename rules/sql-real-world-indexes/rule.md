---
seoDescription: Understanding how SQL indexes work and common real world ways of visualising them
type: rule
archivedreason:
title: Do you know how to visualise SQL indexes?
guid: 668bb820-5ef4-4f8e-872f-04e1846ea982
uri: sql-real-world-indexes
created: 2024-07-24T07:26:54.0000000Z
authors:
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related:
  - sql-indexing-orderby
  - sql-indexing-testing
  - sql-indexing-joins
  - sql-indexing-where
---

It's hard to understand what indexes are on SQL Databases. Find out how to visualise what's happening so you can easily follow what your database queries are doing.

<!--endintro-->

The reason that indexes are called indexes is because they are very similar to how indexes in books work. As such, a good way to understand what indexes might work well is to think of the rows of data in your table as the pages in a book. Then based on the information think about what would be the best index you might find at the end of the book to allow you to quickly answer the query.

For instance in a recipe book that contains main courses, you might want an index of the main ingredient as people may want to quickly find all of the chicken dishes. You may also have an index based on the recipe name.

Another useful thing to know is that if you'd like to see what the index looks like and try using it manually to fulfil your query (this a great way to verify you got the index correct) then you can do the following.

Just write a SELECT statement that contains all the columns you are including in the index. Use an ORDER BY based on the columns in the Index Key to get the data sorted just like the index you are planning to create.

Then try fulfilling some simple queries. A good way to know if your index is going to significantly improve performance is if you can quickly seek to the exact record/s you need rather than having to look at every single row one by one.

For example if you are planning the following index:

```sql
CREATE INDEX IX_Name_Date
  ON dbo.Badges(Name,Date) INCLUDE (Location);
```

Then you can visualise the index by running the following query:

```sql
SELECT
  Name, Date, Location
FROM
  dbo.Badges
ORDER BY
  Name, Date
```

Note how the Name and Date which are the index keys, are included in the ORDER BY clause and the Location is only in the requested columns.

If you'd like to know more or see this in action, check out [How to Plan for Database Performance](https://youtu.be/l18ltcOVN4I)
