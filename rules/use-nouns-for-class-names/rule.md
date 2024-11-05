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

A fundamental principle of object-oriented programming is that a class represents something from outside the code—whether a tangible item, like a Car, or an abstract concept, like a Record. A class should reflect its purpose as a "thing," not an action. Calling a car "Drive" would quickly become confusing, and the same is true in your code. Keeping classes named as nouns maintains clarity and reinforces their role as representations of entities in the system.

<!--endintro-->

## What is a noun?
A noun is a word that names a thing. Common examples include tangible items like Table, Cup, or Computer and abstract entities like Record, Database, or Cloud. In your code, class names should clearly reflect what they represent, giving developers an immediate understanding of the class’s role.

:::bad
Imagine you’re building an e-commerce application, and you create a class called `ProcessOrder`. While it might seem reasonable, this name is misleading — it suggests an action, not a thing. The class’s responsibility is not the act of processing but the concept of an Order itself.
:::

:::good
Naming the class `Order` better represents its role as an entity that holds order-related data and behavior. Later, if you need to perform an action on the order, you might create a `ProcessOrder` method within the`OrderService` or `OrderProcessor` class (see our rule [Do you use verbs for method names?](/verbs-for-method-names)). This keeps the naming consistent with object-oriented principles.
:::

## Events: The exception that proves the rule
In domain-driven design (DDD) and event-driven architectures (EDA), you’ll often see exceptions to this rule. Events like `OrderPlaced` or `UserRegistered` are commonly named with verb phrases to represent specific actions or occurrences within the system, rather than entities with persistent state. This naming convention is acceptable, as it indicates a change or trigger rather than a static object. For other class types, however, sticking to nouns keeps the codebase clear and consistent.
