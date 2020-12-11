---
type: rule
archivedreason: 
title: Long Process - Do you show the status of progress bar on winform's title?
guid: c2741651-fcb9-402e-81ae-f38991c48037
uri: long-process---do-you-show-the-status-of-progress-bar-on-winforms-title
created: 2012-11-27T02:59:56.0000000Z
authors: []
related: []

---

The importance of having the status of progress bar on winform's title:

* Users can clearly see the progress status.
* If the winform is minimized to taskbar, users still can see the progress status.


<!--endintro-->

The form title should take the form of "[XX]% Completed - [Task Description] - [Product Name]".
There is another relevant rule about the [winform title](http://www.ssw.com.au/ssw/Standards/Rules/RulestoBetterInterfaces-Windows-Applications.aspx#TitleBarCaption).
<dl class="badImage">&lt;dt&gt;<img width="420" height="222" src="../../assets/BadProgressForm.gif" alt="Winform's title without progress status">&lt;/dt&gt;
<dd>Figure: Bad Example - The winform's title does not contain the progress status</dd></dl><dl class="goodImage">&lt;dt&gt;<img width="580" height="489" src="../../assets/GoodProgressForm.gif" alt="Winform's title with progress status">&lt;/dt&gt;
<dd>Figure: Good Example - The winform's title contains the status of progress bar</dd></dl><dl class="goodImage">&lt;dt&gt;<img src="../../assets/GoodProgressFormTaskbar.gif" alt="Winform's title with progress status (Taskbar)" style="width:550px;">&lt;/dt&gt;
<dd>Figure: Good Example - You can clearly see the progress status from taskbar when you have the windows minimized</dd></dl><dl class="goodImage">&lt;dt&gt;<img src="../../assets/TaskBarProgress.png" alt="Winform's title with progress status (Taskbar)">&lt;/dt&gt;
<dd>Figure: Good Example - Windows 7 shows the progress in the taskbar (which is visible even when the application is minimized)</dd></dl>
