---
type: rule
archivedreason: 
title: Do you know Microsoft’s recommended frameworks for Automated UI-driven Functional Testing?
guid: 43f325c4-b3f0-4867-9df2-abc9211868db
uri: do-you-know-microsofts-recommended-frameworks-for-automated-ui-driven-functional-testing
created: 2020-03-16T19:59:09.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 34
  title: Brendan Richards
- id: 81
  title: Jason Taylor
related: []

---

This type of testing runs the whole application and uses tools to interact with the application in the same way that a user would – such as clicking buttons or entering text into an input field.


This type of testing is powerful as it tests the entire application, including the UI, and is especially useful for mission-critical pathways such as a shopping cart checkout process.

The downside of this type of test is that it can be complex to write and that the tests can sometimes be brittle – small changes to the UI can break your tests.
Because these tests run on top of your UI, the type of UI drives the choice of the testing framework.




<!--endintro-->

### Coded UI Tests – Deprecated


Visual Studio 2019 will be the last version of visual studio that supports coded UI tests so this should only be considered if you already have significant investment in existing coded UI tests.

Coded UI tests could test Web, Winforms, WPF and Silverlight applications.

### Web Applications: Selenium

Selenium works by automating control of a web browser and running it against a deployed website. It is the recommended approach for testing web applications.

### Desktop and UWP: Appium with WinAppDriver

The Windows Application driver installs a service onto a Windows 10 machine. This service allows you to write test scripts that can launch and interact with windows applications.

### Android and IOS: Xamarin.UITest


Xamarin.UITest runs on top of the NUnit unit test framework and can test mobile applications. It integrates tightly with Xamarin.iOS and Xamarin.Android projects to test Xamarin-based apps but can also test native applications.
