---
type: rule
title: Do you know how to migrate Web.config to ASP.NET Core?
uri: know-how-to-migrate-web-config-to-asp-net-core
authors:
  - title: Nick Curran
    url: https://ssw.com.au/people/nick-curran
related:
  - store-your-secrets-securely
created: 2023-07-31T22:49:30.966Z
guid: d7ecd82c-da04-4f8e-bf79-9bb6002769e9
---
The [`Web.Config`](https://learn.microsoft.com/en-us/troubleshoot/developer/webapps/aspnet/health-diagnostic-performance/create-web-config) file was used in ASP.NET to control the behaviour of individual ASP.NET applications and configure IIS. By default, modern ASP.NET Core applications use the Kestrel web server which is [configured in code](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel/options?view=aspnetcore-7.0). Unless you are deploying your application using IIS, you will need to migrate your `Web.Config` file.

The `Web.Config` file contains data about the package inclusions, module inclusions and configuration values.

## Package Inclusions

In ASP.NET Core, project inclusions are listed in the project's CSPROJ file. The dependencies of your application will need to be reviewed as to whether they are still required, and should be added as required using the NuGet Package Manager.

## Server Configuration

The server's configuration needs to be transferred to code within the `Program.cs` file.

### Custom Error Pages

The `<customErrors>` element within `<system.web>` specifies redirects for the server to use if a response with a HTTP error code is generated. When the relevant [SSW Rule on useful error pages](/404-useful-error-page/) is followed, the mode will be 'RemoteOnly', meaning that the redirect will only be used if accessed from a separate host. The `<customErrors>` element will provide a default redirect, and may contain `<error>` elements that provide more specific redirects for specific error codes.

The easiest way to transcode this configuration is using [`UseStatusCodePagesWithRedirects`](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling?view=aspnetcore-7.0#usestatuscodepageswithredirects).

```xml
<customErrors mode="RemoteOnly" defaultRedirect="~/Error">
    <error statusCode="403" redirect="~/Error?code=403" />
    <error statusCode="404" redirect="~/Error?code=404" />
</customErrors>
```

**Figure: Typical example of custom error redirection**

```cs
var app = builder.Build();
app.UseStatusCodePagesWithRedirects("/Error?code={0}");
```

Figure: The migrated configuration to ASP.NET Core

### Namespaces

The [`<pages>/<namespaces>`](https://learn.microsoft.com/en-us/previous-versions/dotnet/netframework-4.0/ms164642(v=vs.100)) element defines import directives to use during assembly pre-compilation. The same affect can be achieved using modern C# [implicit import functionality](https://learn.microsoft.com/en-us/dotnet/core/project-sdk/overview#implicit-using-directives).

### HTTP Handler Routes

The [`<httpHandlers>`](https://learn.microsoft.com/en-us/previous-versions/dotnet/netframework-4.0/bya7fh0a(v=vs.100)) element links routes to [`IHttpHandler`](https://learn.microsoft.com/en-us/dotnet/api/system.web.ihttphandler?view=netframework-4.8.1) implementations. See the [ASP.NET Core Fundamentals article on Routing](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/routing?view=aspnetcore-7.0) for replacement options, including the use of [`MapGet`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.endpointroutebuilderextensions.mapget?view=aspnetcore-7.0#microsoft-aspnetcore-builder-endpointroutebuilderextensions-mapget(microsoft-aspnetcore-routing-iendpointroutebuilder-system-string-system-delegate)) and [`MapPost`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.endpointroutebuilderextensions.mappost?view=aspnetcore-7.0#microsoft-aspnetcore-builder-endpointroutebuilderextensions-mappost(microsoft-aspnetcore-routing-iendpointroutebuilder-system-string-system-delegate)).

### HTTP Modules

The [`<httpModules>`](https://learn.microsoft.com/en-us/previous-versions/dotnet/netframework-4.0/9b9dh535(v=vs.100)) element configures modules that register themselves with the [`HttpApplication`](https://learn.microsoft.com/en-us/dotnet/api/system.web.httpapplication?view=netframework-4.8.1). See the documentation of individual modules regarding how their modern equivalents are to be used with an ASP.NET Core application.

## Custom Configuration Values

Custom configuration values for the application are stored in the `<appSettings>` element. Where configuration values will be moved will depend on whether they should be secret or not.

In the case of non-secret values, they can be moved to an `appsettings.json` file.

```xml
<appSettings>
    <add key="DefaultVisibility" value="public" />
    <add key="DefaultClientCount" value="30" />
</appSettings>
```

**Figure: Typical example of application settings in Web.config**

```json
{
  "DefaultVisibility": "public",
  "DefaultClientCount": 30
}
```

**Figure: The application settings example migrated to `appsettings.json`**

The class used to access configuration values will also need to be changed if the program is using [System.Configuration.ConfigurationManager](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.configurationmanager) as that class is not available under ASP.NET Core. Instead, use a dependency injected [`IConfiguration`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.configuration.iconfiguration?view=dotnet-plat-ext-7.0) implementation from the `Microsoft.Extensions.Configuration` package.

```cs
String visibility = ConfigurationManager.AppSettings["DefaultVisibility"];
int clientCountStr = int.Parse(ConfigurationManager.AppSettings["DefaultClientCount"]);
// Perform action with configuration values.
```

**Figure: A typical example of using ConfigurationManager to retrieve settings**

```cs
public class TestService
{
    private readonly IConfiguration Configuration;

    public TestService(IConfiguration configuration)
    {
        Configuration = configuration;
    }

    public void Act() {
        var visibility = Configuration.GetValue<string>("DefaultVisibility");
        var clientCountStr = Configuration.GetValue<int>("DefaultClientCount");
        // Perform action with configuration values.
    }
}
```

**Figure: The example code migrated to ASP.NET Core**

## Connection Strings

Connections strings are stored in the `<connectionStrings>` element, and may be directly transferred to the `appsettings.json` file so long as they do not contain any secrets.

```xml
<connectionStrings>
    <add name="DefaultConnection"
         providerName="System.Data.SqlClient"
         connectionString="Server=localhost,1200" />
</connectionStrings>
```

**Figure: A typical example Connection string in Web.config**

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=localhost,1200"
  }
}
```

**Figure: The connection string example migrated to ASP.NET Core**

As discussed above, the `ConfigurationManager` class is no longer available and its usages need to be replaced with calls using `IConfiguration`.

```cs
var connStr = ConfigurationManager.ConnectionsStrings["DefaultConnection"]
                                  .ConnectionString;
```

**Figure: A typical example of how to access a Connection string from Web.config**

```cs
var build = WebApplication.CreateBuilder(args);
var app = builder.Build();
var connStr = app.Configuration.GetConnectionString("DefaultConnection");
```

**Figure: The example migrated to accessing a connection string within `Program.cs`**

If there are secrets in the connection string, then it should be stored using the secrets manager as per [storing secrets securely](/store-your-secrets-securely). Connection strings have a "ConnectionStrings:" prefix, as demonstrated below. The value is accessible through `IConfiguration` as demonstrated above.

```powershell
dotnet user-secrets set ConnectionStrings:DefaultConnection "Server=localhost,1200"
```

**Figure: Command to set the connection string for local development within the project**
