---
type: rule
archivedreason: 
title: Do you know when to use state management in Angular
guid: cb706a95-5263-49dc-b568-a37bcb03058a
uri: when-to-use-state-management-in-angular
created: 2021-05-27T14:09:22.0000000Z
authors:
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

Using observable services takes state management to the next level. Using this method, we can enable communication between different components. However, as the application builds out and we need to create more and more services, it becomes challenging to maintain.

Pros:
* Ease of use - Quick and easy to implement
* Separation of concerns - keeps business logic away from the presentation logic
* Sharing State - You can pass state between different components

Cons:
* Scalability - Once more than one service is introduced, it becomes harder to manage
* Predictability - The way state is managed could vary between different services, confusing.

:::

::: greybox

#### Redux (e.g. NgRx)

Redux provides a comprehensive framework for state management. It defines a strict way of constructing your code in a manner that is scalable and consistent. However, it requires a lot more code and can lead to longer development times. Often this makes sense for large, complicated applications but less so for simple ones.

Pros:
* Sharing of state - Makes global state management simpler
* Separation of concerns - Allows you to separate network/business logic from the UI
* Predictable - Makes state predictable

Cons:
* Speed - It can take a long time to write code
* Boilerplate - Requires the use of many files and has a lot of repetition
* Learning Curve - Can be easy to get wrong if you are an inexperienced user
* Load times - More packages mean longer load times

:::


::: greybox

#### Hybrid Approach

A hybrid approach of combining all three techniques can give the best of both worlds by providing flexibility and allowing different methods to be introduced incrementally. However, it places a burden of knowledge on the developers and can confuse them due to a lack of standardisation.

Pros:
* Flexibility - Let's you decide the best approach on a case-by-case basis
* Incremental - Let's you introduce global state management step-by-step

Cons:
* Standardisation - Lack of standards throughout the codebase can be confusing
* Knowledge burden - Relies on all developers being able to identify the best time to use each solution

:::

