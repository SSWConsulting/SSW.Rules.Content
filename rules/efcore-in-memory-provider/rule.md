---
type: rule
title: Do you use the EF Core In-Memory provider to simplify your tests?
uri: efcore-in-memory-provider
authors:
  - title: Daniel Mackay
    url: https://www.ssw.com.au/people/daniel-mackay/
  - title: William Liebenberg
    url: https://www.ssw.com.au/people/william-liebenberg/
  - title: Jack Pettit
    url: https://www.ssw.com.au/people/jack-pettit/
created: 2023-12-01T02:42:16.722Z
guid: 4e4a6ba5-9ddc-48c3-a7bd-ff3f83a710b7
---
When testing code that depends on Entity Framework Core, the challenge often lies in how to effectively mock out the database access. This is crucial for focusing tests on the functionality surrounding the DB access rather than the database interactions themselves. The EF Core In-Memory provider is a tool designed to address this need.

<!--endintro-->

### Common Pitfalls in Mocking

#### Trying to Mock `DbContext`

Attempting to mock the entire `DbContext` is a common mistake. This approach typically leads to complex and fragile test setups, making the tests hard to understand and maintain.

::: bad 
```csharp
var mockContext = new Mock<ApplicationDbContext>();
// Adding further mock setups...
```
:::

**Figure: Bad Example - Mocking the entire DbContext is overly complex and error-prone.** 



#### Trying to Mock `DbSet`

Similarly, mocking `DbSet` entities often results in tests that don't accurately reflect the behavior of the database, leading to unreliable test outcomes.

::: bad 
```csharp
var mockSet = new Mock<DbSet<MyEntity>>();
// Configuring mockSet behaviors...
```
:::

**Figure: Bad Example - Mocking DbSet entities fails to mimic real database interactions effectively.**

### Good Practice: Using DbContext with In-Memory Provider

Instead of extensive mocking, using `DbContext` with the EF Core In-Memory provider simplifies the setup and reduces the need for mocks. This approach enables more realistic testing of database interactions.

::: good 
```csharp
var options = new DbContextOptionsBuilder<ApplicationDbContext>()
    .UseInMemoryDatabase(Guid.NewGuid().ToString())
    .Options;

var dbContext = new ApplicationDbContext(options);

```
:::

**Figure: Good Example - Using DbContext with an EF Core In-Memory provider for simpler and more effective testing.**

### Caveat: Limitations of In-Memory Testing

While the EF Core In-Memory provider is useful for isolating unit tests, it's important to recognize its limitations:

* **Behavioral Differences:** It doesn't emulate all aspects of a SQL Server provider, such as certain constraints or transaction behaviors.
* **Not Suitable for Query-focused Tests:** For tests that focus on EF queries, more realistic results can be achieved through integration tests with an actual database.

::: info 
Checkout [JK's EF Core Testing Repository](https://github.com/jernejk/MixedEFCoreUnitTesting) for comprehensive examples and advanced scenarios in EF Core testing.
:::