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


<p class="ssw15-rteElement-P">​Change the defaults from 20480KB&#160;to 64000KB and Overwrite as needed. This will allow the users to view Security audits and errors much further into the past with a minimal increase in space - and it will never bloat your server.​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt>​<img src="/PublishingImages/EventViewer_BadSmallLogSize.png" alt="SQLDatabases_EventLog_Bad.png" style="width&#58;665px;height&#58;599px;" /><br></dt><dd>Figure&#58; Bad Example - Using a small log size<br></dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/EventViewer_GoodReasonableLogSize.png" alt="SQLDatabases_EventLog_Bad.png" style="width&#58;665px;height&#58;599px;" /><br></dt><dd>Figure&#58;&#160;Good Example - Using a ​reasonable log size<br></dd></dl>


