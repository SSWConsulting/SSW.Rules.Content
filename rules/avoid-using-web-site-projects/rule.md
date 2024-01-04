---
type: rule
archivedreason: 
title: Do you avoid using Website Projects?
guid: 92494cb4-d366-4b72-a042-0f434029e3ae
uri: avoid-using-web-site-projects
created: 2016-11-16T18:41:17.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-avoid-using-web-site-projects

---

If you're creating new web apps in ASP.NET 2.0, do you still use  **Website projects** ? We strongly recommend using the new  **Web Application projects** .

What's the difference between the two? There is a [detailed comparison here](https&#58;//msdn.microsoft.com/en-us/library/aa730880%28VS.80%29.aspx#wapp_topic5), but to summarize:

<!--endintro-->

* **Website projects**  have no project file and it creates multiples assemblies. (This result in a lot of annoying scenarios.)
* **Web Application projects**  have a physical project file and along with all other standalone classes within the project are compiled into a single assembly.

Please see our kb - [How to upgrade VS 2005 website Projects to be VS 2005 Web Application Projects?](https&#58;//www.ssw.com.au/ssw/KB/KB.aspx?KBID=Q1993822) to do the upgrade.
