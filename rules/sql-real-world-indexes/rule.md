---
seoDescription: Understanding how SQL indexes work and common real world ways of visualising them
type: rule
archivedreason:
title: Do you know how to visualize SQL indexes?
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

It's hard to understand what indexes are on SQL Databases. Find out how to visualize what's happening so you can easily follow what your database queries are doing.

Database indexes get their name from book indexes because they work similarly. To grasp how they function, imagine the rows in your table as pages in a book. Then, consider what kind of index in the book would help you quickly find the information you need.

<!--endintro-->

`youtube: https://www.youtube.com/watch?v=KkRpgtwBXvI`
**Video: How to visualize SQL indexes? | Bryden Oliver | SSW Rules (3 min)**

For instance in a recipe book that contains many types of dishes, you might want an index of the type of recipe. You may also have an index based on the recipe name, or maybe by ingredient.

![Figure: Typical book index](index.png)

```sql
SELECT *
FROM Badges
WHERE Name = 'John Doe';
```

::: bad
Bad example: Using a table scan - the DB needs to look at every row to find the result
:::

```sql
CREATE INDEX IX_Name_Date
ON dbo.Badges(Name) INCLUDE (Location);

SELECT *
FROM Badges
WHERE Name = 'John Doe';
```

::: good
Good example: Using an index - DB can quickly find the result
:::

By using the index, the database can quickly locate the rows where "Name" is 'John Doe' without scanning every row. This approach significantly improves query performance.

## Visualizing indexes

Another useful thing to know is that if you'd like to see what the index looks like and try using it manually to fulfil your query (this a great way to verify you got the index correct) then you can do the following.

Just write a `SELECT` statement that contains all the columns you are including in the index. Use an `ORDER BY` based on the columns in the Index Key to get the data sorted just like the index you are planning to create.

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

Note how the "Name" and "Date", which are the index keys, are included in the `ORDER BY` clause and the "Location" is only in the requested columns.

If you'd like to know more or see this in action, check out [How to Plan for Database Performance](https://youtu.be/l18ltcOVN4I)
