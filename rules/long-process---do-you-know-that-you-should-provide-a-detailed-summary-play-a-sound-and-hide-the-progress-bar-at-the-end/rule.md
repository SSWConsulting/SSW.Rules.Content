---
type: rule
archivedreason: 
title: Long Process - Do you know that you should provide a detailed summary, play a sound and hide the progress bar at the end?
guid: 4927ee44-1fde-4479-a356-c07a6798b804
uri: long-process---do-you-know-that-you-should-provide-a-detailed-summary-play-a-sound-and-hide-the-progress-bar-at-the-end
created: 2012-11-27T03:07:01.0000000Z
authors: []
related: []

---

Whenever a long process is churning away (e.g. about 10 seconds) users will usually do something else, either make a coffee or switch to another window.

<!--endintro-->

Your application should remind the user to go back and check on it by:

* Playing a sound
* Hiding the progress bar
* Showing a message box at the end of the long process


See rule on [Do you know how to make long-running processes user-friendly?](http://www.ssw.com.au/ssw/Standards/Rules/RulestoBetterInterfaces-Windows-Applications.aspx#LongProcessFriendly)

When using Message Box to indicate user a process is done, always includes detailed summary of the process. Don't just say "Process completed."
<dl class="badImage">&lt;dt&gt;<div style="width:40%;">Process completed. </div>&lt;/dt&gt;
<dd>Figure: Bad example – No detailed information</dd></dl>
This is just like standing at a set of traffic lights listening for the beep to know when to walk, rather than constantly looking at the red and green lights.
<dl class="goodImage">&lt;dt&gt;<img alt="Completed Progress Form" src="../../assets/ProgressBarComplete.gif">&lt;/dt&gt;
<dd>Figure: OK Example - A completed progress form</dd></dl><dl class="goodImage">&lt;dt&gt;<div style="width:40%;">Manual extraction process completed.<br><br>Mailboxes scanned: 8<br>Mailboxes skipped: 2<br>Total mailboxes: 10<br>Time Taken: 10 minutes, 15 seconds </div>&lt;/dt&gt;
<dd>Figure: Good example – The user can see what has been processed</dd></dl>
