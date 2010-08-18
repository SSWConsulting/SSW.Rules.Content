---
type: rule
title: Do you profile your code when optimising performance?
uri: do-you-profile-your-code-when-optimising-performance
created: 2009-05-06T08:54:43.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> Imagine that you have just had a User Acceptance Test (UAT), and your app has been reported as being &quot;painfully slow&quot; or &quot;so slow as to be unusable&quot;. Now, as a coder, where do you start to improve the performance? More importantly, do you know how much your massive changes have improved performance - if at all? 
 </span>


  <p>We recommend that you should always use a code profiling tool to measure performance gains whilst optimising your application. Otherwise, you are just flying blind and making subjective, unmeasured decisions. Instead, use a tool such as <a href="http&#58;//www.ssw.com.au/ssw/Redirect/JetbrainsNETProfiler.htm">JetBrains dotTrace profiler</a>. These will guide you as to how to best optimise any code that is lagging behind the pack. You can run this on both ASP.NET and Windows Forms Applications. The optimisation process is as follows&#58; </p>
<ol>
    <li>Profile the application with Jetbrains dotTrace using the &quot;Hot Spot&quot; tab to identify the slowest areas of your application
    <dl class="image">
        <dt><img alt="" style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/JetBrainsProfilerHotSpots.jpg" /> </dt>
        <dd>Figure&#58; Identify which parts of your code take the longest (Hot Spots)</dd>
    </dl>
    </li>
    <li>Some parts of the application will be out of your control e.g. .NET System Classes. Identify the slowest parts of code that you can actually modify from the Hot Spot listing </li>
    <li>Determine the cause of the poor performance and optimise (e.g. improve the WHERE clause or the number of columns returned, reduce the number of loops or use a StringBuilder instead of string concatenation) </li>
    <li>Re-run the profile to confirm that performance has improved </li>
    <li>Repeat from Step 1 until the application is optimised </li>
</ol>



