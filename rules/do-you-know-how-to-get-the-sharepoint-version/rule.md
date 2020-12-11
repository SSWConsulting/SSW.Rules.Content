---
type: rule
archivedreason: 
title: Do you know how to get the SharePoint version?
guid: 6083d824-bf33-47e2-9c88-6cbf86e00dec
uri: do-you-know-how-to-get-the-sharepoint-version
created: 2013-09-10T06:58:12.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

You want to be on the latest version of SharePoint.

There are multiple ways to get it:  



::: bad
Check SharePoint DLL version
:::



::: bad
Check http://&lt;CentralAdminSite&gt;/\_admin/FarmServers. aspx
:::





::: good
Check  http://&lt;AnySiteCollection&gt;/\_vti\_pvt/service.cnf

:::


See [http://www.jeremythake.com/2013/08/get-sharepoint-version-number-of-your-platform-quickly/](http&#58;//www.jeremythake.com/2013/08/get-sharepoint-version-number-of-your-platform-quickly/) for details.


<!--endintro-->


::: greybox
vti\_encoding:SR|utf8-nl 
vti\_extenderversion:SR|16.0.0.4327
:::


 **Figure: On SharePoint 2016, this is what you get for https://intranet.ssw.com.au for example

**
