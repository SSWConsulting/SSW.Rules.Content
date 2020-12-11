---
type: rule
archivedreason: 
title: Do you reduce diagnostic logging level after configure hybrid search?
guid: 8e162448-9d9e-40e9-9483-3cb91a00b2d4
uri: do-you-reduce-diagnostic-logging-level-after-configure-hybrid-search
created: 2017-04-25T23:51:08.0000000Z
authors:
- id: 9
  title: William Yin
related: []

---

By default, SharePoint diagnostic logging level was set to “Information” and “Medium”, which will log quite a big info, and it increased a log after configuring “hybrid search”:

<!--endintro-->
<dl class="image">&lt;dt&gt;<img src="sp-diagnostic-logging.jpg" alt="sp-diagnostic-logging.jpg">&lt;/dt&gt;<dd>Figure: default logging levels<br></dd></dl><dl class="image">&lt;dt&gt;<img src="sp-diagnostic-logging-2.jpg" alt="sp-diagnostic-logging-2.jpg">&lt;/dt&gt;<dd>Figure: lots of "Medium" level search logs</dd></dl>This made us had 60GB logs for only 14 days.
So the solution is to change to "diagnostic logging level" as below to reduce the log size:
<dl class="image">&lt;dt&gt;<img src="sp-diagnostic-logging-3.jpg" alt="sp-diagnostic-logging-3.jpg">&lt;/dt&gt;</dl>
