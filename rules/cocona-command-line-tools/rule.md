---
seoDescription: Build powerful .NET command line tools with Cocona - a lightweight framework that transforms C# methods into CLI commands with automatic help generation, validation, and dependency injection support.
type: rule
title: Do you use Cocona for building great command line tools in .NET?
uri: cocona-command-line-tools
authors:
  - title: Brady Stroud
    url: https://www.ssw.com.au/people/brady-stroud
created: 2025-01-03T00:00:00.000Z
guid: 8a2f4e3d-1b5c-4e6f-8a9b-2c3d4e5f6a7b
related:
    - provide-list-of-arguments
    - do-you-use-a-dependency-injection-centric-architecture
    - dependency-injection
    - use-fluent-validation
---

When building command line applications in .NET, you need a framework that makes argument parsing, validation, and help generation simple and intuitive. [Cocona](https://github.com/mayuki/Cocona) is a lightweight and powerful framework that turns your C# methods into fully-featured CLI commands with minimal boilerplate code.

Cocona has many built-in features that make it feel familiar to .NET developers.

## Why use Cocona?

Cocona offers several advantages over manual argument parsing or other CLI frameworks:

* **Simple and intuitive**: Transform regular C# methods into CLI commands
* **Automatic help generation**: Built-in help text and usage information
* **Type safety**: Strong typing for command parameters and options
* **Dependency injection**: Built-in DI container support
* **Validation support**: Integration with data annotations for parameter validation
* **Async support**: First-class support for async/await patterns
* **Multiple commands**: Easy support for sub-commands and complex CLI structures

<!--endintro-->

## Basic Example

Here's how to create a simple CLI tool with Cocona:

```csharp
// Manual argument parsing - error-prone and verbose
class Program
{
    static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            Console.WriteLine("Usage: myapp <name> [--greeting <greeting>]");
            return;
        }

        string name = args[0];
        string greeting = "Hello";
        
        for (int i = 1; i < args.Length; i++)
        {
            if (args[i] == "--greeting" && i + 1 < args.Length)
            {
                greeting = args[i + 1];
                i++;
            }
        }
        
        Console.WriteLine($"{greeting}, {name}!");
    }
}
```

::: bad
Figure: Bad example - Manual argument parsing is error-prone and verbose.
:::

```csharp
using Cocona;

var app = CoconaApp.Create();
app.AddCommand("greet", (string name, string greeting = "Hello") => 
{
    Console.WriteLine($"{greeting}, {name}!");
});
app.Run();
```

::: good
Figure: Good example - Cocona simplifies command line argument parsing and usage. 😌
:::

## Validation

Cocona integrates seamlessly with data annotations for parameter validation.

```csharp
using Cocona;
using System.ComponentModel.DataAnnotations;

public class FileProcessor
{
    public void ProcessFiles(
        [Argument] string inputPath,
        [Argument, StringLength(50)] string fileName,
        [Argument] string? optionalMetadata,
        [Option('o', Description = "Output directory")] string outputPath = "./output",
        [Option, Range(1, 10)] int threads = 1,
        [Option] bool verbose = false)
    {
        if (verbose)
            Console.WriteLine($"Processing {inputPath} with {threads} threads...");
            
        // Your file processing logic here
        Console.WriteLine($"Files processed and saved to {outputPath}");
    }
}

var app = CoconaApp.Create();
app.AddCommands<FileProcessor>();
app.Run();
```

## Multiple Commands Example

For more complex CLI tools with multiple commands:

```csharp
using Cocona;

public class DatabaseCommands
{
    [Command("migrate")]
    public async Task MigrateDatabase(
        [Option] string connectionString,
        [Option] bool dryRun = false)
    {
        Console.WriteLine($"Migrating database (dry run: {dryRun})...");
        // Migration logic
    }
    
    [Command("seed")]
    public async Task SeedDatabase(
        [Option] string connectionString,
        [Option] string dataFile = "seed.json")
    {
        Console.WriteLine($"Seeding database from {dataFile}...");
        // Seeding logic
    }
}

var app = CoconaApp.Create();
app.AddCommands<DatabaseCommands>();
app.Run();
```

This creates a CLI with commands like:

* `myapp migrate --connection-string "..." --dry-run`
* `myapp seed --connection-string "..." --data-file "custom.json"`

## Integration with Dependency Injection

Cocona works great with .NET's built-in dependency injection:

```csharp
public class EmailCommands
{
    private readonly EmailService _emailService;
    
    public EmailCommands(EmailService emailService)
    {
        _emailService = emailService;
    }
    
    [Command]
    public void Send(string to, string subject, string body)
    {
        _emailService.SendEmail(to, subject, body);
    }
}

var builder = CoconaApp.CreateBuilder();
builder.Services.AddTransient<EmailService>();
builder.Services.AddLogging(b => b.AddConsole());

var app = builder.Build();
app.AddCommands<EmailCommands>();
app.Run();
```

For more information, visit the [Cocona GitHub repository](https://github.com/mayuki/Cocona).

::: info
**Tip:** Improve your CLI tool's UI with tools like [Colorful.Console](https://github.com/khalidabuhakmeh/Colorful.Console) for colored output, or [Spectre.Console](https://spectreconsole.net/) for rich terminal applications.
:::
