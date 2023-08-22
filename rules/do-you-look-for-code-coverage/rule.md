---
type: rule
title: Do you look for Code Coverage?
uri: do-you-look-for-code-coverage
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
  - title: Eric Phan
    url: https://ssw.com.au/people/eric-phan
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
related: []
redirects: []
created: 2012-04-01T11:02:56.000Z
archivedreason: null
guid: 53991e69-caae-4515-be83-2fc2b23202bc
---

Code Coverage shows how much of your code is covered by tests and can be a useful tool for showing how effective your unit testing strategy is. However, it should be looked at with caution.

<!--endintro-->

* You should focus on  **quality** not  **\*quantity\*** of tests.
* You should write tests for fragile code first and not waste time testing trivial methods
* Remember the 80-20 rule - a very high-test coverage is a noble goal but there are diminishing returns.
* If you're modifying code, write the test first, then change the code, then run the test to make sure it passes (AKA red-green-refactor).
* You should run your tests regularly (see [Do you follow a Test Driven Process](/before-starting-do-you-follow-a-test-driven-process)). Ideally, they'll be part of your build (see [Do you know the minimum builds to create for your project?](/do-you-know-the-minimum-builds-to-create-for-your-project)

![Figure: Code Coverage metrics in Visual Studio. This solution has a very high code coverage percentage (around 80% on average)](CodeCoverage2010.png)  

**Tip:** [Do you use Live Unit Testing to see code coverage?](/use-live-unit-testing-to-see-code-coverage)
