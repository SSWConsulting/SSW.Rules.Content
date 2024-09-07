---
seoDescription: Treat automated test code as a first-class citizen by applying best practices and maintaining high-quality code to ensure reliable testing and prevent deployment of poor quality code.
type: rule
title: Do you treat your automated test code as a first-class citizen?
uri: automated-test-code-first-class-citizen
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
created: 2022-11-17T23:31:19.187Z
guid: c3bb3017-1e8f-44d5-98c6-3a714cfb6f2b
---

Good quality automated tests can help your development to continue more quickly and with more safety.

Gating deployments on the successful outcomes of your automated test suites can prevent you from automatically pushing bad code into production.

Depending on your automated tests to make deployment/release decisions means that your test code **must** be excellent quality.

<!--endintro-->

![Figure: Don't make excuses for writing poor quality test code](important-find-a-way.jpg)

You're writing (automated test) code because you, legitimately, have doubts about other (product) code, so this automated test code is as important as the production code - and maybe even more important!

The test code should be treated as a first-class citizen, so:

✅ Same best practices - apply your coding best practices to the test code (e.g. clean coding, maintainability, performing code reviews, etc.)\
✅ Definition of Done - add all of the levels of automated tests you need to complete to your Definition of Done\
❌ "Anyone can write the tests" - don't allocate the work of writing test code to people whose job doesn't normally involve writing production-quality code, the same level of skill is required for the production code and the test code\
❌ Tolerate/skip failing tests - refactor the tests as required as you refactor the product code

### Further reading

* [On treating your test code like production code](https://www.ontestautomation.com/on-treating-your-test-code-like-production-code/) by Bas Dijkstra
