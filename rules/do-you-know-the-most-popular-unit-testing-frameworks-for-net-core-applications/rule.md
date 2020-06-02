---
type: rule
archivedreason: 
title: Do you know the most popular unit testing frameworks for .NET Core applications?
guid: c7465c5f-45be-4185-ade6-836ff4d6b633
uri: do-you-know-the-most-popular-unit-testing-frameworks-for-net-core-applications
created: 2020-03-16T20:05:20.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 81
  title: Jason Taylor
related: []

---


There are three main frameworks to add unit testing. The good news is that they are all acceptable choices&#58;<ul><li>They all have test runner packages for running tests directly from Visual Studio<br></li><li>They all have console-based runners that can runs tests as part of a CI/CD pipeline</li><li>They differ slightly in syntax and feature set<br></li></ul>
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3">​NUnit​​<br></h3><p class="ssw15-rteElement-P">The <a href="https&#58;//github.com/nunit/docs">NUnit</a> project deserves recognition for being the first powerful and open source unit test framework for the .NET universe – and it’s still a solid choice today. Because&#160;NUnit has an open-source .NET&#160;UI control for running tests, NUnit is still SSW’s preferred choice for embedding unit tests and a runner UI inside a windows application.<br></p><h3 class="ssw15-rteElement-H3">xUnit.net – <span class="ssw15-rteStyle-Highlight">(Recommended)</span>​​<br></h3><p class="ssw15-rteElement-P"><a href="https&#58;//xunit.net/">xUnit.net</a> is a newer framework – written by the original creator of NUnit v2 to create a more opinionated and restrictive framework to encourage TDD best practice. For example, when running xUnit tests, the class containing the test methods is instantiated separately for each test so that tests cannot share data and​​​ can run in parallel.<br></p><p class="ssw15-rteElement-P">xUnit.net is currently the most popular framework - and is ​​even used by the .NET&#160;Core team.&#160;</p><p class="ssw15-rteElement-P">xUnit.net is the default choice for .NET&#160;Core web applications and APIs at SSW.<br></p><h3 class="ssw15-rteElement-H3">MSTest​<br></h3><p class="ssw15-rteElement-P"><a href="https&#58;//docs.microsoft.com/en-us/visualstudio/test/getting-started-with-unit-testing">MSTest&#160;​</a>is Microsoft's testing framework. In the past this was a poor choice as although this was the easiest framework to run from Visual Studio, it was extremely difficult to automate these tests from CI/CD build servers. These problems have been completely solved with .NET&#160;Core but for most C# developers this is “too little, too late” and the other unit testing frameworks are now more popular.<br><br></p>


