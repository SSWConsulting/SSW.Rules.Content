---
seoDescription: Customized versions of classes or components should reflect the customization in the name.
type: rule
archivedreason:
title: Do you use verbs for method names?
uri: verbs-for-method-names
created: 2024-11-05T00:00:00.0000000Z
authors:
  - title: Matt Goldman
    url: https://ssw.com.au/people/matt-goldman
related:
  - clear-meaningful-names
  - nouns-for-class-names
  - avoid-generic-names
  - avoid-micro-jargon
  - consistent-words-for-concepts
  - when-to-use-technical-names
  - avoid-using-your-name-in-client-code
  - use-meaningful-modifiers
  - follow-naming-conventions-for-tests-and-test-projects
guid: ca38d766-d16b-4bc3-b206-10b85fe41530

Code becomes easier to understand when names align closely with their meaning. Since classes represent things, they should use nouns. Methods, on the other hand, represent actions and should be named using verbs. A method named Person, for example, could easily confuse your team by suggesting an entity rather than an action.

<!--endintro-->

## What is a verb?
A verb is a word that describes an action or process—something that’s done. Examples include walk, run, think, listen, and breathe, as well as process, calculate, send, and save. While your method names shouldn’t all be single verbs (since that’s often too vague), they should be verb-based, using a verb as the foundation of their meaning.

:::bad
Imagine you’re working on an e-commerce app and need to write code to handle shipping products to customers who have completed an order. You create a method called `Ship`. While Ship is a verb, it’s also a noun, making it ambiguous. Additionally, it’s not descriptive enough to convey the method’s purpose clearly.
:::

:::good
A better name for this method is `SendCustomerOrder`. It’s specific, making it clear what the method does and within what context.
:::

:::bad
Suppose you’re working on an electronic medical record system, and you need to create a way for nurses to document medications that have been administered to patients. You name the method `Administration`. This is problematic for two reasons — it’s a noun, and it’s ambiguous. “Administration” has multiple meanings, and the method name doesn’t make it clear what this action involves.
:::

:::good
A more precise name for this method is `AdministerMedication`. It clearly describes the real-world action it models. Another option could be `RecordMedication`, but this is less effective. First, “record” can be either a noun or a verb, and second, it lacks context — it could imply logging delivery to a pharmacy or entering a new medication type into the system.
:::
