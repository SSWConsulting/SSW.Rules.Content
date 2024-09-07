---
seoDescription: Understanding the testing pyramid models, such as Mike Cohn's automated testing pyramid, is crucial for developing effective test strategies and mitigating risks in software development.
type: rule
title: Do you understand the "testing pyramid" models?
uri: testing-pyramid
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
related:
  - automated-ui-testing-sparingly
  - different-types-of-testing
created: 2022-11-25T02:53:59.794Z
guid: ee5b40cf-cf8e-4b0c-a421-ab34f28d8b76
---

Having an awareness of the different types and levels of testing is critical to developing appropriate test strategies for your applications.

::: greybox
Remember that different types and levels of tests help to mitigate different types of risk in your software.
:::

There are various models to help with this, most stemming from Mike Cohn's simple [automated testing pyramid](https://www.mountaingoatsoftware.com/blog/the-forgotten-layer-of-the-test-automation-pyramid).

<!--endintro-->

![Figure: Mike Cohn's automated testing pyramid (2009)](test-pyramid-cohn.jpg)

> "All models are wrong, but some are useful"
>
> - George Box

The test pyramid is a model and, like all models, it is wrong, though it is perhaps useful.

The core idea of this model is that an effective testing strategy calls for automating checks at three different levels, supplemented by human testing.

The pyramid model shows you where proportionally more automation effort should be placed - so a good strategy would see many automated unit tests and only a few end-to-end (UI-driven) tests.

The pyramid favours automated unit and API tests as they offer greater value at a lower cost. Test cost is a function of execution time, determinism, and robustness directly proportional to the size of the system under test. As automated unit and API tests have a minimal scope, they provide fast, deterministic feedback. In contrast, automated end-to-end and manual tests use a much larger system under test and produce slower, less deterministic and more brittle feedback.

Let's look at the 3 levels of automation in a little more detail.

### Unit tests

The pyramid is supported at the bottom by unit tests as unit testing is the foundation of a solid automation strategy and represents the largest part of the pyramid. Unit tests are typically written using the same language as the system itself, so programmers are generally comfortable with writing them (though you shouldn't assume they're **good** at writing them). Cohn says:

> "Automated unit tests are wonderful because they give specific data to a programmer—there is a bug and it’s on line 47. Programmers have learned that the bug may really be on line 51 or 42, but it’s much nicer to have an automated unit test narrow it down than it is to have a tester say _"There's a bug in how you're retrieving member records from the database, which might represent 1,000 or more lines of code."_ These smaller (scope) tests put positive pressure on the design of the code, since it is easier for bigger (scope) tests with poor code to pass than smaller (scope) tests with poor code." - Mike Cohn

Although writing unit tests is typically a developer task within the agile team, there is also an excellent opportunity for testers to be involved by pairing with developers to help them write better unit tests. It's a mistake to assume that developers know how to write good unit tests, since it is unlikely that they have been trained in test design techniques. The tester does not need to know the programming language, the idea is that the developer can talk through the intent of their unit tests and the tester can ask questions that may identify missing coverage or indicate logical flaws. This is an excellent use of a tester's time, since getting a good set of unit tests in place is foundational to the rest of the automation strategy.

See [Rules to Better Unit Tests](/rules-to-better-unit-tests).

### Acceptance tests (aka "service tests" or "API tests")

The middle layer of the pyramid - variously referred to as acceptance tests, service tests or API tests - increases the scope of tests compared to unit tests and is often (as Cohn refers to it) the "forgotten layer". While there is great benefit to be gained from automating at this level, it is often ignored or overlooked in automation efforts, especially in teams that are [overly-reliant on automated UI tests](/automated-ui-testing-sparingly).

Testing at this level typically requires different tooling because the tests will be manipulating APIs outside of a user interface, so it can be more challenging for testers to be involved here than at the functional UI test level, but a good framework should make it possible for testers to design and write tests at the service/API level too.

Although there is great value in automated unit testing, it can cover only so much of an application's testing needs. Without service-level testing to fill the gap between unit and user interface testing, all other testing ends up being performed through the user interface, resulting in tests that are expensive to run, expensive to write, and often fragile.

### End-to-end/UI tests

Automated UI tests should be kept to a minimum, leveraging their value to check that important user workflows continue to work as expected while avoiding the problems associated with their overuse.

See [Do you remember to use automated UI testing sparingly?](/automated-ui-testing-sparingly)

### An alternative model - the bug filter (Noah Sussman)

Many different test pyramid models have been inspired by Cohn's simple original idea.

An interesting take comes from [Noah Sussman](https://infiniteundo.com/post/158179632683/abandoning-the-pyramid-of-testing-in-favor-of-a) who re-imagined the test pyramid as a bug filter (turning the pyramid on its head in the process):

![Figure: Noah Sussman's bug filter model (2017)](bug-filter.jpg)

Note that the area of the bug filter changes at each level. Unit tests focus solely on product code, but integration tests might include databases or external web services. End-to-end tests cover an even larger architecture. Bugs can appear from these new systems without having passed through a previous filter.

Katrina Clokie (in her book [A Practical Guide to Testing in DevOps](https://leanpub.com/testingindevops)) explains this bug filter model as follows:

> I imagine the bugs that drop through this filter as being butterflies in all stages of their lifecycle. Unit tests are going to capture the eggs — bugs before they develop into anything of consequence. Integration tests are going to capture the caterpillars. These may have arisen from a unit test egg that has hatched in the integrated environment, or may have crawled into our platform via a third-party system. End-to-end tests capture the butterflies."
>
> - Katrina Clokie

### Further reading

- [A Test Pyramid Heresy](https://www.linkedin.com/pulse/test-pyramid-heresy-john-ferguson-smart) by John Ferguson-Smart
- [Why I Still Like Pyramids](http://thatsthebuffettable.blogspot.com/2016/03/why-i-still-like-pyramids.html) by Marcel Gehlen
