---
seoDescription: Reduce the risk of bugs and costly fixes by building a solid foundation of unit tests, double-checking core logic with each compile.
type: rule
title: Do you know why unit tests are important?
uri: why-unit-tests-are-important
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related:
  - important-documents-to-get-started-on-unit-testing
redirects:
  - do-you-know-why-tests-are-important
  - why-tests-are-important
created: 2020-03-11T16:00:41.000Z
archivedreason: null
guid: e72daf98-e2f2-4d09-8e35-254e37018ebb
---

Customers get cranky when developers make a change which causes a bug to pop up somewhere else. One way to reduce the risk of such bugs occurring is to build a solid foundation of [unit tests](https://en.wikipedia.org/wiki/Unit_testing).

<!--endintro-->

When writing code, one of the most time-consuming and frustrating parts of the process is finding that something you have changed has broken something you're not looking at. These bugs often don't get found for a long time, as they are not the focus of the "test please" and only get found later by clients.

Customers may also complain that they shouldn't have to pay for this new bug to be fixed. Although this is understandable, fixing bugs is a large part of the project and is always billable. However, if these bugs can be caught early, they are generally easier, quicker and cheaper to fix.

Unit tests double-check that your core logic is still working every time you compile, helping to minimize the number of bugs that get through your internal testing and end up being found by the client.

Think of this is a "Pay now, pay much less later" approach.
