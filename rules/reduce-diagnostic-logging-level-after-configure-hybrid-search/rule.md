---
type: rule
archivedreason: 
title: Do you reduce diagnostic logging level after configure hybrid search?
guid: 8e162448-9d9e-40e9-9483-3cb91a00b2d4
uri: reduce-diagnostic-logging-level-after-configure-hybrid-search
created: 2017-04-25T23:51:08.0000000Z
authors:
- title: William Yin
  url: https://ssw.com.au/people/william-yin
related: []
redirects:
- do-you-reduce-diagnostic-logging-level-after-configure-hybrid-search

---


By default, SharePoint diagnostic logging level was set to “Information” and “Medium”, which will log quite a big info, and it increased a log after configuring “hybrid search”:<br>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image">​​​
<dt><img src="sp-diagnostic-logging.jpg" alt="sp-diagnostic-logging.jpg" /></dt><dd>Figure: default logging levels​<br></dd></dl><dl class="image"><dt><img src="sp-diagnostic-logging-2.jpg" alt="sp-diagnostic-logging-2.jpg" /></dt><dd>Figure: lots of "Medium" level search logs</dd></dl>This made us had 60GB logs for only 14 days.<p>So the solution is to change to "diagnostic logging level" as below to reduce the log size:​</p><dl class="image"><dt><img src="sp-diagnostic-logging-3.jpg" alt="sp-diagnostic-logging-3.jpg" /></dt></dl>


