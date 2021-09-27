---
type: rule
title: Do you use a logging framework?
uri: do-you-look-for-console-writeline-and-change-it-to-trace-writeline
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
related: []
redirects:
  - do-you-use-a-logging-framework
created: 2012-04-01T09:53:00.000Z
archivedreason: null
guid: 37153c77-e1af-4d82-a200-1ab7fbb6d0b2
---

Unless you are writing a Console application, any output that uses Console.WriteLine will almost certainly be lost.  You're much better off using Trace.WriteLine.

A better approach is to use Trace.WriteLine. You can create a trace listener to send your Trace.WriteLine statements to the Console if you wish, but you can also redirect them elsewhere if required. See [this MSDN article for more information](http&#58;//msdn.microsoft.com/en-us/library/sk36c28t.aspx).

<!--endintro-->

```
Console.WriteLine("Service started");
```

::: bad
 Figure: Bad Example - Using Console.WriteLine to write debug information  
:::

```
Trace.WriteLine("Service started");
```
::: good
 Figure: Better Example - Using Trace.WriteLine to write debug informatio  
:::

The best approach is to use the logging abstractions built into .NET Core and .NET (5+). You can configure
- The logging sinks - where the logs are written to e.g. log file, database, table storage, or Application Insights
- Filter output based off severity (Verbose/Debug/Info/Warning/Error) - so you can dial it up or down without changing code
- Use dependency injection to inject the loggers into your classes so you aren't tightly coupled to a specific framework
- You can extend on this further by using tools like Serilog to include structured objects as well.

```
public class Worker : BackgroundService
{
    private readonly ILogger<Worker> _logger;

    public Worker(ILogger<Worker> logger) =>
        _logger = logger;

    protected override async Task ExecuteAsync(CancellationToken cancellationToken )
    {
        while (!cancellationToken.IsCancellationRequested)
        {
            _logger.LogInformation("Worker running at: {time}", DateTimeOffset.UtcNow);
            await Task.Delay(1000, cancellationToken);
        }
    }
}
```

::: good
Figure: Best Example – Using ILogger to log information
:::