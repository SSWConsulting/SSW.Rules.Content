---
type: rule
archivedreason: 
title: Do you return detailed error messages?
guid: 7af36676-1eed-48dd-854b-2a956ef10e50
uri: do-you-return-detailed-error-messages
created: 2015-08-27T01:00:17.0000000Z
authors:
- title: Jeremy Cade
  url: https://ssw.com.au/people/jeremy-cade
related: []
redirects: []

---

Good error design is as important to the sucess of an API as the API design itself. A good error message provides context and visibility on how to troubleshoot and resolve issues at critical times.

<!--endintro-->

### For REST, start by using the correct HTTP Status Codes...


The HTTP/1.1 RFC lists over 70 different HTTP Status Codes. Very few developers will be able to remember all of them, so it pays to keep it simple and use the most common Status Codes. The basic rule is to use the following three:

* **200 OK** - Everything worked. Success
* **400 Bad Request** - The consuming application did something wrong.
* **500 Internal Server Error** - The API Application did something wrong.


### ...And then include the problem details


RFC 7807 - Problem Details for HTTP APIs (ietf.org) details the specification for returning errors from your API. The HTTP Status Codes are an excellent start - they immediately tell you *where*the problem is, but they don't tell you *what*the problem is.

ASP.Net Core has built in support for the problem details specification. You can see more at the official documentation. Handle errors in ASP.NET Core web APIs | Microsoft Docs

### And for any API (REST, gRPC and GraphQL):

### Make your error messages as verbose as necessary...

Error messages should contain a sufficient level of information that a developer or consuming client can act upon.



```
{
    "errorMessage": "An error has occurred."
}
```




::: bad
Figure: Bad Example - The error message does not contain information that can be acted upon.  
:::



```
{
    "errorMessage": "Client ID is a required field. Please provide a Client ID."
}
```




::: good
Figure: Good Example - The error message provides explicit detail and a short description on how to fix the issue.  
:::

### ...But no more verbose than that




```
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
Figure: Bad Example - this level of data should not be returned in a production environment

:::

### Provide a Tracking or Correlation ID

A tracking or correlation ID will allow the consuming clients to provide the API developers with a reference point in their logs.



```
{
    "errorMessage": "An error has occurred. Please contact technical support"
}
```




::: bad
Figure: Bad Example - No tracking or correlation ID is provided.  
:::



```
{
    "errorMessage": "An error has occurred. Please contact technical support",
    "errorId": "3022af02-482e-4c06-885a-81d811ce9b34"
}
```




::: good
Figure: Good Exmaple - A error ID is provided as part of the reponse.  
:::

### Provide an additional Help Resource

Providing a URI to an additional help resources as part of your request will allow consuming clients to find additional resources or documentation that relates to the defined problem.



```
{
  
  "ErrorType": "DoesNotExist",
  
  "Id": "3022af02-482e-4c06-885a-81d811ce9b34",
  
  "Message": "No Client with a ID of 999999999 was found",
  
  "StatusCode": 404

}
```




::: bad
``Figure: Bad Example - No Help Link Provided

:::



```
{
  
  "ErrorType": "DoesNotExist",
  
  "HelpLink": "http://www.myapiapplication/api/help/doesnotexist",
  
  "Id": "3022af02-482e-4c06-885a-81d811ce9b34",
  
  "Message": "No Client with a ID of 999999999 was found",
  
  "StatusCode": 404

}
```




::: good
Figure: Good Example - A help link is provided as part of the response.

:::
