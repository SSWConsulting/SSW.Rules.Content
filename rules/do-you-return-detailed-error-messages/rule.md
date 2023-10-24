---
type: rule
title: Do you return detailed error messages?
uri: do-you-return-detailed-error-messages
authors:
  - title: Jeremy Cade
    url: https://ssw.com.au/people/jeremy-cade
  - title: Chris Clement
    url: https://www.ssw.com.au/people/chris-clement
related: []
redirects: []
created: 2015-08-27T01:00:17.000Z
archivedreason: null
guid: 7af36676-1eed-48dd-854b-2a956ef10e50
---
Good error design is as important to the success of an API as the API design itself. A good error message provides context and visibility on how to troubleshoot and resolve issues at critical times.

<!--endintro-->

## REST API

### Use the correct HTTP Status Codes

The HTTP/1.1 RFC lists over 70 different HTTP Status Codes. Only some developers will be able to remember all of them, so it pays to keep it simple and use the most common Status Codes. Below are the most common HTTP status codes:

* **2XX** - Success. Examples:

  * 200 OK - Generic success response.
* **4XX** - Client errors. Examples:

  * 400 Bad Request - The server cannot understand the request.
  * 401 Unauthorised - Invalid/non-existent credential for this request.
* **5XX** - Server errors. Examples:

  * 500 Internal Server Error - The server encountered errors preventing the request from being fulfilled.

### Use ProblemDetails Format

[RFC 7807 - Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc7807.html) details the specification for returning errors from your API. 

Problem Details defines a standardised way for HTTP APIs to communicate errors to clients. It introduces a simple and consistent format for describing errors, providing developers with a clear and uniform way to understand and handle errors in HTTP APIs.

Below is an example of an error message in Problem Details format:

```json
{
  "type": "https://example.com/probs/invalid-id",
  "title": "Invalid ID",
  "status": 400,
  "detail": "The provided ID has invalid characters.",
  "instance": "/account/12%203",
  "allowedCharacters": "^[a-zA-Z0-9]+$"
}
```

In the above example:

* `type` specifies a URI that uniquely identifies the type of the problem.
* `title` provides a short, human-readable summary of the problem.
* `status` indicates the HTTP status code for the response.
* `detail` gives a human-readable explanation specific to the occurrence of the problem.
* `instance` provides a URI reference that identifies the specific occurrence of the problem.
* `allowedCharacters` is an example property specificly added to the problem.

Using the above structured message format, APIs can now reliably communicate problems to clients to enable better error handling.

### Use .NET Exception Handler

ASP.NET Core has built-in support for the problem details specification since .NET 7.

### Option 1 - Use built-in ProblemDetails service

```csharp
// Program.cs
// This adds ProblemDetails service
// Read more on https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling?view=aspnetcore-8.0#problem-details
builder.Services.AddProblemDetails();

...

// This instructs the API to use the built-in exception handler
app.UseExceptionHandler();
```

Using this option, the API will generate a problem details response for all HTTP client and server error responses that *don't have body content yet*.

