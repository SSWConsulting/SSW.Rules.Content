---
seoDescription: Learn how to manage a multi-OS development team in source control. This article covers best practices for handling line endings (CRLF vs LF), creating cross-platform setup scripts, configuring Git for consistency, and using .NET CLI for secrets management to boost efficiency across Windows, macOS, and Linux.
type: rule
title: Do you handle Multi-OS dev teams in source control?
uri: do-you-handle-multi-os-dev-teams-in-source-control
authors:
  - title: Tom Iwainski
    url: https://www.ssw.com.au/people/thomas-iwainski
related: []
created: 2024-11-05T12:52:08.000Z
archivedreason: null
guid: 7bc2e9c8-2b12-466b-8ecd-34576e3a1648
---

In today’s development world, teams often consist of developers working on different operating systems (OS), such as Windows, macOS, and Linux. While each OS has its own strengths, managing a cross-platform development environment can introduce challenges. Issues like inconsistent line endings, platform-specific setup scripts, and configuration mismatches can lead to headaches for both individual developers and the team as a whole.

<!--endintro-->

## Addressing Line Ending differences (CRLF vs. LF)

One of the most common issues faced by teams working with Git across different platforms is the handling of line endings. Windows uses **CRLF** (Carriage Return + Line Feed) for line endings, while macOS and Linux use **LF** (Line Feed) only. This can lead to unnecessary diffs in Git and potential merge conflicts.

### Solution: Use Git’s Line Ending configuration

Git provides a way to manage line endings across different operating systems by using the `core.autocrlf` setting. This configuration ensures that line endings are normalized when files are checked in and out of the repository.

- **Windows Users**: Set Git to automatically convert line endings to **CRLF** when checking out files, and convert them back to **LF** when committing.

  ```bash
  git config --global core.autocrlf true
  ```

- **macOS/Linux Users**: Set Git to automatically convert **CRLF** line endings to **LF** when checking out files and leave them as **LF** when committing.

  ```bash
  git config --global core.autocrlf input
  ```

- **Repository-Wide Configuration**: It’s a good practice to enforce this configuration across the team via a `.gitattributes` file, which allows you to define how specific file types should be handled. For example:

  ```text
  * text=auto
  *.cs text eol=lf
  *.sh text eol=lf
  *.bat text eol=crlf
  ```

This ensures that, no matter what OS a developer is using, files are checked out and committed with consistent line endings. The `eol` attribute specifically handles cases like batch scripts or shell scripts that may need different line endings.

## Creating Cross-Platform Setup Scripts for Easy Onboarding

Onboarding new developers is a critical step in ensuring that everyone is up and running quickly, but multi-OS teams often struggle with platform-specific setup instructions. The goal is to make onboarding as seamless as possible, whether a developer is using Windows, macOS, or Linux.

### Solution: Write Cross-Platform setup scripts

The key to ensuring easy onboarding is writing platform-agnostic setup scripts that work regardless of OS. Consider the following practices:

- **Use shell scripts for macOS/Linux**: A shell script (`setup.sh`) can handle setup for Linux/macOS environments. You can use tools like `brew` (Homebrew) or `apt` for macOS/Linux package management to install dependencies.

- **Use PowerShell for Windows**: For Windows users, write a PowerShell script (`setup.ps1`) that handles Windows-specific installations and configurations, such as installing software via Chocolatey or downloading other necessary tools.

- **Universal Setup Script with .NET Core**: If you need a script that works across platforms, consider using **.NET Core**. Since .NET Core is cross-platform and works on Windows, macOS, and Linux, it provides a powerful and consistent environment for writing setup scripts. You can create a `.NET Core` application (like a console app) that checks the operating system and runs the corresponding setup commands.

Example of a cross-platform setup script in **.NET Core**:

```csharp
using System;
  using System.Diagnostics;

  class Program
  {
      static void Main(string[] args)
      {
          // Check for OS type
          string os = Environment.OSVersion.Platform.ToString();

          if (os.Contains("Win"))
          {
              RunCommand("powershell.exe", "-ExecutionPolicy Bypass -File setup.ps1");
          }
          else if (os.Contains("Unix"))
          {
              RunCommand("bash", "setup.sh");
          }
          else
          {
              Console.WriteLine("Unsupported OS");
          }
      }

      static void RunCommand(string command, string arguments)
      {
          var processStartInfo = new ProcessStartInfo
          {
              FileName = command,
              Arguments = arguments,
              RedirectStandardOutput = true,
              UseShellExecute = false
          };

          using (var process = Process.Start(processStartInfo))
          using (var reader = process.StandardOutput)
          {
              string result = reader.ReadToEnd();
              Console.WriteLine(result);
          }
      }
  }
```

This script checks the platform and runs the appropriate setup script based on the OS.

## Consistent Git configuration for Multi-OS Teams

To further ensure smooth collaboration among multi-OS teams, it’s important to standardize Git configurations. Beyond line endings, Git offers other configurations that help maintain consistency.

### Key Git cnfigurations for Multi-OS Teams:

- **User Name and Email**: Ensure each developer has set up their user name and email, as this is crucial for committing with correct author information:

  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "youremail@example.com"
  ```

- **Global `.gitignore`**: A global `.gitignore` file can help ensure that certain system files (e.g., `Thumbs.db` on Windows or `.DS_Store` on macOS) are ignored across all repositories. You can create and set a global `.gitignore` file using the following command:

  ```bash
  git config --global core.excludesfile ~/.gitignore_global
  ```

  And in `~/.gitignore_global`:

  ```text
  .DS_Store
  Thumbs.db
  ```

- **Hooks and Templates**: Some repositories might require hooks or commit templates to enforce conventions like conventional commit messages or certain commit checks. Using a `.githooks` or `.gitmessage` file in the repository can help maintain consistency across platforms.

---

## Handling .NET secrets across platforms

When working with .NET applications, developers often use the Visual Studio UI for managing secrets. The UI doesn’t work well across different platforms. To ensure consistency, the **CLI** is a better choice for managing secrets in a cross-platform environment.

### Solution: Use the .NET CLI for secrets management

Use the `.NET CLI` to store and retrieve secrets, as this approach works consistently on all platforms:

- **Set a secret**:

  ```bash
  dotnet user-secrets set "MySecret" "secret-value"
  ```

- **Get a secret**:

  ```bash
  dotnet user-secrets get "MySecret"
  ```

By relying on the `.NET CLI`, your team ensures that secrets are handled consistently, regardless of the operating system.

For more information visit [Safe storage of app secrets in development in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-8.0&tabs=linux)

---

## General best practices for Cross-Platform efficiency

Finally, here are a few other general tips that can improve team efficiency regardless of their OS:

- **Use Cross-Platform IDEs**: Encourage the use of cross-platform IDEs like **VS Code**, which work equally well on Windows, macOS, and Linux. Configure shared extensions and settings that improve productivity.

- **Use Docker for local development**: Using Docker containers for local development can ensure that all team members, regardless of their OS, are working in a consistent environment. This also helps avoid issues where code works on one developer’s machine but not on another's due to OS-specific dependencies.

- **Use CI/CD Pipelines**: Set up Continuous Integration and Continuous Deployment (CI/CD) pipelines that build and test your application on multiple operating systems to catch any platform-specific issues early.
