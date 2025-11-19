---
seoDescription: Learn how using the Specification pattern can enhance maintainability, flexibility, and readability in software development.
type: rule
title: Do you use the Specification pattern in your software design?
uri: use-specification-pattern
authors:
  - title: Daniel Mackay
    url: https://www.ssw.com.au/people/daniel-mackay
  - title: Matt Goldman
    url: https://www.ssw.com.au/people/matt-goldman
created: 2023-06-17T13:42:55.753Z
guid: D81A5868-E316-4AC5-8C52-CBC3CE944908
related:
   - common-design-patterns
---

When developing software, ensuring that your code is maintainable, flexible, and readable is crucial. One effective way to achieve this is by implementing the Specification pattern. This pattern allows for clear and modular encapsulation of business rules and query criteria, promoting the separation of concerns and enhancing the overall quality of your code.

<!--endintro-->

## What Problem are we Solving here?

Let's take the example below of adding/removing items to/from a customer's order.  When looking up the customer we need to include the current OrderItems and ensure the order is not complete.  This logic is duplicated in both the AddItem and RemoveItem methods, which violates the DRY principle.

Even worse, if the logic changes, we need to update it in multiple places, increasing the risk of bugs and inconsistencies.  Below we correctly check the orders status when adding items, but not when removing them which is a bug.

```csharp
public class OrderService(ApplicationDbContext dbContext)
{
    public async Task AddItem(Guid orderId, OrderItem item)
    {
        var order = dbContext.Orders
            .Include(o => o.OrderItems)
            .FirstOrDefault(o => o.Id == orderId && o.Status != OrderStatus.Complete);
        
        order.AddItem(item);
        
        await dbContext.SaveChangesAsync();
    }
    
    public void RemoveItem(int age)
    {
        // Duplicated logic and bug introduced by not checking OrderStatus
        var order = dbContext.Orders
            .Include(o => o.OrderItems)
            .FirstOrDefault(o => o.Id == orderId);
        
        order.RemoveItem(item);
        
        await dbContext.SaveChangesAsync();
    }
}
```

::: bad
Figure: Bad example - Duplicated query logic to fetch the customer
:::

## What is the Specification Pattern?

The Specification pattern is a design pattern used to define business rules in a reusable and composable way. It encapsulates the logic of a business rule into a single unit, making it easy to test, reuse, and combine with other specifications.

## Use Cases for the Specification Pattern

1. **Reusable Queries**: Specifications can be used to define reusable query criteria for data access layers, making it easier to build complex queries.
2. **Validation Rules**: Specifications can be used to define validation rules for input data, ensuring that it meets the required criteria.
3. **Encapsulating Business Rules**: Specifications can encapsulate complex business rules in the Domain where most business logic should go.
4. **Repository Alternative**: Specifications can be used as an alternative to repositories for querying data.  Instead of encapsulating queries in repositories, you can encapsulate them in specifications.

## Using the Specification Pattern

Steve Smith (aka ["Ardalis"])(<https://github.com/ardalis>) has created an excellent library called [Ardalis.Specifications](https://github.com/ardalis/Specification) that integrates well with EF Core.

To use the Specification pattern, follow these steps:

1. **Define the Specification**:

```csharp
public sealed class TeamByIdSpec : SingleResultSpecification<Team>
{
    public TeamByIdSpec(TeamId teamId)
    {
        Query.Where(t => t.Id == teamId)
        .Include(t => t.Missions)
        .Include(t => t.Heroes);
    }
}
```

2. **Use Specification**:

```csharp
    var teamId = new TeamId(request.TeamId);
    var team = dbContext.Teams
        .WithSpecification(new TeamByIdSpec(teamId))
        .FirstOrDefault();
```

For an end-to-end example of the specification pattern see the [SSW.CleanArchitecture Template](https://github.com/SSWConsulting/SSW.CleanArchitecture).

## Good Example

Re-visiting the example above, we can apply the Specification pattern as follows:

```csharp
public sealed class OrderByIdSpec : SingleResultSpecification<Order>
{
   public IncompleteOrderByIdSpec(Guid orderId)
   {
        Query
            .Include(o => o.OrderItems)
            .Where(o => o.Id == orderId && o.Status != OrderStatus.Complete);
   }
} 

public class OrderService(ApplicationDbContext dbContext)
{
    public async Task AddItem(Guid orderId, OrderItem item)
    {
        var order = dbContext.Orders
            .WithSpecification(new OrderByIdSpec(orderIdorderId))
            .FirstOrDefaultAsync();
        
        order.AddItem(item);
        
        await dbContext.SaveChangesAsync();
    }
    
    public void RemoveItem(int age)
    {
        var order = dbContext.Orders
            .WithSpecification(new IncompleteOrderByIdSpec(orderIdorderId))
            .FirstOrDefaultAsync();
        
        order.RemoveItem(item);
        
        await dbContext.SaveChangesAsync();
    }
}
```

::: good
Figure: Good example - Specification used to keep Order query logic DRY
:::
