---
seoDescription: Learn how to recognize software problems using oracles, heuristics, and specifications to enhance your credibility in bug reporting.
type: rule
title: Do you understand how you know when you’ve found a problem?
uri: know-when-you-have-found-a-problem
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
related:
  - how-to-decide-what-to-test
created: 2022-12-09T01:14:09.366Z
guid: a5ccbdf7-e3ce-4a50-a8cc-88f9d754376b
---
When asked how they spotted a problem, testers often say things like "based on my experience of the product" or "by comparing the product against the specification".

It's worth noting that users often find problems in your software without ever having seen a specification or user story!

So, how do you recognize when you've found a problem? The key concept here is the **oracle**.

<!--endintro-->

### Oracles

::: greybox
An oracle is a heuristic principle or mechanism by which someone recognizes a problem.
:::

Oracles are, by their nature, [heuristic](/how-to-decide-what-to-test). That is, oracles are fallible and context-dependent.

Oracles do not tell us conclusively that there is a problem; rather, they suggest that there may be a problem.
There can be no absolute oracle, so we use many.
Consistency is an important theme in oracles.

As an example, we can detect a bug when the product behaves in a way that is inconsistent with its specification or user story.

### An example oracle

The oracle here is the specification or user story and the problem is that the state of the product is not consistent with that oracle.

The problem might be caused by an out-of-date specification, a genuine bug in the product or something else – or there might actually be no problem at all!

::: greybox
**Tip**: Take the conscious step to understand which oracle you are using to spot a potential problem.

By doing this, you move away from personal opinion towards proof. This is a key step to enhancing your credibility in the eyes of your stakeholders.

Your bug reports are more credible when stakeholders clearly understand why you are claiming your observation to be a potential problem.
:::

### Further reading

* [Cultivate Your Credibility With Oracles And Heuristics](https://www.ministryoftesting.com/dojo/lessons/cultivate-your-credibility-with-oracles-and-heuristics) by Lee Hawkins
