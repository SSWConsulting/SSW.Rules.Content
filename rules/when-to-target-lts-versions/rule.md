---
type: rule
archivedreason: 
title: Do you know when to target LTS versions?
guid: eb220999-cfab-4b17-ae3c-d46ca339e65e
uri: when-to-target-lts-versions
created: 2020-12-22T19:50:21.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
related: []
redirects:
- do-you-know-when-to-target-lts-versions

---


<p class="ssw15-rteElement-P">Long Term Support (LTS) versions of .NET Core / .NET 6+ are officially supported by Microsoft for 3 years following release.&#160;​<br></p>So when considering which version to target for your application, the “Latest LTS when we first deploy to Production” is often the safest choice.<br>Non-LTS versions have much shorter support lifetimes.<br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-P">​Deciding which version to target is​ not always as simple as &quot;always choose LTS&quot;.<br></p><p class="ssw15-rteElement-P">In many cases, the expected lifetime of a project is longer than ​​​this LTS lifetime so future upgrades to your project must always be considered.&#160;</p><p class="ssw15-rteElement-P">The ongoing resources planned to work on this product must also be evaluated.​<br></p><p class="ssw15-rteElement-P">To help in these decisions,&#160; the .NET Core team has released a roadmap for upcoming releases over the next few years. All even-numbered releases will be LTS.<br><br></p><dl class="image"><dt>
      <img src="/PublishingImages/net-schedule.jpg" alt="net-schedule.jpg" style="width&#58;750px;height&#58;415px;" />
   </dt><dd>Figure&#58; The .NET Schedule – from 
      <a href="https&#58;//devblogs.microsoft.com/dotnet/introducing-net-5/">https&#58;//devblogs.microsoft.com/dotnet/introducing-net-5/</a></dd></dl><p class="ssw15-rteElement-P">Important questions to consider include&#58;​​<br></p><ul><li>What is the planned lifecycle of the project?</li><li>Will there be ongoing development in the future?</li><li>How are we planning to distribute and support this project?
   <ul><li>Web services that are automatically deployed to the cloud will be easier to continually update than a desktop app installed on customer PCs<br></li></ul></li>
   <li>​How does my project’s lifecycle align with the .NET release cycle?</li></ul><p class="ssw15-rteElement-P">All supported versions of .NET will receive servicing releases and the work to apply these updates should always be factored into the Total Cost of Ownership for any project.​<br></p><p class="ssw15-rteElement-P">A few invented scenarios are presented below&#58;<br></p><h3 class="ssw15-rteElement-H3"> Example 1<br></h3><p class="ssw15-rteElement-GreyBox">
&quot;It’s November 2020 and we are planning to launch the final version of our ASP.NET Core 3.1 API next week. There is no further planned development work in the next 12 months. If we upgrade to .NET 5 in the final sprint, we would get a performance boost.&quot;<br></p><b>Recommendation&#58;</b><br>Although moving to .NET 5 could introduce a performance improvement, .NET 5 is not LTS and there is little future development planned. In this situation staying with the LTS .Net Core 3.1 is recommended.<br>
<h3 class="ssw15-rteElement-H3">Example 2<br></h3><p class="ssw15-rteElement-GreyBox">
&quot;It’s November 2020 and Build 4463 of our ASP.NET Core API has just been deployed to Azure via GitHub Actions. We plan to continually develop new feature requests over the next 15 months, Finishing in January 2022”<br></p><b>Recommendation&#58;</b><br>When “continual development” is planned, it’s much easier to recommend working against the latest .NET version as it’s released. Upgrading incrementally during active development is often less painful than a larger planned upgrade between LTS versions&#160;<br>
<h3 class="ssw15-rteElement-H3">Example 3</h3><p class="ssw15-rteElement-GreyBox">
&quot;Once finished, we have no plans for further features for the next 2 years. Our planned launch date is October 2021&quot;​<br></p><b>Recommendation&#58;&#160;</b>
<p class="ssw15-rteElement-P">The plan to reach “feature complete and done” followed by no planned subsequent work seems to suggest that development with an LTS version would be best. 
   <br>But if you look at the planned launch date, it’s 1 month before the next LTS release (.NET 6).<br>​In this scenario, I would strongly advocate Developing against .NET 5, but leave some spare capacity to perform an update to &#160;.NET 6 LTS soon after launch.&#160;<br>Then the final, &quot;stable&quot;&#160;version will have a much longer support window.<br></p>


