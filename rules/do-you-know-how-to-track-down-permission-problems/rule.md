---
type: rule
archivedreason: 
title: Do you know how to track down permission problems?
guid: 5ed0bbd5-58ea-41f5-8251-3247a6caf874
uri: do-you-know-how-to-track-down-permission-problems
created: 2013-10-08T15:22:15.0000000Z
authors:
- title: Gerard Beckerleg
  url: https://ssw.com.au/people/gerard-beckerleg
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

You need     [process monitor](http://technet.microsoft.com/en-us/sysinternals/bb896645.aspx) to track down permissions problems.

E.g.      **Problem**

To hunt down a problem where say the IIS server couldn’t write to a directory, even after you have given permissions to the app pool account.

**Solution**

1. Install and run 
      [process monitor](http://technet.microsoft.com/en-us/sysinternals/bb896645.aspx)
2. Apply filter
3. Rejoice


![Figure: Apply filter to only show "ACCESS DENIED" results](process-monitor-filter.jpg)  

![Figure: And here we have the offending account](event-properties.jpg)  

<!--endintro-->
