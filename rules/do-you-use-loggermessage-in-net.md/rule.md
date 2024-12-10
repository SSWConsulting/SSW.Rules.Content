---
seoDescription: Learn how to optimize logging in .NET applications using the LoggerMessage class. Discover the performance benefits, such as reduced object allocations and efficient message parsing, and get practical tips on how to implement this pattern for better logging efficiency and structured logs in high-performance scenarios.
type: rule
title: Do you use LoggerMessage in .NET?
uri: do-you-use-loggermessage-in-net
authors:
  - title: Tom Iwainski
    url: https://www.ssw.com.au/people/thomas-iwainski
related: []
created: 2024-11-05T12:52:08.000Z
archivedreason: null
guid: 2feb782f-0cee-4022-95d9-f44b9f739b90
---

Logging is a critical component in modern applications, but it can easily introduce performance overhead.

The LoggerMessage class in .NET offers a solution to reduce the performance costs associated with logging. By utilizing this pattern, developers can optimize logging with fewer object allocations and reduced overhead.

<!--endintro-->

## Key performance benefits of LoggerMessage

1. **Reduced Object Allocations**: Traditional logger extension methods often require "boxing" of value types (e.g., integers or dates) into objects. LoggerMessage avoids this by using static Action fields and strongly typed parameters, eliminating the need for boxing and reducing memory overhead.

2. **Efficient Message Parsing**: Logger extension methods parse the log message template each time a log entry is made. In contrast, LoggerMessage only parses the template once when the message is defined, leading to fewer computations and faster execution during logging.

3. **Structured Logging**: With LoggerMessage, log templates can include placeholders that are filled with specific log data, such as Item or DateTime. This makes it easier to integrate structured logging with logging frameworks like Serilog, which can enrich logs with meaningful event names.

## How to use LoggerMessage

To use the LoggerMessage pattern, you define a static Action delegate for logging a message. The LoggerMessage.Define method is used to create these delegates with parameters such as:

- Log Level (e.g., LogLevel.Information)
- Event ID (for tracking specific events)
- Message Template (a named format string with placeholders)

For example:

Each log message is represented as an Action delegate.

```csharp
private static readonly Action<ILogger, WorkItem, Exception> s_processingPriorityItem =
    LoggerMessage.Define<WorkItem>(
        LogLevel.Information,
        new EventId(1, nameof(PriorityItemProcessed)),
        "Processing priority item: {Item}");

private static readonly Action<ILogger, Exception> s_failedToProcessWorkItem = LoggerMessage.Define<Exception>(
    LogLevel.Critical,
    new EventId(13, nameof(FailedToProcessWorkItem)),
    "Epic failure processing item!");
```

This delegate is then invoked using strongly typed extension methods like PriorityItemProcessed, making it simple to log information in a structured manner with minimal performance impact.

```csharp
public static void PriorityItemProcessed(
    this ILogger logger, WorkItem workItem) =>
    s_processingPriorityItem(logger, workItem, default!);

public static void FailedToProcessWorkItem(
    this ILogger logger, Exception  ex) =>
    s_failedToProcessWorkItem(logger, ex);
```

Usage example:

```csharp
protected override async Task ExecuteAsync(
    CancellationToken stoppingToken)
{
    using (IDisposable? scope = logger.ProcessingWorkScope(DateTime.Now))
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            try
            {
                WorkItem? nextItem = priorityQueue.ProcessNextHighestPriority();

                if (nextItem is not null)
                {
                    logger.PriorityItemProcessed(nextItem);
                }
            }
            catch (Exception ex)
            {
                logger.FailedToProcessWorkItem(ex);
            }

            await Task.Delay(1_000, stoppingToken);
        }
    }
}

```

## Optimizing further with ILogger.IsEnabled

For even better performance, you can check whether logging is enabled for a particular log level using `ILogger.IsEnabled(LogLevel)`. This check ensures that logging statements aren't called when the log level is not configured, thus avoiding unnecessary object allocations and improving efficiency.

```csharp
if (logger.IsEnabled(LogLevel.Information))
{
    logger.Information("This is a log message.");
}
```

## When to use LoggerMessage

The LoggerMessage pattern is particularly beneficial in scenarios where logging needs to be performed frequently with minimal performance impact. It is most effective when:

- Logging is done in high-throughput scenarios (e.g., background services, real-time applications)
- You require structured logging for easier integration with advanced logging systems (e.g., Serilog, ElasticSearch)
- Reducing object allocations and computational overhead is a priority for the application.

## More information

See this great article on Microsoft Learn which goes into more detail and usage examples: [High-performance logging in .NET](https://learn.microsoft.com/en-us/dotnet/core/extensions/high-performance-logging).