You can also customise the `ProblemDetailsService` behaviour - read more about it in the following link [Handle errors in ASP.NET Core | Customise Problem Details](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling?view=aspnetcore-8.0#customize-problem-details).

⚠️ **Important**
On certain templates, the default .NET Exception Handler middleware will **only** produce ProblemDetails responses for exceptions when running in a non-Development [environment](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments?view=aspnetcore-7.0#environments). See Option 2 below on how to make this consistent across environments.

### Option 2 - Customise Exception Handler Middleware (Recommended)

This option provides more flexibility in controlling the API's behaviour when it encounters thrown exceptions. Read more about it [here](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling?view=aspnetcore-8.0&preserve-view=true#exception-handler-lambda).
By Customising the `ExceptionHandler` middleware, developers have complete control over what format endpoints should return under a particular scenario.

Below is an example of customising the `ExceptionHandler` middleware to produce a `ProblemDetails` response for any exception.

```csharp
app.UseExceptionHandler(exceptionHandlerApp =>
  exceptionHandlerApp.Run(async context =>
  {
    // Obtain the exception
    Exception? exception = context.Features.Get<IExceptionHandlerFeature>()?.Error;

    // Produce a ProblemDetails response
    await Results.Problem(
      statusCode: StatusCodes.Status500InternalServerError,
      type: "https://tools.ietf.org/html/rfc7231#section-6.6.1",
      title: exception?.Message
    ).ExecuteAsync(context);
  }));
```

API will produce consistent response formats in any environment using the above approach.
This approach is the recommended approach for frontend and backend development.

## Any API (REST, gRPC and GraphQL):

### Add Sufficient Details in Error Message

Error messages should contain sufficient information that a developer or consuming client can act upon.

```json
{
    "errorMessage": "An error has occurred."
}
```

::: bad
Figure: Bad example - The error message does not contain information that can be acted upon
:::

```json
{
    "errorMessage": "Client ID is a required field. Please provide a Client ID."
}
```

::: good
Figure: Good example - The error message provides explicit detail and a short description on how to fix the issue
:::

### Sanitize Response

```none
HTTP/1.1 500 Internal Server Error
Transfer-Encoding: chunked
Content-Type: text/plain
Server: Microsoft-IIS/10.0
X-Powered-By: ASP.NET
Date: Fri, 27 Sep 2019 16:13:16 GMT

System.ArgumentException: We don't offer a weather forecast for chicago. (Parameter 'city')
   at WebApiSample.Controllers.WeatherForecastController.Get(String city) in C:\working_folder\aspnet\AspNetCore.Docs\aspnetcore\web-api\handle-errors\samples\3.x\Controllers\WeatherForecastController.cs:line 34
   at lambda_method(Closure , Object , Object[] )
   at Microsoft.Extensions.Internal.ObjectMethodExecutor.Execute(Object target, Object[] parameters)
   at Microsoft.AspNetCore.Mvc.Infrastructure.ActionMethodExecutor.SyncObjectResultExecutor.Execute(IActionResultTypeMapper mapper, ObjectMethodExecutor executor, Object controller, Object[] arguments)
   at Microsoft.AspNetCore.Mvc.Infrastructure.ControllerActionInvoker.<InvokeActionMethodAsync>g__Logged|12_1(ControllerActionInvoker invoker)
   at Microsoft.AspNetCore.Mvc.Infrastructure.ControllerActionInvoker.<InvokeNextActionFilterAsync>g__Awaited|10_0(ControllerActionInvoker invoker, Task lastTask, State next, Scope scope, Object state, Boolean isCompleted)
   at Microsoft.AspNetCore.Mvc.Infrastructure.ControllerActionInvoker.Rethrow(ActionExecutedContextSealed context)
   at Microsoft.AspNetCore.Mvc.Infrastructure.ControllerActionInvoker.Next(State& next, Scope& scope, Object& state, Boolean& isCompleted)
   at Microsoft.AspNetCore.Mvc.Infrastructure.ControllerActionInvoker.InvokeInnerFilterAsync()
--- End of stack trace from previous location where exception was thrown ---
   at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.<InvokeFilterPipelineAsync>g__Awaited|19_0(ResourceInvoker invoker, Task lastTask, State next, Scope scope, Object state, Boolean isCompleted)
   at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.<InvokeAsync>g__Logged|17_1(ResourceInvoker invoker)
   at Microsoft.AspNetCore.Routing.EndpointMiddleware.<Invoke>g__AwaitRequestTask|6_0(Endpoint endpoint, Task requestTask, ILogger logger)
   at Microsoft.AspNetCore.Authorization.AuthorizationMiddleware.Invoke(HttpContext context)
   at Microsoft.AspNetCore.Diagnostics.DeveloperExceptionPageMiddleware.Invoke(HttpContext context)

HEADERS
=======
Accept: */*
Host: localhost:44312
User-Agent: curl/7.55.1
```

::: bad
Figure: Bad example - this level of data should not be returned in a production environment
:::

### Provide a Tracking or Correlation ID

A tracking or correlation ID will allow the consuming clients to provide the API developers with a reference point in their logs.

```json
{
    "errorMessage": "An error has occurred. Please contact technical support"
}
```

::: bad
Figure: Bad example - No tracking or correlation ID is provided
:::

```json
{
    "errorMessage": "An error has occurred. Please contact technical support",
    "errorId": "3022af02-482e-4c06-885a-81d811ce9b34"
}
```

::: good
Figure: Good exmaple - A error ID is provided as part of the reponse
:::

### Provide an additional Help Resource

Providing a URI to an additional help resources as part of your request will allow consuming clients to find additional resources or documentation that relates to the defined problem.

```json
{
  "ErrorType": "DoesNotExist",
  "Id": "3022af02-482e-4c06-885a-81d811ce9b34",
  "Message": "No Client with a ID of 999999999 was found",
  "StatusCode": 404
}
```

::: bad
Figure: Bad example - No help link provided
:::

```json
{
  "ErrorType": "DoesNotExist",
  "HelpLink": "http://www.myapiapplication/api/help/doesnotexist",
  "Id": "3022af02-482e-4c06-885a-81d811ce9b34",
  "Message": "No Client with a ID of 999999999 was found",
  "StatusCode": 404
}
```

::: good
Figure: Good example - A help link is provided as part of the response
:::
