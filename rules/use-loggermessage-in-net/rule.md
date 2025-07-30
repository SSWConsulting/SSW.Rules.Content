---
seoDescription: Learn how to optimize logging in .NET applications using the LoggerMessage class. Discover the performance benefits, such as reduced object allocations and efficient message parsing, and get practical tips on how to implement this pattern for better logging efficiency and structured logs in high-performance scenarios.
type: rule
title: Do you use LoggerMessage in .NET?
uri: use-loggermessage-in-net
authors:
  - title: Tom Iwainski
    url: https://www.ssw.com.au/people/thomas-iwainski
related: []
created: 2024-11-05T12:52:08.000Z
archivedreason: null
guid: 2feb782f-0cee-4022-95d9-f44b9f739b90
---

Logging is a critical component in modern applications, but it can easily introduce performance overhead.

.NET 6 introduced the `LoggerMessageAttribute`, a feature in the `Microsoft.Extensions.Logging` namespace that enables source-generated, highly performant logging APIs. This approach eliminates runtime overheads like boxing and temporary allocations, making it faster than traditional logging methods.

<!--endintro-->

## Key performance benefits of LoggerMessageAttribute

* **Source Generation:** Automatically generates the implementation of partial methods with compile-time diagnostics.
* **Improved Performance:** Reduces runtime overhead by leveraging compile-time optimizations.
* **Flexible Usage:** Supports static and instance-based methods with configurable log levels and message templates.

## How to use LoggerMessageAttribute

Define logging methods as partial and static to trigger the code generator:

```csharp
public static partial class Log
{
    [LoggerMessage(
        EventId = 0,
        Level = LogLevel.Critical,
        Message = "Could not open socket to `{HostName}`")]
    public static partial void CouldNotOpenSocket(
        ILogger logger, string hostName);
}
```

Logging methods can also be used in an instance context by accessing an `ILogger` field or primary constructor parameter:

```csharp
public partial class InstanceLoggingExample(ILogger logger)
{
    [LoggerMessage(
        EventId = 0,
        Level = LogLevel.Critical,
        Message = "Could not open socket to `{HostName}`")]
    public partial void CouldNotOpenSocket(string hostName);
}
```

Using `LoggerMessageAttribute` with `JsonConsole` formatter can produce structured logs.
In our log messages we can specify custom event names as well as utelize string formatters:

```csharp
[LoggerMessage(
        EventId = 9,
        Level = LogLevel.Trace,
        EventName = "PropertyValueEvent")]
        Message = "In {City} the average property value is {Value:E}")]
public static partial void PropertyValueInAustralia(ILogger logger, string city double value);
```

## Constraints

When using `LoggerMessageAttribute`, ensure:

* Logging methods must be `partial` and return `void`.
* Logging method names must not start with an underscore.
* Parameter names of logging methods must not start with an underscore.
* Logging methods may not be defined in a nested type.
* Logging methods cannot be generic.
* If a logging method is `static`, the `ILogger` instance is required as a parameter.

## More information

See this great article on Microsoft Learn which goes into more detail and usage examples: [Compile-time logging source generation in .NET](https://learn.microsoft.com/en-us/dotnet/core/extensions/logger-message-generator).
