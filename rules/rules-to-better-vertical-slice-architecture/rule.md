---
seoDescription: Vertical Slice Architecture – Shipping features in self-contained slices. Discover how VSA groups code by business feature for faster change, easier testing, and safer refactors; explore its concepts, principles, and benefits.
type: rule
archivedreason:
title: Vertical Slice Architecture - Do you know the main principles?
guid: a00b3148-e6b5-4ce8-96c8-0334717dbb97
uri: vertical-slice-architecture
created: 2025-06-06T10:00:00.0000000Z
authors:
  - title: Hugo Pernet
    url: https://ssw.com.au/people/hugo-pernet
  - title: Daniel Mackay
    url: https://ssw.com.au/people/daniel-mackay
  - title: Sam Maher
    url: https://ssw.com.au/people/sam-maher
related:
  - software-architecture-decision-tree
redirects:
---

VSA organises code by business feature rather than technical layer, meaning each change is confined to a single, self-contained slice.

This design brings 3 clear advantages: predictable impact, quicker reviews, and safer releases with minimal ripple across the codebase.

<!--endintro-->

## What is Vertical Slice Architecture?

Vertical Slice Architecture is a feature-first structure where every user action lives in its own folder. Each slice starts with a request or command object that captures the intent, flows through a single handler that contains the domain logic, relies on slice-owned infrastructure like data access or external API wrappers, and includes tests stored alongside the code.

This keeps the full implementation of a feature in one place, making it easier to add, change, or remove functionality without editing multiple layers or impacting unrelated features.

Unlike Clean Architecture, which separates concerns across horizontal layers, VSA keeps everything related to a feature vertically aligned and self-contained.

`youtube: https://www.youtube.com/watch?v=t-97OCqA1bA`
**Video: Why We Love Vertical Slice Architecture | [Sam Maher](https://www.ssw.com.au/people/sam-maher/) | SSW Rules (7 min)**

## Principles

Vertical Slice Architecture groups code by user action, not by shared controller, service, or repository layers. Each feature owns its full flow—from request to persistence—inside a single folder. 

Routes or UI components trigger a request or command object, which is handled by a dedicated handler responsible for orchestrating domain logic, validation, and infrastructure access.

The handler depends only on what it needs and references only infrastructure local to the slice. Features do not reference each other, ensuring low coupling.

External dependencies are injected directly into the slice, and tests are co-located with the code they validate, making behaviour easy to test and reason about in isolation.

## Benefits  

By choosing Vertical Slice Architecture, you get:  

* **High cohesion, low coupling** – each feature is fully self-contained, with no reliance on unrelated code.  
* **Faster development** – smaller surface area per feature means quicker implementation and review.  
* **Safer refactoring** – changes are isolated to one slice, reducing the risk of breaking other parts of the system.  
* **Simplified onboarding** – new developers can focus on one slice without understanding the entire architecture.  
* **Parallel work** – multiple developers can add or modify slices without stepping on each other.  
* **Easier testing** – tests focus on behaviour, not framework or infrastructure setup.  
* **Clean removals** – deleting a feature is as simple as deleting its folder.
