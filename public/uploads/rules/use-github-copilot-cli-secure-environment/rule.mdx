---
type: rule
tips: ""
title: Do you use GitHub Copilot CLI in a secure dockerised environment?
seoDescription: Learn how to run GitHub Copilot CLI in a secure Docker sandbox
  that isolates AI operations to your current project directory. This approach
  provides powerful AI assistance while maintaining strict security boundaries.
uri: use-github-copilot-cli-secure-environment
authors:
  - title: Gordon Beeming
    url: https://ssw.com.au/people/gordon-beeming
  - title: Lewis Toh
    url: https://ssw.com.au/people/lewis-toh
created: 2025-10-16T17:32:00.000Z
guid: babc794e-a638-4d05-b234-52d69ae4f432
---

GitHub Copilot CLI is incredibly powerful, but giving AI deep access to your terminal and file system can be concerning. When you use features like `--allow-all-tools` - which approves all actions - Copilot can execute commands on your behalf, which means one wrong suggestion could have serious consequences.

Running Copilot CLI in a secure Docker container provides the best of both worlds: powerful AI assistance with strict security boundaries that limit the "blast radius" of any potential mistakes.

<!--endintro-->

## The problem with unrestricted access

When running Copilot CLI directly on your host machine:

::: greybox
**Copilot has access to:**

* Your entire file system
* Your SSH keys in `~/.ssh/`
* All your repositories
* Your environment variables and secrets
* System-wide configurations
:::
::: bad
Bad example - Copilot running with full system access creates unnecessary risk - a single mistake like `rm -rf ~` could be catastrophic
:::

## The solution: Docker-based isolation

By running Copilot CLI inside a Docker container, you create a secure sandbox where:

* Copilot can only see your **current project directory**
* Your home directory, SSH keys, and other projects are completely inaccessible
* You can safely use `--allow-all-tools` with confidence (automatic approval)
* The worst-case scenario is limited to the current project

### Understanding the safety net

If Copilot runs a dangerous command like `rm -rf .`:

**❌ Without Docker:**

* Deletes everything in current directory and subdirectories, depending on the folder you ran copilot in, could be catastrophic
* No way to easily recover lost files and folders

**✅ With Docker:**

* Only deletes files in the mounted current directory (mapped to the same path as your host)
* Your other projects and system files are safe
* If setup with git, it is easily recoverable

::: info
**Note:** The container shares your host's network, so it can access local resources and services. This is intentional for development workflows but means it's not a fully firewalled environment.
:::

### Understanding the two modes

Before diving into the setup, it's important to understand the two approaches available. You can install both side-by-side with different command names to give yourself options.

**Safe Mode (Recommended)** - Always asks for confirmation before executing commands. Use this for general development work where you want control over what gets executed.

**YOLO Mode (Auto-Approve)** - Automatically approves all tool usage without confirmation. Convenient for trusted workflows but use with caution as it can execute commands without prompting.

Both modes include security checks for proper GitHub token scopes and warn about overly privileged tokens. The YOLO mode adds the `--allow-all-tools` flag which bypasses execution confirmation.

### Implementation: The copilot_here setup

The complete solution is available at [https://github.com/GordonBeeming/copilot_here](https://github.com/GordonBeeming/copilot_here).

:::info
**Note:** The setup below provides cross-platform support for Linux/macOS and Windows. For the latest version and additional features, always check the GitHub repository.
:::

#### Install

**For Linux/macOS (Bash/Zsh):**

```bash
# Download the script
curl -fsSL https://raw.githubusercontent.com/GordonBeeming/copilot_here/main/copilot_here.sh -o ~/.copilot_here.sh

# Add to your shell profile (~/.zshrc or ~/.bashrc) - only if not already there
if ! grep -q "source ~/.copilot_here.sh" ~/.zshrc 2>/dev/null; then
  echo '' >> ~/.zshrc
  echo 'source ~/.copilot_here.sh' >> ~/.zshrc
fi

# Reload your shell
source ~/.zshrc  # or source ~/.bashrc
```

**For Windows (PowerShell):**

```powershell
# Download the script
$scriptPath = "$env:USERPROFILE\Documents\PowerShell\copilot_here.ps1"
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/GordonBeeming/copilot_here/main/copilot_here.ps1" -OutFile $scriptPath

# Add to your PowerShell profile - only if not already there
if (-not (Select-String -Path $PROFILE -Pattern "copilot_here.ps1" -Quiet -ErrorAction SilentlyContinue)) {
    Add-Content $PROFILE "`n. $scriptPath"
}

# Reload your profile
. $PROFILE
```

### Keeping Up-to-Date

The scripts include automatic update functionality:

```bash
# Linux/macOS or Windows PowerShell
copilot_here --update
```

This will:
- Download and install the latest version of the CLI binary
- Show you the version change
- Automatically reload the updated functions

### Usage Examples

**Interactive Mode:**

```bash
# Start interactive session (asks for confirmation)
copilot_here

