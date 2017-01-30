---
type: rule
archivedreason: 
title: Do you look for Code Coverage?
guid: 53991e69-caae-4515-be83-2fc2b23202bc
uri: do-you-look-for-code-coverage
created: 2012-04-01T11:02:56.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
- title: Matt Wicks
  url: https://ssw.com.au/people/matt-wicks
related: []
redirects: []

---


<p>Code Coverage shows how much of your code is covered by tests and can be a useful tool for showing how effective your unit testing strategy is.&#160; However, it should be looked at with caution.​​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<ul><li>You should focus on <strong>*quality*</strong> not <strong>*quantity*</strong> of tests.</li><li>You should write tests for fragile code first and not waste time testing trivial methods</li><li>Remember the 80-20 rule - a very high test coverage is a noble goal but there are diminishing returns.</li><li>If you're modifying code, write&#160;the test first, then change the code, then run the test to make sure it passes (AKA red-green-refactor).</li><li>You should run your tests regularly (see <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=53774ecb-3e5b-4985-89e9-3a57c2737e4c">Do you follow a Test Driven Process</a>). Ideally, they'll be part of your build (see <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterVersionControlwithTFS%28AKASourceControl%29.aspx#MinimumBuilds">Do you know the minimum builds to create on any branch</a>)</li></ul><dl class="image"><dt><img alt="CodeCoverage_blurred.png" src="/PublishingImages/CodeCoverage2010.png" style="width&#58;600px;height&#58;318px;" /></dt><dd>F igure&#58; Code Coverage metrics in VS2010. This&#160;solution has a very high code coverage percentage (around 80% on average)<span class="ssw-rteStyle-FigureNormal"></span></dd></dl> 
<p>
   <b>Hot Tip&#58; </b> <a href="https&#58;//www.ssw.com.au/SSW/Standards/Rules/RulesToBetterUnitTests.aspx#CodeCoverage">Do you use Live Unit Testing to see code coverage? </a><br></p>


