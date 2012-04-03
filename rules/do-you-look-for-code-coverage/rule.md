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


<p><span style="font-family&#58;'calibri','sans-serif';font-size&#58;11pt;">Code Coverage shows how much of your code is covered by tests and can be a useful tool for showing how effective your unit testing strategy is.&#160; However, it should be looked at with caution.</span></p>
<br><excerpt class='endintro'></excerpt><br>
<ul><li>​You should focus on quality not quantity of tests.</li>
<li>You should write tests for fragile code first and not waste time testing trivial methods</li>
<li>Remember the 80-20 rule - a very high test coverage is a noble goal but there are diminishing returns.</li>
<li>If you're modifying code, write&#160;the test first, then change the code, then run the test to make sure it passes.</li></ul>
<img alt="CodeCoverage_blurred.png" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/CodeCoverage2010.png" style="margin&#58;5px;width&#58;600px;height&#58;318px;" /><br><span class="ssw-rteStyle-FigureNormal">Figure&#58; Code Coverage metrics in VS2010. This&#160;solution has a very high code coverage percentage (around 80% on average)</span><br>


