---
type: rule
title: Do you avoid using Web Site Projects?
uri: do-you-avoid-using-web-site-projects
created: 2016-11-16T18:41:17.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>If you're creating new web apps in ASP.NET 2.0, do you still use&#160;<strong>Web Site projects</strong>? We strongly recommend using the new&#160;<strong>Web Application projects</strong>.</p><p>What's the difference between the two? There is a&#160;<a href="https&#58;//msdn.microsoft.com/en-us/library/aa730880%28VS.80%29.aspx#wapp_topic5" target="_blank">detailed comparison here</a>, but to summarize&#58;​​<br></p> </span>

<ul><li><strong>Web Site projects</strong>&#160;have no project file and it creates multiples assemblies. (This result in a lot of annoying scenarios.)</li><li><strong>Web Application projects</strong>&#160;have a physical project file and along with all other standalone classes within the project are compiled into a single assembly.<br></li></ul><p>Please see our kb -&#160;<a href="https&#58;//www.ssw.com.au/ssw/KB/KB.aspx?KBID=Q1993822">How to upgrade VS 2005 Web Site Projects to be VS 2005 Web Application Projects?</a>&#160;to do the upgrade. ​​<br><br></p>


