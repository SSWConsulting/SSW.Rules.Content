---
type: rule
title: Do you know the best Unit Testing framework?
uri: the-best-unit-testing-framework
authors:
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
related: []
redirects:
  - do-you-know-the-best-unit-testing-framework
created: 2017-02-02T18:12:03.000Z
archivedreason: Content is outdated, current unit testing framework options can
  be found in
  [https://www.ssw.com.au/rules/testing-tools](/testing-tools)
guid: 0afc7db0-4f87-4dd9-983d-3f4ebca4fce1
---

When getting started with unit testing, it is important to use the right tools for the job.

<!--endintro-->

::: bad  
![Bad Example: MS Test was the default testing library for previous versions of .NET and Visual Studio but lacked many features that were available in more complete tools like NUnit](bestunittest-bad1.png)  
:::

::: ok
OK Example: NUnit - For previous versions of .NET, NUnit was the best testing library but required work on the Continuous Integration server to get the unit tests to run in a CI environment. One of the key features that NUnit had that MS Test didn't was the TestCase attribute that allows you to specify inline data to be used when invoking that test
:::

::: good  
Good Example: XUnit comes out of the box with .NET Core and includes most of the great features of NUnit, while also being supported out of the box with Team Foundation Server and Visual Studio Team Services
:::
