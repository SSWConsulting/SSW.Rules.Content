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



<span class='intro'> <p class="p1">Did you know that writing your own logging infrastructure code wastes time? You should use a logging library, and&#160;t<span style="line-height&#58;20.8px;">he best logging library is Serilog.</span></p><p class="p2"><span style="line-height&#58;20.8px;">Serilog&#160;</span>is a NuGet package that can be included in any .NET application, is easy to configure, supports many different output targets, has great performance, and allows for runtime changes to the configuration. Serilog also&#160;supports&#160;full integration with log4net so is easy to use with any older codebase using log4net.</p> </span>

<p>Serilog supports all the log4net&#160;concepts of logging at different levels of importance (e.g. Error, Warning, Information) and having different logs for different components of your application (e.g. a Customer Log and an Order Log).</p><p class="p1">Serilog's main advantage over previous loggers is its ability to serialize and log full .net objects rather than just strings.<span style="line-height&#58;20.8px;">&#160;Serilog also has a&#160;powerful, nested context system allowing log events to be grouped by request, operation etc.&#160;</span><br></p><p class="p1">Serilog has the concept of &quot;sinks&quot;&#58; pluggable modules that can&#160;consume, store and/or act on logging events. The most powerful sink is Seq - a web application that allows the user to perform complex search queries&#160;on incoming log data in real time.</p><p class="p1">Other sinks allow you to&#58;</p><ul class="p1"><li>save logs to a file<br></li><li>export to log4net (and subsequently use any log4net appender)</li><li>save to a&#160;database</li><li>export to Application Insights, New Relic, and many other APM platforms<br></li></ul><p>Many other sinks are available as described here&#58;&#160;<a href="https&#58;//github.com/serilog/serilog/wiki/Provided-Sinks">https&#58;//github.com/serilog/serilog/wiki/Provided-Sinks </a></p><dl class="badImage"><dt> <img src="/PublishingImages/trace-logging-bad.jpg" alt="" /> </dt><dd>Figure&#58; Bad Example - Using Debug or Trace for logging, or writing hard coded mechanisms for logging does not allow you to configure logging at runtime</dd></dl><dl class="badImage"><dt> <img src="/PublishingImages/trace-logging-bad-2.jpg" alt="" /> </dt><dd>Figure&#58; Bad Example - Roll your own logging components lack functionality, and have not been tested as thoroughly for quality or performance as log4net</dd></dl><dl class="goodImage"><dt> <img alt="serilog.png" src="/PublishingImages/serilog.png" /> </dt><dd>Figure&#58; Good Example - Using serilog&#160;allows persisting structured&#160;log data to multiple stores, querying that data intelligently&#160;and&#160;requires less work to install and configure than a roll-you-own logger, and provides many more features</dd></dl> <dl class="goodImage"> <dt> <img alt="seq2.png" src="/PublishingImages/seq2.png" style="width&#58;800px;" /> </dt><dd>Figure&#58; Good Example - Seq provides a powerful UI for searching and viewing your structured logs</dd></dl><p>Serilog&#160;should be added to your project via the NuGet package manager.<br></p><p>See also&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=9ea489f4-032b-4e5b-a0e0-df5a0c3148fe">Do you use the best middle tier .NET libraries?</a></p>


