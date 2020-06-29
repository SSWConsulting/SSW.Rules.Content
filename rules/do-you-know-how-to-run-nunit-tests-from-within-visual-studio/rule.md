---
type: rule
title: Do you know how to run nUnit tests from within Visual Studio?
uri: do-you-know-how-to-run-nunit-tests-from-within-visual-studio
created: 2020-03-12T22:45:00.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <h3 class="ssw15-rteElement-H3">Option 1&#58; External tool (not recommended)​<br></h3><p>Using NUnit with Visual Studio&#58; To make it easy to use, you need to add it as an external tool in Visual Studio.</p><p>In Visual Studio&#58;</p><ol><li>Go to Tools &gt; External Tools</li><li>Click &quot;Add&quot; button</li><li>Type in&#58;</li></ol><ul><li>Title&#58; NUnit GUI</li><li>Command&#58; Location of nUnit.exe file</li><li>Argument&#58; /run (so that the tests run automatically when started)</li><li>Initial Directory&#58; $(Target directory)<br></li></ul> </span>

<dl class="badImage"><dt>​<img src="./NUnitInVStudio.jpg" alt="NUnitInVStudio.jpg" /></dt><dd>Figure&#58; Bad Example - NUnit In Visual Studio</dd></dl><h3 class="ssw15-rteElement-H3">Option 2&#58; Test Driven .net​​<br></h3><p>TestDriven.net has better NUnit integration – from both code and Solution Explorer windows.</p><dl class="image"><dt><img src="./UseTestDriven.jpg" alt="UseTestDriven.jpg" /></dt><dd>Figure&#58; Better way - Use TestDriven.Net - it has a 'Run Test(s)' command for a single test (above) or...</dd></dl><dl class="image"><dt><img src="./GUIBringUpAction.jpg" alt="GUIBringUpAction.jpg" /></dt><dd>Figure&#58; ...you can right-click on a project and select 'Test With &gt; NUnit' to bring up the GUI. It is certainly more convenient</dd></dl><p>​To run unit testing&#58; Tools &gt; NUnit GUI to launch NUnit and run the tests.</p><h3 class="ssw15-rteElement-H3">Option 3&#58; Other Tools​<br></h3><p>Other Visual Studio tools including Resharper and Coderush have their own integration with NUnit. If you’re already using one of these, installing TestDriven.net is unnecessary.<br></p>


