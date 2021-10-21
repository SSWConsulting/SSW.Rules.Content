---
type: rule
title: Do you use subcutaneous tests?
uri: subcutaneous-tests
authors:
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
related:
  - the-different-types-of-test
  - automated-ui-testing
  - the-main-principles-of-clean-architecture
created: 2021-10-21T01:29:13.823Z
guid: 75b71400-ebae-4ae7-a65e-b4ac7aa6fba8
---
Automated-UI testing tools like [Playwright](https://playwright.dev/) are a great way to test the real experience of the users. Unfortunately, sometimes these tests can feel a bit too fragile. When that happens, Subcutaneous (aka just beneath the skin) tests look to solve this pain point by doing integration testing just below the UI.
            
<!--endintro-->

Martin Fowler was one of the first people to [introduce the concept of Subcutaneous tests](https://martinfowler.com/bliki/SubcutaneousTest.html) into the mainstream. Subcutaneous tests are great for solving problems where automated-UI tests struggle to manipulate the UI in the right way.

They are:
* Written by developers
* Test the full underlying behaviour of your app but bypasses the UI
* Requires business logic to be implemented in the API / middle layer and not in the UI.
* Tests can be much easier to write than using technologies that drive a UI

  e.g. Playwright

Jason Taylor has a fantastic example of Subcutaneous testing in his [Clean Architecture template](https://github.com/jasontaylordev/CleanArchitecture/tree/main/tests/Application.IntegrationTests)