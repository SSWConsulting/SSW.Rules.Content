---
type: rule
archivedreason: 
title: DBAs - Do you increase the Log Size of your Event Viewer?
guid: ec7db65c-24e4-4a4d-9f58-dfebd5e5164a
uri: dbas---do-you-increase-the-log-size-of-your-event-viewer
created: 2019-11-22T20:19:16.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

Change the defaults from 20480KB to 64000KB and Overwrite as needed. This will allow the users to view Security audits and errors much further into the past with a minimal increase in space - and it will never bloat your server.

<!--endintro-->
<dl class="badImage">&lt;dt&gt;<img src="EventViewer_BadSmallLogSize.png" alt="SQLDatabases_EventLog_Bad.png" style="width:665px;height:599px;"><br>&lt;/dt&gt;<dd>Figure: Bad Example - Using a small log size<br></dd></dl><dl class="goodImage">&lt;dt&gt;<img src="EventViewer_GoodReasonableLogSize.png" alt="SQLDatabases_EventLog_Bad.png" style="width:665px;height:599px;"><br>&lt;/dt&gt;<dd>Figure: Good Example - Using a reasonable log size<br></dd></dl>
