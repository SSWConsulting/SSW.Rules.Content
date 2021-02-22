---
type: rule
archivedreason: 
title: Do you use the best trace logging library?
guid: 5ecb7c85-0a65-494c-ac1a-51c71c4546aa
uri: do-you-use-the-best-trace-logging-library
created: 2013-09-11T21:38:08.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Drew Robson
  url: https://ssw.com.au/people/drew-robson
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
related: []
redirects: []

---


<p class="p1">Did you know that writing your own logging infrastructure code wastes time? You should use a logging library, and t<span style="line-height:20.8px;">he best logging library is Serilog.</span></p><p class="p2"><span style="line-height:20.8px;">Serilog </span>is a NuGet package that can be included in any .NET application, is easy to configure, supports many different output targets, has great performance, and allows for runtime changes to the configuration. Serilog also supports full integration with log4net so is easy to use with any older codebase using log4net.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>Serilog supports all the log4net concepts of logging at different levels of importance (e.g. Error, Warning, Information) and having different logs for different components of your application (e.g. a Customer Log and an Order Log).</p><p class="p1">Serilog's main advantage over previous loggers is its ability to serialize and log full .net objects rather than just strings.<span style="line-height:20.8px;"> Serilog also has a powerful, nested context system allowing log events to be grouped by request, operation etc. </span><br></p><p class="p1">Serilog has the concept of "sinks": pluggable modules that can consume, store and/or act on logging events. The most powerful sink is Seq - a web application that allows the user to perform complex search queries on incoming log data in real time.</p><p class="p1">Other sinks allow you to:</p><ul class="p1"><li>save logs to a file<br></li><li>export to log4net (and subsequently use any log4net appender)</li><li>save to a database</li><li>export to Application Insights, New Relic, and many other APM platforms<br></li></ul><p>Many other sinks are available as described here: <a href="https://github.com/serilog/serilog/wiki/Provided-Sinks">https://github.com/serilog/serilog/wiki/Provided-Sinks </a></p><dl class="badImage"><dt> <img src="trace-logging-bad.jpg" alt="" /> </dt><dd>Figure: Bad Example - Using Debug or Trace for logging, or writing hard coded mechanisms for logging does not allow you to configure logging at runtime</dd></dl><dl class="badImage"><dt> <img src="trace-logging-bad-2.jpg" alt="" /> </dt><dd>Figure: Bad Example - Roll your own logging components lack functionality, and have not been tested as thoroughly for quality or performance as log4net</dd></dl><dl class="goodImage"><dt> <img alt="serilog.png" src="serilog.png" /> </dt><dd>Figure: Good Example - Using serilog allows persisting structured log data to multiple stores, querying that data intelligently and requires less work to install and configure than a roll-you-own logger, and provides many more features</dd></dl> <dl class="goodImage"> <dt> <img alt="seq2.png" src="seq2.png" style="width:800px;" /> </dt><dd>Figure: Good Example - Seq provides a powerful UI for searching and viewing your structured logs</dd></dl><p>Serilog should be added to your project via the NuGet package manager.<br></p><p>See also <a href=/do-you-use-the-best-middle-tier-net-libraries>Do you use the best middle tier .NET libraries?</a></p>


