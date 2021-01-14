---
type: rule
archivedreason: 
title: Do you know the best Unit Testing framework?
guid: 0afc7db0-4f87-4dd9-983d-3f4ebca4fce1
uri: do-you-know-the-best-unit-testing-framework
created: 2017-02-02T18:12:03.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects:
- the-best-unit-testing-framework

---

When getting started with unit testing, it is important to use the right tools for the job.

<!--endintro-->


::: bad  
![](bestunittest-bad1.png)  
:::
![bestunittest-bad2.png](bestunittest-bad1.png)

::: bad  
![Bad Example: MS Test was the default testing library for previous versions of .NET and Visual Studio but lacked many features that were available in more complete tools like NUnit](bestunittest-bad1.png)  
:::


::: ok  
![](bestunittest-bad1.png)  
:::
![bestunittest-ok2.png](bestunittest-bad1.png)

::: ok  
![OK Example: NUnit - For previous versions of .NET, NUnit was the best testing library but required work on the Continuous Integration server to get the unit tests to run in a CI environment. One of the key features that NUnit had that MS Test didn't was the TestCase attribute that allows you to specify inline data to be used when invoking that test](bestunittest-bad1.png)  
:::


::: good  
![](bestunittest-bad1.png)  
:::
![bestunittest-good2.png](bestunittest-bad1.png)

::: good  
![Good Example: XUnit comes out of the box with .NET Core and includes most of the great features of NUnit, while also being supported out of the box with Team Foundation Server and Visual Studio Team Services](bestunittest-bad1.png)  
:::
