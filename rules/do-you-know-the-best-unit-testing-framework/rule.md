---
type: rule
title: Do you know the best Unit Testing framework?
uri: do-you-know-the-best-unit-testing-framework
created: 2017-02-02T18:12:03.0000000Z
authors:
- id: 24
  title: Adam Stephensen

---



<span class='intro'> When getting started with unit testing, it is important to use the right tools for the job.​<br> </span>

<dl class="badImage"><dt><img src="/PublishingImages/bestunittest-bad1.png" alt="bestunittest-bad1.png" /></dt><dt><img src="/PublishingImages/bestunittest-bad1.png" alt="bestunittest-bad2.png" /></dt><dd>Bad Example&#58; MS Test was the default testing library for previous versions of .NET and Visual Studio but lacked many features that were available in more complete tools like NUnit<br></dd></dl><dl class="image"><dt><img src="/PublishingImages/bestunittest-bad1.png" alt="bestunittest-ok1.png" /></dt><dt><img src="/PublishingImages/bestunittest-bad1.png" alt="bestunittest-ok2.png" /></dt><dd>OK Example&#58; NUnit - For previous versions of .NET, NUnit was the best testing library but required work on the Continuous Integration server to get the unit tests to run in a CI environment. One of the key features that NUnit had that MS Test didn't was the TestCase attribute that allows you to specify inline data to be used when invoking that test<br></dd></dl> <dl class="goodImage"> <dt><img src="/PublishingImages/bestunittest-bad1.png" alt="bestunittest-good1.png" /></dt><dt><img src="/PublishingImages/bestunittest-bad1.png" alt="bestunittest-good2.png" /></dt><dd>Good Example&#58; XUnit comes out of the box with .NET Core and includes most of the great features of NUnit, while also being supported out of the box with Team Foundation Server and Visual Studio Team Services <br></dd></dl>


