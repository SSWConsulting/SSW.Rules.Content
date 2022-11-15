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

::: greybox
Why perform component testing? To mitigate the risk of code changes.
:::

### Integration testing
inc. API

original: They are coded by a developer
Slower
Test the interaction of components eg. Databases, Web Services

Atlassian: Integration tests verify that different modules or services used by your application work well together. For example, it can be testing the interaction with the database or making sure that microservices work together as expected. These types of tests are more expensive to run as they require multiple parts of the application to be up and running.


::: greybox
Why perform integration testing? To mitigate the risk of code changes.
:::

### Consumer-driven contract testing
type of int, why call out separately?

::: greybox
Why perform consumer-driven contract testing? To mitigate the risk of code changes.
:::

Regression

::: greybox
Why perform regression testing? To mitigate the risk of code changes.
:::

System

UAT

End-to-end?

Atlassian: End-to-end testing replicates a user behavior with the software in a complete application environment. It verifies that various user flows work as expected and can be as simple as loading a web page or logging in or much more complex scenarios verifying email notifications, online payments, etc...

End-to-end tests are very useful, but they're expensive to perform and can be hard to maintain when they're automated. It is recommended to have a few key end-to-end tests and rely more on lower level types of testing (unit and integration tests) to be able to quickly identify breaking changes.

Acceptance
Atlassian: Acceptance tests are formal tests that verify if a system satisfies business requirements. They require the entire application to be running while testing and focus on replicating user behaviors. But they can also go further and measure the performance of the system and reject changes if certain goals are not met.

Performance/load/stress

Atlassian: Performance tests evaluate how a system performs under a particular workload. These tests help to measure the reliability, speed, scalability, and responsiveness of an application. For instance, a performance test can observe response times when executing a high number of requests, or determine how a system behaves with a significant amount of data. It can determine if an application meets performance requirements, locate bottlenecks, measure stability during peak traffic, and more. 

Load
original: Setup by developers
Simulate expected load on your application
Use the performance stats as a baseline for regression. You don't want to decrease performance in your application.
Tip: try to execute these from the cloud

Stress
original: Setup by developers
Hit your application very hard, and try to see where your limits are (CPU, Network, Memory)

::: greybox
Don't confuse test approaches & techniques (focused on the "how") with types of testing (the "what"). For example, [exploratory testing](https://www.ssw.com.au/rules/what-is-exploratory-testing) - as an approach - applies well to several of the types of testing outlined above.
:::

**Add your rule to a category**