---
type: rule
title: Do you reduce diagnostic logging level after configure hybrid search?
uri: do-you-reduce-diagnostic-logging-level-after-configure-hybrid-search
created: 2017-04-25T23:51:08.0000000Z
authors:
- id: 9
  title: William Yin

---



<span class='intro'> By default, SharePoint diagnostic logging level was set to “Information” and “Medium”, which will log quite a big info, and it increased a log after configuring “hybrid search”&#58;<br> </span>

<dl class="image">​​​
<dt><img src="/PublishingImages/sp-diagnostic-logging.jpg" alt="sp-diagnostic-logging.jpg" /></dt><dd>Figure&#58; default logging levels​<br></dd></dl><dl class="image"><dt><img src="/PublishingImages/sp-diagnostic-logging-2.jpg" alt="sp-diagnostic-logging-2.jpg" /></dt><dd>Figure&#58; lots of &quot;Medium&quot; level search logs</dd></dl>This made us had 60GB logs for only 14 days.<p>So the solution is to&#160;change&#160;to &quot;diagnostic logging level&quot; as below to reduce the log size&#58;​</p><dl class="image"><dt><img src="/PublishingImages/sp-diagnostic-logging-3.jpg" alt="sp-diagnostic-logging-3.jpg" /></dt></dl>


