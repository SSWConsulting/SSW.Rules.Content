---
seoDescription: Handle exceptions in your ASP.NET application effectively with a generic exception handler in Global.asax, ensuring unhandled errors are logged and notified.
type: rule
title: Do you have generic exception handler in your Global.asax?
uri: have-generic-exception-handler-in-your-global-asax
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-have-generic-exception-handler-in-your-global-asax
created: 2016-08-25T14:47:18.000Z
archivedreason: null
guid: c2e66516-0d81-493e-a878-3fbd2fc96607
---

Add your code to handle generic exception of your ASP.NET application in Application_Error.

<!--endintro-->

```cs
private static readonly ILog log = LogManager.GetLogger(typeof(MvcApplication));

protected void Application_Error(object sender, EventArgs e)
{
    Exception ex = Server.GetLastError().GetBaseException();
    log.Fatal("Unhandled Exception", ex);
}
```

**Figure. Exception handler in Global.asax.cs**
