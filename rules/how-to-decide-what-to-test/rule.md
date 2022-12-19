---
type: rule
title: Do you know how to decide what to test?
uri: how-to-decide-what-to-test
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
related:
  - know-when-you-have-found-a-problem
  - what-is-exploratory-testing
  - risk-based-testing
created: 2022-12-08T00:05:15.114Z
guid: 22353d13-869b-48b5-b775-a8a872167c24

---

While user stories should have good [acceptance criteria](/acceptance-criteria), checking that these criteria are met is really just the starting point before engaging in deeper testing.

Without detailed test cases, it can be difficult to work out what to test outside of the acceptance criteria. Using test ideas and heuristics to come up with these ideas are important skills for good [exploratory testing](/what-is-exploratory-testing).
            
<!--endintro-->

Taking an exploratory approach to testing gives testers more freedom to choose what to test and how to test, but they can then find it hard to decide what to test.

It's helpful to think in terms of **test ideas**.

### Test ideas

> Test ideas are brief notions about something that could be tested - Rikard Edgren

> Test idea: an idea for testing something - James Bach

When tasked with testing something new, you don't necessarily know how to unearth interesting test ideas and so following rules probably doesn't help. 

Under such conditions of uncertainty (which are normal in software development), look for methods or ways of coming up with test ideas that might work, while acknowledging that they might not - these are **heuristics**.

### Heuristics

::: greybox
A heuristic is a fallible method for solving a problem or making a decision.

A heuristic is an experience-based technique for problem solving, learning and discovery.
:::

> A heuristic is a way to help me come up with test ideas - Lee Hawkins

You'll likely build up your own toolbox of heuristics to draw from as you become more familiar with them and realise their power. 

### Getting started - consistency heuristics

To get started with the use of heuristics, try some **consistency heuristics**. A great example comes from Michael Bolton in the form of [HICCUPPS](https://developsense.com/blog/2012/07/few-hiccupps), which is a mnemonic as follows:

* **H**istory. We expect the present version of the system to be consistent with past versions of it.
* **I**mage. We expect the system to be consistent with an image that the organization wants to project, with its brand or with its reputation.
* **C**omparable Products. We expect the system to be consistent with systems that are in some way comparable. This includes other products in the same product line; competitive products, services, or systems; or products that are not in the same category but which process the same data; or alternative processes or algorithms.
* **C**laims. We expect the system to be consistent with things important people say about it, whether in writing (references, specifications, design documents, manuals, whiteboard sketches, etc.) or in conversation (meetings, public announcements, lunchroom conversations, etc.).
* **U**sers' Desires. We believe that the system should be consistent with ideas about what reasonable users might want. 
* **P**roduct. We expect each element of the system (or product) to be consistent with comparable elements in the same system.
* **P**urpose. We expect the system to be consistent with the explicit and implicit uses to which people might put it.
* **S**tatutes. We expect a system to be consistent with laws or regulations that are relevant to the product or its use.

As an example of using the "Product" part of this heuristic, note that in Trello, there is an inconsistency in the way fields on cards can be edited. Clicking in the Description or Tasks fields puts the field straight into Edit mode, whereas to edit a Comment requires an explicit click on the "Edit" action. This is a case of the Trello product being inconsistent with itself in terms of editing fields on a card.

### Further reading

* [Cultivate your Credibility with Oracles and Heuristics](https://www.ministryoftesting.com/dojo/lessons/cultivate-your-credibility-with-oracles-and-heuristics) by Lee Hawkins
