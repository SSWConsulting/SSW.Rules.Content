---
type: rule
archivedreason: 
title: Do you know how the Gated Checkin process works?
guid: cc2b35d3-ab58-48da-85a6-04bba80f019f
uri: do-you-know-how-the-gated-checkin-process-works
created: 2013-06-28T19:08:28.0000000Z
authors:
- id: 23
  title: Damian Brady
related: []

---


Gated Checkins are great for verifying your project builds successfully before a checkin occurs, but the workflow and dialog messages can be difficult to follow.  Sometimes it’s not clear what you need to do next as a developer.


<br><excerpt class='endintro'></excerpt><br>
<p>​​The process for a project with a Gated Checkin build is&#58;</p><ol><li>The developer clicks 
      <strong>Check In</strong></li><li>Changes are not checked in, but are shelved and a build is queued</li><li>The developer is notified when a build succeeds and prompted to “Reconcile” their workspace</li></ol><p> 
   <strong>Note&#58;</strong> This relies on the 
   <strong>Build Notifications</strong> tool running, which may not be the case.  If it’s not running, the developer has to manually reconcile their workspace before they can effectively continue working.</p> ​ 
<dl class="image"><dt>
      <img src="/PublishingImages/gated-checkin-1.jpg" alt="" />
   </dt><dd>Figure&#58; The developer is notified if a gated check-in resulted in a commit</dd></dl><p>If you don't have the 
   <strong>Build Notifications</strong> tool running or you click 
   <strong>Ignore</strong>, you will have to manually reconcile. There are a few ways to do this.</p><p>You can click 
   <strong>Check In</strong> again.  This will fail, but any files you’re trying to check in will be reconciled as a result.  You should definitely not do this if you’ve made additional changes since checking in.</p><dl class="badImage"><dt>
      <img src="/PublishingImages/gated-checkin-2.jpg" alt="" />
   </dt><dd>Figure&#58; Bad Example - Reconcile by clicking &quot;Check In&quot; again.  This will fail, but any files you're trying to check in will be reconciled.</dd></dl><p>Alternatively, you can open the queued build and choose 
   <strong>Actions | Reconcile Workspace...</strong> to fix your workspace</p><dl class="goodImage"><dt>
      <img src="/PublishingImages/gated-checkin-3.jpg" alt="" />
   </dt><dd>Figure&#58; OK Example – Open the Build and choose Actions | Reconcile Workspace...</dd></dl><p>The best way is to click the link in the notification to open a specific build window with a 
   <strong>Reconcile Workspace</strong> link included.<br> 
   <strong>Note&#58;</strong> This notification will disappear if you close it or navigate away from the 
   <strong>Pending Changes</strong> window in 
   <strong>Team Explorer</strong>.</p><dl class="goodImage"><dt>
      <img src="/PublishingImages/gated-checkin-4.jpg" alt="" />
   </dt><dd>Figure&#58; Good Example #1 – Click the link in the notification after clicking Check In</dd></dl><dl class="goodImage"><dt>
      <img src="/PublishingImages/gated-checkin-5.jpg" alt="" />
   </dt><dd>Figure&#58; Good Example #2 – Click on the link in the notification to open the build, then click Reconcile Workspace when the build finishes</dd></dl><p>Read our suggestion to Microsoft on how to<a href="http&#58;//www.ssw.com.au/ssw/standards/BetterSoftwareSuggestions/TeamFoundationServer.aspx#improve-gated-checkin">improve the Gated Checkin workflow</a>.</p>


