---
type: rule
archivedreason: 
title: Do you know when to use BCS?
guid: c29408c9-17df-4cba-b354-70f1f0ffb70b
uri: do-you-know-when-to-use-bcs
created: 2010-06-04T05:43:44.0000000Z
authors:
- title: Paul Neumeyer
  url: https://ssw.com.au/people/paul-neumeyer
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---


  If you want an easy way to access data in remote or legacy systems, provide one or more of the CRUD operations to the end users and search the data within the SharePoint search framework, then you should consider BCS. You can also use MS Office applications to access the data from SharePoint.<br>
<br>
However, BCS doesn't do everything.  It does not provide support for WorkFlow or EventReceivers on the list in SharePoint.  <br>
<br>
BCS is good for synchronising the data at SharePoint with one other system.  It is not suitable for publishing the data to multiple systems (i.e. syndication). If you need to implement syndication, use a standard SharePoint List and attach either a Workflow or an EventReceiver to handle sending updates to the end systems instead.<br>
<br>

<br><excerpt class='endintro'></excerpt><br>
  <br>
<br>
<img alt="" src="BCSBadExample.jpg" /> <br>
<font size="+0" class="ms-rteCustom-FigureBad">Use BCS with multiple systems(not working)<br>
</font><br>
<br>
<img alt="" src="BCSGoodExample.jpg" /><br>
<font size="+0" class="ms-rteCustom-FigureGood">Use BCS with one system at time</font><br>
<br>



