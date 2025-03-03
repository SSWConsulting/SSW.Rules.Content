---
seoDescription: Customized versions of classes or components should reflect the customization in the name.
type: rule
archivedreason:
title: Do you use meaningful modifiers for custom implementations?
uri: use-meaningful-modifiers
created: 2024-11-05T00:00:00.0000000Z
authors:
  - title: Matt Goldman
    url: https://ssw.com.au/people/matt-goldman
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
  - title: Daniel Mackay
    url: https://ssw.com.au/people/daniel-mackay
related:
  - clear-meaningful-names
  - verbs-for-method-names
  - nouns-for-class-names
  - avoid-generic-names
  - avoid-micro-jargon
  - consistent-words-for-concepts
  - when-to-use-technical-names
  - avoid-using-your-name-in-client-code
  - follow-naming-conventions-for-tests-and-test-projects
guid: 5a4fe6d7-4df6-4baf-848a-6645c2ef549a
---

When creating custom controls, avoid vague or generic names like CustomStepper or CustomDbContext. Generic terms like “custom” or “base” don’t communicate what makes the component unique, and they add little value for other developers. Instead, use meaningful modifiers that describe the component’s specific purpose or customization.

<!--endintro-->

## Why it matters

Meaningful modifiers make it clear what a class, module, or component does or how it differs from a standard version. This helps developers understand its role without digging through code and reduces the chance of naming conflicts with other libraries.

:::greybox
Naming a custom **`DbContext`** implementation **`CustomDbContext`** or a specialized input control **`CustomInput`** doesn’t provide any real information. It’s unclear what is customized, making it harder to understand and maintain.
:::
:::bad
Bad example - A modifier that doesn't tell you what has been modified is of no value
:::

:::greybox
A more descriptive name, like **`WriteOnlyDbContext`** or **`BorderlessTextInput`**, indicates exactly what’s different about the component, making it easier to understand its function at a glance.
:::
:::good
Good example - A modifier that clearly conveys what is different from the original can save developers time reading through the code
:::
