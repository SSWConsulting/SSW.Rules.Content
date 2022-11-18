---
type: rule
title: Do you know how to decide whether a test is a good candidate for automation?
uri: good-candidate-for-automation
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
related:
  - why-testing-cannot-be-completely-automated
created: 2022-11-18T01:24:52.668Z
guid: 926270de-f1f2-4dad-8a0d-f076a431aba0
---
Automation can be an awesome part of a test strategy, but not all tests are good candidates to be automated.

While [all testing cannot be automated](https://www.ssw.com.au/rules/why-testing-cannot-be-completely-automated) due to the uniquely human skills that are required (e.g. exploration, learning, experimentation), it also doesn't make sense to try to automate all of the tests that could be automated.

Let's look at how to decide whether a test is a good candidate to be handed over to the machines.

![Figure: Making wise decisions about what to automate can prevent you wasting valuable time automating less valuable tests](automate-or-not.jpg)

<!--endintro-->

> If you try to "automate" bad testing, you’ll find yourself doing bad testing faster and worse than you've ever done it before.
>        - Michael Bolton

### Good candidates for automation

When deciding what to automate, there are certain attributes that make a test a good candidate to implement via automated means.

#### Unit tests

fdsfsd

#### Repetitive tests that run for multiple builds

dd

#### Smoke/most common user workflows

* TODO

#### Lots of configs/options

das

#### dd

SmartBear:

Repetitive tests that run for multiple builds.
Tests that tend to cause human error.
Tests that require multiple data sets.
Frequently used functionality that introduces high risk conditions.
Tests that are impossible to perform manually.

1. DO automate tasks as close to the code as possible
   Unit tests are so important because they exercise code functionality without touching any dependency. If a developer makes a change that results in a hole in logic, that hole will be detected before the change makes it to the tester, saving everyone valuable time. A popular trend today is TDD, or test-driven development. This is where the developer writes the unit tests before he or she writes the code, ensuring that they begin by thinking about all the possible use cases for the software before solving the technical challenges of writing the code.

Services tests are also extremely valuable because they test the functionality of the software without going through the UI. Many of today’s applications use APIs that make REST requests to the server. When going through the UI there are often limitations to what a user can do, but when going directly through the API more test cases can be executed. For example, a UI might limit the type of characters that can be entered in a form field, but there may not be server-side validation on the input, which could be discovered through API testing.

2. DO automate repetitive tasks
   Some tests are so important that they need to run repeatedly. A perfect example of this is the login test: if your users can’t log into the application, you have a real customer service problem! But no one wants to spend time manually logging into an application again and again. Automating your login test cases ensures that authentication is tested with a wide variety of users and accounts, both valid and invalid.
3. DO automate things users will do every day
   What is the primary function of your software?  What is the typical path that a user will take when using your software? These are the kinds of activities that should have automated test cases. Rather than running through a manual user path every morning, you can set your automated test to do it and you’ll be notified right away if there is a problem.  
4. DO automate basic smoke-level tests
   I like to think of smoke-level tests as tests of features that we would be really embarrassed by if they failed in the field. One company where I worked early in my career had a search feature that was broken for weeks, and no one noticed because we hadn’t run a test on it. Unfortunately, the bug was pushed out to production and seen by customers. Automating these tests and running them with every build can help catch major problems quickly.
5. DO automate things that will save you time
   A coworker of mine was testing a feature which needed a completely new account set up each time the test was run. Rather than set it up manually every time, he created automation that would set up a new account for him, saving him valuable time.
6. DO automate things that will allow you to exercise lots of different options
   A test that fills out a form by filling in all of the available fields is not completely testing the form. What if there is one missing field? What if there are two missing fields? What if one of those fields is required? With automation, you can exercise many different combinations of form submission in much less time than it would take to do manually.
7. DO automate things that will alert you when something is wrong
   I have several negative tests in my API test suites that verify that a user can’t do something when they don’t have permission to do it. Recently some of those tests failed, alerting me to the fact that someone had changed the permission structure, and now a user was able to view content they shouldn’t.

### Take care when deciding to automate these tests

don't just take manual test cases and automate them

### Don't even think about automation for these tests

Some types of test just don't make sense to even try to automate:

* Exploratory tests
* User experience tests for usability
* Tests that will only need to be run once
* What else?

8. DON’T automate test cases that you know will be flaky
   If you can’t come up with a way to run an automated test on a feature and have it pass consistently, you may want to run that test manually or find a different way to assert your results.  When I was first getting started with automation, I wanted to test that a feature sent an email and that the email was received. I discovered that email clients are tricky to test in the UI, because there’s no way of knowing how long it will take before the email is delivered. Instead, I verified that the email provider had sent the email, and occasionally did a manual check of the inbox to make sure that the email arrived.
9. DON’T automate test cases for features that are in the early stages and are expected to go through many changes
   It’s great to write unit tests for new code, which as mentioned above is usually done by the developer. And automated services tests can be created before there is a UI for a new feature. But if you know that your API endpoints or your UI will be changing quite a bit as the story progresses, you may want to hold off on services or UI automation until things have settled down a bit.  For the moment, manual testing will be your best strategy.
10. DON’T automate test cases for features that no one cares about
    Your application probably runs on a wide variety of browsers, and your inclination may be to run your tests on all of them. But it could be that only one percent of users are running your application on a certain browser. If that’s the case, why go through the stress of trying to run your tests on this browser?  Similarly, if there is a feature in your application that will be deprecated soon and only one percent of your users are using it, your time would probably be better spent automating another feature.
11. DON’T automate weird edge test cases
    There will always be bugs in software, but some will be more likely to be seen by users than others. You may be fascinated by the bug that is caused by going to a specific sequence of pages, entering non-UTF-8 characters, and then clicking the Back button three times in a row, but since it’s very unlikely that an end user will do this, it’s not worth your time to design an automated test for it.
12. DON’T automate bugs you are sure will never be seen again
    I once worked with someone who felt that every bug found needed a corresponding test. This is not always the case. Some bugs are merely cosmetic and are unlikely to appear again. A good example of this is the typo. If a developer accidentally entered text that said “Contcat us” instead of “Contact us”, that was simply an oversight. No developer would ever go into the code and revert to the earlier misspelling, so there’s no need to automate a test that verifies that text.

**Add your rule to a category**