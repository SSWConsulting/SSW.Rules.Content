---
type: rule
archivedreason: 
title: Do you avoid reviewing performance without metrics?
guid: 6bdcdd2d-695a-46fa-93cc-cd761276586a
uri: do-you-avoid-reviewing-performance-without-metrics
created: 2009-03-17T05:48:04.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Matt Wicks
  url: https://ssw.com.au/people/matt-wicks
related: []
redirects: []

---



  <p>​If a client says&#58;<br></p>
<div class="greyBox">
<em>&quot;This application is too slow, I don't really want to put up with such poor performance. Please fix.&quot;</em></div>
<p>We don't jump in and look at the code and clean it up and reply with something like&#58;</p>
<div class="greyBox"><em>&quot;I've looked at the code and cleaned it up - not sure if this is suitable - please tell me if you are OK with the performance now.&quot;</em></div>

<br><excerpt class='endintro'></excerpt><br>
<p>A better way is&#58;</p><ul><li>Ask the client to tell us how slow it is (in seconds) and how fast they ideally would like it (in seconds)</li><li>Add some code to record the time the function takes to run</li><li>Reproduce the steps and record the time</li><li>Change the code</li><li>Reproduce the steps and record the time again</li><li>Reply to the customer&#58;<br>&quot;It was 22 seconds, you asked for around 10 seconds. It is now 8 seconds.&quot;<br></li></ul><dt> <img src="/PublishingImages/Code-Auditor-performance.jpg" alt=" " class="ms-rteCustom-ImageArea" border="0" style="border&#58;0px solid;" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Good example – Add some code to check the timing, before fixing any performance issues (An example from SSW Code Auditor)</span>
   <p></p></dt><dt>Also, never forget to do incremental changes in your tests!</dt><dd>For example, if you are trying to measure the optimal number of processors for&#160;a&#160;server, do not go from 1 processor to 4 processors at once&#58;</dd><dt><img src="/PublishingImages/1to4.png" alt="1to4.png" style="margin&#58;5px;" /></dt><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example - Going from 1 to 4 all at once gives you incomplete measurements and data</dd><dt><br></dt><dt>Do it incrementally, adding 1 processor each time, measuring the results, and then adding more&#58;</dt><dd><img src="/PublishingImages/1234.png" alt="1234.png" style="margin&#58;5px;" /></dd><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - Going from 1 to 2, then measuring, then incrementally adding one more, measuring...</dd><dt>This gives you the most complete set of data to work from.<br></dt><dt><br></dt><dt><p>This is because performance is an emotional thing, sometimes it just *feels* slower. Without numbers, a person cannot really know for sure whether something has become quicker.</p><h4>Related</h4><p>For sample code on how to measure performance for windows application form, please refer to rule <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterUnitTests.aspx#Performance">Do you have tests for Performance?</a>&#160;on <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterUnitTests.aspx">Rules To Better Unit Tests</a>.</p>​
   <h3 class="ssw15-rteElement-H3">Related Rule</h3><ul><li> 
         <span style="line-height&#58;1.6;"> <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=cb28d27b-542f-4f02-bfa4-31b3672ed0d5">Do you keep your website loading ti me acceptable? </a></span><br></li></ul></dt>


