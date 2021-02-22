---
type: rule
archivedreason: 
title: Practices - Do you know to use NgRx on complex applications?
guid: 4dfae201-17ca-4d5e-90de-90dd492c3e1b
uri: use-ngrx-on-complex-applications
created: 2016-08-02T14:25:26.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
related: []
redirects:
- practices-do-you-know-to-use-ngrx-on-complex-applications

---

**Heads Up:** For new teams creating their first SPA using Angular, it is recommend to limit the initial focus to learning Angular, TypeScript, and RxJs. Avoid including advanced state management patterns such as NgRx, unless someone on the team has prior experience. Start with a simple approach to state management and evolve your design once the team has mastered the basics. When your team is ready, be sure to investigate the multitude of patterns, supporting libraries, and best practices available for advanced state management. If you are developing an application that absolutely requires advanced state management then be sure to invest in some training and / or enlist the help of another developer with the right skillset.

State management is complex and time-consuming.

On large applications, it becomes very difficult to maintain state. The redux pattern helps resolve this issue.


NgRx is the redux pattern implemented for Angular.        [View on GitHub](https://github.com/ngrx).


<!--endintro-->

![Figure: NgRx supercharges the redux pattern with RxJS](ngrx.png)  

Benefits:

* Easy state management
* Better tooling and debugging
* Simpler applications to build
* Increased performance
* Code that is easy to test


![Figure: NgRx supercharges the redux pattern with RxJS](img1.png)  

![Figure: The redux pattern is a way to implement a predictable state container](img2.png)  

The three principles of the redux pattern:

1. The entire state of the application is represented in a single JavaScript object called a store.
2. The store is acted upon using special functions called reducers.
3. State is immutable and reducers are the only part of the application that can change state.


### What do we mean by complex?


State management such as ngrx is most useful when applied to shared data  - that can be changed or "mutated" in multiple ways. When applied to data that is not shared there is a risk of adding much more effort with little value

**Simple Example**

"Add a company edit form to capture a company's address and contact details, when the user clicks 'save', we send a HTTP POST to an API". 

In this type of scenario, the company details you are editing are not shared with any other component so you get little benefit from using state management.

**Complex example**

"Add a checkout screen where users can change order quantities and see the totals immedately update. Also there is a widget in the toolbar that shows number of items and cart total at all times"

This type of complexity is perfect for ngrx! The state of your shopping cart can be in kept the Store an both the main Checkout Component and the Cart widget can be kept in sync by selecting this state from the store and raising actions to mutate that state in controlled and predictable ways.
