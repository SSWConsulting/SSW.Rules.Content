---
seoDescription: We often use ours or our company name to denote a custom version of something. Unless you're publishing a library, this is never a good idea.
type: rule
archivedreason:
title: (For consultants) Do you avoid using your or your company’s name in client code?
uri: avoid-using-your-name-in-client-code
created: 2024-11-05T00:00:00.0000000Z
authors:
  - title: Matt Goldman
    url: https://ssw.com.au/people/matt-goldman
related:
  - clear-meaningful-names
  - verbs-for-method-names
  - nouns-for-class-names
  - avoid-generic-names
  - avoid-micro-jargon
  - consistent-words-for-concepts
  - when-to-use-technical-names
  - use-meaningful-modifiers
  - follow-naming-conventions-for-tests-and-test-projects
guid: 7d9eb8d3-4522-40c9-bcbd-b22f48f50edf
---

When building solutions for clients, it’s tempting to include personal or company identifiers in control or component names, like `GoldieEntry` or `SSWButton`. However, naming controls after yourself or your company in client projects can create confusion, dilute the client’s branding, and look unprofessional. For consultants, the goal should be to name components in ways that make sense within the client’s business context.


<!--endintro-->

## Why It Matters
Names that reflect the client’s brand or domain are clearer and more meaningful for the client’s internal teams and stakeholders. They also reduce the risk of naming conflicts and make it easier for future developers to understand the purpose of a component in context.

:::greybox
Naming a custom entry field `GoldieEntry` or `SSWEntry` might make sense in a personal or shared library but is out of place in a client project.
:::
:::bad
Naming client IP after yourself or your company is not cool
:::

:::greybox
Instead, using something like `NorthwindStepper` is more client-aligned and indicates that this is a customized variation of a standard control.
:::
:::good
Naming client IP with the client's branding is better
:::

**Note:** This approach is ok to denote a branded version of something, but often it's better to indicate the customization itself in the name. See our rule [Do you use meaningful modifiers for custom implementations?](/use-meaningful-modifiers).
