---
type: rule
archivedreason: 
title: Do you follow naming conventions for tests and test projects?
guid: 1aea50c6-b2cc-4e1e-a483-34b4776e0e1e
uri: do-you-follow-naming-conventions-for-tests-and-test-projects
created: 2020-03-24T00:04:10.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 34
  title: Brendan Richards
- id: 78
  title: Matt Wicks
related: []

---

### Test Projects


Tests typically live in separate projects – and you usually create a project from a template for your chosen test framework.
Because your test projects are startup projects (in that they can be independently started), they should target specific .NET runtimes and not just .NET Standard.
A unit test project usually targets a single code project.

### Project Naming


Integration and unit tests should be kept separate and should be named to clearly distinguish the two.
This is to make it easier to run only unit tests on your build server (and this should be possible as unit tests should have no external dependencies) 
Integration tests require dependencies and often won't run as part of your build process.  These should be automated later in the DevOps pipeline.

<!--endintro-->

### Test Project Location


Test projects can be located either:

* Directly next to the project under test – which makes them easy to find, or
* In a separate tests location – which makes it easier to deploy the application without tests included.

<dl class="badImage">&lt;dt&gt;
      <img src="clean-architecture-naming.png" alt="clean-architecture-naming.png">
   &lt;/dt&gt;<dd>Figure: In the above project, the tests are clearly placed in a separate location which makes it easy to deploy to production without them. It’s easy to tell which project is under test and what style of tests will be found in each test project. 
      <a href="https://github.com/jasontaylordev/CleanArchitecture">https://github.com/jasontaylordev/CleanArchitecture</a></dd></dl>
### Naming Conventions for Tests

There are a few “schools of thought” when it comes to naming the tests themselves. 
Internal consistency within a project is important.
It’s usually a bad idea to name tests after the class or method under test – as this naming can quickly get out-of-sync if you use refactoring tools – and one of the key benefits from unit testing is the confidence to refactor!
 
Remember that descriptive names are useful – but the choice of name is not the developer’s only opportunity to create readable tests.

* Write tests that are easy to read by following the three A's (Arrange, Act, and Assert)
* Use a good assertion library to make test failures informative (e.g. [Shouldly](https://github.com/shouldly/shouldly) or [FluentAssertions](https://fluentassertions.com/))
* Use comments and refer to bug reports to document the “why” when you have a test for a specific edge-case.
* Remember that the F12 shortcut will navigate from the body of your test straight to the method you’re calling.
* The point of a naming convention is to make code more readable, not less - so use your judgement and call in others to verify your readability.

<dl class="badImage">&lt;dt&gt;<img src="bad-naming.png" alt="bad-naming.png">&lt;/dt&gt;<dd>Figure: Bad Example - From the test explorer view you cannot tell what a test is meant to test from the name</dd></dl>
**[Method/PropertyName]\_Should\_[ExpectedBehavior]\_When\_[StateUnderTest]**
 **Figure: The "should" naming convention is effective – it encourages developers to clearly define the expected result upfront without requiring too much verbosity.** 
The following test names use the "should" naming convention:

**Withdraw\_Should\_ThrowException\_When\_InvalidAccountInfo** 

 **Checkout\_Should\_Add10Precent\_When\_CountryIsAustralia** 

 **Purchase\_Should\_Suceed\_When\_BalanceIsWithinCreditLimit**


::: good
Figure: Good Examples - Without looking at code, I know what the unit tests are trying to do

:::


A list of other suggested conventions can be found here: [7 Popular Unit Test Naming Conventions](https://dzone.com/articles/7-popular-unit-test-naming).
