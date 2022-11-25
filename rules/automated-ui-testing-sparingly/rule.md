---
type: rule
title: Do you remember to use automated UI testing sparingly?
uri: automated-ui-testing-sparingly
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
created: 2022-11-24T05:16:00.941Z
guid: 6cbe4a66-f7c0-4e73-85a4-2346ed5334a6
---
The availability of so many automated UI testing frameworks and tools can lead teams to focus too heavily on automating their testing at the UI level. 

This is a classic illustration of [the law of the instrument or Maslow's hammer](https://en.wikipedia.org/wiki/Law_of_the_instrument), a cognitive bias that involves an over-reliance on a familiar tool. Abraham Maslow wrote in 1966, "If the only tool you have is a hammer, it is tempting to treat everything as if it were a nail."

![Figure: Remember that sometimes a drill is the tool you need, not a hammer](hammer-not-drill.jpg)

While automated UI testing has its place in an overall test strategy (involving both humans and automation), you need to exercise care about how much of your testing is performed at this level.

<!--endintro-->

The topmost layer of the pyramid is deliberately small and represents the small amount of end-to-end user interface-based automated checks that should be written and executed against the system. 

![Figure: Mike Cohn's automated test pyramid (2009)](test-pyramid-cohn.jpg)

Tests at the level of the UI most closely mimic user interaction with the software and are ideal for checking the most important customer workflows. 

However, testing at this level offers the slowest feedback (since interacting with the user interface is necessarily slower than interacting with smaller units of code within the system) and these checks are also the slowest to write. These tests are also very vulnerable to changes in the software's user interface and so are generally much less reliable than tests at lower levels (e.g. unit and service/API tests).

and less deterministic

attacking automation from the UI has been - and remains - an all too popular approach, often at the expense of higher value, lower cost alternatives lower down the pyramid.

There is always back-end functionality and business logic that is incredibly hard to “reach” via the user interface and internal infrastructure is nearly impossible to exercise/test via automation at this level. In a multi-tiered approach, you should be able to “reach” any behavior or functionality that the team deems to have value to automate rather than being hamstrung by the reach of the user interface.

**Add Pros and cons, with green tick and red cross icons**

**Add your rule to a category**

related
https://www.ssw.com.au/rules/why-testing-cannot-be-completely-automated
https://www.ssw.com.au/rules/different-types-of-testing