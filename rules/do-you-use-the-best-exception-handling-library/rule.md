---
type: rule
title: Do you use the best exception handling library?
uri: do-you-use-the-best-exception-handling-library
created: 2013-09-11T19:17:07.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 38
  title: Drew Robson

---



<span class='intro'> <p>​​When developing software, exceptions are a fact-of-life you will need to deal with. Don't reinvent the wheel, use an existing exception handling library or service.</p><p>​​​The best exception handling service&#160;is <a href="/rules-to-better-application-insights-for-visual-studio-online">Application Insights for ​Visual Studio Online​</a>, but if you can't use that, then use <a href="https&#58;//www.nuget.org/packages/elmah/">ELMAH​</a>.</p><p>Your users should never see the “yellow screen of death” in ASP.NET, or the “unhandled exception” message in a Windows application. Errors should always be caught and logged – preferably in a SQL database.​</p><p><br></p> </span>

<p>​<span style="line-height&#58;1.6;">At SSW we use&#160;Application Insights for Visual Studio Online.</span></p><p class="greyBox">​ 
   <span style="line-height&#58;1.6;"></span> 
   <span style="line-height&#58;1.6;">
      <em>Application Insights will tell you if your application goes down or runs slowly under load. If there are any uncaught exceptions, you’ll be able to drill into the code to pinpoint the problem. You can also find out what your users are doing with the application so that you can tune it to their needs in each development cycle.
&#160;</em></span>​</p><p style="line-height&#58;20px;">If <span style="line-height&#58;20.7999992370605px;">Application Insights for Visual Studio Online</span>&#160;is not available we use ELMAH when developing web applications<span style="line-height&#58;1.6;">. From its 
      </span><span class="s2" style="line-height&#58;1.6;"><a href="https&#58;//www.nuget.org/packages/ELMAH">NuGet page</a>&#58;</span></p><p class="greyBox"> 
   <em>ELMAH with initial configuration for getting started quickly. ELMAH (Error Logging Modules and Handlers) is an application-wide error logging facility that is completely pluggable. It can be dynamically added to a running ASP.NET web application, or even all ASP.NET web applications on a machine, without any need for re-compilation or re-deployment.</em></p><p>If you are still developing Windows applications, then SSW Exception Logger is the one to use. Read 
   <a href="http&#58;//www.ssw.com.au/ssw/NetToolKit/04ExceptionReporter.aspx">SSW .NET Toolkit – LadyLog User Guide</a>.</p><p>ELMAH can be easily added to your application from NuGet, and it configures itself.</p><p><img src="/PublishingImages/2014-09-08_10-56-57-compressor.png" alt="2014-09-08_10-56-57-compressor.png" style="margin&#58;5px;width&#58;650px;" /><br><strong>Figure&#58; Add ELMAH to your web application from NuGet</strong></p><p>See also&#160;<a href="/Pages/use-the-best-exception-handling-framework.aspx" style="line-height&#58;20.7999992370605px;">Do&#160;you use the best middle tier .Net libraries?</a></p>


