---
type: rule
archivedreason: 
title: Do you know when to use state management in Angular?
guid: cb706a95-5263-49dc-b568-a37bcb03058a
uri: when-to-use-state-management-in-angular
created: 2021-05-27T14:09:22.0000000Z
authors:
- title: Chris Clement
  url: https://ssw.com.au/people/chris-clement
- title: Matt Goldman
  url: https://ssw.com.au/people/matt-goldman
- title: Piers Sinclair
  url: https://ssw.com.au/people/piers-sinclair
related:
- use-ngrx-on-complex-applications
redirects: []

---

State management in Angular can quickly become unmaintainable if done incorrectly. It is important to fully understand why you are implementing state management and then decide how you are going to do it.

<!--endintro-->

There are many different options you can choose from, including the following:

::: greybox

#### State managed in parent-child component hierarchies

In this method, components do not know about the state of other components but rather receive data via inputs and emit data via events. It works well for simple scenarios but falls over when lots of communication is required between different components.

Pros:

* Simplicity - Out of the box

Cons:

* Communication - No shared state across component trees
* Scalability - When the depth of hierarchies grows, it becomes hard to deal with
* Separation of concerns - Tight coupling between components in the tree
* Testability - You cannot properly unit test parent-child components

:::

::: greybox

#### State management in observable services

Using observable services takes state management to the next level. Using this method, we can enable communication between different component trees. This solution is suitable for most scenarios.

Pros:

* Sharing state - You can pass state between different component trees
* Ease of use - Quick and easy to implement
* Separation of concerns - Keeps business logic away from the presentation logic

Cons:

* Scalability - Services can become a web of dependencies if not kept in check
* Predictability - Consistency is not enforced in the way state is managed
* Testability - It can be hard to test services due to the inherent dependency web

:::

::: greybox

#### Redux e.g. NgRx [(see rule: https://www.ssw.com.au/rules/use-ngrx-on-complex-applications)](/use-ngrx-on-complex-applications)

Redux is a design pattern which centralizes the state into a single shared store across the application. It introduces several constraints on how data flows in and out of the state store in order to make the state scalable and consistent. However, it requires a lot more code and can lead to longer development times. Often this makes sense for large, complicated applications but less so for simple ones.

Pros:

* Centralized state - Makes global state management simpler
* Separation of concerns - Goes one step further by separating business logic and state management
* Predictability - Makes state change predictable by enforcing consistecy
* Testability - Pure functions are much easier to test as they have no external dependencies

Cons:

* Velocity - It can take more code to write
* Boilerplate - Requires the use of many files and has a lot of repetition
* Learning curve - Can be easy to get wrong if you are an inexperienced user
* Third-party library - Not part of the standard Angular library may increase overhead when upgrading Angular. Also introduces additional bundles in the published artifact.
:::
