---
type: rule
archivedreason: WebForms is three technologies behind - WebForms, then MVC, then .NET Core with Controllers, then .NET Core with minimal APIs
title: Do you know to embed an RS report in ASP.NET page the right way (using Report Viewer instead of IFrame)?
guid: a09c4313-0c5b-4ee9-9095-ed2a01d43e9e
uri: embed-rs-report-in-asp-net-page
created: 2024-09-16T09:01:00.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- when-to-use-reporting-services
redirects: []

---

::: info
**Warning:** This rule is obsolete and has been replaced with [Do you know the best way to do printable reports?](https://www.ssw.com.au/rules/do-you-know-the-best-way-to-do-printable-reports)
:::

Visual Studio provides a Report Viewer control for WebForms, so use it instead of the old IFrame method. The report viewer control is super easy to use - just drag the control into your page designer and select the properties you like.

<!--endintro-->

The bad old way was to use an IFrame and point it to the report's URL (including parameters). This is bad because you might encounter a typing error. If you want to disable vertical scrollbar, you need to adjust the height of IFrame manually. Furthermore, you can't configure the report's authentication separately.

```sql
<IFRAME width="100%" height="700" TITLE="Report" src="http://reports.internal.ssw.com.au/ReportServer?
    %2fTimeProOnlineReports%2fClientRegisteredProductsByDate
    &rs:Command=Render&ClientContactID=<%=mintClientContactID%>&ClientExInfo=<%=clientInfo%>&rc:Parameters=false">
</IFRAME>                      
```

::: bad  
Bad Example - Embed report using IFrame
:::

```sql
<rsweb:ReportViewer ID="ReportViewer1" runat="server" SizeToReportContent="True" ProcessingMode="Remote" Width="100%" AsyncRendering="false">
    <ServerReport ReportServerUrl="http://reports.internal.ssw.com.au/reportserver"
    ReportPath="/TimeProOnlineReports/ClientRegisteredProductsByDate" />
</rsweb:ReportViewer>
```

::: good  
Good Example - Embed report using Report Viewer
:::

::: bad  
![Figure: Bad example - IFrame with vertical scrollbar](IFrame.gif)  
:::

::: good  
![Figure: Good example - Report Viewer without vertical scrollbar](ReportViewer.gif)
:::
