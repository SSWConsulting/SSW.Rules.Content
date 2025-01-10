---
seoDescription: Learn how to use Microsoft's `FakeLogger` in unit tests to verify logging behavior in .NET applications. This guide shows you how to capture log entries, check log levels, and ensure your logging works as expected during testing.
type: rule
title: Do you use Logging Fakes?
uri: use-logging-fakes
authors:
  - title: Tom Iwainski
    url: https://www.ssw.com.au/people/thomas-iwainski
related: []
created: 2024-11-05T12:52:08.000Z
archivedreason: null
guid: dc76970f-deea-4e92-9d55-731e83bee7b5
---

Unit tests are an essential part of ensuring .NET applications work correctly. However, when it comes to testing logging, things can get tricky. You don't want to rely on actual logging infrastructure like file writes or external logging systems during tests, as this could lead to unnecessary complexity and slow down your test suite.

Microsoft provides a simple solution with `FakeLogger`. This logger allows you to capture and verify logging calls in unit tests without needing to integrate with a real logging framework.

By incorporating `FakeLogger` into tests, you can ensure that the logging functionality is correct and meets your application's needs, all while maintaining fast and isolated tests.

<!--endintro-->

## What is the FakeLogger?

The FakeLogger is a mock logger provided by Microsoft for unit testing. It is part of the Microsoft.Extensions.Logging namespace and is used primarily in tests to verify that logging actions occur during the execution of the application, without sending log output to external destinations like the console or log files. Instead, it "fakes" the log output, allowing assertions to be made on the log entries.

The advantage of using `FakeLogger` is that it behaves like a real `ILogger<T>`, but it stores the logs in memory, making them available for examination during tests.

## Benefits of using FakeLogger

- **No External Dependencies** - Since `FakeLogger` does not actually write logs anywhere (such as to disk or a remote server), it keeps unit tests isolated and fast
- **Verify Log Entries** - You can assert that certain log messages were generated during the execution of specific methods, helping to verify that logging statements are firing correctly
- **Easy Integration** - `FakeLogger` is easy to integrate into any unit test framework, making it a seamless addition to your existing test suite

## How to use FakeLogger

To get started with `FakeLogger`, you need to install the necessary package.

Then you can begin using the FakeLogger in unit tests. Here's how to use it:

### Step 1: Create the FakeLogger

You start by creating an instance of `FakeLogger<T>`. This logger will capture any log entries for later verification.

```csharp
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Logging.Abstractions;

public class MyServiceTests
{
    [Fact]
    public void TestLoggingBehavior()
    {
        // Create a FakeLogger instance
        var logger = new FakeLogger<MyService>();

        // Create the service and pass in the fake logger
        var myService = new MyService(logger);

        // Act: Call a method that should log something
        myService.DoSomethingThatLogs();

        // Assert: Verify that a log entry was captured
        var logEntries = logger.GetLogEntries();
        Assert.Contains(logEntries, log => log.Message.Contains("Operation completed successfully"));
    }
}
```

### Step 2: Define the MyService class

Here's an example class that uses logging. This class would typically contain methods that trigger logging when certain actions are taken.

```csharp
public class MyService
{
    private readonly ILogger<MyService> _logger;

    public MyService(ILogger<MyService> logger)
    {
        _logger = logger;
    }

    public void DoSomethingThatLogs()
    {
        // Log a success message
        _logger.LogInformation("Operation completed successfully.");
    }
}
```

In the example above, MyService uses `ILogger<MyService>` to log an informational message when the `DoSomethingThatLogs()` method is called.

### Step 3: Verify log entries

The next step in your unit test is to check the logs that were captured by `FakeLogger`. You can use methods like `GetLogEntries()` to retrieve the logs and assert on their contents.

```csharp
var logEntries = logger.GetLogEntries();

Assert.Single(logEntries);
Assert.Equal("Operation completed successfully.", logEntries[0].Message);
```

This assertion checks that exactly one log entry was captured and that the message matches the expected text.

## Advanced usage of FakeLogger

While the basic usage of FakeLogger is straightforward, you can also use it to verify log levels, event IDs, and other log-related data.

### Verifying Log Levels

You can verify that the correct log level was used when logging messages. For example, if you're testing that an error is logged, you can assert that the log level is `LogLevel.Error`.

```csharp
var logger = new FakeLogger<MyService>();
var myService = new MyService(logger);

myService.DoSomethingThatLogsError();  // Imagine this method logs an error

var logEntries = logger.GetLogEntries();
Assert.Contains(logEntries, log => log.LogLevel == LogLevel.Error);
```

### Verifying Log Event IDs

In some scenarios, you may log messages with specific event IDs to categorize logs. FakeLogger captures these event IDs, allowing you to assert that they are set correctly.

```csharp
public void LogWithEventId()
{
    _logger.LogInformation(new EventId(1001, "SomeEvent"), "Event 1001 triggered.");
}

var logger = new FakeLogger<MyService>();
var myService = new MyService(logger);

myService.LogWithEventId();

var logEntries = logger.GetLogEntries();
Assert.Contains(logEntries, log => log.EventId.Id == 1001 && log.Message.Contains("Event 1001 triggered"));
```
