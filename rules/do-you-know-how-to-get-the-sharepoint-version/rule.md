---
type: rule
archivedreason: 
title: Do you know how to get the SharePoint version?
guid: 6083d824-bf33-47e2-9c88-6cbf86e00dec
uri: do-you-know-how-to-get-the-sharepoint-version
created: 2013-09-10T06:58:12.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

You want to be on the latest version of SharePoint.

There are multiple ways to get it:

::: bad
Check SharePoint DLL version
:::

::: bad
Check `http://<CentralAdminSite>/\_admin/FarmServers.aspx`
:::

::: good
Check `http://<AnySiteCollection>/\_vti\_pvt/service.cnf`
:::

See [Get SharePoint version number of your platform quickly](https://jeremythake.com/get-sharepoint-version-number-of-your-platform-quickly-6d092d2d1aff) for details.

<!--endintro-->

``` dotnet
vti\_encoding:SR|utf8-nl 
vti\_extenderversion:SR|16.0.0.4327  
```
**Figure: On SharePoint 2016, this is what you get for intranet.ssw.com.au for example**
