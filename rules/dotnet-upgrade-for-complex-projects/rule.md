---
type: rule
title: Do you know how to handle complex .NET migrations?
uri: dotnet-upgrade-for-complex-projects
authors:
  - title: Jernej Kavka (JK)
    url: https://ssw.com.au/people/jk
    img: https://github.com/SSWConsulting/SSW.People.Profiles/raw/main/Jernej-Kavka/Images/Jernej-Kavka-Profile.jpg
  - title: Gordon Beeming
    url: https://www.ssw.com.au/people/gordon-beeming
related:
  - dotnet-upgrade-assistant
  - migrate-from-system-web-to-modern-alternatives
created: 2023-07-16T23:08:53.979Z
guid: 9de5ca88-a6aa-4fe5-af47-d6d2169cde86
---
There's not 1 single thing that makes a .NET project complicated to migrate to the latest .NET framework. Generally though it's a combination of the following:

* Long lived code base
* Lots of external dependencies
* Lots of application components (web, desktop, services, etc)
* etc

Your first action should always be to use the [.NET Upgrade Assistant](https://dotnet.microsoft.com/en-us/platform/upgrade-assistant). You can read more about the tool at [Do you know how to modernize your .NET applications?](https://www.ssw.com.au/rules/dotnet-upgrade-assistant/) It is strongly advised to follow this rule before progressing further, particularly if you haven't had the opportunity to do so yet. 

Below you will find some tips and tricks to help you with your more complicated migrations.

<!--endintro-->

# Preparation

### Upgrade the projects to use the sdk style csproj format

You can use the [try-convert](https://github.com/dotnet/try-convert) dotnet tool to convert your projects to the new sdk style csproj format. This will make it easier to upgrade the projects to the latest .net framework.

Install the tool using 

```bash
dotnet tool install -g try-convert
```

Upgrade your web projects using

```bash
try-convert --keep-current-tfms --force-web-conversion
```

and your other projects using

```bash
try-convert --keep-current-tfms
```

### Change all your projects to be able to target multiple Target framework monikers (TFM)

In all your project files change the `TargetFramework` to `TargetFrameworks`. You want to do  this early on to enable a smoother flow later to not need unload and reload projects or have to close and reopen Visual Studio.

What this will allow you to do is add your target framework and compile the code. This will allow you to see what code is not compatible with the new framework and fix those issues while still developing/deploying your project in the current target framework. 

```csharp
<TargetFrameworks>net472;net8.0</TargetFrameworks>
```

# Upgrading

At this point, ensure your project can target both the .NET Framework and the new target framework. Iterate through the following steps to gain an understanding of how many projects are ready and how much work lies ahead. 

1. Add the target framework to your project
2. Compile to see what breaks
3. Fix what is easy to fix

   1. Remember to commit after each fix to help your reviewers 😉
4. Anything that is not easy to fix, create a PBI with details of the issue

   1. This allows another developer on your team to work on that PBI independently
5. If you have a project that is able to compile at this point you can leave the new TFM in your project and continue to the next project

   1. If not, you can remove the new TFM and continue to the next project
   2. Repeat these steps once the PBIs have been completed related to this project

Outlined below are rules designed to assist in the project upgrade process during migration. Please note that the applicability of certain rules may vary based on individual project requirements.

* [Do you know how to migrate from System.Web to modern alternatives?](https://www.ssw.com.au/rules/migrate-from-system-web-to-modern-alternatives/)
* [Do you know how to migrate from EDMX to EF Core?](https://www.ssw.com.au/rules/migrate-from-edmx-to-ef-core/)

# Web application

There are several ways to migrate project from ASP.NET to ASP.NET Core. You can read more about this at [Do you know the different ways to modernize your application?](https://www.ssw.com.au/rules/modernize-your-app/) We recommend using the Strangler Fig pattern to incrementally migrate your project with [YARP](https://microsoft.github.io/reverse-proxy/).






1. Create side-by-side incremental project with .NET Upgrade Assistant
2. Configure YARP 

```csharp
 var webRoutes = new List<RouteConfig>
            {
                // Route for token
                new()
                {
                    RouteId = "tokenServePath",
                    ClusterId = tokenClusterId,
                    Match = new RouteMatch
                    {
                        Path = "/token/{**catch-all}",
                    },
                },

                // Route for WebUI App
                new RouteConfig
                {
                    RouteId = "webUIServePath",
                    ClusterId = webUiClusterId,
                    Match = new RouteMatch
                    {
                        Path = "/api/v2/{**catch-all}",
                    },
                },

                // Route for WebApp App
                new RouteConfig
                {
                    RouteId = "webAppServePath",
                    ClusterId = webAppClusterId,
                    Match = new RouteMatch
                    {
                        Path = "/api/{**catch-all}",
                    },
                },

                // Route for Angular
                new RouteConfig
                {
                    RouteId = "angularUIServePath",
                    ClusterId = angularClusterId,
                    Match = new RouteMatch
                    {
                        Path = "{**catch-all}",
                    },
                }
            };
```
::: greybox
Figure: Example code for setting up different paths within YARP's configuration.
:::
3. Create PBIs to identify the upcoming tasks.

```csharp
public class ApplicationHeaderSecurity : IHttpModule
    {
        public void Init(HttpApplication context)
        {
            context.PreSendRequestHeaders += OnPreSendRequestHeaders;
        }

        public void Dispose() { }

        void OnPreSendRequestHeaders(object sender, EventArgs e)
        {
            if (HttpContext.Current != null)
            {
                HttpContext.Current.Response.Headers.Remove("Server");
                HttpContext.Current.Response.Headers.Remove("eTag");
            }
        }
    }
```
::: greybox
Figure: Original code within an ASP.NET application.
:::
```csharp
public class ApplicationHeaderSecurityMiddleware
{
    static IImmutableList<string> HeadersToRemove => ImmutableList.Create("eTag");

    private readonly RequestDelegate _next;

    public ApplicationHeaderSecurityMiddleware(RequestDelegate next)
    {
        _next = next;
    }

    public async Task Invoke(HttpContext context)
    {
        foreach (var header in HeadersToRemove)
        {
            context.Response.Headers.Remove(header);
        }

        await _next.Invoke(context);
    }

}
public static class ApplicationHeaderSecurityMiddlewareExtensions
{
    public static IApplicationBuilder UseApplicationHeaderSecurityMiddleware(this IApplicationBuilder builder)
    {
        return builder.UseMiddleware<ApplicationHeaderSecurityMiddleware>();
    }
}
```
::: greybox
Figure: Updated code within an ASP.NET Core application.
:::

Listed below are rules crafted to aid in the project migration process. Please ensure to incorporate only those rules that are applicable to your specific project.

* [Do you know how to migrate Global.asax to ASP.NET Core?](https://www.ssw.com.au/rules/know-how-to-migrate-global-asax-to-asp-net-core/)
* [Do you know how to migrate OWIN to ASP.NET Core?](https://www.ssw.com.au/rules/know-how-to-migrate-owin-to-asp-net-core/)
* [Do you know how to migrate Web.config to ASP.NET Core?](https://www.ssw.com.au/rules/know-how-to-migrate-owin-to-asp-net-core/)