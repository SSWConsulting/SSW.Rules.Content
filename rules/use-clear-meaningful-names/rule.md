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

In the early days of coding, we had to store more information in our heads than in our computers, leading to all sorts of creative abbreviations and clever shortcuts. But today, storage and readability are no longer limitations—our computers can handle verbose names better than our brains can handle cryptic codes. Clinging to those old practices can hurt your code’s readability and make life harder for your team. Mental gymnastics waste time and money!

Names should always describe at first glance what something represents.

`youtube: https://www.youtube.com/watch?v=t-t7P2BZnS4`

**Video: Naming Conventions | Jeoffrey Fischer (5 min)**

<!--endintro-->

## ⚠️ Avoid mental encoding

Keep names obvious. It’s easy to invent codes to keep names short, like `cstmrMgr` to represent a "customer manager" - and you might feel clever doing it. But this kind of shorthand requires other developers (or your future self) to mentally decode each abbreviation. There’s no good reason not to simply call it `CustomerManager` (although there are reasons to avoid "manager" as a name, see [Do you avoid generic names like “manager,” “processor,” “data,” or “info”?](/avoid-generic-names)).

## Be verbose

Today, we have the luxury of not worrying about character limits. While you shouldn’t use full sentences for a class or method name, there’s no reason to squeeze names into cryptic codes (testing can be an exception, see [Do you follow naming conventions for tests and test projects?](/follow-naming-conventions-for-tests-and-test-projects)).
Full, meaningful words make your code readable and maintainable.

## Scenario - Creating a game with user accounts and multiplayer

:::greybox
`Nrg` - variable short for "energy," — it’s easy to write, and you know what it means.
:::
:::bad
Bad example - Being clever for you can cause confusion to others  - they might misinterpret "energy" as something else, like power or ammo. Then if you add enemies, would you name their energy variable `nmeNrg`?
:::

:::greybox
`PlayerHealth` - clearly describes the specific kind of "energy" (health) and who it belongs to (the player)
:::
:::good
Good example - instantly understandable to anyone reading the code
:::

Now let’s say you’re working on an invitation and activation feature. You need a variable to store the validity period for an invitation - the live time.

:::greybox
`itrDays` - shorthand for "invitation-time-remaining in days"
:::
:::bad
Bad example - others will have fun deciphering this one
:::

:::greybox
`InvitationTimeRemainingInDays` - no explanation needed here!
:::
:::good
Good example - leaves no room for misinterpretation and makes the purpose obvious
:::

:::greybox
`UserValidator` - this class is responsible for validating a user
:::
:::bad
Bad example - Validating what exactly? Login credentials? Profile information? Something else?
:::

:::greybox
`UserValidationHandler` - indicates it’s an engine responsible for executing multiple rules to handle user-related validation

`UserNameLengthValidator` - validator is for a specific aspect of a user - the length of a username
`UserEmailFormatValidator` - validator for another specific aspect - ensures email contains "@" and a domain
:::
:::good
Good example - the definition of the classes is in their names
:::

:::info
**Remember:** Names should always describe what something represents without mental gymnastics to decode it.
:::
