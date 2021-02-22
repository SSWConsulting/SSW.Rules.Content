---
type: rule
archivedreason: 
title: Do you use a logging framework?
guid: 37153c77-e1af-4d82-a200-1ab7fbb6d0b2
uri: do-you-look-for-console-writeline-and-change-it-to-trace-writeline
created: 2012-04-01T09:53:00.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
- title: Matt Wicks
  url: https://ssw.com.au/people/matt-wicks
related: []
redirects:
- do-you-use-a-logging-framework

---

Unless you are writing a Console application, any output that uses Console.WriteLine will almost certainly be lost.  You're much better off using Trace.WriteLine.

A better approach is to use Trace.WriteLine. You can create a trace listener to send your Trace.WriteLine statements to the Console if you wish, but you can also redirect them elsewhere if required. See [this MSDN article for more information](http&#58;//msdn.microsoft.com/en-us/library/sk36c28t.aspx).

<!--endintro-->



```
Console.WriteLine("Service started");
```




::: bad
 Figure: Bad Example - Using Console.WriteLine to write debug information  
:::



```
Trace.WriteLine("Service started");
```




::: good
 Figure: Better Example - Using Trace.WriteLine to write debug informatio  
:::

The best approach is to use a logging framework like Serilog. You can direct output to different sinks (e.g. log file, database, table storage or Application Insights), include structured objects as well and filter output based off severity (Verbose/Debug/Info/Warning/Error).



```
Log.Debug(“Service started”);
```




::: good
Figure: Best Example – Using Serilog to write debug information

:::
