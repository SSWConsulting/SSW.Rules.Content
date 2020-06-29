---
type: rule
title: Do you run Unit Tests in Visual Studio?
uri: do-you-run-unit-tests-in-visual-studio
created: 2020-03-12T20:14:02.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> When you build the test project, the tests appear in Test Explorer. If Test Explorer is not visible, choose Test on the Visual Studio menu, choose Windows, and then choose Test Explorer.<br> </span>

​<dl class="image"><dt><img src="test-explorer.jpg" alt="test-explorer.jpg" /></dt>
<dd>Figure&#58; Test Explorer</dd></dl><p>As you run, write, and rerun your tests, Test Explorer displays the results in default groups of Failed Tests, Passed Tests, Skipped Tests and Not Run Tests. You can change the way Test Explorer groups your tests.<br>You can perform much of the work of finding, organizing and running tests from the Test Explorer toolbar.<br></p><dl class="image"><dt><img src="run-tests.jpg" alt="run-tests.jpg" /></dt><dd>Figure&#58; Run Tests</dd></dl><p>You can run all the tests in the solution, all the tests in a group, or a set of tests that you select. Do one of the following&#58;</p><ul><li>To run all the tests in a solution, choose Run All</li><li>To run all the tests in a default group, choose Run... and then choose the group on the menu</li><li>Select the individual tests that you want to run, open the context menu for a selected test and then choose Run Selected Tests.</li></ul><p>The pass/fail bar at the top of the Test Explorer window is animated as the tests run. At the conclusion of the test run, the pass/fail bar turns green if all tests passed or turns red if any test failed.<br><br></p><p>Tip&#58; If you are using dotnet Core/5+&#160;you can do this from the terminal by running&#160;<i>dotnet test</i><br></p>


