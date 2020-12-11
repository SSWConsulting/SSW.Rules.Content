---
type: rule
archivedreason: 
title: Do you know the best practice for managing state?
guid: ca46ad62-e44e-4266-a68b-e8d1b04e3b08
uri: do-you-know-the-best-practice-for-managing-state
created: 2017-08-15T23:35:06.0000000Z
authors:
- id: 24
  title: Adam Stephensen
- id: 1
  title: Adam Cogan
related: []

---

State management is complex and time-consuming.

<!--endintro-->

The redux pattern helps resolve this issue.
<dl class="badImage">&lt;dt&gt;<img src="maintaining-state.png" alt="maintaining-state.png"><br>&lt;/dt&gt;<dd>Bad example: maintaining state on individual components</dd></dl><dl class="goodImage">&lt;dt&gt;<img src="redux-logo.png" alt="redux-logo.png"> <br>&lt;/dt&gt;<dd> Good example: use the redux pattern</dd></dl>
The 4 principles of the redux pattern:

1. The entire state of the application is represented in a single JavaScript object called a store [https://redux.js.org/docs/basics/Store.html].
2. The store is acted upon using special functions called reducers [ https://redux.js.org/docs/basics/Reducers.html].
3. State is immutable and reducers are the only part of the application that can change state.
4. Reducers are pure JavaScript functions. This means they cannot import external dependencies.


<font color="#333333">Side Effects<br></font>

<font color="#333333">To perform operations that require external dependencies (such as communicating with a web server), we can implement side effects. These can use external dependencies but they cannot directly modify the store. They can invoke reducers to modify the store when the side effect is complete</font>

<font color="#333333"><br>redux-saga is a library that provides redux application side effects.<br>The advantages of using redux-saga are:<br><ol><li>Collects all asynchronous operations in one place, making the code clearer.<br></li><li>Uses an  ES6 feature called Generators to make asynchronous flows easy to read, write and test.<br></li><li>Generators also let these asynchronous flows look like your standard synchronous code (kind of like async/await in C#). This solves “callback hell” [<a href="https://en.wiktionary.org/wiki/callback_hell">https://en.wiktionary.org/wiki/callback_hell </a>]</li></ol></font>

<font color="#333333"></font>
