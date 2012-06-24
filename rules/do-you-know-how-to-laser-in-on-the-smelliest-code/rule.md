---
type: rule
title: Do you know how to laser in on the smelliest code?
uri: do-you-know-how-to-laser-in-on-the-smelliest-code
created: 2012-03-16T08:36:31.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 23
  title: Damian Brady
- id: 24
  title: Adam Stephensen

---



<span class='intro'> <p>Rather than randomly browsing for dodgy code, use Visual Studio's Code Metrics feature to identify &quot;Hot Spots&quot; that require investigation.</p>
<p><img src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/lotto-balls.jpeg" alt="467510-lotto-balls.jpeg" style="margin&#58;5px;" /><br><span class="ssw-rteStyle-FigureBad">​Figure&#58; The bad was is to browse the code</span></p>
<p><img src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/VS%2011%20Code%20Metrics.png" alt="" style="margin&#58;5px;" />&#160;</p>
<span class="ssw-rteStyle-FigureNormal">Figure&#58; Run Code Metrics&#160;in VS11</span>
<img class="ssw-rteStyle-ImageArea" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/CodeMetrics_3.png" alt="" style="margin&#58;5px;width&#58;657px;" />
<div class="ssw-rteStyle-FigureNormal">Figure&#58; Red dots indicate the code that is hard to maintain e.g. Save() and LoadCustomer()</div>
<p>Identifying the problem areas is only the start of the process. From here, you should speak to the developers responsible for this dodgy code. There might be good reasons why they haven't invested time on this.</p>
<img alt="Two devs talking" class="ssw-rteStyle-ImageArea" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/two-devs-talking.jpg" />
<span class="ssw-rteStyle-FigureNormal">Figure&#58; Find out who&#160;the devs are&#160;by using the Annotate tool, and start a conversation.</span>
<p><strong>Tip&#58; </strong>To learn how to use Annotate, see <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSourceControlwithTFS.aspx#UsingSourceControl">Do you know the benefits of Source Control?</a>.</p>
<p class="ssw-rteStyle-GreyBox"><span>Suggestion to MS&#58; allow us to visualize the developers responsible for the bad code (currently and historically)</span>​</p> </span>




