---
seoDescription: Discover the best dependency injection containers for .NET applications, including Autofac, Unity, and more, with insights on choosing the right one for your needs.
type: rule
archivedreason:
title: Do you know the best dependency injection container? 
guid: d4fc76e9-0802-48bd-83d7-4e068a19d33b
uri: the-best-dependency-injection-container
created: 2013-02-01T16:43:44.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
- title: Yazhi Chen
  url: https://ssw.com.au/people/yazhi-chen
related:
- do-you-use-a-dependency-injection-centric-architecture
- generate-dependency-graphs
- do-you-know-what-to-do-about-asp-net-core-aka-asp-net-5-default-dependency-injection
redirects:
- do-you-know-the-best-dependency-injection-container-(aka-dont-waste-days-evaluating-ioc-containers)
- do-you-know-the-best-dependency-injection-container-(aka-don’t-waste-days-evaluating-ioc-containers)
- do-you-know-the-best-dependency-injection-container-aka-do-not-waste-days-evaluating-ioc-containers
- do-you-know-the-best-dependency-injection-container-(aka-do-not-waste-days-evaluating-ioc-containers)

---

## IoC (Inversion of Control) and Dependency Injection

IoC is a design pattern that shifts the responsibility of managing object dependencies from the individual classes to a centralized container or framework. This decoupling enhances flexibility and scalability by allowing the framework to handle object creation and wiring.

Dependency injection is a method for managing Inversion of Control (IoC). This involves creating an interface and passing it as a parameter, allowing us to determine which implementation of the interface we intend to use.

## IoC containers

IoC containers are powerful tools that apply the IoC principle and automatically handle dependency resolution and object instantiation. They act as central repositories for services and take care of managing the lifespan of objects. At SSW we recommend using [.NET built-in Dependency Injection](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection?WT.mc_id=AZ-MVP-33518) as default. Read more on [Dependency injection in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-8.0&WT.mc_id=AZ-MVP-33518).

However, in larger applications, manually registering dependencies can become cumbersome and easy to forget. In those cases, we recommend using [Scrutor](https://github.com/khellang/Scrutor). While it isn't a DI container itself, it works on top of the .NET built-in Dependency Injection capabilities and adds assembly scanning to automatically register discovered types.

<!--endintro-->

## .NET IoC containers

* [.NET built-in Dependency Injection](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection?WT.mc_id=AZ-MVP-33518) (recommended)
* [Autofac](https://autofac.org/)
* [Unity](https://github.com/unitycontainer/unity)
* [Castle Winsdor](https://github.com/castleproject/Windsor)
* [StructureMap](https://github.com/structuremap/structuremap) (not recommended)
* [Ninject](https://github.com/ninject/Ninject) (not recommended)
* (and more)

When selecting a Dependency Injection container it is worth considering a number of factors such as:

* Ease of use
* Configurability: Fluent API and/or XML Configuration
* Performance (Unless you have a very high traffic application the difference should be minimal)
* NuGet Support

The top tools all contain comparable functionality. In practice which one you use makes little difference, especially when you consider that your container choice should not leak into your domain model.

**Important:** Unless a specific shortfall is discovered with the container your team uses, you should continue to use the same container across all of your projects, become an expert with it and invest time on building features rather than learning new container implementations.

::: bad  
![Figure: Bad Example - Ninject and StructureMap were top containers but are no longer actively developed. Together with Autofac, they do not support the latest version of .NET](di-container-bad.png)  
:::

## Examples of using IoC container

```csharp
public class Program
{
    private static void Main()
    {        
        IContainer container = IoC.Initialize(); 
        new BadgeTaskJob(container).Run();
    }
}
```

::: bad
Bad example - Use the StructureMap IoC container but did not do the proper dependency injection
:::

```csharp
var builder = Host.CreateApplicationBuilder(args);
builder.Services.AddScoped<BadgeTaskJob>();
using IHost host = builder.Build();
using var scope = host.Services.CreateScope();
scope.ServiceProvider.GetRequiredService<BadgeTaskJob>().Run();
```

::: good
Good example - Use .NET built-in Dependency Injection for console app
:::

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddSingleton<ITelemetryInitializer, AppInsightsTelemetryInitializer>();
builder.Services.AddSingleton<AssetDomain>();
var app = builder.Build();
app.Run();
```

::: good
Good example - Use ASP.Net Core built-in Dependency Injection for web app
:::
