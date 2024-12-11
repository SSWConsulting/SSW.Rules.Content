---
type: rule
archivedreason:
title: Do you use the correct authentication for reports?
guid: e619bac7-d1f3-4549-949c-0113ddcfa6ca
uri: use-correct-authentication-for-report
created: 2024-09-16T09:06:00.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- when-to-use-reporting-services
redirects: []

---

Using anonymous authentication is not recommended because of security reasons.

<!--endintro-->

* Anonymous accounts (the IUSER_*and IWAM_* accounts) are managed by windows security system. We do not want to use these accounts because we have to manually configure our report server security settings.
* We do not want everyone on the Internet update or overwrite stuffs on the report server. Besides, anonymous authentication is no longer supported in RS 2008.

The best way to expose your report is to use ReportViewer and setup the credentials on it using ReportViewerCredentials.

```csharp
Dim userName As String = ConfigurationManager.AppSettings("ReportViewer_UserName")
Dim password As String = ConfigurationManager.AppSettings("ReportViewer_Password")
Dim domain As String = ConfigurationManager.AppSettings("ReportViewer_UserDomain")
reportViewer.ServerReport.ReportServerCredentials = New ReportViewerCredential(userName, password, domain)

Dim paramList As List(Of ReportParameter) = New List(Of ReportParameter)
paramList.Add(New ReportParameter("ClientContactID", mintClientContactID, False))
reportViewer.ServerReport.SetParameters(paramList)
```

::: info
**Warning:** This is only supported for .NET Full Framework because of the ReportViewer component.
:::
