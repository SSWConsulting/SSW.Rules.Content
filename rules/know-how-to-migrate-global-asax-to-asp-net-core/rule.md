---
type: rule
title: Do you know how to migrate Global.asax to ASP.NET Core?
uri: know-how-to-migrate-global-asax-to-asp-net-core
authors:
  - title: Nick Curran
    url: https://ssw.com.au/people/nick-curran
created: 2023-07-31T23:29:08.804Z
guid: 06510ae9-8215-4227-97ae-711c8c35a948
---
The [`Global.asax`](https://learn.microsoft.com/en-us/previous-versions/dotnet/netframework-4.0/2027ewzw(v=vs.100)) is an optional file that dictates how an ASP.NET application handles application, session and request events. The code for handling those events is written in `Global.asax.cs`, and when migrating to ASP.NET Core this code will need to be restructured.

## Application Events

The methods given below are automatically linked to event handlers on the [HttpApplication](https://learn.microsoft.com/en-us/dotnet/api/system.web.httpapplication?view=netframework-4.8.1) class at runtime.

The `Application_Start()` or `Application_OnStart()` method is called once upon the first request being received by the server, and is typically used to initialize static values. The logic for this starting method should be included at the beginning of [`Program.cs`](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/startup?view=aspnetcore-7.0) in the ASP.NET Core project.

The `Application_Init()` method is called after all event handler modules have been added. Its logic can be migrated by registering the logic with the [WebApplication.Lifetime](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplication.lifetime?view=aspnetcore-7.0) property [ApplicationStarted](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.ihostapplicationlifetime.applicationstarted?view=dotnet-plat-ext-7.0#microsoft-extensions-hosting-ihostapplicationlifetime-applicationstarted).

The `Application_End()` and `Application_Disposed()` methods are fired upon application termination. They can be migrated by registering the logic with the [WebApplication.Lifetime](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplication.lifetime?view=aspnetcore-7.0) properties [ApplicationStopping](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.ihostapplicationlifetime.applicationstopping?view=dotnet-plat-ext-7.0#microsoft-extensions-hosting-ihostapplicationlifetime-applicationstopping) and [ApplicationStopped](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.ihostapplicationlifetime.applicationstopped?view=dotnet-plat-ext-7.0#microsoft-extensions-hosting-ihostapplicationlifetime-applicationstopped).

Therefore, the following `Global.asax.cs` snippet would migrate as per the figures below.

```cs
public class MvcApplication : HttpApplication
{
    protected void Application_Start() {
        Console.WriteLine("Start");
    }

    protected void Application_Init() {
        Console.WriteLine("Init");
    }

    protected void Application_Stopping() {
        Console.WriteLine("Stopping");
    }

    protected void Application_Stopped() {
        Console.WriteLine("Stopped");
    }
}
```
::: bad
Figure: Basic example application code from a `Global.asax.cs` file.
:::

```cs
Console.WriteLine("Start");

var builder = WebApplication.CreateBuilder(args);
// ...
var app = builder.Build();
app.Lifetime.ApplicationStarted.Register(() => Console.WriteLine("Init"));
app.Lifetime.ApplicationStopping.Register(() => Console.WriteLine("Stopping"));
app.Lifetime.ApplicationStopped.Register(() => Console.WriteLine("Stopped"));
```
::: good
Figure: The above code migrated to ASP.NET Core.
:::

## Session Events

The `Session_Start()` is called when a new user session is detected. The `Session_Start()` method can be replaced using middleware that determines if a pre-set session variable was previously set. Additional approaches for replacing `Session_Start()` can be found in [this StackOverflow thread](https://stackoverflow.com/questions/52533831/is-there-a-session-start-equivalent-in-net-core-mvc-2-1).

`Session_End()` is called when a user session is ended, typically by timeout. There is [no equivalent functionality for `Session_End()`](https://github.com/aspnet/Session/issues/20) in ASP.NET Core, and the any session management logic will need to be refactored to account for this.

## Request Lifecycle Methods

The events raised during a request are [documented in the HttpApplication API](https://learn.microsoft.com/en-us/dotnet/api/system.web.httpapplication?view=netframework-4.8.1#remarks). The logic to be executed before and after a request should be implemented using [middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-7.0).

```cs
public class MvcApplication : HttpApplication
{
    protected void Application_BeginRequest() {
        Console.WriteLine("Begin request");
    }

    protected void Application_EndRequest() {
        Console.WriteLine("End request");
    }
}
```
::: bad
Figure: Basic example request lifecycle code from a `Global.asax.cs` file.
:::

```cs
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.Use(async (context, next) => 
{
    Console.WriteLine("Begin request");
    await next.Invoke();
    Console.WriteLine("End request");
})
```
::: good
Figure: Using middleware to execute logic before and after a request.
:::

## Error Handling

Global error handling logic in [`Application_Error()`](https://learn.microsoft.com/en-us/dotnet/api/system.web.httpapplication.error?view=netframework-4.8.1) method should be migrated to use middleware registered with the [`UseExceptionHandler()`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.exceptionhandlerextensions.useexceptionhandler?view=aspnetcore-7.0) method.

```cs
public class MvcApplication : HttpApplication
{
    protected void Application_Error(object sender, EventArgs e) {
        var error = Server.GetLastError();
        Console.WriteLine("Error was: " + error.ToString());
    }
}
```
::: bad
Figure: Basic example error handling code from a `Global.asax.cs` file.
:::

```cs
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.UseExceptionHandler(exceptionHandlerApp => 
{
    exceptionHandlerApp.Run(async context =>
    {
        var handlerPathFeature = context.Features.Get<IExceptionHandlerPathFeature>();
        var error = handlerPathFeature.Error;
        Console.WriteLine("Error was: " + error.ToString());

        // NOTE: context.Response allows you to set the returned status code
        // and response contents.
    })
});
```
::: good
Figure: Using exception handling middleware.
:::

See [here](https://learn.microsoft.com/en-us/aspnet/core/web-api/handle-errors?view=aspnetcore-7.0) for more options for handling errors in ASP.NET Core.
