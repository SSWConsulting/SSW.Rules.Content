---
type: rule
archivedreason: 
title: Do you know how to track down permission problems?
guid: 5ed0bbd5-58ea-41f5-8251-3247a6caf874
uri: do-you-know-how-to-track-down-permission-problems
created: 2013-10-08T15:22:15.0000000Z
authors:
- id: 33
  title: Gerard Beckerleg
- id: 1
  title: Adam Cogan
related: []

---

You need     [process monitor](http://technet.microsoft.com/en-us/sysinternals/bb896645.aspx) to track down permissions problems.

E.g.      **Problem**

To hunt down a problem where say the IIS server couldn’t write to a directory, even after you have given permissions to the app pool account.

**Solution**

1. Install and run <br>      [process monitor](http://technet.microsoft.com/en-us/sysinternals/bb896645.aspx)
2. Apply filter
3. Rejoice

<dl class="image">&lt;dt&gt;
      <img src="process-monitor-filter.jpg" alt="">
   &lt;/dt&gt;<dd>Figure: Apply filter to only show "ACCESS DENIED" results</dd></dl><dl class="image">&lt;dt&gt;
         <img src="event-properties.jpg" alt="">
      &lt;/dt&gt;<dd>Figure: And here we have the offending account</dd></dl>
<!--endintro-->
