---
type: rule
title: Is your automated test code a first-class citizen?
uri: automated-test-code-first-class-citizen
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
created: 2022-11-17T23:31:19.187Z
guid: c3bb3017-1e8f-44d5-98c6-3a714cfb6f2b
---
Good quality automated tests can help your development to continue more quickly and with more safety.

Gating deployments on the successful outcomes of your automated test suites can prevent you from automatically pushing bad code into production.

Depending on your automated tests to make deployment/release decisions means that your test code must be of excellent quality.

<!--endintro-->

![Figure: xxx](important-find-a-way.jpg)

You're writing (automated test) code because you, legitimately, have doubts about other (product) code. This means that this automated test code is as important as the production code (maybe even more important!). 

The test code should be treated as a first-class citizen, so:

✅ Apply your coding best practices to the test code (e.g. clean coding, maintainability, performing code reviews, etc.)\
✅ Add all of the levels of automated tests you need to complete to your Definition of Done\
✅ ddd\
❌ Allocate the work of writing test code to people whose job doesn't normally involve writing production-quality code
❌ fff

**Add your rule to a category**