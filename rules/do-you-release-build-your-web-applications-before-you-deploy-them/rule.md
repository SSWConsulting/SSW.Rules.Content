---
type: rule
archivedreason: 
title: Do you release build your web applications before you deploy them?
guid: 5c5fb2f8-f771-4d33-8198-357918f75db1
uri: do-you-release-build-your-web-applications-before-you-deploy-them
created: 2016-11-16T18:34:36.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- release-build-your-web-applications-before-you-deploy-them

---

Additionally to the reasons found on rule [Do you always deploy Release builds to production](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=2e8cdcb8-70e6-4fbe-b255-4d81b8b74125), there are more reasons doing this with ASP.NET

    * ASP.NET conducts a batch compilation on "release builds", which means it tries to compile all files in the current folder into one DLL
    * No resource caching is performed on debug build assemblies, which means that each request/response for a resource is not cached

According to [MSDN web developer tips](https&#58;//blogs.msdn.microsoft.com/), you can choose one of the following to release build your web application

    * In web.config file, set &lt;compilation debug="false"/&gt;
    * Disable the &lt;compilation debug="true"/&gt; switch for all ASP.NET applications on the server by setting the following in Machine.config


<!--endintro-->



```
<system.web> <deployment retail="true"/> </system.web>
```



::: good
The setting in machine.config will also turn off trace output in a page and detailed error messages remotely

:::

Machine.config file is typically located at %SystemRoot%\Microsoft.NET\Framework\%VersionNumber%\CONFIG.
