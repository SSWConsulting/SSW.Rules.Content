---
type: rule
archivedreason: 
title: Do you know how the Gated Checkin process works?
guid: cc2b35d3-ab58-48da-85a6-04bba80f019f
uri: do-you-know-how-the-gated-checkin-process-works
created: 2013-06-28T19:08:28.0000000Z
authors:
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related: []
redirects: []

---

Gated Checkins are great for verifying your project builds successfully before a checkin occurs, but the workflow and dialog messages can be difficult to follow.  Sometimes it’s not clear what you need to do next as a developer.   
<!--endintro-->

The process for a project with a Gated Checkin build is:

1. The developer clicks  **Check In**
2. Changes are not checked in, but are shelved and a build is queued
3. The developer is notified when a build succeeds and prompted to “Reconcile” their workspace


**Note:** This relies on the **Build Notifications** tool running, which may not be the case.  If it’s not running, the developer has to manually reconcile their workspace before they can effectively continue working.

![Figure: The developer is notified if a gated check-in resulted in a commit](gated-checkin-1.jpg)  

If you don't have the **Build Notifications** tool running or you click **Ignore**, you will have to manually reconcile. There are a few ways to do this.

You can click **Check In** again. This will fail, but any files you’re trying to check in will be reconciled as a result.  You should definitely not do this if you’ve made additional changes since checking in.


::: bad  
![Figure: Bad Example - Reconcile by clicking "Check In" again.  This will fail, but any files you're trying to check in will be reconciled.](gated-checkin-2.jpg)  
:::

Alternatively, you can open the queued build and choose **Actions | Reconcile Workspace...** to fix your workspace


::: good  
![Figure: OK Example – Open the Build and choose Actions | Reconcile Workspace...](gated-checkin-3.jpg)  
:::

The best way is to click the link in the notification to open a specific build window with a **Reconcile Workspace** link included.
**Note:** This notification will disappear if you close it or navigate away from the **Pending Changes** window in **Team Explorer**.


::: good  
![Figure: Good Example #1 – Click the link in the notification after clicking Check In](gated-checkin-4.jpg)  
:::

::: good  
![Figure: Good Example #2 – Click on the link in the notification to open the build, then click Reconcile Workspace when the build finishes](gated-checkin-5.jpg)  
:::

Read our suggestion to Microsoft on how to [improve the Gated Checkin workflow](http://www.ssw.com.au/ssw/standards/BetterSoftwareSuggestions/TeamFoundationServer.aspx#improve-gated-checkin).
