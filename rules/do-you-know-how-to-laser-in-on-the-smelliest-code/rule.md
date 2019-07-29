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



<span class='intro'> <p>Rather than randomly browsing for dodgy code, use Visual Studio's Code Metrics feature to identify &quot;Hot Spots&quot; that require investigation.<br></p><dl class="badImage"><dt> 
      <img alt="467510-lotto-balls.jpeg" src="/PublishingImages/lotto-balls.jpeg" style="width&#58;600px;" /> 
   </dt><dd>​Figure&#58; The bad was is to browse the code<br>​<br><br></dd></dl> </span>

<dl class="image"><dt> 
      <img src="/PublishingImages/VS%2011%20Code%20Metrics.png" alt="Run Code Metrics" /> 
   </dt><dd>Figure&#58; Run Code Metrics&#160;in Visual Studio</dd></dl><dl class="image"><dt> 
      <img src="/PublishingImages/CodeMetrics_3.png" alt="Red dots indicate the code that is hard to maintain" style="width&#58;750px;height&#58;389px;" /> 
   </dt><dd>Figure&#58; Red dots indicate the code that is hard to maintain. E.g. Save() and LoadCustomer()</dd></dl><p>Identifying the problem areas is only the start of the process. From here, you should speak to the developers responsible for this dodgy code. There might be good reasons why they haven't invested time on this.</p><dl class="image"><dt> 
      <img class="ms-rteCustom-ImageArea" src="/PublishingImages/two-devs-talking.jpg" alt="Two devs talking" /> 
      <br> 
   </dt><dd>Figure&#58; Find out who&#160;the devs are&#160;by using CodeLens and start a conversation<span style="color&#58;#444444;">​</span></dd></dl>​<strong>Tip&#58;</strong> To learn how to use Annotate, see 
<a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSourceControlwithTFS.aspx#UsingSourceControl">Do you know the benefits of Source Control?</a>
<p>
   <br>
</p><div><p class="ssw15-rteElement-GreyBox">
      <b>​Suggestion to Microsoft&#58;</b> allow us to visualize the developers responsible for the bad code (currently and historically)&#160;using CodeLens.<br></p></div>


