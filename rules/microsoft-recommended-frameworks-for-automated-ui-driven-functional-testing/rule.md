---
type: rule
archivedreason: 
title: Do you know Microsoft’s recommended frameworks for Automated UI-driven Functional Testing?
guid: 43f325c4-b3f0-4867-9df2-abc9211868db
uri: microsoft-recommended-frameworks-for-automated-ui-driven-functional-testing
created: 2020-03-16T19:59:09.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
- title: Jason Taylor
  url: https://ssw.com.au/people/jason-taylor
related: []
redirects:
- do-you-know-microsofts-recommended-frameworks-for-automated-ui-driven-functional-testing
- do-you-know-microsoft’s-recommended-frameworks-for-automated-ui-driven-functional-testing

---


<p class="ssw15-rteElement-P">This type of testing runs the whole&#160;application and uses tools to interact with the application in the same way that a user would – such as clicking buttons or entering text into an input field.<br></p><div><p class="ssw15-rteElement-P">This type of testing is powerful as it tests the entire application, including the UI,&#160;and is especially useful for mission-critical pathways such as a shopping cart checkout process.<br></p><p class="ssw15-rteElement-P">The downside of this type of test is that it can be complex to write and that the tests can sometimes be brittle – small changes to the UI can break your tests.<br></p>Because these tests run on top of your UI, the type of UI drives the choice of the testing framework.<br><br><br></div>
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3">​Coded UI Tests – Deprecated​​<br></h3><p class="ssw15-rteElement-P">Visual Studio 2019 will be the last version of visual studio that supports coded UI tests so this should only be considered if you already have significant investment in existing coded UI tests.​<br></p><p class="ssw15-rteElement-P">Coded UI tests could test Web, Winforms, WPF and Silverlight applications.​<br></p><h3 class="ssw15-rteElement-H3">​​Web Applications&#58; Selenium</h3><p class="ssw15-rteElement-P">Selenium works by automating control of a web browser and running it against a deployed website. It is the recommended approach for testing web applications.<br></p><h3 class="ssw15-rteElement-H3">​​Desktop and UWP&#58; Appium with WinAppDriver</h3><p>The Windows Application driver installs a service onto a Windows 10 machine. This service allows you to write test scripts that can launch and interact with windows applications.<br></p><h3 class="ssw15-rteElement-H3">Android and IOS&#58; Xam​​arin.UITest​​<br></h3><p>Xamarin.UITest runs on top of the NUnit unit test framework and can test mobile applications. It inte​grates tightly with Xamarin.iOS and Xamarin.Android projects to test Xamarin-based apps but can also test native applications.<br>​<br></p>


