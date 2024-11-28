---
seoDescription: In object-oriented programming (OOP), a class represents a thing. Therefore, you should use a noun for your class name as this most accurately represents what it's modelling.
type: rule
archivedreason:
title: Do you use nouns for class names?
uri: nouns-for-class-names
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
  - avoid-generic-names
  - avoid-micro-jargon
  - consistent-words-for-concepts
  - when-to-use-technical-names
  - avoid-using-your-name-in-client-code
  - use-meaningful-modifiers
  - follow-naming-conventions-for-tests-and-test-projects
guid: b5fa18cd-5fb7-4273-9b09-70379de7ef60
---

A fundamental principle of object-oriented programming is that a class represents something from outside the code—whether a tangible item, like a car, or an abstract concept, like a record. A class should reflect its purpose as a "thing," not an action. Calling a car "drive" would quickly become confusing, and the same is true in your code. Keeping classes named as nouns maintains clarity and reinforces their role as representations of entities in the system.

<!--endintro-->

## What is a noun?

[A noun is a word that names a thing](https://www.merriam-webster.com/dictionary/noun). Common examples include tangible items like table, cup, or computer and abstract entities like record, database, or cloud. In your code, class names should clearly reflect what they represent, giving developers an immediate understanding of the class’s role.

Fun fact: [Some languages even capitalize nouns in normal writing!](https://www.thoughtco.com/capitalization-in-german-4069437) They can just know what's a noun by checking if it's capitalized - but in English we need to remember.

:::greybox
`ProcessOrder`
:::
:::bad
Bad example - This name suggests an action which sounds like it could be a method - but it's meant to represent the order itself.
:::  

:::greybox
`Order` - better represents its role as an entity that holds order-related data and behavior
:::
:::good
A class name that clearly represents a thing is much easier to understand - you couldn't misinterpret this as a method
:::  

Later, if you need to perform an action on the order, you might create a `ProcessOrder` method within the`OrderService` or `OrderProcessor` class (see our rule [Do you use verbs for method names?](/verbs-for-method-names))

## Events: The exception that proves the rule

In domain-driven design (DDD) and event-driven architectures (EDA), you’ll often see exceptions to this rule. Events like `OrderPlaced` or `UserRegistered` are commonly named with verb phrases to represent specific actions or occurrences within the system, rather than entities with persistent state. This naming convention is acceptable, as it indicates a change or trigger rather than a static object. For other class types, however, sticking to nouns keeps the codebase clear and consistent.
