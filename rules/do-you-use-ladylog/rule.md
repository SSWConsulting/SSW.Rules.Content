---
type: rule
archivedreason: Has been replaced by Application Insights
title: Do you use LadyLog?
guid: 174015a0-7bf7-436c-9893-8821bb230722
uri: do-you-use-ladylog
created: 2013-09-11T21:50:56.0000000Z
authors:
- title: Adam Cogan
  url: /people/adam-cogan
related: []
redirects: []

---

Your users should never see the "unhandled exception" message in Windows Forms, WPF and Silverlight. You should always log errors somewhere (preferably a SQL database).

<!--endintro-->


::: bad  
![Figure: Bad example - your users should never have unhandled exceptions in Windows Forms](ladylog-bad.jpg)  
:::

LadyLog is a Windows UI for your application that allows users to Log meaningful errors.


::: good  
![Figure: Good example - your users get a nice professional error reporting window](ladylog-good.jpg)  
:::

See     [SSW .NET Toolkit - LadyLog](http://www.ssw.com.au/ssw/NetToolKit/04ExceptionReporter.aspx).

We have a program called [SSW Code Auditor](http://www.ssw.com.au/ssw/CodeAuditor/Default.aspx) to check for this rule.
