---
type: rule
title: Do you look for Code Coverage?
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

---



<span class='intro'> <p><span style="font-family&#58;'calibri','sans-serif';font-size&#58;11pt;">Code Coverage shows how much of your code is covered by tests and can be a useful tool for showing how effective your unit testing strategy is.&#160; However, it should be looked at with caution.</span></p> </span>

<ul><li>​You should focus on <strong>*quality*</strong> not <strong>*quantity*</strong> of tests.</li>
<li>You should write tests for fragile code first and not waste time testing trivial methods</li>
<li>Remember the 80-20 rule - a very high test coverage is a noble goal but there are diminishing returns.</li>
<li>If you're modifying code, write&#160;the test first, then change the code, then run the test to make sure it passes (AKA red-green-refactor).</li>
<li>You should run your tests regularly (see <a href="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/Pages/TestDrivenProcess.aspx">Do you follow a Test Driven Process</a>). Ideally, they'll be part of your build (see <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSourceControlwithTFS.aspx#MinimumBuilds">Do you know the minimum builds to create on any branch</a>)</li></ul>
<img alt="CodeCoverage_blurred.png" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/CodeCoverage2010.png" style="margin&#58;5px;width&#58;600px;height&#58;318px;" /><br><span class="ssw-rteStyle-FigureNormal">Figure&#58; Code Coverage metrics in VS2010. This&#160;solution has a very high code coverage percentage (around 80% on average)</span><br>


