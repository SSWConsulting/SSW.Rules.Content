---
seoDescription: Reset your local Git changes and revert to the last commit with "git reset --hard HEAD".
type: rule
archivedreason:
title: Do you know these important git commands?
guid: 15698c3c-cf80-4c5c-9030-022aa47933d1
uri: important-git-commands
created: 2014-05-22T20:02:08.0000000Z
authors:
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []
---

## Git Command Line
The bread and butter of git. This is the traditional and most powerful way to use Git. 

- Emphasizes power, control, and completeness
- Mentions the learning curve but highlights the benefits
- Perfect for developers who want full functionality

### 1. git init
Creates a new Git repository in the current folder.

```
git init
```

This sets up Git tracking for your project. It creates a .git directory containing metadata about your repo, including commit history, branches, and remote settings.

### 2. git clone
Creates a local copy of a remote repository.

```
git clone #repository-url
```

Example:

```
git clone https://github.com/test/hello-world.git
```

This copies all the files, history, and branches from the remote repo.

### 3. git status
Shows the current state of your working directory and staging area.

```
git status
```

You’ll see:

- Files that have been modified
- Files that are staged
- Untracked files

Here are some most frequesntly used `git status` commands:

| Command | Description |
|---------|-------------|
| `git status` | Shows the basic status of working directory and staging area |
| `git status -s` | Shows status in short format (compact view) |
| `git status -b` | Shows branch and tracking info in short format |
| `git status --porcelain` | Machine-readable output format |

### 4. git add
Adds files to the staging area so they’re ready to be committed.

```
git add {{file}}
git add .
```
`git add {{file}}` adds a specific file.

`git add .` adds all changes in the current directory and subdirectories.

Tip: Use git status before running this to see which files you’re staging.

### 5. git commit
Saves a snapshot of your staged changes with a message.

```
git commit -m “@feature auth added”
```

Each commit should describe why the changes were made—not just what was changed.

Use clear, concise messages that help teammates (and your future self) understand the history.

### 6. git diff
Shows differences between your working directory and the staging area or between commits.

| Command | Description | Use Case |
|---------|-------------|----------|
| `git diff` | Shows unstaged changes | Most common - see what you've changed |
| `git diff --staged` | Shows staged changes | Review changes before committing |
| `git diff HEAD` | Shows all changes since last commit | See everything that's changed |
| `git diff <filename>` | Shows changes in specific file | Focus on one file's changes |
| `git diff --stat` | Shows change summary | Quick overview of what files changed |

This helps you preview what’s going to be committed or what changed between commits.

### 7. git log
Displays the commit history.

```
git log
```

You’ll see:

- Commit hashes (SHA)
- Author names
- Dates
- Commit messages

You can customize the output of git log with many options. Here are some of the most useful ones:

| Command / Option                | What it does                                                                 |
|---------------------------------|------------------------------------------------------------------------------|
| `git log`                       | Shows the full commit history (default format)                               |
| `git log --oneline`             | Shows each commit as a single line (short hash + message)                    |
| `git log --stat`                | Shows files changed and the number of insertions/deletions per commit        |
| `git log -p`                    | Shows the actual diff (patch) introduced in each commit                      |
| `git log --author="Name"`       | Shows commits by a specific author                                           |
| `git log --graph`               | Shows a text-based graph of the branch structure                             |
| `git log --decorate`            | Shows branch and tag names alongside commits                                 |
| `git log --pretty=oneline`      | Shows each commit on one line (more detailed than `--oneline`)               |
| `git log --abbrev-commit`       | Shows only a short SHA-1 for each commit                                     |

### 8. git reset
Resets your staging area or moves HEAD to a different commit.

| Command / Option                | What it does                                                                 |
|---------------------------------|------------------------------------------------------------------------------|
| `git reset`                     | By default, unstages files (moves from staging area back to working directory)|
| `git reset <commit>`            | Moves the current branch to the specified commit (default is `--mixed`)      |
| `git reset --soft <commit>`     | Moves HEAD to commit, keeps changes staged (in index)                        |
| `git reset --mixed <commit>`    | Moves HEAD to commit, unstages changes (default behavior)                    |
| `git reset --hard <commit>`     | Moves HEAD to commit, discards all changes in working directory and index     |
| `git reset HEAD <file>`         | Unstages a specific file (keeps changes in working directory)                |

