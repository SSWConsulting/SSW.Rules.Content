---
type: rule
archivedreason: 
title: Long Process - Do you know that you should provide a detailed summary, play a sound and hide the progress bar at the end?
guid: 4927ee44-1fde-4479-a356-c07a6798b804
uri: long-process-do-you-know-that-you-should-provide-a-detailed-summary-play-a-sound-and-hide-the-progress-bar-at-the-end
created: 2012-11-27T03:07:01.0000000Z
authors: []
related: []
redirects: []

---

Whenever a long process is churning away (e.g. about 10 seconds) users will usually do something else, either make a coffee or switch to another window.

<!--endintro-->

Your application should remind the user to go back and check on it by:

* Playing a sound
* Hiding the progress bar
* Showing a message box at the end of the long process

See rule on [Do you know how to make long-running processes user-friendly?](/long-process-do-you-know-how-to-make-long-running-processes-user-friendly)

When using Message Box to indicate user a process is done, always includes detailed summary of the process. Don't just say "Process completed."

::: greybox
Process completed.  
:::
::: bad
Figure: Bad example – No detailed information 
:::

This is just like standing at a set of traffic lights listening for the beep to know when to walk, rather than constantly looking at the red and green lights.

::: greybox
Process completed.  
Time Taken: 15 seconds   
:::
::: good  
Figure: OK Example - A completed progress form  
:::

::: greybox
100%  
Manual extraction process completed.  

Mailboxes scanned: 8  
Mailboxes skipped: 2  
Total mailboxes: 10  
Time Taken: 10 minutes, 15 seconds  
:::
::: good
Figure: Good example – The user can see what has been processed
:::
