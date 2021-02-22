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


<p>Rather than randomly browsing for dodgy code, use Visual Studio's Code Metrics feature to identify "Hot Spots" that require investigation.<br></p><dl class="badImage"><dt> 
      <img alt="467510-lotto-balls.jpeg" src="lotto-balls.jpeg" style="width:600px;" /> 
   </dt><dd>​Figure: The bad was is to browse the code<br></dd></dl>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt>
      <img src="VS 11 Code Metrics.png" alt="Run Code Metrics" />
   </dt><dd>Figure: Run Code Metrics in Visual Studio</dd></dl><dl class="image"><dt>
      <img src="CodeMetrics_3.png" alt="Red dots indicate the code that is hard to maintain" style="width:750px;height:389px;" />
   </dt><dd>Figure: Red dots indicate the code that is hard to maintain. E.g. Save() and LoadCustomer()</dd></dl><p>Identifying the problem areas is only the start of the process. From here, you should speak to the developers responsible for this dodgy code. There might be good reasons why they haven't invested time on this.</p><dl class="image"><dt>
      <img class="ms-rteCustom-ImageArea" src="codelens-start-conversation.png" alt="codelens-start-conversation.png" />  
      <br>
   </dt><dd>Figure: Find out who the devs are by using CodeLens and start a conversation<span style="color:#444444;">​</span></dd></dl>​<strong>Tip:</strong> To learn how to use Annotate, see 
<a href="http://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSourceControlwithTFS.aspx#UsingSourceControl">Do you know the benefits of Source Control?</a> 
<p> 
   <br> 
</p><div><p class="ssw15-rteElement-GreyBox"> 
      <b>​Suggestion to Microsoft:</b> allow us to visualize the developers responsible for the bad code (currently and historically) using CodeLens.<br></p></div>


