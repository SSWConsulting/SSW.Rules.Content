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



<span class='intro'> <p>The best exception handling framework is ELMAH.</p><p>Your users should never see the “yellow screen of death” in ASP.NET, or the “unhandled exception” message in a Windows application. Errors should always be caught and logged – preferably in a SQL database.</p> </span>

<p>​<span class="s1">ELMAH is the exception logger to use for web applications. From its 
      <a href="https&#58;//www.nuget.org/packages/ELMAH">
         <span class="s2">NuGet page</span></a>&#58;</span></p>
<p class="greyBox"><em>ELMAH with initial configuration for getting started quickly. ELMAH (Error Logging Modules and Handlers) is an application-wide error logging facility that is completely pluggable. It can be dynamically added to a running ASP.NET web application, or even all ASP.NET web applications on a machine, without any need for re-compilation or re-deployment.</em></p><p>
      <strong>Note&#58; </strong>If you are still developing Windows applications, then SSW Exception Logger is the one to use. Read 
      <a href="http&#58;//www.ssw.com.au/ssw/NetToolKit/04ExceptionReporter.aspx">
         <span class="s2">SSW .NET Toolkit – LadyLog User Guide</span></a>.</p>


