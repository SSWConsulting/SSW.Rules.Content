---
seoDescription: Ensure accurate downloads by detecting client CLR versions and offering Setup.exe or .application files accordingly.
type: rule
title: Do you set the appropriate download (.exe or .application) for your web users?
uri: set-the-appropriate-download-for-your-web-users
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T02:17:00.000Z
archivedreason: outdated
guid: 4596ed75-d396-487e-a189-eb5b3f80b315
---

In general, you should set the user to download the Setup.exe of your ClickOnce application. However there are many cases where the only prerequisite of the application is .NET 2, and the users don't need the Setup.exe. Instead, the .application file would allow the user to install the application, or run it instantly if they already have .Net 2. The following code allows you to check for the .NET 2 runtime on the client's machine (note: `Request.Browser.ClrVersion` may return 0.0 on some browsers).

<!--endintro-->

```vb
dim verHave as Version = Request.Browser.ClrVersion
dim verNeed as Version = new Version("2.0.50727")

if ( verHave < verNeed ) then
    Response.Write("<a href=""./Download/Setup.exe"">")
else
    Response.Write("<a href=""./Download/SSWDiagnostics.application"">")
end if
```

**Figure: Code to detect the client's CLR version and offers the download accordingly**
