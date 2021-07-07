---
type: rule
archivedreason: 
title: Do you use Live Unit Testing to see code coverage?
guid: 7cb53405-eee4-4181-9f61-b7253ce9221d
uri: use-live-unit-testing-to-see-code-coverage
created: 2020-03-12T23:43:11.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-use-live-unit-testing-to-see-code-coverage

---

Visual Studio 2017 introduces a new feature called Live Unit Testing. This gives the developer insight into code coverage of the file that they are working on, so they can quickly and easily see if there’s a unit test that covers the code they are working on.

<!--endintro-->

![Figure: Enable it by selecting Test | Live Unit Testing | Start](lut-codecoverage1.jpg)  


::: bad  
![Figure: Bad Example – This method isn't covered by any unit tests, so the developer should consider writing a unit test for it](lut-codecoverage2.jpg)  
:::

![Figure: The developer can right click and create a test immediately](lut-codecoverage3.jpg)  


::: good  
![Figure: Good Example – Developer can see that the code is covered by 2 passing tests and one failing test](lut-codecoverage4.jpg)  
:::

For more details see Joe Morris’s video on [.NET Tooling Improvements Overview – Live Unit Testing](https://channel9.msdn.com/Events/Connect/2016/171)
