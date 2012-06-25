---
type: rule
archivedreason: 
title: Do you know how to laser in on the smelliest code?
guid: c69ca2e5-0323-430e-ae26-62a753d4ace5
uri: do-you-know-how-to-laser-in-on-the-smelliest-code
created: 2012-03-16T08:36:31.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []

---


<p>Rather than randomly browsing for dodgy code, use Visual Studio's Code Metrics feature to identify &quot;Hot Spots&quot; that require investigation.</p>
<img src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/lotto-balls.jpeg" alt="467510-lotto-balls.jpeg" class="ms-rteCustom-ImageArea" />
<span class="ssw-rteStyle-FigureBad">​Figure&#58; The bad was is to browse the code</span>
<img alt="Run Code Metrics" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/VS%2011%20Code%20Metrics.png" class="ms-rteCustom-ImageArea" />
<span class="ssw-rteStyle-FigureNormal">Figure&#58; Run Code Metrics&#160;in VS11</span>
<img alt="Red dots indicate the code that is hard to maintain" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/CodeMetrics_3.png" class="ms-rteCustom-ImageArea" />
<span class="ssw-rteStyle-FigureNormal">Figure&#58; Red dots indicate the code that is hard to maintain. E.g. Save() and LoadCustomer()</span>
<p>Identifying the problem areas is only the start of the process. From here, you should speak to the developers responsible for this dodgy code. There might be good reasons why they haven't invested time on this.</p>
<img alt="Two devs talking" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/two-devs-talking.jpg" class="ms-rteCustom-ImageArea" />
<span class="ssw-rteStyle-FigureNormal">Figure&#58; Find out who&#160;the devs are&#160;by using the Annotate tool, and start a conversation.</span>
<p><strong>Tip&#58;</strong> To learn how to use Annotate, see <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSourceControlwithTFS.aspx#UsingSourceControl">Do you know the benefits of Source Control?</a>.</p>
<div class="ssw-rteStyle-GreyBox"><p>Suggestion to MS&#58; allow us to visualize the developers responsible for the bad code (currently and historically)</p></div>
<br><excerpt class='endintro'></excerpt><br>



