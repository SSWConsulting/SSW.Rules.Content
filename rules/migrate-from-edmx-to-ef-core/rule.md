---
type: rule
title: Do you know how to migrate from EDMX to EF Core
guid: d0ba79cd-ee1c-48ae-aa4d-b7b6b974d244
uri: migrate-from-edmx-to-ef-core
authors: 
- title: Jernej Kavka (JK)
  url: https://ssw.com.au/people/jk
  img: https://github.com/SSWConsulting/SSW.People.Profiles/raw/main/Jernej-Kavka/Images/Jernej-Kavka-Profile.jpg
- title: Gordon Beeming
  url: https://www.ssw.com.au/people/gordon-beeming

related:
- dotnet-upgrade-for-complex-projects
- migrate-from-system-web-to-modern-alternatives
---

Some older projects .NET Framework project will have EDMX instead of modern DbContext first introduced in [Entity Framework 4.1](https://devblogs.microsoft.com/cesardelatorre/entity-framework-4-1-just-released/) which first introduced DbContext and Code-First approach back in 2012, replacing the ObjectContext that EDMX used for Database-First approach.

In this rule, we’ll use ObjectContext and Entities interchangeably. ObjectContext is the base class which is used by the generated class which will generally end with Entities (e.g. DataEntities).

## Strategies

There are a few strategies regarding the migration from a full rewrite with to a more in-place migration. Depending on scale and complexity of the project. This rule will describe an approach that balances the code we need to rewrite and modernisation.

The focus is to minimise the amount of time no deployments are made due to migration.

The strategy in this rules will include:

1. Abstract existing `ObjectContext/Entities` class with a custom `IDbContext` interface (e.g. `ITenantDbContext`)
2. Scaffold DB
    1. When to use EF Core 8+
    2. When to use EF Core 3.1
    3. EF Core Power Tools **[TODO: Add link]**
3. Implement interface from step 1
    1. Replace `ObjectSet<T>` with `DbSet<T>`
    2. **[TODO: Not done]** Make any other necessary changes
4. Update namespaces (for Entities, EF Core namespaces and removing legacy namespaces)
5. Update dependency injection
6. **[TODO: Not done]** Update migration strategy (from DB-first to Code-first)
7. **[TODO: Not done]** Optional: Upgrade to .NET 8+ (if on .NET Framework or .NET Core 3.1)
8. **[TODO: Not done]** Optional: Upgrade to EF Core 8+ (if EF Core 3.1 path was necessary)

Step 6 and 7 are required when upgrading from .NET Framework to .NET 8 and solution is too complex to do the migration in one go. For simple projects, if EDMX is the only major blocking issue, they should go straight to .NET 8 and EF Core 8.

::: greybox

NOTE: With some smart abstraction strategies, it is possible to do steps 3 - 5 while still have a working application. Only recommended for experienced developers in architecture and how EF operates, to avoid bugs related to running 2 EF tracking systems. This will impact EF internal caching and saving changes.

:::

## 1. Abstracting access to ObjectContext/Entities

Before starting, it’s important to note that ObjectContext and EDMX are no longer supported and we need to do a full rewrite of the data layer. You can wrap ObjectContext with an interface that looks like modern DbContext as most commonly used methods are identical.

The wrapper below not only allows us to use ObjectContext in a more cleaner way (see Clean Architecture **[TODO: Add link]**) but also allows us to better manage the differences between ObjectContext and DbContext without needing to refactor the business logic.

::: greybox

```csharp
using System.Data.Entity.Core.Objects;

public interface ITenantDbContext
{
    ObjectSet<Client> Clients { get; }

    int SaveChanges();
    Task<int> SaveChangesAsync(CancellationToken ct = default);
}

/// <summary>
/// Implement DbContext as internal, so that external libraries cannot access it directly.
/// Expose functionality via interfaces instead.
/// </summary>
internal class TenantDbContext : ITenantDbContext
{
    private readonly DataEntities _entities;

    public TenantDbContext(DataEntities entities)
    {
        _entities = entities;
    }

    public ObjectSet<Client> Clients => _entities.Clients;

    public int SaveChanges() => _entities.SaveChanges();
    public Task<int> SaveChangesAsync(CancellationToken ct = default) => _entities.SaveChangesAsync(ct);
}
```

:::

::: good

Figure: Abstracting ObjectEntities behind an interface and use interface to reduce the amount of issues while migrating.

:::

::: greybox

NOTE: The changes made in this section are still compatible with .NET Framework, allowing us to deliver value to the clients while the above changes are made.

:::

# Resources

- How to migrate to EF Core 3.1 video - [https://learn.microsoft.com/en-us/shows/on-net/migrating-edmx-projects-to-entity-framework-core](https://learn.microsoft.com/en-us/shows/on-net/migrating-edmx-projects-to-entity-framework-core#time=08m10s)
- Official porting docs to EF Core 3.1 - https://learn.microsoft.com/en-us/ef/efcore-and-ef6/porting/port-edmx

# Alternative

EF Core 3.1 EDMX - [Walk-through: Using an Entity Framework 6 EDMX file with .NET Core | ErikEJ's blog](https://erikej.github.io/ef/dotnetcore/2020/06/15/ef6-use-edmx-dotnetcore.html)

While the above blog is supposedly working in EF Core 3.1, there is no information whether that is true for .NET 8. It would still require a lot of migrations.

Limitations:

- EDMX is not supported in .NET Standard or .NET or any other SDK-style projects (required for .NET migrations)
- Requires a dedicated .NET Framework project that is not yet upgraded to SDK-style project to generate and update EDMX, models and ObjectContext
- EF6 and EDMX are out of support
- Built for EF Core 3.1 which is out of support
- Unknown if it works on .NET 8 even with legacy .NET Framework support
- ObjectContext (the core of EDMX) was slowly phasing out, being replaced by DbContext since 2012