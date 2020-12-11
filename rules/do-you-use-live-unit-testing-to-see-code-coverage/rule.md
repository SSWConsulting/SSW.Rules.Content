---
type: rule
archivedreason: 
title: Do you use Live Unit Testing to see code coverage?
guid: 7cb53405-eee4-4181-9f61-b7253ce9221d
uri: do-you-use-live-unit-testing-to-see-code-coverage
created: 2020-03-12T23:43:11.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

Visual Studio 2017 introduces a new feature called Live Unit Testing. This gives the developer insight into code coverage of the file that they are working on, so they can quickly and easily see if there’s a unit test that covers the code they are working on.

<!--endintro-->
<dl class="image">&lt;dt&gt;<img src="lut-codecoverage1.jpg" alt="lut-codecoverage1.jpg">&lt;/dt&gt;<dd>Figure: Enable it by selecting Test | Live Unit Testing | Start</dd></dl><dl class="badImage">&lt;dt&gt;<img src="lut-codecoverage2.jpg" alt="lut-codecoverage2.jpg">&lt;/dt&gt;<dd>Figure: Bad Example – This method isn't covered by any unit tests, so the developer should consider writing a unit test for it</dd></dl><dl class="image">&lt;dt&gt;<img src="lut-codecoverage3.jpg" alt="lut-codecoverage3.jpg">&lt;/dt&gt;<dd>Figure: The developer can right click and create a test immediately</dd></dl><dl class="goodImage">&lt;dt&gt;<img src="lut-codecoverage4.jpg" alt="lut-codecoverage4.jpg">&lt;/dt&gt;<dd>Figure: Good Example – Developer can see that the code is covered by 2 passing tests and one failing test</dd></dl>
For more details see Joe Morris’s video on .NET Tooling Improvements Overview – Live Unit Testing:
