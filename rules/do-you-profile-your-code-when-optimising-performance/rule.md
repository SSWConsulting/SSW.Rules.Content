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



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>

<p>We recommend that you should always use a code profiling tool to measure performance gains whilst optimising your application. Otherwise, you are just flying blind and making subjective, unmeasured decisions. Instead, use a tool such as <a href="http&#58;//www.ssw.com.au/ssw/Redirect/JetbrainsNETProfiler.htm">JetBrains dotTrace profiler</a>. These will guide you as to how to best optimise any code that is lagging behind the pack. You can run this on both ASP.NET and Windows Forms Applications. The optimisation process is as follows&#58; </p>
<ol>
<li>Profile the application with Jetbrains dotTrace using the &quot;Hot Spot&quot; tab to identify the slowest areas of your application 
<dl class="image">
<dt><img style="border-right&#58;0px solid;border-top&#58;0px solid;border-left&#58;0px solid;border-bottom&#58;0px solid;" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/JetBrainsProfilerHotSpots.jpg" border="0" /> </dt>
<dd>Figure&#58; Identify which parts of your code take the longest (Hot Spots)</dd></dl>
<li>Some parts of the application will be out of your control e.g. .NET System Classes. Identify the slowest parts of code that you can actually modify from the Hot Spot listing 
<li>Determine the cause of the poor performance and optimise (e.g. improve the WHERE clause or the number of columns returned, reduce the number of loops or use a StringBuilder instead of string concatenation) 
<li>Re-run the profile to confirm that performance has improved 
<li>Repeat from Step 1 until the application is optimised </li></ol>


