---
type: rule
archivedreason: 
title: Long Process - Do you show the status of progress bar on winform's title?
guid: c2741651-fcb9-402e-81ae-f38991c48037
uri: long-process-do-you-show-the-status-of-progress-bar-on-winforms-title
created: 2012-11-27T02:59:56.0000000Z
authors: []
related: []
redirects: []

---

The importance of having the status of progress bar on winform's title:

* Users can clearly see the progress status
* If the winform is minimized to taskbar, users still can see the progress status


<!--endintro-->

The form title should take the form of "[XX]% Completed - [Task Description] - [Product Name]".

There is another relevant rule about the [winform title](/title-bar-do-you-put-the-current-document-project-name-as-the-first-word-of-your-title-bar).

::: bad  
![Figure: Bad Example - The winform's title does not contain the progress status](../../assets/BadProgressForm.gif)  
:::

::: good  
![Figure: Good Example - The winform's title contains the status of progress bar](../../assets/GoodProgressForm.gif)  
:::

::: good  
![Figure: Good Example - You can clearly see the progress status from taskbar when you have the windows minimized](../../assets/GoodProgressFormTaskbar.gif)  
:::

::: good  
![Figure: Good Example - Windows 7 shows the progress in the taskbar (which is visible even when the application is minimized)](../../assets/TaskBarProgress.png)  
:::
