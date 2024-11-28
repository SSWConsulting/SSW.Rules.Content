---
seoDescription: Naming things is hard, but also important. Using clear, meaningful names will make your code more readable and reduce cognitive load and risk for your development team.
type: rule
archivedreason:
title: Do you use clear, meaningful names?
uri: clear-meaningful-names
created: 2024-11-05T00:00:00.0000000Z
authors:
  - title: Matt Goldman
    url: https://ssw.com.au/people/matt-goldman
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
  - title: Daniel Mackay
    url: https://ssw.com.au/people/daniel-mackay
related:
  - nouns-for-class-names
  - verbs-for-method-names
  - avoid-generic-names
  - avoid-micro-jargon
  - consistent-words-for-concepts
  - when-to-use-technical-names
  - avoid-using-your-name-in-client-code
  - use-meaningful-modifiers
  - follow-naming-conventions-for-tests-and-test-projects
redirects:
  - do-you-follow-naming-conventions
guid: bfcbc0ef-d2f8-4e77-85d9-97ccb841eb19
---

`youtube: https://www.youtube.com/watch?v=t-t7P2BZnS4`

**Video: Hear from Jeoffrey Fischer about how to follow good naming conventions!**

In the early days of coding, we had to store more information in our heads than in our computers, leading to all sorts of creative abbreviations and clever shortcuts. But today, storage and readability are no longer limitations—our computers can handle verbose names better than our brains can handle cryptic codes. Clinging to those old practices can hurt your code’s readability and make life harder for your team.

<!--endintro-->

## Avoid mental encoding

It’s easy to invent clever codes to keep names short, like `cstmrMgr` to represent a "customer manager." But using shorthand requires other developers (or your future self) to mentally decode each abbreviation, slowing comprehension and increasing the risk of misinterpretation. Instead, use instantly recognizable names — there’s no need to not simply call it `CustomerManager` (although there are reasons to avoid "manager" as a name, see our rule [Do you avoid generic names like “manager,” “processor,” “data,” or “info”?](/avoid-generic-names)).

## Be verbose

Today, there’s no reason to squeeze names into character limits or cryptic codes. While you shouldn’t use full sentences for a class or method name (test cases might be an exception, see our rule [Do you follow naming conventions for tests and test projects?](/follow-naming-conventions-for-tests-and-test-projects)), full, meaningful words make your code far more readable and maintainable.

:::greybox
Imagine you’re creating a game and need a variable to store the player’s health. You might decide to use an integer called `NRG`. It’s short for "energy," which might seem clever — it’s easy to write, and you know what it means. But this has some problems:

* Other developers might misinterpret "energy" as something else, like power or ammo. Wouldn't "health" better represent the intended meaning here?
* If you add enemies with their own energy, what will you name their variable? (Spoiler: `nmeNrg`.)

:::
:::bad
Using clever abbreviations is unnecessary, and can easily cause confusion
:::

:::greybox
A better name for this variable is `PlayerHealth`. It clearly describes the specific kind of "energy" (health) and who it belongs to (the player), making it instantly understandable to anyone reading the code.
:::
:::good
A clear and precise name avoids confusion and conveys its meaning clearly
:::

:::greybox
Now let’s say you’re working on an invitation and activation feature. You need a variable to store the validity period for an invitation, so you create one called: `ttlDays`.
While `ttlDays` might seem logical as shorthand for "time-to-live in days," other developers might interpret it as "total days," or spend extra time deciphering its intended use.
:::
:::bad
Unnecessary abbreviations can often be ambiguous
:::

:::greybox
Just call it `TimeToLiveInDays`. It leaves no room for misinterpretation and makes the purpose of the variable obvious on sight.
:::
:::good
Use a clear, unambiguous name
:::

:::greybox
Consider a class named `UserValidator`. At first glance, it seems sensible — it’s presumably responsible for validating a user. But when you think about it, "UserValidator" doesn’t really tell us much. What exactly is it validating? Is it responsible for validating login credentials, profile information, or something else entirely?
:::
:::bad
Vague or generic names that lack specificity can easily lead to confusion
:::

:::greybox
A clearer approach is to ensure each class has a specific responsibility. If it’s meant to handle all user-related validation rules, something like `ValidationHandler` indicates it’s an engine responsible for executing multiple rules and returning a result. But if the class is responsible for validating only a specific aspect of a user, a name like `UserNameLengthValidator` makes its role unmistakable; it tells us this class should validate only the length of a username.
:::
:::good
More specific names convey clearer meaning with greater precision
:::

:::info
**Remember:** Names should describe what something represents without mental gymnastics to decode it. A clear, meaningful name is one of the simplest ways to make your code more readable, maintainable, and welcoming for future collaborators (and for yourself).
:::
