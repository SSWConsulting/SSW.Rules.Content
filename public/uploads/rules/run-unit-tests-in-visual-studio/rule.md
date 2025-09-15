---
seoDescription: Run unit tests in Visual Studio by building your test project and exploring results in Test Explorer.
type: rule
title: Do you run Unit Tests in Visual Studio?
uri: run-unit-tests-in-visual-studio
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-run-unit-tests-in-visual-studio
created: 2020-03-12T20:14:02.000Z
archivedreason: null
guid: b606067f-d978-4b03-8139-03bf1b5b9921
---

When you build the test project in Visual Studio, the tests appear in Test Explorer. If Test Explorer is not visible, choose Test | Windows | Test Explorer.

<!--endintro-->

![Figure: Test Explorer in Visual Studio](vs-test-explorer.jpg "Screenshot of the Test Explorer in Visual Studio")

As you run, write, and rerun your tests, the Test Explorer displays the results in a default grouping of **Project**, **Namespace**, and **Class**. You can change the way the Test Explorer groups your tests.

You can perform much of the work of finding, organizing and running tests from the **Test Explorer** toolbar.

![Figure: Use the Test Explorer toolbar to find, organize and run tests](test-explorer-toolbar.jpg "Screenshot of the Test Explorer toolbar in Visual Studio")

You can run all the tests in the solution, all the tests in a group, or a set of tests that you select:

- To run all the tests in a solution, choose Run All
- To run all the tests in a default group, choose Run and then choose the group on the menu
- Select the individual tests that you want to run, open the context menu for a selected test and then choose Run Selected Tests.

:::greybox
**Tip:** If individual tests have no dependencies that prevent them from being run in any order, turn on parallel test execution in the settings menu of the toolbar. This can noticeably reduce the time taken to run all the tests.
![Figure: turn on "Run Tests In Parallel" to reduce the elapsed time to run all the tests](test-explorer-parallel-runs.jpg "Screenshot of enabling parallel test runs in Visual Studio")
:::
As you run, write and rerun your tests, Test Explorer displays the results in groups of Failed Tests, Passed Tests, Skipped Tests and Not Run Tests. The details pane at the bottom or side of the Test Explorer displays a summary of the test run.

:::greybox

**Tip:** If you are using dotnet Core/5+, you can run tests from the command line by running _dotnet test_
:::
