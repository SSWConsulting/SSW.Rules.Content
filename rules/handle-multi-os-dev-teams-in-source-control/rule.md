---
seoDescription: Learn how to manage a multi-OS development team in source control. This article covers best practices for handling line endings (CRLF vs LF), creating cross-platform setup scripts, configuring Git for consistency, and using .NET CLI for secrets management to boost efficiency across Windows, macOS, and Linux.
type: rule
title: Do you handle Multi-OS dev teams in source control?
uri: handle-multi-os-dev-teams-in-source-control
authors:
  - title: Tom Iwainski
    url: https://www.ssw.com.au/people/thomas-iwainski
related: []
created: 2024-11-05T12:52:08.000Z
archivedreason: null
guid: 7bc2e9c8-2b12-466b-8ecd-34576e3a1648
---

In today’s development world, teams often consist of developers working on different operating systems (OS), such as Windows, macOS, and Linux. While each OS has its own strengths, managing a cross-platform development environment can introduce challenges.

Issues like inconsistent line endings, platform-specific setup scripts, and configuration mismatches can lead to headaches for both individual developers and the team as a whole.

<!--endintro-->

## Addressing Line Ending differences (CRLF vs. LF)

One of the most common issues faced by teams working with Git across different platforms is the handling of line endings. Windows uses **CRLF** (Carriage Return + Line Feed) for line endings, while macOS and Linux use **LF** (Line Feed) only. This can lead to unnecessary diffs in Git and potential merge conflicts.

### Solution: Use Git’s Line Ending configuration

Git provides a way to manage line endings across different operating systems by using the `core.autocrlf` setting. This configuration ensures that line endings are normalized when files are checked in and out of the repository.

* **Windows users**: Set Git to automatically convert line endings to **CRLF** when checking out files, and convert them back to **LF** when committing.

  ```bash
  git config --global core.autocrlf true
  ```

* **macOS/Linux users**: Set Git to automatically convert **CRLF** line endings to **LF** when checking out files and leave them as **LF** when committing.

  ```bash
  git config --global core.autocrlf input
  ```

* **Repository-Wide configuration**: It's a good practice to enforce this configuration across the team via a `.gitattributes` file, which allows you to define how specific file types should be handled. For example:

  ```text
  * text=auto
  *.sh text eol=lf
  *.bat text eol=crlf
  ```

This ensures that, no matter what OS a developer is using, files are checked out and committed with consistent line endings. The `eol` attribute specifically handles cases like batch scripts or shell scripts that may need different line endings.

## Creating Cross-Platform Setup Scripts for Easy Onboarding

Onboarding new developers is a critical step in ensuring that everyone is up and running quickly, but multi-OS teams often struggle with platform-specific setup instructions. The goal is to make onboarding as seamless as possible, whether a developer is using Windows, macOS, or Linux.

### Solution: Write Cross-Platform Setup Scripts Using PowerShell

To streamline onboarding and ensure compatibility across different platforms, it’s crucial to write setup scripts that work on all major operating systems. PowerShell is an ideal choice because it is natively available on Windows and can also be installed on macOS and Linux, making it a truly cross-platform solution. Here's how you can approach writing cross-platform setup scripts with PowerShell:

* **PowerShell for Windows, macOS, and Linux**: Instead of using separate scripts for each platform, write a PowerShell script (`setup.ps1`) that works on all platforms. PowerShell Core (now simply known as PowerShell) is cross-platform and can be run on Windows, macOS, and Linux, allowing you to write one script for all environments. You can use package managers like `Chocolatey` on Windows, `Homebrew` on macOS, or `apt`/`yum` on Linux within the same PowerShell script.

* **Handling OS-Specific Logic in PowerShell**: PowerShell makes it easy to detect the operating system and execute different setup commands depending on the platform. For example, you can check whether the script is running on Windows, macOS, or Linux and then call the appropriate package manager or command for each environment.

Here’s an example of a cross-platform setup script in PowerShell:

```powershell
# Detect the OS and perform platform-specific setup

$os = $env:OS

if ($os -like "*Windows*") {
    Write-Host "Setting up for Windows..."
    # Windows-specific setup, e.g., installing packages via Chocolatey
    choco install somepackage
}
elseif ($os -like "*Linux*" -or $os -like "*Unix*") {
    Write-Host "Setting up for Linux/macOS..."
    # Linux/macOS-specific setup
    if ($IsMacOS) {
        # macOS-specific package manager (Homebrew)
        brew install somepackage
    }
    else {
        # Linux-specific package manager (apt, yum, etc.)
        sudo apt-get install somepackage
    }
}
else {
    Write-Host "Unsupported OS detected."
}

Write-Host "Setup complete!"
```

This script does the following:

1. It checks the environment variable `$env:OS` to detect the operating system.
2. Depending on the platform, it uses the appropriate package manager:
   * **Windows**: Uses `choco` (Chocolatey) to install software.
   * **macOS**: Uses `brew` (Homebrew) for package installation.
   * **Linux**: Uses `apt-get` or similar package managers.

By using PowerShell, you can create a single script that works across all major platforms, reducing the need for platform-specific scripts and simplifying the setup process for your users.

## Consistent Git configuration for Multi-OS Teams

To further ensure smooth collaboration among multi-OS teams, it’s important to standardize Git configurations. Beyond line endings, Git offers other configurations that help maintain consistency.

### Key Git configurations for Multi-OS Teams

* **User Name and Email**: Ensure each developer has set up their user name and email, as this is crucial for committing with correct author information:

  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "youremail@example.com"
  ```

* **Global `.gitignore`**: A global `.gitignore` file can help ensure that certain system files (e.g., `Thumbs.db` on Windows or `.DS_Store` on macOS) are ignored across all repositories. You can create and set a global `.gitignore` file using the following command:

  ```bash
  git config --global core.excludesfile ~/.gitignore_global
  ```

  And in `~/.gitignore_global`:

  ```text
  .DS_Store
  Thumbs.db
  ```

* **Hooks and Templates**: Some repositories might require hooks or commit templates to enforce conventions like conventional commit messages or certain commit checks. Using a `.githooks` or `.gitmessage` file in the repository can help maintain consistency across platforms.
