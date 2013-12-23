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



<span class='intro'> <p>​<a href="/SoftwareDevelopment/RulesForErrorHandling/Pages/use-the-best-exception-handling-framework.aspx">Do&#160;you use the best middle tier .Net libraries?</a>&#160;The best exception handling library is TFS&#160;Application Insights​.</p><p>Your users should never see the “yellow screen of death” in ASP.NET, or the “unhandled exception” message in a Windows application. Errors should always be caught and logged – preferably in a SQL database.</p><p><br></p> </span>

<p>​<span style="line-height&#58;1.6;">At SSW we use TFS Application Insights.&#160;TFS Application Insights is available as part of&#160;<a href="http&#58;//msdn.microsoft.com/en-us/library/dn481095.aspx">Visual Studio Online​</a>&#58;</span></p><p class="greyBox">​ 
   <span style="line-height&#58;1.6;"></span>
   <span style="line-height&#58;1.6;"><em>Application Insights is a set of services that provide actionable insight into a production application.&#160;</em></span>​</p> 
<p style="line-height&#58;20px;">If TFS Application Insights&#160;is not available we use ELMAH.</p><p> 
   <span class="s1">ELMAH is the exception logger to use for web applications. From its 
      <span class="s2"> 
         <a href="https&#58;//www.nuget.org/packages/ELMAH">NuGet page</a>&#58;</span></span></p><p class="greyBox">
   <em>ELMAH with initial configuration for getting started quickly. ELMAH (Error Logging Modules and Handlers) is an application-wide error logging facility that is completely pluggable. It can be dynamically added to a running ASP.NET web application, or even all ASP.NET web applications on a machine, without any need for re-compilation or re-deployment.</em></p><p> 
   <strong>Note&#58; </strong>If you are still developing Windows applications, then SSW Exception Logger is the one to use. Read 
   <a href="http&#58;//www.ssw.com.au/ssw/NetToolKit/04ExceptionReporter.aspx">SSW .NET Toolkit – LadyLog User Guide</a>.</p>


