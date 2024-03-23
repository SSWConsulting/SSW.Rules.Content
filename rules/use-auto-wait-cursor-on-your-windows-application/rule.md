---
type: rule
title: Do you use Auto wait cursor on your windows application?
uri: use-auto-wait-cursor-on-your-windows-application
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T02:02:00.000Z
guid: 4aa7ca6d-e9fe-4d11-933a-bf2095c4efe4
---
It can be extremely tiresome to have to continually remember to set and unset the wait cursor for an application. If an exception occurs you have to remember to add a try finally block to restore the cursor, or if you popup a message box you must remember to change the cursor first otherwise the user will just sit there thinking the application is busy. 

<!--endintro-->

::: bad
![Figure: Bad example - Cursor set manually](autowaitcursor_bad.jpg)
:::

::: good
![Figure: Good example - Implemented Auto wait cursor](autowaitcursor_good.jpg)
:::

We use AutoWaitCursor Class that automatically monitors the state of an application and sets and restores the cursor according to whether the application is busy or not. All that required are a few lines of setup code and your done. [see this great blog on how to use AutoWaitCursor.](http://snipplr.com/view/24851/) If you have a multithreaded application, it won't change the cursor unless the main input thread is blocked. Infact you can remove all of your cursor setting code everywhere!
