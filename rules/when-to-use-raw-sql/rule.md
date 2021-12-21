---
type: rule
title: Do you know when to use raw sql?
uri: when-to-use-raw-sql
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
related:
  - implement-business-logic-in-middle-tier
created: 2021-12-13T17:27:02.725Z
guid: b3f3734b-ef73-4f84-972a-efe7a5a0bc24
---
Raw SQL comes with risks but sometimes it is the best solution.

<!--endintro-->

Using raw SQL involves taking care of SQL injection and other risks, however there are a number of situations where it may be the best solution.

The most obvious is a SQL UPDATE statement which updates a large number of rows.

```
await context.Database.ExecuteSqlInterpolatedAsync($"UPDATE Employees SET Active = {activeState}", ct);
```

::: good
Good example - Updating a large number of rows quickly with SQL
:::