---
seoDescription: It's a common belief that consistency matters more than anything else in your code, and this is especially true of the names you use to represent concepts.
type: rule
archivedreason:
title: Are you consistent with the words you use to represent concepts?
uri: consistent-words-for-concepts
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
  - when-to-use-technical-names
  - avoid-using-your-name-in-client-code
  - use-meaningful-modifiers
  - follow-naming-conventions-for-tests-and-test-projects
guid: 782822da-92e3-4912-855b-cf1f2a05542b
---

There’s more than one way to skin a cat (apparently—we don’t have any rules on cat-skinning), and equally, there’s often more than one term to represent a concept. While some terms may have nuanced differences, they can often seem interchangeable. But once you’ve picked a term, stick with it and use it everywhere. Inconsistent language is one of the quickest ways to violate the DRY principle and add unnecessary complexity to your codebase.


<!--endintro-->

## Why Consistency Matters
### The DRY Principle
The DRY (Don’t Repeat Yourself) principle states that within a codebase, there should be a single authoritative source of knowledge for each concept. Inconsistent naming makes it harder for developers to find existing code, as they may search for one term and miss relevant code that uses another name.
### Cognitive Load
Using multiple terms to describe the same thing adds cognitive load and increases the mental effort required to understand the codebase. Consistency reduces this burden and makes it easier for anyone to follow the logic.

## Scenario
Imagine you’re working on an e-commerce app, and you’ve been tasked with adding SMS and email notifications when an order is shipped. You notice the word “consignment” used throughout the codebase and assume this is the relevant concept. You begin searching for a `SendConsignment` method but can’t find it. Assuming no notification logic exists, you go ahead and implement a `SendConsignment` method along with the required dependencies and notification options.    

Later, you open a pull request, and a colleague calls, confused, asking why you’ve re-implemented an entire feature. After some back and forth, they show you the existing `SendOrder` method, which already handles notifications.

```csharp
public void SendOrder(NotificationType type)
{ 
    // existing implementation
}
```
:::bad
The name used for this method is not consistent with the name used for the same concept everywhere else in the code base
:::

## Outcome
What went wrong here? Was it a lack of diligence in searching for existing functionality, or the use of different terms — “order” and “consignment” — interchangeably? Likely a bit of both, but primarily, the issue is rooted in inconsistent terminology.    

In this case, the terms “order” and “consignment” may seem related, but they have distinct meanings. An order is something a customer places, indicating their intent to purchase goods or services. A consignment, on the other hand, refers to what a supplier sends to a customer, which may partially or fully fulfill an order.    

In this scenario, the `SendOrder` method should have been called `SendConsignment`, assuming “consignment” was already used in the codebase. 

```csharp
public void SendConsignment(NotificationType type)
{ 
    // new implementation
}
```
:::good
The name used for this method is the same name used for this concept throughout the code base
:::


To clarify, it's not necessarily wrong to have a `SendOrder` method, if the term order is ubiquitous (see our rule [Do you use ubiquitous language?](/ubiquitous-language)). It might represent a pipeline for example, tracking a workflow from submission by the customer to receipt by the customer, and everything in between. But if “order” was the chosen term, the team should have used it consistently across the code. Any introduction of new terminology, such as “consignment,” should be a proactive, team-wide decision that includes any necessary refactoring.

## DRY Principle Implications
In a worst-case scenario, someone unfamiliar with the `SendOrder` method might merge the `SendConsignment` code without realizing it’s redundant. Now, two methods exist for the same function — each handling notifications differently. This violates the DRY principle, as you now have two distinct pieces of knowledge on handling order shipments, potentially leading to divergent behavior and increased maintenance overhead.
