---
seoDescription: Optimize EF Core queries by using bulk inserts, batching queries, reducing SaveChanges calls, and using transactions for better performance.
type: rule
title: Do you optimize your EF Core queries?
uri: optimize-ef-core-queries
authors:
  - title: Toby Churches
    url: https://www.ssw.com.au/people/toby-churches/
created: 2025-03-07T14:15:55.753Z
guid: 4e9a9cb1-bf8f-4a2c-bc9a-1d5e0c94f8bb
---

EF Core provides a powerful way to interact with databases using .NET, but poor query optimization can lead to significant performance issues. Developers often fall into common pitfalls like inserting data in a loop, running excessive queries, or keeping track of too many entities. By following these best practices, you can improve performance and reduce database load.

<!--endintro-->

## 1. Perform bulk insertions instead of looping

One of the most common mistakes is inserting entities one by one inside a loop. This results in multiple round trips to the database, which is extremely inefficient.

::: greybox

```csharp
foreach (var item in items)
{
    context.MyEntities.Add(item);
    context.SaveChangesAsync();
}
```

:::
::: bad
Figure: Bad example – Calling `SaveChangesAsync()` inside a loop causes multiple database hits
:::

Instead, use **bulk insertion** techniques like `AddRangeAsync()` and call `SaveChangesAsync()` once:

::: greybox

```csharp
context.MyEntities.AddRangeAsync(items);
context.SaveChangesAsync();
```

:::
::: good
Figure: Good example – Using `AddRangeAsync()` minimizes database calls and improves performance
:::

For **even larger datasets**, consider using external libraries like **EF Core Bulk Extensions** for optimized bulk insert performance.

---

## 2. Batch queries to reduce database calls

When retrieving data in a loop, developers sometimes execute multiple queries instead of batching them upfront.

::: greybox

```csharp
foreach (var id in ids)
{
    var entity = context.MyEntities.FirstOrDefaultAsync(e => e.Id == id);
    ProcessEntity(entity);
}
```

:::
::: bad
Figure: Bad example – Each iteration performs a separate database query, leading to N queries
:::

If you know the approximate size of your dataset, and it is suitable for your database server, retrieve all records in a single query before processing:

::: greybox

```csharp
var entities = context.MyEntities.Where(e => ids.Contains(e.Id)).ToListAsync();
foreach (var entity in entities)
{
    ProcessEntity(entity);
}
```

:::
::: good
Figure: Good example – Fetches all required records in one query, reducing database load
:::

### Handling large datasets

If the dataset is **too large to fetch at once**, consider batching:

::: greybox

```csharp
int batchSize = 100;
for (int i = 0; i < ids.Count; i += batchSize)
{
    var batch = ids.Skip(i).Take(batchSize).ToList();
    var entities = context.MyEntities.Where(e => batch.Contains(e.Id)).ToList();
    ProcessEntities(entities);
}
```

:::
::: ok
Figure: OK example – Processes data in batches to balance efficiency and memory usage
:::

The benefit of loading data into memory at once is that you can process it more efficiently without making multiple database calls. This opens up opportunities for parallel processing and other optimizations on the application side.

---

## 3. Stop tracking entities when not needed

By default, EF Core tracks entities, which increases memory usage and slows down performance. If you're just **reading data** without modifying it, disable tracking.

::: greybox

```csharp
var entities = context.MyEntities.ToListAsync();
```

:::
::: bad
Figure: Bad example – Unnecessary tracking increases memory usage
:::

::: greybox

```csharp
var entities = context.MyEntities.AsNoTracking().ToListAsync();
```

:::
::: good
Figure: Good example – `AsNoTracking()` prevents EF Core from tracking entities, reducing memory usage
:::

::: info
**Note:** This optimization technique is not always applicable. If you need to modify entities (`context.SaveChangesAsync()`), you should leave tracking enabled to ensure changes are detected. Only disable tracking for read-only queries. see our [Rules to Better Entity Framework](/use-asnotracking-for-readonly-queries).
:::

---

## 4. Call `SaveChangesAsync()` less frequently

Each call to `SaveChangesAsync()` triggers a database transaction and commits changes to the database, which is costly in terms of performance.

::: greybox

```csharp
foreach (var entity in entities)
{
    entity.UpdatedAt = DateTime.UtcNow;
    context.SaveChangesAsync(); 
}
```

:::
::: bad
Figure: Bad example – Calling `SaveChangesAsync()` in a loop causes multiple transactions, slowing down performance
:::

::: greybox

```csharp
foreach (var entity in entities)
{
    entity.UpdatedAt = DateTime.UtcNow;
}
context.SaveChangesAsync();
```

:::
::: good
Figure: Good example – Updates all entities in memory first, then commits changes in a single transaction
:::

Whenever possible, defer calling `SaveChangesAsync()` until after all modifications have been made.

---

## 5. Use transactions to speed up performance

EF Core automatically wraps `SaveChangesAsync()` calls in a transaction, but **explicit transactions** allow multiple operations to be committed together, improving performance and reducing the risk of partial failures. When working with large data modifications, batch processing, or multiple related database operations, using transactions ensures **data consistency** and **reduces performance overhead**.

::: greybox

```csharp
foreach (var entity in entities)
{
    context.Add(entity);
    await context.SaveChangesAsync(); // Each iteration creates a separate transaction
}
```

:::
::: bad
Figure: Bad example – Each `SaveChangesAsync()` call inside the loop creates a separate transaction, leading to unnecessary database overhead
:::

::: greybox

```csharp
using var transaction = await context.Database.BeginTransactionAsync();
try
{
    foreach (var entity in entities)
    {
        context.Add(entity);
    }
    
    await context.SaveChangesAsync(); // One transaction instead of multiple
    await transaction.CommitAsync();
}
catch
{
    await transaction.RollbackAsync();
}
```

:::
::: good
Figure: Good example – Using an explicit transaction ensures all entities are added in a **single** transaction, reducing overhead and improving reliability
:::

### Combining transactions with batching

For very large datasets, committing everything in one transaction may still be inefficient. Instead, **process data in batches** while keeping transactions:

::: greybox

```csharp
int batchSize = 100;
using var transaction = await context.Database.BeginTransactionAsync();

try
{
    for (int i = 0; i < entities.Count; i += batchSize)
    {
        var batch = entities.Skip(i).Take(batchSize).ToList();
        context.AddRange(batch);
        await context.SaveChangesAsync();
    }

    await transaction.CommitAsync();
}
catch
{
    await transaction.RollbackAsync();
}
```

:::
::: good
Figure: Good example – Transactions combined with batching allow **efficient processing of large datasets** while keeping database transactions minimal
:::

### When to use transactions

* When performing multiple **related** `Add`, `Update`, or `Delete` operations that should **either all succeed or all fail** (atomicity).
* When inserting or modifying **large amounts of data**, reducing **multiple individual transactions** into a single one.
* When using **batch processing** to ensure database efficiency while still maintaining consistency.
* When working with **multiple tables** and ensuring referential integrity across related records.

---

## Summary: ✅ Optimize EF Core queries for better performance

* Use **bulk insertions** (`AddRangeAsync()`) instead of inserting in a loop  
* Fetch **data in a single query** instead of querying in a loop
* **Batch large datasets** to balance efficiency and memory usage
* **Use `AsNoTracking()`** when you don’t need entity tracking
* **Call `SaveChangesAsync()` less frequently** to reduce database overhead
* **Use transactions** for multiple operations to improve efficiency and reliability

Following these practices ensures your EF Core queries are efficient, reducing database load and improving application performance.
