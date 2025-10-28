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
Bad Example - Copilot running with full system access creates unnecessary risk - a single mistake like `rm -rf ~` could be catastrophic
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
* Only deletes files in the mounted /work directory which is mapped to your current project folder
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
**Note:** The functions below provide cross-platform support for Linux/macOS and Windows. For the latest version, always check the GitHub repository.
:::

#### Option 1: Safe Mode (Recommended)

This mode asks for confirmation before executing any commands, giving you full control.

**For Linux/macOS (Bash/Zsh):**

Add the following function to your shell profile (e.g., `~/.zshrc`, `~/.bashrc`):

```bash
copilot_here() {
  # --- SECURITY CHECK ---
  if ! gh auth status 2>/dev/null | grep "Token scopes:" | grep -q "'copilot'"; then
    echo "❌ Error: Your gh token is missing the required 'copilot' scope."
    echo "Please run 'gh auth refresh -h github.com -s copilot' to add it."
    return 1
  fi

  if gh auth status 2>/dev/null | grep "Token scopes:" | grep -q -E "'(admin:|manage_|write:public_key|delete_repo|(write|delete)_packages)'"; then
    echo "⚠️  Warning: Your GitHub token has highly privileged scopes (e.g., admin:org, admin:enterprise)."
    printf "Are you sure you want to proceed with this token? [y/N]: "
    read confirmation
    local lower_confirmation
    lower_confirmation=$(echo "$confirmation" | tr '[:upper:]' '[:lower:]')
    if [[ "$lower_confirmation" != "y" && "$lower_confirmation" != "yes" ]]; then
      echo "Operation cancelled by user."
      return 1
    fi
  fi
  # --- END SECURITY CHECK ---

  local image_name="ghcr.io/gordonbeeming/copilot_here:latest"

  printf "Checking for the latest version of copilot_here... "
  (docker pull "$image_name" > /dev/null 2>&1) &
  local pull_pid=$!
  local spin='|/-\'
  
  local i=0
  while ps -p $pull_pid > /dev/null; do
    i=$(( (i+1) % 4 ))
    printf "%s\b" "${spin:$i:1}"
    sleep 0.1
  done

  wait $pull_pid
  local pull_status=$?
  
  if [ $pull_status -eq 0 ]; then
    echo "✅"
  else
    echo "❌"
    echo "Error: Failed to pull the Docker image. Please check your Docker setup and network."
    return 1
  fi

  local copilot_config_path="$HOME/.config/copilot-cli-docker"
  mkdir -p "$copilot_config_path"

  local token=$(gh auth token 2>/dev/null)
  if [ -z "$token" ]; then
    echo "⚠️  Could not retrieve token using 'gh auth token'. Please ensure you are logged in."
  fi

  local docker_args=(
    --rm -it
    -v "$(pwd)":/work
    -v "$copilot_config_path":/home/appuser/.copilot
    -e PUID=$(id -u)
    -e PGID=$(id -g)
    -e GITHUB_TOKEN="$token"
    "$image_name"
  )

  if [ $# -eq 0 ]; then
    docker run "${docker_args[@]}" copilot --banner
  else
    docker run "${docker_args[@]}" copilot -p "$*"
  fi
}
```

Then reload your shell (e.g., `source ~/.zshrc`).

**For Windows (PowerShell):**

