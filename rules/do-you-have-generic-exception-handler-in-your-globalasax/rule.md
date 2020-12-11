---
type: rule
archivedreason: 
title: Do you have generic exception handler in your Global.asax?
guid: c2e66516-0d81-493e-a878-3fbd2fc96607
uri: do-you-have-generic-exception-handler-in-your-globalasax
created: 2016-08-25T14:47:18.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

Add your code to handle generic exception of your ASP.NET application in Application\_Error.

<!--endintro-->

private static readonly ILog log = LogManager.GetLogger(typeof(MvcApplication));

        protected void Application\_Error(object sender, EventArgs e)
        {
            Exception ex = Server.GetLastError().GetBaseException();
            log.Fatal("Unhandled Exception", ex);
        }
 **Figure. Exception handler in Global.asax.cs
**
