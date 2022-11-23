---
type: rule
title: Do you know how to decide whether a test is a good candidate for automation?
uri: good-candidate-for-automation
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
related:
  - why-testing-cannot-be-completely-automated
  - what-is-exploratory-testing
  - different-types-of-testing
  - why-unit-tests-are-important
created: 2022-11-18T01:24:52.668Z
guid: 926270de-f1f2-4dad-8a0d-f076a431aba0
---
Automation can be an awesome part of a test strategy, but not all tests are good candidates to be automated.

While [all testing cannot be automated](https://www.ssw.com.au/rules/why-testing-cannot-be-completely-automated) due to the uniquely human skills that are required (e.g. exploration, learning, experimentation), it also doesn't make sense to try to automate all of the tests that could be automated.

Let's look at how to decide whether a test is a good candidate to be handed over to the machines.

![Figure: Making wise decisions about what to automate can prevent you wasting valuable time automating less valuable tests](automate-or-not.jpg)

<!--endintro-->

** See last section of http://katrinatester.blogspot.com/2015/11/testing-for-non-testers-pathway.html **

> If you try to "automate" bad testing, you’ll find yourself doing bad testing faster and worse than you've ever done it before.
>        - Michael Bolton

### ✅ Good candidates for automation

When deciding what to automate, there are certain attributes that make a test a good candidate to implement via automated means.

#### Unit tests

A solid foundation of reliable automated unit tests helps you to develop (and refactor) with more safety. Since unit tests are designed to be small in scope, they are fast to execute and so large numbers of unit tests can be run automatically as part of your CI/CD pipeline without introducing significant extra time to your build/deployment process. Unit tests are an ideal candidate for automation.

#### Repetitive tests that run for multiple builds

If you have particular types of tests that run across multiple builds, then they should be probably be automated. The repetitious nature of such tests makes it worthwhile to spend the time to automate them. API tests are a good example.

#### Smoke tests and tests covering the most common user workflows

Smoke testing is designed to verify that the critical functionality of the software is working, at a very high level. Smoke tests can be useful right after a new build is made to decide whether or not you can run deeper (and more expensive) tests, or right after a deployment to make sure that they application is running properly in the newly deployed environment. 

Given the high value of smoke tests and their repetitious nature, they are generally great candidates for automation. You might additionally consider automating some tests to cover the most commonly-used user workflows, so that you receive fast feedback of any breaking changes to these important workflows.

#### Tests of many different configurations, options or data sets

There are good benefits to be had, both in terms of time to execute and coverage, in automating tests where many different configurations, product options or data sets need to be tested. For example, the same automated test can be used to exercise a web application running across different browsers and/or devices.

#### Tests that are impractical or impossible for humans to perform

Scale/perf/etc

### Take care when deciding to automate these tests

blurb

#### Automating "manual" test cases

don't just take manual test cases and automate them

#### Automated test for every bug

auto test for every bug, some exceptions, e.g.
Some bugs are merely cosmetic and are unlikely to appear again. A good example of this is the typo. If a developer accidentally entered text that said “Contcat us” instead of “Contact us”, that was simply an oversight. No developer would ever go into the code and revert to the earlier misspelling, so there’s no need to automate a test that verifies that text.

#### What else is in this bucket?

todo

### ❌ Don't even think about automation for these tests

Some types of test just don't make sense to even try to automate:

* Exploratory tests
* User experience tests for usability
* Tests that will only need to be run once
* Tests for features that are in the early stages of development and are expected to go through many changes
* Tests of obscure edge cases (that are not shown to be prevalent in usage data)
* What else?

**Add your rule to a category**
add some relateds: unit tests, different types rule,