---
type: rule
title: Data - Do you avoid deleting records by flagging them as IsDeleted (aka
  Soft Delete)?
uri: avoid-deleting-records-by-flagging-them-as-isdeleted
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - data-do-you-avoid-deleting-records-by-flagging-them-as-isdeleted-aka-soft-delete
  - data-do-you-avoid-deleting-records-by-flagging-them-as-isdeleted-(aka-soft-delete)
created: 2019-11-25T19:14:13.000Z
archivedreason: null
guid: 56fff82d-9ed7-4aee-ab22-68e4c61fe162
---
When users are deleting a lot of records as part of normal operations - they can and do make mistakes. Instead of the painful process of having to go to a backup to get these records, why not simply flag the records as IsDeleted?

<!--endintro-->

::: good
Advantages

:::

* You do not have to delete all related records e.g. Customers, Orders, Order Details. Instead, you can just flag the parent record as deleted with an "IsDeleted" bit field.
* You do not lose historical data e.g. how many products one of your previous clients purchased.
* You can actually see who deleted the record, as your standard audit columns (e.g. DateUpdated, UserUpdated are still there. The record does not just vanish.

::: bad
Disadvantages

:::

* Depending on your interface design, you may have to join to parent tables to ensure that deleted child records do not appear. Typically, the interface would be designed in such a way that you would not need be able to created new records based on the deleted items (e.g. you cannot create a new order record for a customer that is deleted). Performance of queries can potentially suffer if you have to do these joins.
* While storage space is very cheap, you are not removing records from your database. You may need to archive records if the number of deleted records becomes large.

### Best Approach for Implementing Soft Delete in EF Core for modern web application.

### 1. `ISoftDeleteEntity` Interface

Implement an interface `IsSoftDeleteEntity` with a boolean property `IsDeleted,` Entities requiring soft delete should implement this interface.

```sql
public interface ISoftDeleteEntity
{
    bool IsDeleted { get; set; }
}
```

### 2. Global Query Filters

Apply global query filters to automatically exclude soft-deleted entities:

```sql
modelBuilder.Entity<MyEntity>().HasQueryFilter(e => !e.IsDeleted);
```

This ensures queries do not return entities marked as deleted automatically eliminating the need to add an extra where condition in the actual queries.

### 3. EF Core Interceptors for Soft Delete

Override the default delete behavior using EF Core interceptors by using an interceptor. This changes entity state to `Modified` and sets `IsDeleted` to `true` instead of completely removing the record.

```chsarp
public class SoftDeleteInterceptor : SaveChangesInterceptor
{
    public override InterceptionResult<int> SavingChanges(DbContextEventData eventData, InterceptionResult<int> result)
    {
        foreach (var entry in eventData.Context.ChangeTracker.Entries<ISoftDeleteEntity>())
        {
            if (entry.State == EntityState.Deleted)
            {
                entry.Entity.IsDeleted = true;
                entry.State = EntityState.Modified;
            }
        }
        return base.SavingChanges(eventData, result);
    }
}
```

:::greybox
Note: Make sure the entites that require soft delete has implemented the ISoftDeleteEntity interface for them to be captured into this interceptor.
:::

### 4. Registering the Interceptor

Register the custom interceptor in the `DbContext` configuration:

```chsarp
services.AddDbContext<MyDbContext>(options =>
    options.UseSqlServer(connectionString)
           .AddInterceptors(new SoftDeleteInterceptor()));
```

This integrates the interceptor with the EF Core context, this will ensure to run the entity through this interceptor every time context.saveChanges() is triggered.

- - -

Also see [Using Audit Tools](/use-temporal-tables-to-audit-data-changes) for alternatives to this approach using 3rd party auditing tools.
::: greybox

Watch William Liebenberg's SpendOps talk for more details about why soft deletes are advantageous in Azure:

* SSW TV video: 
         [Real-life SpendOps with Azure Cosmos DB](https://www.youtube.com/watch?v=qfPQR8XlwFo)
* NDC video: 
         [Azure SpendOps – The Art of Effectively Managing Azure Costs](https://www.youtube.com/watch?v=zxSlKiWOOzw)

:::