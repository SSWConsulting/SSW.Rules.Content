---
type: rule
title: Do you take care when casting IQueryable to IEnumerable?
uri: take-care-when-casting-iqueryable-to-ienumerable
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
created: 2021-12-13T17:00:03.219Z
guid: ee5bfbb5-7743-462b-bc8a-f32b3fb015b0
---
When you cast IQueryable to IEnumerable and then query the data from there, Entity Framework must collect the data at the point you do the cast. This can result in very significant extra database load, and extra processing on the client side.

**NOTE:** Using `.AsEnumerable()` achieves the same effect.

<!--endintro-->

### Counting

```cs
// All examples below will result in a SQL query similar to:
// SELECT * FROM Sales

// The ToList generates a list of all records client side and then counts them.
int count1 = context.Sales
    .ToList()
    .Count();

// This implicitly treats the sales as an enumerable and enumerates all the items to count them.
IEnumerable<Sale> sales = context.Sales;
int count2 = sales.Count;	

// EF Core will evaluate everything before `.AsEnumerable()` and after that line, everything is in-memory.
int count3 = context.Sales
    .AsEnumerable()
    .Count();
    
// This is the most common source of `IEnumerable` casting which can cause significant performance issues.
public IEnumerable<Sale> GetSales() => context.Sales;

// The code on the first glance looks alright but in fact it fetches the entire table from SQL Server
// because it receives the query as `IEnumerable` before running `.Count()`.
int count4 = GetSales().Count();
```

::: bad
Bad example - All these examples read the entire table instead of just returning the count from the database.
:::

```cs
// All of the examples below will result in SQL query:
// SELECT COUNT(*) FROM Sales
int count1 = context.Sales.Count();

IQueryable<Sale> query = _context.Sales;
int count2 = query.Count();

public IQueryable<Sale> GetSales() => context.Sales;
int count3 = GetSales().Count();
```

::: good
Good example - Only the count is returned by the query
:::

### Where

```cs
// All of the examples below will result in a SQL query like:
// SELECT * FROM Sales

List<Sale> sales1 = context.Sales
    .AsEnumerable()
    .Where(x => x.Id == 5)
    .ToList();

private IEnumerable<Sale> Sales { get { return context.Sales; } }
List<Sale> sales2 = Sales
    .Where(x => x.Id == 5)
    .ToList();
```

::: bad
Bad example - The whole table is returned from the database and then discarded in code.
:::

```cs
// All Examples will result in a SQL query like:
// SELECT * FROM Sales WHERE Id = 5

List<Sale> sales1 = context.Sales
    .Where(x => x.Id == 5)
    .ToList();

private IQueryable<Sale> Sales { get { return context.Sales; } }
List<Sale> sales2 = Sales
    .Where(x => x.Id == 5)
    .ToList();
```

::: good
Good example - Filtering is done on the database before returning data.
:::