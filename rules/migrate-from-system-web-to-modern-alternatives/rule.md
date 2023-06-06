---
type: rule
title: Do you know to migrate from System.Web to modern alternatives
guid: 71755477-0a38-4402-a5c8-1347883df481
uri: migrate-from-system-web-to-modern-alternatives
authors: 
- title: Jernej Kavka (JK)
  url: https://ssw.com.au/people/jk
- title: Gordon Beeming
  url: https://www.ssw.com.au/people/gordon-beeming

related:
- dotnet-upgrade-for-complex-projects

---

# Do you know to migrate from System.Web to modern alternatives

When upgrading a web application from .NET Framework to .NET Standard or .NET, you will likely have to address System.Web. On upgrade, the reference to System.Web is either removed or will cause compile-time errors.

When it’s removed, the most common compile time error will be HttpContext.Current.

There are several options available depending on the scenario and stage of migration.

## 1. Replace with IHttpContextAccessor (.NET only)

When moving to .NET, you’ll find `HttpContext.Current` no longer exists. You can use `IHttpContextAccessor` instead in constructor and access it via `httpContextAccessor.HttpContext`.

::: greybox

```csharp
public class SomeService
{
		public void DoSomething()
		{
		    var httpContext = HttpContext.Current;
				// Rest of the code
		}
}
```

:::

::: bad

Figure: Bad example.

:::

::: greybox

```csharp
public class SomeService
{
		private readonly IHttpContextAccessor _httpContextAccessor;

		public SomeService(IHttpContextAccessor httpContextAccessor)
		{
				_httpContextAccessor = httpContextAccessor;
		}

		public void DoSomething()
		{
		    var httpContext = _httpContextAccessor.HttpContext;
				// Rest of the code
		}
}
```

:::

::: good

Figure: Good example.

:::

## 2. Abstracting functionality

You can also abstract what you need from HttpContext, which can be useful it you want to run the code in a non-web environment like a console app or if you want to keep dependency on .NET Framework.

If you multi-target .NET and .NET Framework, we need to add back System.Web reference for .NET Framework. We do that by updating the csproj file.

::: greybox

```xml
<ItemGroup Condition="'$(TargetFramework)' == 'net472'">
    <Reference Include="System.Web" />
</ItemGroup>
```

:::

Next step is to define an interface. For this case, we’ll only expose currently authenticated user. We are calling it IApplicationContext as it contains context for current request, whether it’s coming from an HttpContext or somewhere else if it’s a background job or console application.

::: greybox

```csharp
public interface IRequestContext
{
    string GetCurrentUsername();
}
```

:::

Below you can see multiple implementations of `IRequestContext` as an example. You may need to implement in the web application project of the respective platform.

::: greybox

```csharp
// For .NET Framework
public class LegacyHttpRequestContext : IRequestContext
{
    public string GetCurrentUsername()
		    => HttpContext.Current?.User?.Identity?.Name;
}

// For .NET Core and .NET
public class HttpRequestContext : IRequestContext
{
    private readonly IHttpContextAccessor _httpContextAccessor;

    public HttpRequestContext(IHttpContextAccessor httpContextAccessor)
    {
        _httpContextAccessor = httpContextAccessor;
    }

    public string GetCurrentUsername()
        => _httpContextAccessor.HttpContext.User.Identity?.Name;
}

// For background jobs, console applications, MAUI, etc.
public class BackgroundJobRequestContext : IRequestContext
{
    private readonly string _username;

    public BackgroundJobRequestContext(string username)
    {
        _username = username;
    }

		public string GetCurrentUsername() => _username;
}
```

:::

NOTE: If the above code needs to be in a multi-target project, you can use the `#if NET472_OR_GREATER` pragma to target specifically .NET Framework code.

## 3. Abstract HttpContext Accessor (.NET Framework only)

For projects heavily dependent on **`HttpContext`** and where abstracting **`HttpContext`** is impractical, you can mimic the behavior of **`IHttpContextAccessor`** in .NET Framework. While **`IHttpContextAccessor`** is available to .NET applications, it’s not for .NET Framework applications.

::: greybox

```csharp
namespace Microsoft.AspNetCore.Http
{
    // Make sure, we only use it in .NET Framework, .NET already has it's own implementation.
#if NET472_OR_GREATER
    // Interface identical to .NET IHttpContextAccessor.
    public interface IHttpContextAccessor
    {
        HttpContext HttpContext { get; }
    }

    // Simple implementation of IHttpContextAccessor for .NET Framework
    public class LegacyHttpContextAccessor : IHttpContextAccessor
    {
        public HttpContext HttpContext => HttpContext.Current;
    }
#endif
}
```

:::

## 4. Last resort: System.Web adapters

As a final resort, you can use **`System.Web`** adapters. These allow you to access **`HttpContext.Current`** without needing to port the code. Be aware that while this might seem like an easy solution, not all projects have been able to adopt this without issues. Therefore, it should only be used as a last resort if all other options fail.

Please refer to the official Microsoft documentation on [System.Web adapters | Microsoft Learn](https://learn.microsoft.com/en-us/aspnet/core/migration/inc/adapters?view=aspnetcore-7.0) for more details.

NOTE: The above strategies are not mutually exclusive and can be combined depending on your specific needs and constraints. The goal is to make your code more adaptable and ready for the migration to .NET or .NET Standard.