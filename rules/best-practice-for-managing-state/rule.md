---
type: rule
title: Do you know the best practice for managing state?
uri: best-practice-for-managing-state
authors:
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-know-the-best-practice-for-managing-state
created: 2017-08-15T23:35:06.000Z
archivedreason: null
guid: ca46ad62-e44e-4266-a68b-e8d1b04e3b08
---

State management is complex and time-consuming. The redux pattern helps resolve this issue.

<!--endintro-->

::: bad  
![Figure: Bad example - Maintaining state on individual components](maintaining-state.png)  
:::

::: good  
![Figure: Good example - use the redux pattern](redux-logo.png)  
:::

### The 4 principles of the redux pattern

1. The entire state of the application is represented in a single JavaScript object called a [store](https://redux.js.org/docs/basics/Store.html).
2. The store is acted upon using special functions called [reducers](https://redux.js.org/docs/basics/Reducers.html).
3. State is immutable and reducers are the only part of the application that can change state.
4. Reducers are pure JavaScript functions. This means they cannot import external dependencies.

### Side Effects

To perform operations that require external dependencies (such as communicating with a web server), we can implement side effects. These can use external dependencies but they cannot directly modify the store. They can invoke reducers to modify the store when the side effect is complete.

Redux-Saga is a library that provides redux application side effects.

The advantages of using Redux-Saga are:
* Collects all asynchronous operations in one place, making the code clearer
* Uses an  ES6 feature called Generators to make asynchronous flows easy to read, write and test
* Generators also let these asynchronous flows look like your standard synchronous code (kind of like async/await in C#). This solves [“callback hell"](https://en.wiktionary.org/wiki/callback_hell)
