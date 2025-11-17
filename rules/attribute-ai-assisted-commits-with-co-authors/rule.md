---
type: rule
tips: ""
title: Do you attribute AI-assisted commits with co-authors?
seoDescription: Learn how to properly attribute commits when using GitHub
  Copilot CLI or other AI coding assistants. This standard ensures proper credit
  and transparency in AI-human collaboration.
uri: attribute-ai-assisted-commits-with-co-authors
authors:
  - title: Gordon Beeming
    url: https://ssw.com.au/people/gordon-beeming
  - title: Lewis Toh
    url: https://ssw.com.au/people/lewis-toh
related:
  - keep-task-summaries-from-ai-assisted-development
created: 2025-10-17T09:52:00.000Z
guid: 244a09ee-ca89-4998-9ebd-a432f7eb5d51
---
When AI assistants make code changes on your behalf, proper attribution is essential. Adding yourself as a co-author when AI implements changes ensures transparency about who verified the work and maintains accurate contribution history.

This practice is especially important in team environments where AI assists with implementing features, fixing bugs, or making changes.

<!--endintro-->

### The Problem with Missing Attribution

When AI makes changes without proper attribution, we don't know who checked the work of the AI:

::: greybox
**Git History:**

```
feat: Add authentication module
Author: GitHub Copilot <noreply@github.com>
```

:::
::: bad
Bad Example - No indication of who checked the AI's work
:::

### The Problem with Giant End-of-Session Commits

When you don't commit frequently during a Copilot session:

::: greybox
**Single massive commit at the end:**

```
feat: Complete authentication system

- Add login page
- Add registration page
- Add password reset
- Add email verification
- Add OAuth providers
- Add user profile page
- Update database schema
- Add API endpoints
- Add tests
- Update documentation
- Fix styling issues
- Refactor validation logic
```

**Issues:**
* 47 files changed, 3,421 insertions(+), 892 deletions(-)
* Impossible to review effectively
* Can't revert specific changes
* Lost context about which changes relate to which sub-tasks
* No connection to [task documentation](keep-task-summaries-from-ai-assisted-development) created during the session
:::
::: bad
Bad Example - One giant commit makes it hard to understand the work progression and loses the relationship to task docs
:::

## The Solution: Co-Author Attribution + Frequent Commits

Git supports multiple authors via the `Co-authored-by` trailer in commit messages. Combined with frequent, small commits, this creates a clear and reviewable history.

### The Benefits of This Approach

**Proper Attribution:**
* Both the AI implementer and the human verifier receive credit
* Transparent collaboration history

**Small, Vertical Commits:**
* Each commit represents one logical change
* Easy to review and understand
* Can revert specific changes without affecting others
* Clear progression of work

**Connection to Task Documentation:**
* Commits align with [task documentation](keep-task-summaries-from-ai-assisted-development) created during the session
* Easy to cross-reference commit history with task docs
* Provides complete context for future developers

::: greybox
**Better approach - Multiple focused commits:**

```
feat: Add login page with form validation

Co-authored-by: Gordon Beeming <gordon@example.com>
---
feat: Add user registration with email verification

Co-authored-by: Gordon Beeming <gordon@example.com>
---
feat: Add OAuth provider integration (Google, GitHub)

Co-authored-by: Gordon Beeming <gordon@example.com>
---
docs: Document authentication implementation

Updates task doc with OAuth setup details

Co-authored-by: Gordon Beeming <gordon@example.com>
```

**Result:**
* Focused commits instead of 1 giant commit
* Each commit is reviewable independently
* Clear relationship to task documentation
* Easy to understand the implementation sequence
:::
::: good
Good Example - Small, focused commits with proper attribution and documentation
:::

### How to Identify Yourself

Check these sources to determine your details for co-author attribution:

1. **Git config**: `git config user.name` and `git config user.email`
2. **GitHub user**: If in GitHub Codespaces, use the logged-in user
3. **Environment variables**: Check for user information in your development environment

### Co-Author Commit Format

The standard Git co-author format:

::: greybox

```bash
git commit -m "feat: Add recipe search functionality

Co-authored-by: Gordon Beeming <me@gordonbeeming.com>"
```

**Git History Shows:**
* **Author:** GitHub Copilot (or AI Assistant)
* **Co-author:** Gordon Beeming

**Result:** Both the AI implementer and human verifier are visible in GitHub's UI and git log
:::
::: good
Good Example - You get proper credit for verifying and approving the AI's work
:::

### Multiple Co-Authors

For collaborative work where multiple people reviewed the AI's work:

```bash
git commit -m "feat: Implement user authentication system

Co-authored-by: Gordon Beeming <gordon@example.com>
Co-authored-by: Daniel Mackay <daniel@example.com>"
```

