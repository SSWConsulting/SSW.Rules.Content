---
type: rule
title: Do you know how to migrate OWIN to ASP.NET Core?
uri: know-how-to-migrate-owin-to-asp-net-core
authors:
  - title: Nick Curran
    url: https://ssw.com.au/people/nick-curran
related:
  - choosing-authentication
created: 2023-07-31T23:22:58.333Z
guid: 004c52d9-30a5-4b9c-963a-e93988a31075
---
OWIN is the [Open Web Interface for .NET](http://owin.org/), which was intended to provide a standard interface between .NET web servers and web applications for ASP.NET. It provided the ability to chain middleware together to form pipelines and to register modules.

The [Katana libraries](https://github.com/aspnet/AspNetKatana/) provided a flexible set of popular components for OWIN-based web applications. These components were supplied through packages prefixed with `Microsoft.Owin`.

Middleware and module registering functionality are now core features of ASP.NET Core. Microsoft provides adapters to and from the [OWIN interface for ASP.NET](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/owin?view=aspnetcore-7.0) that can be used to gradually migrate custom OWIN components. By contrast, ASP.NET Core has native ports for Katana components.

## CORS functionality

CORS functionality was enabled in OWIN with the [UseCors(...)](https://learn.microsoft.com/en-us/previous-versions/aspnet/mt181143(v=vs.113)) extension method. For ASP.NET Core, it is provided by the [UseCors(...)](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.corsmiddlewareextensions.usecors?view=aspnetcore-7.0#microsoft-aspnetcore-builder-corsmiddlewareextensions-usecors(microsoft-aspnetcore-builder-iapplicationbuilder)) extension method in the [`Microsoft.AspNet.Cors`](https://www.nuget.org/packages/Microsoft.AspNet.Cors) package.

```cs
public void Configuration(Owin.IAppBuilder app) {
    // ... other logic ...
    app.UseCors(getCorsOption());
    // ... other logic ...
}

private static CorsOptions BuildCorsOptions() {
    var corsPolicy = new CorsPolicy
    {
        AllowAnyMethod = true,
        AllowAnyHeader = true,
        SupportsCredentials = true
    };
    corsPolicy.Origins.Add("https://staging.northwind.com");
    return new CorsOptions 
    {
        PolicyProvider = new CorsPolicyProvider
        {
            PolicyResolver = context => Task.FromResult(corsPolicy)
        }
    };
}
```

::: bad
Figure: Basic OWIN CORS example.
:::

```cs
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.UseCors(corsPolicyBuilder => {
    corsPolicyBuilder.AllowAnyMethod()
                     .AllowAnyHeader()
                     .AllowCredentials()
                     .WithOrigins(new string[] { "https://staging.northwind.com" });
})
```

::: good
Figure: Basic OWIN CORS example ported to ASP.NET Core.
:::

## Third-Party Authentication

A common use for OWIN was to provide access to [third-party authentication sources](/choosing-authentication/). [AspNet.Security.OAuth.Providers](https://github.com/aspnet-contrib/AspNet.Security.OAuth.Providers) is a collection of security middleware that works natively in ASP.NET Core to support authentication sources such as GitHub and Azure DevOps. The full list of providers is published [here](https://github.com/aspnet-contrib/AspNet.Security.OAuth.Providers#providers), and the details of the migration differ from provider to provider.
