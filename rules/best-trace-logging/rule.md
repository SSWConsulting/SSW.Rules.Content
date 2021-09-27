---
type: rule
title: Do you use the best trace logging library?
uri: best-trace-logging
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
  - title: Brendan Richards
    url: https://ssw.com.au/people/brendan-richards
related: []
redirects:
  - do-you-use-the-best-trace-logging-library
created: 2013-09-11T21:38:08.000Z
archivedreason: null
guid: 5ecb7c85-0a65-494c-ac1a-51c71c4546aa
---

Did you know that writing your own logging infrastructure code wastes time? There are awesome logging abstractions in .NET Core and .NET 5+ that you should use instead!

These abstractions allow you to:
- create log entries in a predictable and familiar fashion - you use the same patterns for logging in a [Background Service](https://docs.microsoft.com/en-us/dotnet/core/extensions/logging?tabs=command-line) as you would in a [Blazor WASM app](https://docs.microsoft.com/en-us/aspnet/core/blazor/fundamentals/logging?view=aspnetcore-5.0&pivots=webassembly) (just some slightly different bootstrapping 😉)
- use Dependency Injection; your code doesn't take a dependency on a particular framework (as they are abstractions)
- filter output based off severity (Verbose/Debug/Info/Warning/Error) - so you can dial it up or down without changing code
- have different logs for different components of your application (e.g. a Customer Log and an Order Log)
- multiple logging sinks - where the logs are written to e.g. log file, database, table storage, or Application Insights
- supports log message templates allowing logging providers to implement [semantic or structured logging](https://github.com/NLog/NLog/wiki/How-to-use-structured-logging)
- can be used with a range of [3rd party logging providers](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/logging/#third-party-logging-providers-1)

<!--endintro-->

Read more at [Logging in .NET Core and ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/logging)

::: bad  
![Figure: Bad Example - Using Debug or Trace for logging, or writing hard coded mechanisms for logging does not allow you to configure logging at runtime](trace-logging-bad.jpg)  
:::


::: bad  
![Figure: Bad Example - Roll your own logging components lack functionality, and have not been tested as thoroughly for quality or performance as log4net](trace-logging-bad-2.jpg)
:::


```
_logger.LogInformation("Getting item {Id} at {RequestTime}", id, DateTime.Now);
```
::: good  
Good Example - Using templates allows persisting structured log data (DateTime is a complex object)
:::


::: good
![Figure: Good Example - Seq provides a powerful UI for searching and viewing your structured logs](seq2.png)  
:::


`youtube: https://www.youtube.com/embed/pUMs8TkuMFk`
