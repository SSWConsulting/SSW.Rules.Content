---
type: rule
title: Do you know the different types of testing?
uri: different-types-of-testing
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
related:
  - what-is-exploratory-testing
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

### Unit testing
(+ related)

Original: They are coded by a developer
Quick
Independent
Test just 1 behaviour in isolation
Tip: Use mock objects to make it faster and not to be bothered by external dependencies eg. the web service going down. The popular ones are Moq and nSubstitute

Atlassian: Unit tests are very low level and close to the source of an application. They consist in testing individual methods and functions of the classes, components, or modules used by your software. Unit tests are generally quite cheap to automate and can run very quickly by a continuous integration server.

Other: This test ensures that the code developed in each component works efficiently as expected. In unit testing, developers care strictly and only about the interface and specifications of the particular component.

You can test each unit of code individually. You can also move on to the next unit of the component. In addition, the process also helps document the development of each unit code. A unit test is so essential that without it, functional tests will face many problems.

For example, a developer creates a calculator application. A unit test would check if the user can enter two numbers and receive the correct answer for sum. Separate unit tests would verify other features of the calculator, such as subtraction, multiplication, and division.

Other: Unit testing is a type of software testing which is done on an individual unit or component to test its corrections. Typically, Unit testing is done by the developer at the application development phase. Each unit in unit testing can be viewed as a method, function, procedure, or object. Developers often use test automation tools such as NUnit, Xunit, JUnit for the test execution.

Unit testing is important because we can find more defects at the unit test level.

For example, there is a simple calculator application. The developer can write the unit test to check if the user can enter two numbers and get the correct sum for addition functionality.

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