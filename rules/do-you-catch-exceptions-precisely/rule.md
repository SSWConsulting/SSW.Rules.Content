---
type: rule
title: Do you catch exceptions precisely?
uri: do-you-catch-exceptions-precisely
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
related: []
redirects: []
created: 2013-09-11T19:22:41.000Z
archivedreason: null
guid: 1072907b-d837-45e1-9db5-2a9236bf362f
---
In a try-catch block, avoid catching generic [Exception](https://learn.microsoft.com/en-us/dotnet/api/system.exception?redirectedfrom=MSDN&view=net-8.0) types as this masks the underlying problem. Instead, target only the specific exceptions you can manage, which helps in accurately identifying and rectifying the error.

It is essential to foresee the exceptions that the code in the try block might raise. Catching these specific exceptions at the point of occurrence provides the most context for effectively addressing the issue.

<!--endintro-->

```cs
try 
{ 
     connection.Open();
}
catch (Exception ex) 
{ 
     // Omitted for brevity
}
```

::: bad
Bad code – Catching the general Exception
:::

```cs
try 
{ 
     connection.Open(); 
}
catch (InvalidOperationException ex) 
{ 
     // Omitted for brevity
}
catch (SqlException ex) 
{ 
     // Omitted for brevity
}
```

::: good
Good code - Catch with specific Exception
:::

To further elaborate, here are some reasons why catching specific exceptions is important:

1. **Contextual Handling** - Specific exceptions enable tailored responses. You can close resources in response to an `IOException` or take other actions for a `NullPointerException`.

1. **Code Readability** - Specific exceptions make code more readable. They allow developers to better anticipate potential errors, making the code easier to maintain.

1. **Debugging and Traceability** - A detailed exception type speeds up debugging. A general exception conceals the root cause and complicates diagnosis.

1. **Logging** - Catching a specific exception enables detailed logging, crucial for post-mortem analysis.

1. **Forward Compatibility** - Specific exceptions minimize the risk of future updates causing unintended issues. A broad `Exception` class could inadvertently catch new, unrelated exceptions.

1. **Error Recovery** - Knowing the exact type of exception informs whether to retry an operation, failover, or terminate the program.

1. **Resource Optimization** - Catching broad exceptions is computationally expensive. Targeting specific exceptions allows for more optimized code.

Global exception handlers for a program are an exception to the rule, as they need to catch any uncaught exceptions for the sake of [good user experience](/do-you-present-the-user-with-a-nice-error-screen/). Frameworks often provide mechanisms for this scenario, such as:

* `ASP.NET Core` - You can use [exception handler pages](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling?view=aspnetcore-8.0#exception-handler-page), [middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling?view=aspnetcore-8.0#iexceptionhandler) and [exception handler lambdas](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling?view=aspnetcore-8.0#exception-handler-lambda)

* [Mediator pattern](/keep-business-logic-out-of-the-presentation-layer/) - you can use [error handling middleware](https://github.com/jbogard/MediatR/wiki#exceptions-handling)
