---
type: rule
tips: ""
title: Do you attribute AI-assisted commits with co-authors?
seoDescription: Learn how to properly attribute commits when using GitHub
  Copilot CLI or other AI coding assistants. This standard ensures proper credit
  and transparency in AI-human collaboration.
uri: attribute-ai-assisted-commits-with-co-authors
authors:
  - title: ""
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
- 47 files changed, 3,421 insertions(+), 892 deletions(-)
- Impossible to review effectively
- Can't revert specific changes
- Lost context about which changes relate to which sub-tasks
- No connection to [task documentation](keep-task-summaries-from-ai-assisted-development) created during the session
:::
::: bad
Bad Example - One giant commit makes it hard to understand the work progression and loses the relationship to task docs
:::

## The Solution: Co-Author Attribution + Frequent Commits

Git supports multiple authors via the `Co-authored-by` trailer in commit messages. Combined with frequent, small commits, this creates a clear and reviewable history.

### The Benefits of This Approach

**Proper Attribution:**
- Both the AI implementer and the human verifier receive credit
- Transparent collaboration history

**Small, Vertical Commits:**
- Each commit represents one logical change
- Easy to review and understand
- Can revert specific changes without affecting others
- Clear progression of work

**Connection to Task Documentation:**
- Commits align with [task documentation](keep-task-summaries-from-ai-assisted-development) created during the session
- Easy to cross-reference commit history with task docs
- Provides complete context for future developers

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
- Focused commits instead of 1 giant commit
- Each commit is reviewable independently
- Clear relationship to task documentation
- Easy to understand the implementation sequence
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

```bash
git commit -m "Type: Brief description

Co-authored-by: Your Name <your.email@example.com>"
```

::: good
Good Example - Clear attribution shows who verified the AI's work
:::

### Co-Author Example

::: greybox
```bash
git commit -m "feat: Add recipe search functionality

Co-authored-by: Gordon Beeming <me@gordonbeeming.com>"
```

**Git History Shows:**
- **Author:** GitHub Copilot (or AI Assistant)
- **Co-author:** Gordon Beeming

**Result:** Both the AI implementer and human verifier are visible in GitHub's UI and git log
:::
::: good
Good Example - You get proper credit for verifying and approving the AI's work
:::

### Multiple Co-Authors Example

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

### ✅ DO Add Yourself as Co-Author When:

- **AI implements features**: You review and approve code generated by AI
- **AI fixes bugs**: You verify the fix works correctly
- **AI refactors code**: You ensure the refactoring is appropriate
- **AI writes tests**: You validate test coverage and correctness
- **Pair programming with AI**: You actively collaborate with AI on the solution

### ❌ DON'T Add Co-Authors For:

- **Automated updates**: Dependency bumps, bot-generated changes
- **Manual work**: Code you write yourself without AI assistance

## Implementation for GitHub Copilot CLI

### Configure Copilot Instructions

Add this section to your `.github/copilot-instructions.md`:

```markdown
## Git Commit Guidelines

### Commit Frequently
Commit changes incrementally as you complete logical units of work.

**Why commit frequently:**
- ✅ Creates small, focused commits that are easy to review and understand
- ✅ Enables vertical slicing - each commit represents a single logical change
- ✅ Avoids one giant commit at the end of a session with dozens of unrelated changes
- ✅ Makes it easier to track progress and document work in [task docs created](task-docs-created)
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

**When to add yourself as co-author:**
- ✅ When AI implements a feature you requested
- ✅ When AI fixes a bug and you verify the fix
- ✅ When AI refactors code and you approve the changes
- ✅ When collaborating with AI on any code changes
- ❌ Not needed for automated updates (dependency bumps, etc.)
```

### Automatic Attribution Script

Create a helper script to automatically add yourself as co-author:

```bash
#!/bin/bash
# save as: .github/scripts/commit-with-coauthor.sh

# Get current git user details
COAUTHOR_NAME=$(git config user.name)
COAUTHOR_EMAIL=$(git config user.email)

# Commit with co-author
git commit -m "$1

Co-authored-by: $COAUTHOR_NAME <$COAUTHOR_EMAIL>"
```

**Usage:**
```bash
chmod +x .github/scripts/commit-with-coauthor.sh
./.github/scripts/commit-with-coauthor.sh "feat: Add authentication module"
```

## Benefits

This practice provides:

✅ **Proper Credit:** Both AI and human contributors receive recognition  
✅ **Transparency:** Clear record of who verified the AI's work  
✅ **Collaboration History:** Easy to trace AI-assisted changes  
✅ **Small, Reviewable Commits:** Focused changes instead of giant end-of-session commits  
✅ **Vertical Slicing:** Each commit represents one logical unit of work  
✅ **Task Documentation Alignment:** Commits correspond to [task docs created](task-docs-created) during the session  
✅ **Team Visibility:** Managers can see AI collaboration patterns  
✅ **GitHub Insights:** Contribution graphs reflect collaborative work  
✅ **Future Context:** Helps understand how changes were created  
✅ **Easy Reverting:** Can undo specific changes without affecting other work

### GitHub UI Benefits

When you use co-authors, GitHub automatically:

- Shows all co-authors on the commit in the UI
- Counts the commit toward each co-author's contributions
- Links the commit to all co-authors' profiles
- Includes it in contribution graphs for all co-authors

::: greybox
**GitHub Commit View:**

```
feat: Add authentication module

Author: GitHub Copilot
Co-authored-by: Gordon Beeming <gordon@example.com>
```

**Shows:**
- Gordon's avatar appears on the commit
- Commit counts toward Gordon's contributions
- Links to Gordon's profile from the commit
:::
::: good
Good Example - GitHub recognizes and displays all contributors
:::

## Real-World Scenarios

### Scenario 1: AI Implements Feature

::: greybox
**You ask AI:**
"Add dark mode support to the dashboard"

**Your commit:**
```bash
git commit -m "feat: Implement dark mode toggle

Co-authored-by: Gordon Beeming <gordon@example.com>"
```
:::
::: good
Good Example - You get credit for directing and verifying the AI's work
:::

### Scenario 2: AI Fixes Bug

::: greybox
**You identify:**
"The validation logic has a bug when email field is empty"

**Your commit:**
```bash
git commit -m "fix: Handle empty email validation correctly

Co-authored-by: Gordon Beeming <gordon@example.com>"
```
:::
::: good
Good Example - You are credited for finding and verifying the fix
:::

### Scenario 3: Copilot CLI Implementation

::: greybox
**Command:**
```bash
copilot_here "add TypeScript types for all API responses"
```

**Copilot commits:**
```bash
git commit -m "feat: Add TypeScript types for API responses

Co-authored-by: Gordon Beeming <gordon@example.com>"
```

**Result:** Gordon is credited for the type safety improvement alongside the AI
:::
::: good
Good Example - The person who directed Copilot gets proper attribution
:::

## Advanced: Git Hooks for Automatic Attribution

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

## Conclusion

Proper commit attribution is essential when AI assists with code changes. By consistently adding yourself as co-author to commits, you:

- Ensure fair credit for all contributors (both AI and human)
- Maintain transparent collaboration history
- Provide context for future developers
- Support accurate contribution metrics

This practice transforms AI from a black box into a transparent collaborator, showing who verified the work and ensuring accountability.

Remember: **If AI wrote it and you approved it, you both deserve credit for it.**
