---
type: rule
archivedreason: Rule is misleading, content has been added to the unit testing framework rule
title: Do you know the best test framework to run your integration tests?
guid: 22123684-53fe-4602-b1ba-9fac0c98b3d0
uri: the-best-test-framework-to-run-your-integration-tests
created: 2020-03-23T17:48:41.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
related: []
redirects:
- do-you-know-the-best-test-framework-to-run-your-integration-tests

---

Both NUnit and xUnit are great choices for unit testing – and are highly recommended. Both these frameworks are optimized for unit testing - and xUnit, in particular, has been designed to encourage strong unit test principles by keeping tests isolated.

<!--endintro-->

When it comes to writing integration tests, you often write tests against slower shared resources and you need more flexibility on how to discover, set up and run your tests.

Fixie solves this issue by providing an extensible conventions based system to control how tests are discovered and executed.

* You can switch from the default frequent instance-per-test test class construction (xUnit-style) to infrequent shared class instance (NUnit style)
* You can configure async setup methods to manage expensive dependencies
* This configuration is via conventions to keep your testing code concise
* In fixie, tests don't run in parallel – which is more suitable for integration tests over shared resources


Read the Fixie Documentation here:     [https://github.com/fixie/fixie/wiki](https&#58;//github.com/fixie/fixie/wiki)
