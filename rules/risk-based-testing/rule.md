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

This problem can seem overwhelming, but focusing on risk is a good approach so let's look at risk-based testing.

<!--endintro-->

### What is risk-based testing?

Think of risk as the possibility of a negative or undesirable event or outcome; **a risk is a problem that might happen**.


Quality risk is the possibility that the software might fail to deliver one or more of its key quality attributes, e.g. reliability, usability, performance, capability, etc.

::: greybox
Risk-based testing uses an analysis of quality risks to prioritize tests and allocate testing effort
::: 

### How does a risk-based approach help with test planning?

Risk-based testing delivers the following benefits:

* Find the scariest problems first\
Running the tests in risk order gives the highest likelihood of discovering problems in severity order, so we find the most important problems first.


* Pick the right tests out of the infinite cloud of possible tests\
Allocating test effort based on risk is the most efficient way to minimize the residual quality risk upon release.

* Release when risk of delay balances risk of dissatisfaction\
Measuring test results based on risk allows the organisation to know the residual level of quality risk during test execution and to make smarter release decisions.


* Give up tests you worry about the least\
If the schedule requires it, dropping tests in reverse risk order reduces the test execution period with the least possible increase in quality risk.


These benefits allow testing to be more efficient and targeted, especially in time and/or resource constrained situations (which is pretty much always the case!).

### Putting risk-based testing into practice

The concept of risk-based testing is straightforward and you can put it into practice easily - by starting simple!

#### Identify risks

**TODO**
risk analysis workshops
risk lists, etc.

::: greybox
**Tip:** Start with a simple approach to your risk analysis, then become more advanced as your teams become more familiar with the risk-based approach

**Tip:** diverse opinions, tech/biz/test
:::

#### Prioritise testing based on the risks

**TODO** sadas




### Resources

Rex Black: lots of risk-based testing articles, examples, templates, etc. at [rbcs-us.com/resources/category/risk-based](https://rbcs-us.com/resources/category/risk-based) (go here first: [Risk-based Testing: What It Is & How You Can Benefit](https://rbcs-us.com/resources/articles/risk-based-testing-what-it-is-and-how-you-can-benefit/))

James Bach: [Heuristic Risk-based Testing](http://www.satisfice.com/articles/hrbt.pdf)

David Greenlees: [Awareness of Risk Identification in Software Testing](http://www.stickyminds.com/article/awareness-risk-identification-software-testing)

**Add your rule to a category**