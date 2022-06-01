---
type: rule
title: Do you test your JavaScript?
uri: test-your-javascript
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Chris Clement
    url: https://www.ssw.com.au/people/chris-clement/
related: []
redirects:
  - do-you-test-your-javascript
created: 2020-03-11T22:56:26.000Z
archivedreason: null
guid: fa6c9020-0efd-4211-9c2c-ef4bcc98aab5
---

The need to build rich web user interfaces is resulting in more and more JavaScript in our applications.

Because JavaScript does not have the safeguards of strong typing and compile-time checking, it is just as important to unit test your JavaScript as your server-side code.

<!--endintro-->

You can write unit tests for JavaScript using:

* [Jest](https&#58;//jestjs.io/) **(Recommended)**
* [Karma](https&#58;//karma-runner.github.io/latest/index.html)
* [Jasmine](https&#58;//jasmine.github.io/)

Jest is recommended since [it run faster than Karma](https://charith-hettiarachchi.medium.com/why-use-jest-over-karma-for-angular-testing-b56ffa82f8) due to Karma run tests in browser while Jest run tests in Node.