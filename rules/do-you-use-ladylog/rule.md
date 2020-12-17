---
type: rule
archivedreason: Has been replaced by Application Insights
title: Do you use LadyLog?
guid: 174015a0-7bf7-436c-9893-8821bb230722
uri: do-you-use-ladylog
created: 2013-09-11T21:50:56.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

Your users should never see the "unhandled exception" message in Windows Forms, WPF and Silverlight. You should always log errors somewhere (preferably a SQL database).

<!--endintro-->
<dl class="badImage">&lt;dt&gt;
      <img src="ladylog-bad.jpg" alt="">
   &lt;/dt&gt;<dd>Figure: Bad example - your users should never have unhandled exceptions in Windows Forms</dd></dl>
LadyLog is a Windows UI for your application that allows users to Log meaningful errors.
<dl class="goodImage">&lt;dt&gt;
      <img src="ladylog-good.jpg" alt="">
   &lt;/dt&gt;<dd>Figure: Good example - your users get a nice professional error reporting window</dd></dl>
See     [SSW .NET Toolkit - LadyLog](http://www.ssw.com.au/ssw/NetToolKit/04ExceptionReporter.aspx).

We have a program called [SSW Code Auditor](http://www.ssw.com.au/ssw/CodeAuditor/Default.aspx) to check for this rule.
