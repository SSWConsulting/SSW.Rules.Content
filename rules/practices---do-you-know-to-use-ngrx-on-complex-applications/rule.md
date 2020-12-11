---
type: rule
archivedreason: 
title: Practices - Do you know to use NgRx on complex applications?
guid: 4dfae201-17ca-4d5e-90de-90dd492c3e1b
uri: practices---do-you-know-to-use-ngrx-on-complex-applications
created: 2016-08-02T14:25:26.0000000Z
authors:
- id: 24
  title: Adam Stephensen
related: []

---

**Heads Up:** For new teams creating their first SPA using Angular, it is recommend to limit the initial focus to learning Angular, TypeScript, and RxJs. Avoid including advanced state management patterns such as NgRx, unless someone on the team has prior experience. Start with a simple approach to state management and evolve your design once the team has mastered the basics. When your team is ready, be sure to investigate the multitude of patterns, supporting libraries, and best practices available for advanced state management. If you are developing an application that absolutely requires advanced state management then be sure to invest in some training and / or enlist the help of another developer with the right skillset.

State management is complex and time-consuming.

On large applications, it becomes very difficult to maintain state. The redux pattern helps resolve this issue.


NgRx is the redux pattern implemented for Angular.        [View on GitHub](https://github.com/ngrx).


<!--endintro-->
<dl class="image">&lt;dt&gt; <img src="ngrx.png" alt="ngrx.png" data-pin-nopin="true"> &lt;/dt&gt;<dd>Figure: NgRx supercharges the redux pattern with RxJS <br></dd><dd></dd></dl>
Benefits:

* Easy state management
* Better tooling and debugging
* Simpler applications to build
* Increased performance
* Code that is easy to test

<dl class="image">&lt;dt&gt; <img src="img1.png" alt="img1.png"> &lt;/dt&gt;<dd>Figure: NgRx supercharges the redux pattern with RxJS <br></dd></dl><dl class="image">&lt;dt&gt;<img src="img2.png" alt="img2.png">&lt;/dt&gt;<dd>Figure: The redux pattern is a way to implement a predictable state container</dd></dl>
The three principles of the redux pattern:

1. The entire state of the application is represented in a single JavaScript object called a store.
2. The store is acted upon using special functions called reducers.
3. State is immutable and reducers are the only part of the application that can change state.
