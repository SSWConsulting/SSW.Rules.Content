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



  <p>If a client says&#58;</p>
<div class="greyBox">
<em>&quot;This application is too slow, I don't really want to put up with such poor performance. Please fix.&quot;</em></div>
<p>We don't jump in and look at the code and clean it up and reply with something like&#58;</p>
<div class="greyBox">&quot;I've looked at the code and cleaned it up - not sure if this is suitable - please tell me if you are OK with the performance now.&quot;</div>

<br><excerpt class='endintro'></excerpt><br>
<p>A better way is&#58;</p>
  <ul>
    <li>Ask the client to tell us how slow it is (in seconds) and how fast they ideally would like it (in seconds)
    </li>
    <li>Add some code to record the time the function takes to run
    </li>
    <li>Reproduce the steps and record the time
    </li>
    <li>Change the code
    </li>
    <li>Reproduce the steps and record the time again
    </li>
    <li>Reply to the customer&#58;<br> &quot;It was 22 seconds, you asked for around 10 seconds. It is now 8 seconds.&quot;<br></li>
</ul>
<dt><img border="0" class="ms-rteCustom-ImageArea" alt=" " src="/Management/RulesToSuccessfulProjects/PublishingImages/Code-Auditor-performance.jpg" style="border&#58;0px solid;" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Good example – Add some code to check the timing, before fixing any performance issues (An example from SSW Code Auditor)</span>
<p>This is because performance is an emotional thing, sometimes it just *feels* slower. Without numbers, a person cannot really know for sure whether something has become quicker. </p>
<h4>Related</h4>
<p>For sample code on how to measure performance for windows application form, please refer to rule <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterUnitTests.aspx#Performance">Do you have tests for Performance?</a>&#160;on <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterUnitTests.aspx">Rules To Better Unit Tests</a>.</p>
</dt>



