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



<span class='intro'> <p class="p1">Did you know that writing your own logging infrastructure code wastes time? You should use a trace logging library, and&#160;t<span style="line-height&#58;20.7999992370605px;">he best trace logging library is Log4Net.</span></p><p class="p2">Log4net is a NuGet package that can be included in any .Net application, is easy to configure, supports many different output targets, has great performance, and allows for runtime changes to configuration.</p> </span>

<p class="p1">It also supports the concept of logging at different levels of importance (e.g. Error, Warning, Information) and having different logs for different components of your application (e.g. a Customer Log and an Order Log).</p><p class="p1">For example, log4net allows you to support the following scenarios by making configuration changes in XML config files.</p><p class="p1">On all non-development machines&#58;</p><ul class="ul1"><li class="li2">Write all Error Log Messages to the Windows Event Log, the database and email them to the administrators group</li><li class="li2">Write all Warning messages to the database and email them to the administrators group</li><li class="li2">Write all Information messages to the database, and email any information messages in the Order component to the Order Fulfilment team for them to check</li></ul><p class="p3">On development machines&#58;</p><ul class="ul1"><li class="li2">Write all Error Log Messages to the database</li><li class="li2">Write all Warning messages to the database</li><li class="li2">Write all Information messages on the area I am currently developing to the database</li></ul><dl class="badImage"><dt><img src="/PublishingImages/trace-logging-bad.jpg" alt="" /></dt><dd>Figure&#58; Bad Example - Using Debug or Trace for logging, or writing hard coded mechanisms for logging does not allow you to configure logging at runtime</dd></dl><dl class="badImage"><dt><img src="/PublishingImages/trace-logging-bad-2.jpg" alt="" /></dt><dd>Figure&#58; Bad Example - Roll your own logging components lack functionality, and have not been tested as thoroughly for quality or performance as log4net</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/trace-logging-good.jpg" alt="" /></dt><dd>Figure&#58; Good Example - Using log4net requires less work to install and configure than a roll-you-own logger, and provides many more features</dd></dl>

<p>Log4Net should be added to your project via the NuGet package manager.</p><p>See also&#160;<a href="/do-you-use-the-best-middle-tier-net-libraries" style="line-height&#58;20.7999992370605px;">Do you use the best middle tier .Net libraries?</a><span style="line-height&#58;20.7999992370605px;">&#160;</span><br></p>


