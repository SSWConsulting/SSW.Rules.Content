---
seoDescription: Learn how to resolve report display issues in Firefox/Chrome for SQL Server Reporting Services 2005/2008
type: rule
archivedreason: IE is not a thing anymore - this has been resolved now in current browsers
title: Do you know how to display reports properly in Firefox / Chrome (Reporting Services 2005/2008)?
guid: ceec2c5c-fef2-42dd-ae29-a5ff9885020f
uri: display-reports-properly-in-firefox-chrome
created: 2024-09-16T09:14:00.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- when-to-use-reporting-services
redirects: []

---

Sometimes users try to view SQL Server Reports in Firefox or Chrome Browser, it does not display at all or displays in a half screen.

<!--endintro-->

They found it strange when the same report works absolutely fine in Internet Explorer.

::: bad  
![Figure: Bad example - SQL Report viewed in Firefox / Chrome (which does not display report properly or display only half the screen)](BadImageInFirefox.jpg)  
:::

The Solution:

Add the code below to "%ProgramFiles%\Microsoft SQL Server\MSSQL.3\ReportingServices\ReportManager\Styles\ReportingServevices.css"

```sql
 .DocMapAndReportFrame
 {
 min-height: 860px;
 min-width: 2000px;
 }
```

::: good  
![Figure: Good example - SQL Report viewed in Firefox / Chrome (which displays properly in Firefox and Chrome)](GoodImageInFirefox.jpg)
:::

Read [how to display reports properly for Reporting Services 2008R2/2012](https://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSQLReportingServices.aspx#FirefoxChromeReportDisplay20082012).
