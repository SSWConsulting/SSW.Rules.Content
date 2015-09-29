---
type: rule
title: Do you use the best trace logging library?
uri: do-you-use-the-best-trace-logging-library
created: 2013-09-11T21:38:08.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 38
  title: Drew Robson
- id: 34
  title: Brendan Richards

---



<span class='intro'> <p class="p1">Did you know that writing your own logging infrastructure code wastes time? You should use a logging library, and&#160;t<span style="line-height&#58;20.8px;">he best logging library is Serilog.</span></p><p class="p2"><span style="line-height&#58;20.8px;">Serilog&#160;</span>is a NuGet package that can be included in any .Net application, is easy to configure, supports many different output targets, has great performance, and allows for runtime changes to configuration. Serilog also&#160;supports&#160;full integration with log4net so is easy to use with any older codebase using log4net.</p> </span>

<p class="p1">Serilog supports all the log4net&#160;concepts of logging at different levels of importance (e.g. Error, Warning, Information) and having different logs for different components of your application (e.g. a Customer Log and an Order Log).</p><p class="p1"><span style="line-height&#58;20.8px;">Serilog's main advantage over previous loggers is its ability to serialize and log full .net objects rather than just strings.</span><span style="line-height&#58;20.8px;">&#160;Serilog also has a&#160;powerful, nested context system allowing log events to be grouped by request, operation etc.&#160;</span><br></p><p class="p1">Serilog has the concept of &quot;sinks&quot;&#58; pluggable modules that that can&#160;consume, store and/or act on logging events. The most pwerfult sink is Seq - a web aplication that allows the user to perform complex search queries&#160;on incoming log data in real time.</p><p class="p1">Other sinks allow you to&#58;</p><ul class="p1"><li><span style="line-height&#58;1.6;">​save logs to a file</span><br></li><li><span style="line-height&#58;1.6;">export to log4net (and subsequently use any log4net appender)</span></li><li><span style="line-height&#58;1.6;">save to a&#160;database</span></li><li><span style="line-height&#58;1.6;">export to Application Insights, New Relic and many other APM platforms<br></span></li></ul><div><span style="line-height&#58;20.8px;">Many other sinks are available as described here&#58;&#160;<a href="https&#58;//github.com/serilog/serilog/wiki/Provided-Sinks">https&#58;//github.com/serilog/serilog/wiki/Provided-Sinks​</a></span></div><dl class="badImage"><dt><img src="/PublishingImages/trace-logging-bad.jpg" alt="" /></dt><dd>Figure&#58; Bad Example - Using Debug or Trace for logging, or writing hard coded mechanisms for logging does not allow you to configure logging at runtime</dd></dl><dl class="badImage"><dt><img src="/PublishingImages/trace-logging-bad-2.jpg" alt="" /></dt><dd>Figure&#58; Bad Example - Roll your own logging components lack functionality, and have not been tested as thoroughly for quality or performance as log4net</dd><p class="ssw15-rteElement-P">​<br></p><p class="ssw15-rteElement-P"><img alt="serilog.png" src="/SiteAssets/do-you-use-the-best-trace-logging-library/serilog.png" style="margin&#58;5px;" /><br></p></dl><dl class="goodImage"><dt></dt><dd>Figure&#58; Good Example - Using serilog&#160;requires less work to install and configure than a roll-you-own logger, and provides many more features</dd><p class="ssw15-rteElement-P"><img alt="seq2.png" src="/SiteAssets/do-you-use-the-best-trace-logging-library/seq2.png" style="margin&#58;5px;width&#58;650px;" /><br></p><dd>Figure&#58; Good Example - Seq provides a powerful UI for searching and viewing your structured logs</dd></dl>

<p>Serilog&#160;should be added to your project via the NuGet package manager.</p><p>See also&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=9ea489f4-032b-4e5b-a0e0-df5a0c3148fe" style="line-height&#58;20.8px;">Do you use the best middle tier .Net libraries?</a><span style="line-height&#58;20.8px;">&#160;</span><br></p>


