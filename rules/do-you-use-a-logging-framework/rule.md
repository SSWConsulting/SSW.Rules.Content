---
type: rule
title: Do you use a logging framework?
uri: do-you-use-a-logging-framework
created: 2012-04-01T09:53:00.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 23
  title: Damian Brady
- id: 78
  title: Matt Wicks

---



<span class='intro'> <p class="MsoListParagraph"><span lang="EN-AU">Unless you are writing a Console application, any output that uses Console.WriteLine will almost certainly be lost.&#160; You're much better off using Trace.WriteLine.</span></p>
<p class="MsoListParagraph"><span lang="EN-AU">A better approach is to use Trace.WriteLine. You can create a trace listener to send your Trace.WriteLine statements to the Console if you wish, but you can also redirect them elsewhere if required.&#160;See <a href="http&#58;//msdn.microsoft.com/en-us/library/sk36c28t.aspx">this MSDN article for more information</a>.</span></p>
 </span>

<p class="ssw15-rteElement-CodeArea"><span lang="EN-AU">Console.WriteLine(&quot;Service started&quot;);​</span></p><dd class="ssw15-rteElement-FigureBad"><span lang="EN-AU"></span>​&#160;Figure&#58; Bad Example - Using Console.WriteLine to write debug information</dd><p class="ssw15-rteElement-CodeArea">Trace.WriteLine(&quot;Service started&quot;);​​</p><dd class="ssw15-rteElement-FigureGood">​​&#160;Figure&#58; Better Example - Using Trace.WriteLine to write debug informatio</dd><p>The best approach is to use a logging framework like Serilog. You can direct output to different sinks (e.g. log file, database, table storage or Application Insights), include structured objects as well and filter output based off severity (Verbose/Debug/Info/Warning/Error).<br></p><p class="ssw15-rteElement-CodeArea">Log.Debug(“Service started”);&#160;​​<br></p><dd class="ssw15-rteElement-FigureGood">​​Figure&#58; Best Example – Using Serilog to write debug information<br></dd>


