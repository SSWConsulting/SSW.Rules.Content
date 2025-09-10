---
type: rule
title: Do you leave explanatory notes for non-standard code?
seoDescription: Learn how to leave clear, permanent comments for non-standard code. This standard ensures future developers understand the reasoning behind specific implementations, preventing accidental bugs.
uri: leave-explanatory-notes-for-non-standard-code
authors:
  - title: Gordon Beeming
    url: https://ssw.com.au/people/gordon-beeming
  - title: Daniel Mackay
    url: https://ssw.com.au/people/daniel-mackay
related:
  - code-commenting
created: 2025-09-09T00:00:00.000Z
archivedreason: null
guid: B60B8EC3-A44F-43C9-94F0-13E8ABCB9533
---

Sometimes, you need to write code that deviates from the standard pattern. It might be a workaround for a library bug, an optimization for a critical performance path, or a temporary solution pending a larger refactor. Without context, a future developer, or even you, months later, might see this "weird" code and refactor it back to the standard pattern, unknowingly reintroducing a bug.

To prevent this, it's crucial to leave a clear, permanent note directly in the code. This ensures the "why" behind the decision is never lost.

<!--endintro-->

### The Problem with Temporary Comments

Developer comments are often temporary. We use them as personal reminders to fix something before a pull request is merged. These are often unstructured and can be confusing if left in the codebase permanently.

::: greybox

```csharp
// GB: We need to drop database each run in DEBUG mode for local testing
var db = sqlServer
    .AddDatabase("clean-architecture")
    .WithDropDatabaseCommand();
```

:::
::: bad
Bad Example - This format is ambiguous. Is it a permanent note or a temporary reminder for the author to fix later?
:::

### The Problem with External Documentation

Another common approach is to document these decisions in a wiki, like Confluence. While great for detailed documentation, it has a major flaw.

::: greybox
**Wiki Page: "Local Development & Testing Setup"**

...To ensure idempotent and reliable local test runs, the database for the 'clean-architecture' project must be dropped and recreated on each execution when running in `DEBUG` mode. This prevents data contamination between test sessions...
:::
::: bad
Bad Example - Documentation is disconnected from the code. A developer won't see this unless they know to look for it, making it easy to miss.
:::

## The Solution: A Standardized NOTE Format

To solve this, use a standardized, prefixed format for these permanent notes. This makes them easy to identify, read, and search for across the entire codebase.

The format is:

**`// NOTE: [{{ DATE }}] {{ INITIALS }} - {{ REASON }}`**  
**`// {{ OPTIONAL: see URL }}`**

This approach provides the best of both worlds: the explanation is right next to the code, but it can also link out to more detailed documentation if needed.

::: greybox

```csharp
// NOTE: [10 Sep 2025] GB - We need to drop database each run in DEBUG mode for local testing
// see [https://github.com/SSWConsulting/SSW.CleanArchitecture/issues/421](https://github.com/SSWConsulting/SSW.CleanArchitecture/issues/421)
var db = sqlServer
    .AddDatabase("clean-architecture")
    .WithDropDatabaseCommand();
```

:::
::: good
Good Example - The `NOTE:` prefix makes the intent clear. The comment is permanent, explains the deviation, and provides a link for more context.
:::

This standardized format ensures:

✅ **Clarity:** It's immediately obvious that this is a permanent and important note.  
✅ **Discoverability:** The reason for the non-standard code is impossible to miss.  
✅ **Consistency:** The format is easy to recognize and search for codebase-wide.  
✅ **Traceability:** It provides a clear link between the code and the business/technical requirement in the work item or documentation.  
