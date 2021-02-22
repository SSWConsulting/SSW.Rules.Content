---
type: rule
archivedreason: 
title: DBAs - Do you increase the Log Size of your Event Viewer?
guid: ec7db65c-24e4-4a4d-9f58-dfebd5e5164a
uri: increase-the-log-size-of-your-event-viewer
created: 2019-11-22T20:19:16.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- dbas-do-you-increase-the-log-size-of-your-event-viewer

---

Change the defaults from 20480KB to 64000KB and Overwrite as needed. This will allow the users to view Security audits and errors much further into the past with a minimal increase in space - and it will never bloat your server.

<!--endintro-->


::: bad  
![Figure: Bad Example - Using a small log size](EventViewer\_BadSmallLogSize.png)  
:::


::: good  
![Figure: Good Example - Using a reasonable log size](EventViewer\_GoodReasonableLogSize.png)  
:::
