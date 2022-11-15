---
type: rule
title: Do you know the different types of testing?
uri: different-types-of-testing
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
related:
  - what-is-exploratory-testing
  - rules-to-better-unit-tests
created: 2022-11-04T01:39:46.642Z
guid: 912111cb-ac1a-4414-8cb2-89cc310eb41f
---
There are many different types of testing, each designed to help mitigate different types of risk.

A good test strategy employs a combination of different types of testing, performed using an appropriate mix of human testing and automation.

<!--endintro-->

![Figure: Each different type of testing serves a different purpose (Keith Edkins, "Too much choice!", license: CC BY-SA 2.0)](too-much-choice.jpg)

The following list of types of testing is not exhaustive, but covers the more common types you should consider when building a comprehensive test strategy.

explain why we don't say functional and non-functional

### Smoke testing

Smoke testing is designed to verify that the critical functionality of software is working, at a very high level. The software is put under limited pressure (undergoing only shallow testing) to make sure no smoke comes out.

The smoke test is meant to be quick to execute, with the goal of giving you some assurance that the major features of your system are working as expected. Smoke tests can be useful right after a new build is made to decide whether or not you can run deeper (and more expensive) tests, or right after a deployment to make sure that they application is running properly in the newly deployed environment.

::: greybox
Why perform smoke testing? To mitigate the risk of the basic and critical functionality failing to work as expected.
:::

### Unit testing

Unit testing is designed to help mitigate the risk of code changes. Unit tests are designed to be small in scope and they typically consist of testing individual methods and functions of the classes, components or modules used by your software. Unit tests are generally quick to run and are executed as part of a CI pipeline.

Unit tests are usually written by developers and external dependencies are mocked so that the tests only test the method or function of interest and not anything the method or function might depend on.



::: greybox
Why perform unit testing? To mitigate the risk of code changes.
:::

See [Rules to Better Unit Tests](https://ssw.com.au/rules/rules-to-better-unit-tests)

### Component testing

### Integration testing
inc. API

### Consumer-driven contract testing
type of int, why call out separately?

Regression


System

UAT

End-to-end?


Acceptance

Performance/load/stress

Atlassian: unit, integration, functional, end-to-end, acceptance, performance, smoke

::: greybox
Don't confuse test approaches & techniques (focused on the "how") with types of testing (the "what"). For example, [exploratory testing](https://www.ssw.com.au/rules/what-is-exploratory-testing) - as an approach - applies well to several of the types of testing outlined above.
:::

**Add your rule to a category**