### 9. git checkout
Switches branches or restores files.

Switch to a branch:

```
git checkout main
```

### 10. git branch
Lists, creates, or deletes branches.

List branches:

```
git branch
```

Create a new branch:

```
git branch @feature/login-form
```

Delete a branch:

```
git branch -d old-feature
```

### 11. git merge
Combines changes from one branch into another.

```
git checkout @feature/login-form
git merge main
```

This merges the main branch into the feature branch.

If there are conflicting changes in the same files, Git will prompt you to resolve them manually.

### 12. git pull
Downloads changes from a remote repository and merges them into your local branch.

```
git pull origin main
```

This is equivalent to:

```
git fetch
git merge
```

Use `git pull --rebase` to avoid unnecessary merge commits.

### 13. git push
Uploads your local commits to a remote repository.

| Command / Option                      | What it does                                                        |
|---------------------------------------|---------------------------------------------------------------------|
| `git push`                            | Pushes current branch to its tracked remote branch                  |
| `git push origin <branch>`            | Pushes the specified local branch to the remote named "origin"      |
| `git push -u origin <branch>`         | Pushes branch and sets upstream (tracks remote branch)              |
| `git push --force` or `git push -f`   | Forces push, overwriting remote branch history                      |
| `git push --all`                      | Pushes all local branches to the remote                             |
| `git push --tags`                     | Pushes all local tags to the remote                                 |
| `git push origin --delete <branch>`   | Deletes a branch on the remote repository                           |

Use this to share your work with others.

### 14. git stash
Temporarily saves changes that you don’t want to commit yet.

```
git stash
```

This clears your working directory so you can switch branches cleanly.

Restore stashed changes:

```
git stash pop
```

View all stashes:

```
git stash list
```

### 15. git remote
Manages remote repositories.

| Command / Option                  | What it does                                              |
|-----------------------------------|-----------------------------------------------------------|
| `git remote`                      | Lists the short names of all configured remotes           |
| `git remote -v`                   | Lists remotes and their URLs (fetch and push)             |
| `git remote add <name> <url>`     | Adds a new remote repository                              |
| `git remote remove <name>`        | Removes a remote repository                               |
| `git remote rename <old> <new>`   | Renames a remote repository                               |
| `git remote show <name>`          | Shows detailed info about a specific remote               |
| `git remote set-url <name> <url>` | Changes the URL of a remote repository                    |

## Git Clients
Alternatively, developers could choose a user-friendly visual interface that makes version control more accessible. It's perfect for developers who prefer visual interfaces and handles most day-to-day Git tasks without needing to memorize commands.

### 1. [GitHub Desktop](https://github.com/apps/desktop)
GitHub Desktop is a free, streamlined Git client that great integration with GitHub repositories.

- ✅ Completely free and open source
- ✅ Dead simple interface perfect for Git beginners
- ✅ Excellent GitHub integration with pull requests and issues
- ❌ Limited advanced Git features
- ❌ No built-in merge conflict resolution tools
- ❌ Primarily designed for GitHub (limited with other Git hosts)

`youtube: https://www.youtube.com/embed/qUYkRWGWntE?si=rtdB4GXHMsH9CaG8`
**Video: GitHub Desktop is for everyone - Universe 2022 (12 mins)**

### 2. [GitKraken](https://www.gitkraken.com/)
GitKraken is a premium Git GUI that offers a comprehensive visual interface with advanced features and beautiful design.

- ✅ Stunning visual repository graph and history
- ✅ Excellent merge conflict resolution tools
- ✅ Supports multiple Git hosting services (GitHub, GitLab, Bitbucket, etc.)
- ❌ Requires paid subscription for private repositories and teams
- ❌ Can be overwhelming for beginners
- ❌ Resource-heavy application (uses more memory)