::: good
Good Example - All reviewers are properly credited
:::

## When to Add Yourself as Co-Author

### ✅ DO Add Yourself as Co-Author When

* **AI implements features**: You review and approve code generated by AI
* **AI fixes bugs**: You verify the fix works correctly
* **AI refactors code**: You ensure the refactoring is appropriate
* **AI writes tests**: You validate test coverage and correctness
* **Pair programming with AI**: You actively collaborate with AI on the solution

### ❌ DON'T Add Co-Authors For

* **Automated updates**: Dependency bumps, bot-generated changes
* **Routine maintenance**: Scheduled tasks with no specific requester

## Implementation for your AI Assistant

### Option 1: Configure AI Assistant Instructions (⭐ Recommended)

Add the following section to your AI assistant configuration (e.g., `.github/copilot-instructions.md`, `.cursorrules`, `.ai/instructions.md`, or your preferred location):

```markdown
## Git Commit Guidelines

### Commit Frequently
Commit changes incrementally as you complete logical units of work.

**Why commit frequently:**
- ✅ Creates small, focused commits that are easy to review and understand
- ✅ Enables vertical slicing - each commit represents a single logical change
- ✅ Avoids one giant commit at the end of a session with dozens of unrelated changes
- ✅ Makes it easier to track progress and document work in task docs created
- ✅ Allows reverting specific changes without losing other work
- ✅ Provides clear checkpoints during development

**When to commit:**
- ✅ After adding a new feature or component
- ✅ After fixing a bug
- ✅ After updating documentation (including task documentation)
- ✅ After refactoring code
- ✅ Before making major changes (safety checkpoint)
- ✅ After successful test runs

**Exception:** Do not commit when working on the `gitbutler/workspace` branch - GitButler manages commits on this branch.

### Co-Author Attribution for AI-Assisted Work

**ALWAYS add yourself as a co-author on commits** when AI implements code to ensure proper attribution.

**How to identify yourself:**
1. **Git config**: Check `git config user.name` and `git config user.email`
2. **GitHub user**: If running in GitHub Codespaces, use the logged-in GitHub user
3. **Environment**: Check environment variables for user information

**Co-Author Format:**
```bash
git commit -m "Type: Brief description

Co-authored-by: Your Name <your.email@example.com>"
```

**Example:**

```bash
git commit -m "feat: Add recipe search functionality

Co-authored-by: Gordon Beeming <me@gordonbeeming.com>"
```

### Option 2: Git Hooks for Automatic Attribution

Create a `prepare-commit-msg` hook to automatically add yourself as co-author:

```bash
#!/bin/bash
# .git/hooks/prepare-commit-msg

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2

# Only add co-author for regular commits (not merges, rebases, etc.)
if [ -z "$COMMIT_SOURCE" ]; then
  COAUTHOR_NAME=$(git config user.name)
  COAUTHOR_EMAIL=$(git config user.email)
  
  # Add co-author if not already present
  if ! grep -q "Co-authored-by: $COAUTHOR_NAME" "$COMMIT_MSG_FILE"; then
    echo "" >> "$COMMIT_MSG_FILE"
    echo "Co-authored-by: $COAUTHOR_NAME <$COAUTHOR_EMAIL>" >> "$COMMIT_MSG_FILE"
  fi
fi
```

::: info
**Note:** Git hooks are local and not committed to the repository. Share this with your team via documentation.
:::

## Benefits

✅ **Proper Credit:** Both AI and human contributors receive recognition  
✅ **Transparency:** Clear record of who verified the AI's work  
✅ **Collaboration History:** Easy to trace AI-assisted changes  
✅ **Small, Reviewable Commits:** Focused changes instead of giant end-of-session commits  
✅ **Vertical Slicing:** Each commit represents one logical unit of work  
✅ **Task Documentation Alignment:** Commits correspond to task docs created during the session  
✅ **Team Visibility:** Team can see AI collaboration patterns  
✅ **Future Context:** Helps understand how changes were created  
✅ **Easy Reverting:** Can undo specific changes without affecting other work

### GitHub UI Benefits

::: greybox
**GitHub Commit View:**

```
feat: Add authentication module

Author: GitHub Copilot
Co-authored-by: Gordon Beeming <gordon@example.com>
```
* Gordon's avatar appears on the commit
* Commit counts toward Gordon's contributions
* Links to Gordon's profile from the commit
:::
::: good
Good Example - GitHub recognizes and displays all contributors
:::

## Conclusion

Proper commit attribution is essential when AI assists with code changes. By consistently adding yourself as co-author to commits, you:

* Ensure fair credit for all contributors (both AI and human)
* Maintain transparent collaboration history
* Provide context for future developers
