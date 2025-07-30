---
seoDescription: Enable Live Unit Testing in Visual Studio to gain insight into test coverage and receive immediate feedback on code changes.
type: rule
title: Do you use Live Unit Testing to see code coverage?
uri: use-live-unit-testing-to-see-code-coverage
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-use-live-unit-testing-to-see-code-coverage
created: 2020-03-12T23:43:11.000Z
archivedreason: null
guid: 7cb53405-eee4-4181-9f61-b7253ce9221d
---

By enabling Live Unit Testing in a Visual Studio solution, you gain insight into the test coverage and the status of your tests.

Whenever you modify your code, Live Unit Testing dynamically executes your tests and immediately notifies you when your changes cause tests to fail, providing a fast feedback loop as you code.

:::greybox
**Note:** The Live Unit Testing feature requires Visual Studio Enterprise edition
:::

<!--endintro-->

To enable Live Unit Testing in Visual Studio, select Test | Live Unit Testing | Start

You can get more detailed information about test coverage and test results by selecting a particular code coverage icon in the code editor window:

![Figure: This code is covered by 3 unit tests, all of which passed](live-unit-testing-good.jpg "Screenshot of the Code Editor showing tests and their status against a method in Visual Studio")

::: greybox
**Tip:** If you find a method that isn't covered by _any_ unit tests, consider writing a unit test for it. You can simply right-click on the method and choose Create Unit Tests to add a unit test in context.
:::

For more details see [Joe Morris’s video on .NET Tooling Improvements Overview – Live Unit Testing](https://www.youtube.com/watch?v=kBlLi4BYCKk).
