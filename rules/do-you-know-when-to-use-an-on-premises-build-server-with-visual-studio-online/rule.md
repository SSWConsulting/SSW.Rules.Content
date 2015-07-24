---
type: rule
archivedreason: 
title: Do you know when to use an on-premises build server with Visual Studio Online?
guid: 3ef53ffe-23ec-452a-83ac-c57b307febb7
uri: do-you-know-when-to-use-an-on-premises-build-server-with-visual-studio-online
created: 2014-08-25T05:28:30.0000000Z
authors:
- id: 23
  title: Damian Brady
related:
- do-you-use-the-best-deployment-tool
- do-you-estimate-all-tasks-at-the-start-of-the-sprint

---


If you are using <a href="http&#58;//www.visualstudio.com/">Visual Studio Online</a>, there's an awesome <a href="http&#58;//blogs.msdn.com/b/visualstudioalm/archive/2012/03/27/build-on-the-team-foundation-service.aspx">Hosted Build Server</a> option you can use to perform your builds with little to no setup. But if you're working on a project that has continuous integration and a long build time, it's not long before those build minutes start to add up.
<br><excerpt class='endintro'></excerpt><br>
<span style="line-height&#58;20.799999237060547px;">To reduce your build costs, you could&#160;reduce the number of builds or try to reduce the build time.&#160;Continuous integration is very important so you don't want to turn that off, and <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSourceControlwithTFS.aspx#CheckinRegularly">we encourage checking in early and often</a>. Reducing the build time is a nice idea, but you can't always reduce it enough to make a difference.</span><div><span style="line-height&#58;20.799999237060547px;"><br></span></div><div><span style="line-height&#58;20.799999237060547px;">For large, expensive projects, the best option is to configure an on-premises build server rather than using hosted builds.</span></div><div><span style="line-height&#58;20.799999237060547px;"><br></span></div><div><span style="line-height&#58;20.799999237060547px;">To configure an on-premises build server for Visual Studio Online, check out Anthony Borton's great walkthrough&#58;</span></div><div><span style="line-height&#58;20.799999237060547px;"><a href="http&#58;//myalmblog.com/2014/04/13/configuring-on-premises-build-server-for-visual-studio-online/">http&#58;//myalmblog.com/2014/04/13/configuring-on-premises-build-server-for-visual-studio-online/​</a><br></span></div><div><span style="line-height&#58;20.799999237060547px;"><br></span></div><div><span style="line-height&#58;20.799999237060547px;">Once you have a build server configured, you'll be able to see the build controller&#160;as an option when you configure a new build definition.</span></div><div><span style="line-height&#58;20.799999237060547px;"><br></span></div><div><span style="line-height&#58;20.799999237060547px;"><img src="/PublishingImages/vso_build.png" alt="vso_build.png" style="margin&#58;5px;width&#58;650px;" /><br></span></div><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - We have the option of an on-premises build controller&#160;as well as the Hosted Build controller</dd>


