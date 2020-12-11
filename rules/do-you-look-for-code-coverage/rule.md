---
type: rule
archivedreason: 
title: Do you look for Code Coverage?
guid: 53991e69-caae-4515-be83-2fc2b23202bc
uri: do-you-look-for-code-coverage
created: 2012-04-01T11:02:56.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 23
  title: Damian Brady
- id: 3
  title: Eric Phan
- id: 78
  title: Matt Wicks
related: []

---

Code Coverage shows how much of your code is covered by tests and can be a useful tool for showing how effective your unit testing strategy is.  However, it should be looked at with caution.

<!--endintro-->

* You should focus on  **\*quality\*** not  **\*quantity\*** of tests.
* You should write tests for fragile code first and not waste time testing trivial methods
* Remember the 80-20 rule - a very high-test coverage is a noble goal but there are diminishing returns.
* If you're modifying code, write the test first, then change the code, then run the test to make sure it passes (AKA red-green-refactor).
* You should run your tests regularly (see [Do you follow a Test Driven Process](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=53774ecb-3e5b-4985-89e9-3a57c2737e4c)). Ideally, they'll be part of your build (see [Do you know the minimum builds to create on any branch](http://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterVersionControlwithTFS%28AKASourceControl%29.aspx#MinimumBuilds))

<dl class="image">&lt;dt&gt;<img alt="CodeCoverage_blurred.png" src="CodeCoverage2010.png" style="width:600px;height:318px;">&lt;/dt&gt;<dd>Figure: Code Coverage metrics in Visual Studio. This solution has a very high code coverage percentage (around 80% on average)<br></dd></dl>
**Tip:** [Do you use Live Unit Testing to see code coverage?](https://www.ssw.com.au/SSW/Standards/Rules/RulesToBetterUnitTests.aspx#CodeCoverage)