Save the following as `copilot_here.ps1` in a location of your choice (e.g., `C:\Users\YourName\Documents\PowerShell\`):

```powershell
function Copilot-Here {
    [CmdletBinding()]
    param (
        [Parameter(ValueFromRemainingArguments=$true)]
        [string[]]$Prompt
    )

    # --- SECURITY CHECK ---
    Write-Host "Verifying GitHub CLI authentication..."
    $authStatus = gh auth status 2>$null
    if (-not ($authStatus | Select-String -Quiet "'copilot'")) {
        Write-Host "❌ Error: Your gh token is missing the required 'copilot' scope." -ForegroundColor Red
        Write-Host "Please run 'gh auth refresh -h github.com -s copilot' to add it."
        return
    }

    $privilegedScopesPattern = "'(admin:|manage_|write:public_key|delete_repo|(write|delete)_packages)'"
    if ($authStatus | Select-String -Quiet $privilegedScopesPattern) {
        Write-Host "⚠️  Warning: Your GitHub token has highly privileged scopes." -ForegroundColor Yellow
        $confirmation = Read-Host "Are you sure you want to proceed with this token? [y/N]"
        if ($confirmation.ToLower() -ne 'y' -and $confirmation.ToLower() -ne 'yes') {
            Write-Host "Operation cancelled by user."
            return
        }
    }
    Write-Host "✅ Security checks passed."
    # --- END SECURITY CHECK ---

    $imageName = "ghcr.io/gordonbeeming/copilot_here:latest"

    Write-Host -NoNewline "Checking for the latest version of copilot_here... "
    $pullJob = Start-Job -ScriptBlock { param($img) docker pull $img } -ArgumentList $imageName
    $spinner = '|', '/', '-', '\'
    $i = 0
    while ($pullJob.State -eq 'Running') {
        Write-Host -NoNewline "$($spinner[$i])`b"
        $i = ($i + 1) % 4
        Start-Sleep -Milliseconds 100
    }

    Wait-Job $pullJob | Out-Null
    $pullOutput = Receive-Job $pullJob
    
    if ($pullJob.State -eq 'Completed') {
        Write-Host "✅"
    } else {
        Write-Host "❌" -ForegroundColor Red
        Write-Host "Error: Failed to pull the Docker image." -ForegroundColor Red
        if (-not [string]::IsNullOrEmpty($pullOutput)) {
            Write-Host "Docker output:`n$pullOutput"
        }
        Remove-Job $pullJob
        return
    }
    Remove-Job $pullJob

    $copilotConfigPath = Join-Path $env:USERPROFILE ".config\copilot-cli-docker"
    if (-not (Test-Path $copilotConfigPath)) {
        New-Item -Path $copilotConfigPath -ItemType Directory -Force | Out-Null
    }

    $token = gh auth token 2>$null
    if ([string]::IsNullOrEmpty($token)) {
        Write-Host "⚠️  Could not retrieve token using 'gh auth token'." -ForegroundColor Yellow
    }

    $dockerBaseArgs = @(
        "--rm", "-it",
        "-v", "$((Get-Location).Path):/work",
        "-v", "$($copilotConfigPath):/home/appuser/.copilot",
        "-e", "GITHUB_TOKEN=$token",
        $imageName
    )

    $copilotCommand = @("copilot")
    if ($Prompt.Length -eq 0) {
        $copilotCommand += "--banner"
    } else {
        $copilotCommand += "-p", ($Prompt -join ' ')
    }

    $finalDockerArgs = $dockerBaseArgs + $copilotCommand
    docker run $finalDockerArgs
}

Set-Alias -Name copilot_here -Value Copilot-Here
```

Then add it to your PowerShell profile. Open your profile for editing:

```powershell
notepad $PROFILE
```

Add this line (adjust the path to where you saved the file):

```powershell
. C:\Users\YourName\Documents\PowerShell\copilot_here.ps1
```

Reload your PowerShell profile:

```powershell
. $PROFILE
```

**Usage:**

```bash
# Linux/macOS and Windows (same commands!)
copilot_here "clean and reinstall dependencies"
```

```
> Copilot suggests: rm -rf node_modules package-lock.json && npm install
Execute this command? [y/N]: y
✅ Executed safely in /work directory only
```

::: good
Good Example - Safe mode asks for confirmation before executing commands on both platforms
:::

#### Option 2: YOLO Mode (Auto-Approve)

This mode automatically approves all tool usage. Use with caution!

**For Linux/macOS (Bash/Zsh):**

Add this function alongside the safe version with a different name like `copilot_yolo`:

```bash
copilot_yolo() {
  # --- SECURITY CHECK ---
  if ! gh auth status 2>/dev/null | grep "Token scopes:" | grep -q "'copilot'"; then
    echo "❌ Error: Your gh token is missing the required 'copilot' scope."
    echo "Please run 'gh auth refresh -h github.com -s copilot' to add it."
    return 1
  fi

  if gh auth status 2>/dev/null | grep "Token scopes:" | grep -q -E "'(admin:|manage_|write:public_key|delete_repo|(write|delete)_packages)'"; then
    echo "⚠️  Warning: Your GitHub token has highly privileged scopes (e.g., admin:org, admin:enterprise)."
    printf "Are you sure you want to proceed with this token? [y/N]: "
    read confirmation
    local lower_confirmation
    lower_confirmation=$(echo "$confirmation" | tr '[:upper:]' '[:lower:]')
    if [[ "$lower_confirmation" != "y" && "$lower_confirmation" != "yes" ]]; then
      echo "Operation cancelled by user."
      return 1
    fi
  fi
  # --- END SECURITY CHECK ---

  local image_name="ghcr.io/gordonbeeming/copilot_here:latest"

  printf "Checking for the latest version of copilot_here... "
  (docker pull "$image_name" > /dev/null 2>&1) &
  local pull_pid=$!
  local spin='|/-\'
  
  local i=0
  while ps -p $pull_pid > /dev/null; do
    i=$(( (i+1) % 4 ))
    printf "%s\b" "${spin:$i:1}"
    sleep 0.1
  done

  wait $pull_pid
  local pull_status=$?
  
  if [ $pull_status -eq 0 ]; then
    echo "✅"
  else
    echo "❌"
    echo "Error: Failed to pull the Docker image. Please check your Docker setup and network."
    return 1
  fi

  local copilot_config_path="$HOME/.config/copilot-cli-docker"
  mkdir -p "$copilot_config_path"

  local token=$(gh auth token 2>/dev/null)
  if [ -z "$token" ]; then
    echo "⚠️  Could not retrieve token using 'gh auth token'. Please ensure you are logged in."
  fi

  local docker_args=(
    --rm -it
    -v "$(pwd)":/work
    -v "$copilot_config_path":/home/appuser/.copilot
    -e PUID=$(id -u)
    -e PGID=$(id -g)
    -e GITHUB_TOKEN="$token"
    "$image_name"
  )

  if [ $# -eq 0 ]; then
    docker run "${docker_args[@]}" copilot --banner --allow-all-tools
  else
    docker run "${docker_args[@]}" copilot -p "$*" --allow-all-tools
  fi
}
```

Then reload your shell (e.g., `source ~/.zshrc`).

**For Windows (PowerShell):**

Save the following as `copilot_yolo.ps1` (or add to your existing file):

```powershell
function Copilot-Yolo {
    [CmdletBinding()]
    param (
        [Parameter(ValueFromRemainingArguments=$true)]
        [string[]]$Prompt
    )

    # --- SECURITY CHECK ---
    Write-Host "Verifying GitHub CLI authentication..."
    $authStatus = gh auth status 2>$null
    if (-not ($authStatus | Select-String -Quiet "'copilot'")) {
        Write-Host "❌ Error: Your gh token is missing the required 'copilot' scope." -ForegroundColor Red
        Write-Host "Please run 'gh auth refresh -h github.com -s copilot' to add it."
        return
    }

    $privilegedScopesPattern = "'(admin:|manage_|write:public_key|delete_repo|(write|delete)_packages)'"
    if ($authStatus | Select-String -Quiet $privilegedScopesPattern) {
        Write-Host "⚠️  Warning: Your GitHub token has highly privileged scopes." -ForegroundColor Yellow
        $confirmation = Read-Host "Are you sure you want to proceed with this token? [y/N]"
        if ($confirmation.ToLower() -ne 'y' -and $confirmation.ToLower() -ne 'yes') {
            Write-Host "Operation cancelled by user."
            return
        }
    }
    Write-Host "✅ Security checks passed."
    # --- END SECURITY CHECK ---

    $imageName = "ghcr.io/gordonbeeming/copilot_here:latest"

    Write-Host -NoNewline "Checking for the latest version of copilot_here... "
    $pullJob = Start-Job -ScriptBlock { param($img) docker pull $img } -ArgumentList $imageName
    $spinner = '|', '/', '-', '\'
    $i = 0
    while ($pullJob.State -eq 'Running') {
        Write-Host -NoNewline "$($spinner[$i])`b"
        $i = ($i + 1) % 4
        Start-Sleep -Milliseconds 100
    }

    Wait-Job $pullJob | Out-Null
    $pullOutput = Receive-Job $pullJob
    
    if ($pullJob.State -eq 'Completed') {
        Write-Host "✅"
    } else {
        Write-Host "❌" -ForegroundColor Red
        Write-Host "Error: Failed to pull the Docker image." -ForegroundColor Red
        if (-not [string]::IsNullOrEmpty($pullOutput)) {
            Write-Host "Docker output:`n$pullOutput"
        }
        Remove-Job $pullJob
        return
    }
    Remove-Job $pullJob

    $copilotConfigPath = Join-Path $env:USERPROFILE ".config\copilot-cli-docker"
    if (-not (Test-Path $copilotConfigPath)) {
        New-Item -Path $copilotConfigPath -ItemType Directory -Force | Out-Null
    }

    $token = gh auth token 2>$null
    if ([string]::IsNullOrEmpty($token)) {
        Write-Host "⚠️  Could not retrieve token using 'gh auth token'." -ForegroundColor Yellow
    }

    $dockerBaseArgs = @(
        "--rm", "-it",
        "-v", "$((Get-Location).Path):/work",
        "-v", "$($copilotConfigPath):/home/appuser/.copilot",
        "-e", "GITHUB_TOKEN=$token",
        $imageName
    )

    $copilotCommand = @("copilot")
    if ($Prompt.Length -eq 0) {
        $copilotCommand += "--banner", "--allow-all-tools"
    } else {
        $copilotCommand += "-p", ($Prompt -join ' '), "--allow-all-tools"
    }

    $finalDockerArgs = $dockerBaseArgs + $copilotCommand
    docker run $finalDockerArgs
}

Set-Alias -Name copilot_yolo -Value Copilot-Yolo
```

Add it to your PowerShell profile (same process as Option 1) and reload.

**Usage:**

```bash
# Linux/macOS and Windows (same commands!)
copilot_yolo "clean and reinstall dependencies"
```

```
> Copilot suggests: rm -rf node_modules package-lock.json && npm install
✅ Auto-executed in /work directory only
```

::: good
Good Example - YOLO mode executes commands without asking for approval on both platforms
:::

::: info
**Tip:** Install both functions so you can choose based on the situation. Use `copilot_here` by default and `copilot_yolo` only in trusted projects.
:::

## How it works

### Security features

1. **File System Isolation**
   * Only mounts your current project directory to `/work`
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

## ✅ Benefits

This approach provides:

* **Security:** Strict isolation limits damage potential
* **Confidence:** Use powerful features like `--allow-all-tools` safely
* **Portability:** Same setup works across all machines
* **Cross-platform:** Works on Linux, macOS, and Windows
* **Auto-authentication:** Seamlessly uses your existing `gh` login
* **Cognitive ease:** Feel safe letting AI execute commands
* **Flexibility:** Choose safe or YOLO mode based on context

## Learn more

For detailed implementation, troubleshooting, and the complete source code:

* **Blog post 📖:** [Taming the AI: My Paranoid Guide to Running Copilot CLI in a Secure Docker Sandbox](https://gordonbeeming.com/blog/2025-10-03/taming-the-ai-my-paranoid-guide-to-running-copilot-cli-in-a-secure-docker-sandbox)

* **GitHub Repository:** [https://github.com/GordonBeeming/copilot_here](https://github.com/GordonBeeming/copilot_here)

## Conclusion

Security and convenience don't have to be mutually exclusive. By running Copilot CLI in a Docker sandbox, you get powerful AI assistance with strict boundaries that protect your broader system. This setup works identically across Linux, macOS, and Windows, allowing you to embrace features like `--allow-all-tools` with confidence, knowing the worst-case scenario is limited to your current project.
