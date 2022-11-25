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
The availability of so many great automated UI testing frameworks and tools can lead teams to focus too heavily on automating their testing at the UI level. 

This is a classic illustration of [the law of the instrument or Maslow's hammer](https://en.wikipedia.org/wiki/Law_of_the_instrument), a cognitive bias that involves an over-reliance on a familiar tool. Abraham Maslow wrote in 1966, "If the only tool you have is a hammer, it is tempting to treat everything as if it were a nail."

![Figure: Remember that sometimes a drill is the tool you need, not a hammer](hammer-not-drill.jpg)

While automated UI testing has its place in an overall test strategy (involving both humans and automation), you need to exercise care about how much of your testing is performed at this level.

<!--endintro-->

Explain why automation at the UI level needs to be used sparingly (slow, fragile, less deterministic, etc.) Reminder about using automation at lower levels (especially API). Detail some of the pros/cons of UI automation. 

Refer Test Pyramid
End-to-end tests (aka "UI tests" or "functional tests")

The topmost layer of the pyramid is deliberately small and represents the small amount of end-to-end user interface-based automated checks that should be written and executed against the system. Tests at this level most closely mimic user interaction with the application and are ideal for checking that core customer workflows are always checked. However, testing at this level offers the slowest feedback (since interacting with the user interface is necessarily slower than interacting with smaller units of code within the system) and these checks are also the slowest to write. These tests are also very vulnerable to changes in the system's user interface and so are generally much less reliable than tests lower down the pyramid.

On this topic, Cohn says "Suppose we wish to test a very simple calculator that allows a user to enter two integers, click either a multiply or divide button, and then see the result of that operation. To test this through the user interface, we would script a series of tests to drive the user interface, type the appropriate values into the fields, press the multiply or divide button, and then compare expected and actual values. Testing in this manner would certainly work but would be brittle, expensive, and time consuming. Additionally, testing an application this way is partially redundant—think about how many times a suite of tests like this will test the user interface. Each test case will invoke the code that connects the multiply or divide button to the code in the guts of the application that does the math. Each test case will also test the code that displays results. And so on. Testing through the user interface like this is expensive and should be minimized. Although there are many test cases that need to be invoked, not all need to be run through the user interface."

The responsibility for writing automated checks at the UI level has generally been given to testers or dedicated developers (with titles such as "automation engineers"), rather than the developers working on the application code itself. The majority of commercial (so-called) automated testing tools are focused towards leveraging the functional UI as the point of entry, so attacking automation from the UI has been - and remains - an all too popular approach, often at the expense of higher value, lower cost alternatives lower down the pyramid.

There is always back-end functionality and business logic that is incredibly hard to “reach” via the user interface and internal infrastructure is nearly impossible to exercise/test via automation at this level. In a multi-tiered approach, you should be able to “reach” any behavior or functionality that the team deems to have value to automate rather than being hamstrung by the reach of the user interface.



**Add your rule to a category**

related
https://www.ssw.com.au/rules/why-testing-cannot-be-completely-automated
https://www.ssw.com.au/rules/different-types-of-testing