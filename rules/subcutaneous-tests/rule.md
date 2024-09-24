---
seoDescription: Subcutaneous tests, a type of integration testing that bypasses the UI, providing a more stable and efficient way to test your application's underlying behavior.
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

Automated UI testing tools like [Playwright](https://playwright.dev/) and [Selenium](https://www.selenium.dev/) are great for testing the real experience of the users. Unfortunately, these tests can sometimes feel a bit too fragile as they are very sensitive to changes made to the UI.

Subcutaneous ("just beneath the skin") tests look to solve this pain point by doing integration testing just below the UI.

<!--endintro-->

Martin Fowler was one of the first people to [introduce the concept of subcutaneous tests](https://martinfowler.com/bliki/SubcutaneousTest.html) into the mainstream, though it has failed to gather much momentum. Subcutaneous tests are great for solving problems where automated UI tests have difficulty interacting with the UI or struggle to manipulate the UI in the ways required for the tests we want to write.

Some of the key qualities of these tests are:

- They are written by developers (typically using the same framework as the unit tests)
- They can test the full underlying behaviour of your app, but bypass the UI
- They require business logic to be implemented in an API / middle layer and not in the UI
- They can be much easier to write than using technologies that drive a UI, e.g. Playwright or Selenium

The [Introduction To Subcutaneous Testing](https://www.ministryoftesting.com/dojo/lessons/introduction-to-subcutaneous-testing) by Melissa Eaden provides a good overview of this approach.

### Integrate with DevOps

The gold standard ⭐ is to automatically run subcutaneous tests inside your DevOps processes such as when you perform a Pull Request or a build. You can do this using [GitHub Actions](https://github.com/features/actions) or [Azure DevOps](https://azure.microsoft.com/en-au/services/devops/).

Every test should reset the database so you always know your resources are in a consistent state.

::: good
![Figure: Good example - Define your workflows in yml files and containerize your testing](githubactionyml.png)
:::

::: good
![Figure: Good example - Your tests can then run in your DevOps pipelines](githubpipeline.png)
:::

Jason Taylor has a fantastic example of Subcutaneous testing in his [Clean Architecture template](https://github.com/jasontaylordev/CleanArchitecture/tree/main/tests).