# Start interactive session (auto-approves)
copilot_yolo
```

**Non-Interactive Mode with Prompts:**

```bash
# Safe mode - asks for confirmation
copilot_here --prompt "clean and reinstall dependencies"
copilot_here -p "explain the code in ./my-script.js"

# YOLO mode - auto-approves
copilot_yolo --prompt "clean and reinstall dependencies"
copilot_yolo -p "generate README for this project"
```

```bash
> Copilot suggests: rm -rf node_modules package-lock.json && npm install
Execute this command? [y/N]: y
✅ Executed safely in current directory only
```

::: good
Good example - Use `-p` or `--prompt` flag to pass prompts directly to Copilot CLI
:::

**With Image Variants:**

```bash
# Use .NET image
copilot_here --dotnet --prompt "build and test this .NET project"
copilot_here -d -p "explain this C# code"

# Use .NET + Playwright image
copilot_here --dotnet-playwright --prompt "run playwright tests"
copilot_here -dp -p "write browser automation tests"
```

::: info
**Tip:** Install both functions so you can choose based on the situation. Use `copilot_here` by default and `copilot_yolo` only in trusted projects.
:::

## How it works

### Security features

1. **File System Isolation**
   * Only mounts your current project directory (to the same path as on your host)
   * Your home directory, SSH keys, and other projects are completely hidden
   * Configuration stored in isolated `~/.config/copilot-cli-docker`

2. **Token Scope Validation**
   * Checks that your GitHub token has the required `copilot` scope
   * Warns if your token has dangerous elevated permissions
   * Requires explicit confirmation for high-privilege tokens

3. **User Permission Mapping (Linux/macOS)**
   * Uses `PUID` and `PGID` to match your user ID inside the container
   * Files created by Copilot have correct ownership on your host
   * Windows Docker Desktop handles permissions automatically

4. **Network Access**
   * Container shares host network for development workflows
   * Can access local services and APIs (by design)
   * Not a fully firewalled environment

### Specialized Docker Image Variants

Different development scenarios call for different tools. The setup supports multiple image variants:

**Available variants:**
- **Base image (default)** - Node.js 20, Git, and essential tools
- **`--dotnet` (`-d`)** - .NET 8, 9 & 10 SDKs
- **`--dotnet8` (`-d8`)** - .NET 8 SDK only
- **`--dotnet9` (`-d9`)** - .NET 9 SDK only
- **`--dotnet10` (`-d10`)** - .NET 10 SDK only
- **`--playwright` (`-pw`)** - Browser automation with Playwright
- **`--dotnet-playwright` (`-dp`)** - .NET + Playwright combined
- **`--rust` (`-rs`)** - Rust toolchain
- **`--dotnet-rust` (`-dr`)** - .NET + Rust combined

**Usage:**

```bash
# Use .NET image
copilot_here --dotnet -p "build and test this .NET project"
copilot_here -d -p "explain this C# code"

# Use .NET + Playwright image
copilot_here --dotnet-playwright -p "run playwright tests for this app"
copilot_here -dp -p "write browser automation tests"

# YOLO mode with .NET image
copilot_yolo --dotnet -p "create a new ASP.NET Core API project"
copilot_yolo -d -p "scaffold a new web API"
```

### Additional Features

- **`-h` or `--help`** - Show usage help and examples (Bash/Zsh) or `-Help` (PowerShell)
- **`--no-cleanup`** - Skip cleanup of unused Docker images (Bash/Zsh) or `-NoCleanup` (PowerShell)
- **`--no-pull`** - Skip pulling the latest image (Bash/Zsh) or `-NoPull` (PowerShell)

The functions automatically clean up unused Docker images tagged with the project label, keeping your system tidy.

## ✅ Benefits

This approach provides:

* **Security:** Strict isolation limits damage potential
* **Confidence:** Use powerful features like `--allow-all-tools` safely
* **Portability:** Same setup works across all machines
* **Cross-platform:** Works on Linux, macOS, and Windows
* **Auto-authentication:** Seamlessly uses your existing `gh` login
* **Cognitive ease:** Feel safe letting AI execute commands
* **Flexibility:** Choose safe or YOLO mode based on context
* **Language support:** Specialized images for .NET, Rust, browser testing, and more

## Learn more

For detailed implementation, troubleshooting, and the complete source code:

* **Blog post 📖:** [Taming the AI: My Paranoid Guide to Running Copilot CLI in a Secure Docker Sandbox](https://gordonbeeming.com/blog/2025-10-03/taming-the-ai-my-paranoid-guide-to-running-copilot-cli-in-a-secure-docker-sandbox)

* **GitHub Repository:** [https://github.com/GordonBeeming/copilot_here](https://github.com/GordonBeeming/copilot_here)

## Conclusion

Security and convenience don't have to be mutually exclusive. By running Copilot CLI in a Docker sandbox, you get powerful AI assistance with strict boundaries that protect your broader system. This setup works identically across Linux, macOS, and Windows, allowing you to embrace features like `--allow-all-tools` with confidence, knowing the worst-case scenario is limited to your current project.
