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

### The Problem with Unrestricted Access

When running Copilot CLI directly on your host machine:

::: greybox
**Copilot has access to:**
- Your entire file system
- Your SSH keys in `~/.ssh/`
- All your repositories
- Your environment variables and secrets
- System-wide configurations
:::
::: bad
Bad Example - Copilot running with full system access creates unnecessary risk - a single mistake like `rm -rf ~` could be catastrophic
:::

## The Solution: Docker-Based Isolation

By running Copilot CLI inside a Docker container, you create a secure sandbox where:

- Copilot can only see your **current project directory**
- Your home directory, SSH keys, and other projects are completely inaccessible
- You can safely use `--allow-all-tools` with confidence (automatic approval)
- The worst-case scenario is limited to the current project

### Understanding the Safety Net

If Copilot runs a dangerous command like `rm -rf .`:

**❌ Without Docker:**
- Deletes everything in current directory and subdirectories, depending on the folder you ran copilot in, could be catastrophic
- No way to easily recover lost files and folders


**✅ With Docker:**
- Only deletes files in the mounted /work directory which is mapped to your current project folder
- Your other projects and system files are safe
- If setup with git, it is easily recoverable

::: info
**Note:** The container shares your host's network, so it can access local resources and services. This is intentional for development workflows but means it's not a fully firewalled environment.
:::

## Implementation: The copilot_here Setup

The complete solution is available at [https://github.com/GordonBeeming/copilot_here](https://github.com/GordonBeeming/copilot_here).

:::info
**Note:** The functions below are the current recommended setup (MacOS/Linux only). For the latest version, always check the GitHub repository.
:::

### Option 1: The Safe Version (Default)

This version prompts for confirmation before executing commands - perfect for daily use.

**Add to your shell profile** (`~/.zshrc`, `~/.bashrc`, etc.):

```bash
copilot_here() {
  # --- SECURITY CHECK ---
  # 1. Ensure the 'copilot' scope is present using a robust grep check.
  if ! gh auth status 2>/dev/null | grep "Token scopes:" | grep -q "'copilot'"; then
    echo "❌ Error: Your gh token is missing the required 'copilot' scope."
    echo "Please run 'gh auth refresh -h github.com -s copilot' to add it."
    return 1
  fi

  # 2. Warn if the token has highly privileged scopes.
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

  # Define the image name for easy reference
  local image_name="ghcr.io/gordonbeeming/copilot_here:latest"

  # Pull the latest version of the image to stay up-to-date.
  echo "Checking for the latest version of copilot_here..."
  docker pull "$image_name" > /dev/null 2>&1

  # Define path for our persistent copilot config on the host machine.
  local copilot_config_path="$HOME/.config/copilot-cli-docker"
  mkdir -p "$copilot_config_path"

  # Use the 'gh' CLI itself to reliably get the current auth token.
  local token=$(gh auth token 2>/dev/null)
  if [ -z "$token" ]; then
    echo "⚠️  Could not retrieve token using 'gh auth token'. Please ensure you are logged in."
  fi

  # Base Docker command arguments
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
    # No arguments provided, start interactive mode with the banner.
    docker run "${docker_args[@]}" copilot --banner
  else
    # Arguments provided, run in non-interactive (but safe) mode.
    docker run "${docker_args[@]}" copilot -p "$*"
  fi
}
```

**Usage:**
```bash
$ copilot_here "clean and reinstall dependencies"
> Copilot suggests: rm -rf node_modules package-lock.json && npm install
Execute this command? [y/N]: y
✅ Executed safely in /work directory only
```

::: good
Good Example - Safe mode will ask for confirmation before executing commands
:::

### Option 2: The Auto-Approve Version (Power Users)

For trusted projects where you value speed, add the YOLO version:

```bash
copilot_yolo() {
  # --- SECURITY CHECK ---
  # 1. Ensure the 'copilot' scope is present using a robust grep check.
  if ! gh auth status 2>/dev/null | grep "Token scopes:" | grep -q "'copilot'"; then
    echo "❌ Error: Your gh token is missing the required 'copilot' scope."
    echo "Please run 'gh auth refresh -h github.com -s copilot' to add it."
    return 1
  fi

  # 2. Warn if the token has highly privileged scopes.
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

  # Define the image name for easy reference
  local image_name="ghcr.io/gordonbeeming/copilot_here:latest"

  # Pull the latest version of the image to stay up-to-date.
  echo "Checking for the latest version of copilot_here..."
  docker pull "$image_name" > /dev/null 2>&1

  # Define path for our persistent copilot config on the host machine.
  local copilot_config_path="$HOME/.config/copilot-cli-docker"
  mkdir -p "$copilot_config_path"

  # Use the 'gh' CLI itself to reliably get the current auth token.
  local token=$(gh auth token 2>/dev/null)
  if [ -z "$token" ]; then
    echo "⚠️  Could not retrieve token using 'gh auth token'. Please ensure you are logged in."
  fi

  # Base Docker command arguments
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
    # No arguments provided, start interactive mode with banner and auto-approval.
    docker run "${docker_args[@]}" copilot --banner --allow-all-tools
  else
    # Arguments provided, run in non-interactive mode with auto-approval.
    docker run "${docker_args[@]}" copilot -p "$*" --allow-all-tools
  fi
}
```

**Usage:**
```bash
$ copilot_yolo "clean and reinstall dependencies"
> Copilot suggests: rm -rf node_modules package-lock.json && npm install
✅ Auto-executed in /work directory only
```
::: good
Good Example - Yolo mode will executing commands without asking for approval
:::

::: info
**Tip:** Install both functions so you can choose based on the situation. Use `copilot_here` by default and `copilot_yolo` only in trusted projects.
:::

## How It Works

### Security Features

1. **File System Isolation**
   - Only mounts your current project directory to `/work`
   - Your home directory, SSH keys, and other projects are completely hidden
   - Configuration stored in isolated `~/.config/copilot-cli-docker`

2. **Token Scope Validation**
   - Checks that your GitHub token has the required `copilot` scope
   - Warns if your token has dangerous elevated permissions
   - Requires explicit confirmation for high-privilege tokens

3. **User Permission Mapping**
   - Uses `PUID` and `PGID` to match your user ID inside the container
   - Files created by Copilot have correct ownership on your host

4. **Network Access**
   - Container shares host network for development workflows
   - Can access local services and APIs (by design)
   - Not a fully firewalled environment

## Benefits

This approach provides:

✅ **Security:** Strict isolation limits damage potential\
✅ **Confidence:** Use powerful features like `--allow-all-tools` safely\
✅ **Portability:** Same setup works across all machines\
✅ **Auto-authentication:** Seamlessly uses your existing `gh` login\
✅ **Cognitive ease:** Feel safe letting AI execute commands\
✅ **Flexibility:** Choose safe or YOLO mode based on context

## Learn More

For detailed implementation, troubleshooting, and the complete source code:

📖 **Blog Post:** [Taming the AI: My Paranoid Guide to Running Copilot CLI in a Secure Docker Sandbox](https://www.gordonbeeming.xyz/blog/taming-the-ai-my-paranoid-guide-to-running-copilot-cli-in-a-secure-docker-sandbox)

🔧 **GitHub Repository:** [https://github.com/GordonBeeming/copilot_here](https://github.com/GordonBeeming/copilot_here)

## Conclusion

Security and convenience don't have to be mutually exclusive. By running Copilot CLI in a Docker sandbox, you get powerful AI assistance with strict boundaries that protect your broader system. This setup allows you to embrace features like `--allow-all-tools` with confidence, knowing the worst-case scenario is limited to your current project.
