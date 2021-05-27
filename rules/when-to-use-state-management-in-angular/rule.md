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

State management in Angular can quickly become unmaintainable if done incorrectly. It is important to fully understand why you are implementing state management and then make a descision on how you are going to do it. 

<!--endintro-->

There are many different options you can choose from including the following:

::: greybox

#### Local state in component

Pros:
* Speed - Quick and easy to code
* Boilerplate - Very little boilerplate needed

Cons:
* Sharing state - Hard for different components to communicate
* Scalabilitiy - If the application starts to require more interaction between components it might not scale well
* Separation of concerns - Hard to keep UI apart from data

:::

::: greybox

#### State management in services

Pros:
* 

Cons:
*

:::

::: greybox

#### Hybrid Approach

Pros:
* Flexibility - Let's you decide the best approach on a case-by-case basis
* Incremental - Let's you introduce global state management step-by-step

Cons:
* Standardisation - Lack of standards throughout the code base can be confusing
* Knowledge burden - Relies on all developers being able to identify the best time to use each solution

:::

::: greybox

#### Redux

Pros:
* Sharing of state - Makes global state management simpler
* Separation of concerns - Allows you to separate network/business logic from the UI
* Predictable - Makes state predictable

Cons:
* Speed - Takes a longer time to write code
* Boilerplate - Requires the use of many files and has a lot of repetition
* Learning Curve - Can be easy to get wrong if you are an inexperienced user
* Load times - More packages mean longer load times

:::

