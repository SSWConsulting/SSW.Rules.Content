---
type: rule
title: Do you take a risk-based approach to test planning?
uri: risk-based-testing
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
related:
  - complete-testing-is-impossible
created: 2022-10-13T23:36:34.812Z
guid: d252b9eb-0edc-40a1-80ca-b4eb13ad508a
---
We know that [complete testing is impossible](https://www.ssw.com.au/rules/complete-testing-is-impossible) so how do we decide which finite set of tests to perform out of the infinite cloud of possible tests for a story, feature or release?

This problem can seem overwhelming, but focusing on risk is a good approach. Let's look at the idea of risk-based testing.

<!--endintro-->

### What is risk-based testing?

Before we 
Risk-based testing uses an analysis of quality risks to prioritize tests and allocate testing effort

what is risk? And quality risk?
Risk: the possibility of a negative or undesirable event or
outcome
JB: Risk is a problem that might happen
Quality risk: the possibility that the product or system might fail to deliver one or more of the key quality attributes endangering our ability to achieve the quality attributes, endangering our ability to achieve the quality
outcomes we want

### How does a risk-based approach help with test planning?

Risk-based testing delivers the following benefits:

* Find the scary stuff first\
Running the tests in risk order gives the highest likelihood of discovering problems in severity order

* Pick the right tests out of the infinite cloud of possible tests\
Allocating test effort based on risk is the most efficient way to minimize the residual quality risk upon release
* Release when risk of delay balances risk of dissatisfaction\
Measuring test results based on risk allows the organisation to know the residual level of quality risk during test execution and to make smart release decisions

* Give up tests you worry about the least\
If the schedule requires it, dropping tests in reverse risk order reduces the test execution period with the least possible increase in quality risk.


These benefits allow testing to be more efficient and targeted, especially in time and/or resource constrained situations (which is pretty much always the case!).




### Resources

Rex Black: lots of articles, examples, templates, etc. at [rbcs-us.com/resources/category/risk-based](https://rbcs-us.com/resources/category/risk-based) (go here first: [Risk-based Testing: What It Is & How You Can Benefit](https://rbcs-us.com/resources/articles/risk-based-testing-what-it-is-and-how-you-can-benefit/))

James Bach: [Heuristic Risk-based Testing](http://www.satisfice.com/articles/hrbt.pdf)

David Greenlees: [Awareness of Risk Identification in Software Testing](http://www.stickyminds.com/article/awareness-risk-identification-software-testing)

**Add your rule to a category**