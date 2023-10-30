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

We know that [complete testing is impossible](/complete-testing-is-impossible) so how do we decide which finite set of tests to perform out of the infinite cloud of possible tests for a story, feature or release?

This problem can seem overwhelming, but focusing on risk is a good approach so let's look at risk-based testing.

<!--endintro-->

### What is risk-based testing?

Think of risk as the possibility of a negative or undesirable event or outcome; **a risk is a problem that *might* happen**.

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

Identifying quality risks is the first step in making use of a risk-based approach to testing. 

Risk analysis workshops are a good way to involve different stakeholders in this process and you can drive these workshops in at least a couple of different ways:

* Begin with details about the situation and identify risks associated with them. With this approach, you study the software and repeatedly ask yourself "What could go wrong here?"
* Begin with a set of potential risks and match them to the details of the situation. With this approach, you consult a predefined list of risks and determine whether they apply here and now. These risk lists could be in the form of a set of Quality Criteria categories, generic risk lists or risk catalogues.

::: greybox
**Tip:** Start with a simple approach to your risk analysis, then become more advanced as your teams become more familiar with the risk-based approach

**Tip:** Try to gather diverse opinions about risk. Technical folks will likely identify different types of risk to business stakeholders, while testers will bring yet another perspective.
:::

#### Order the risks

After identifying quality risks, the next job is to order them. 

Consider the **likelihood** and **impact** of each risk as a simple way to perform this ordering exercise. So a risk that seems quite likely to eventuate and would result in significant impact to all of your users would rank higher than one that is less likely to happen or would only cause problems for a small number of users.

#### Prioritize testing based on the risks

Formulate your test plans to address the highest risks first, to ensure that you're covering the riskiest stuff first and increasing the chances of finding the most important problems earlier rather than later.

### Resources

- Rex Black: [Risk-based Testing: What It Is & How You Can Benefit](https://drive.google.com/file/d/108dLBHVbYCvA1_y2cIDKjIXQj3B9AEnj/view?usp=sharing)\
See more [resources for “Risk Based”](https://www.rexblack.com/templates-and-examples) (testing articles, examples, templates, etc.)

- James Bach: [Heuristic Risk-based Testing](http://www.satisfice.com/articles/hrbt.pdf)

- David Greenlees: [Awareness of Risk Identification in Software Testing](http://www.stickyminds.com/article/awareness-risk-identification-software-testing)
