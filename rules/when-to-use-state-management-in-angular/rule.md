---
type: rule
archivedreason: 
title: Do you know when to use state management in Angular
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

#### Local state in component

Local state is the most basic use case. In this method, components do not know about the state of other components. It works well for simple scenarios but falls over when lots of communication is required between different components.

Pros:
* Speed - Quick and easy to code
* Boilerplate - Very little boilerplate needed

Cons:
* Sharing state - Hard for different components to communicate
* Scalability - If the application starts to require more interaction between components, it might not scale well
* Separation of concerns - Hard to keep UI apart from data

:::

::: greybox

#### State management in observable services

Using observable services takes state management to the next level. Using this method, we can enable communication between different components. This solution is suitable for most scenarios, however as your application grows in complexity, it can become challenging to maintain.

Pros:
* Ease of use - Quick and easy to implement
* Separation of concerns - keeps business logic away from the presentation logic
* Sharing State - You can pass state between different components

Cons:
* Scalability - Once more than one service is introduced, it becomes harder to manage
* Predictability - The way state is managed could vary between different services, confusing.

:::

::: greybox

#### Redux (e.g. NgRx[(see rule: https://www.ssw.com.au/rules/use-ngrx-on-complex-applications)](https://www.ssw.com.au/rules/use-ngrx-on-complex-applications))

Redux is a design pattern which centralises the state into a single shared store across the application. It introduces several constraints on how data flows in and out of the state store in order to make the state scalable and consistent. However, it requires a lot more code and can lead to longer development times. Often this makes sense for large, complicated applications but less so for simple ones.

Pros:
* Centralised state - Makes global state management simpler
* Separation of concerns - Allows you to separate network/business logic from the UI
* Predictable - Makes state change predictable due to the use of pure functions
* Unidirectional data flow - Eliminate rouge services mutating the state without firing a trackable action

Cons:
* Velocity - It can take more code to write
* Boilerplate - Requires the use of many files and has a lot of repetition
* Learning Curve - Can be easy to get wrong if you are an inexperienced user
* Third-party library - Not part of the standard Angular library may increase overhead when upgrading Angular. Also introduces additional bundles in the published artifact
* 
:::
