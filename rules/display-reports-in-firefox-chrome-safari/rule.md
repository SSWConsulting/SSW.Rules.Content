---
type: rule
archivedreason: IE is not a thing anymore - this has been resolved now in current browsers
title: Do you know how to display reports in Firefox, Chrome and Safari (SQL Reporting Services 2008R2/2012)?
guid: f0e69d45-a0ae-4411-943a-a5ebb986fe2b
uri: display-reports-in-firefox-chrome-safari
created: 2024-09-16T09:13:00.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- when-to-use-reporting-services
redirects: []

---

SQL Reporting Services works great with Internet Explorer but other browsers sometimes don’t work correctly, Here’s the solution.

<!--endintro-->

::: bad  
![Figure: Bad example - SQL RS does not work in Chrome by default](report-display-bad_1726800492478.jpg)  
:::

This issue is caused by Reporting Services emitting Quirks Mode HTML, to fix this make the following changes to the ReportingServices.js file the full path to this file is:

::: greybox
C:\Program Files\Microsoft SQL Server\MSRS10_50.MSSQLSERVER\Reporting Services\ReportManager\js\ReportingServices.js
:::

Add the following java script:

```sql
function pageLoad() {    
var element = document.getElementById("ctl31_ctl10");
if (element) 
{
       element.style.overflow = "visible"; 
} }
```

Once this change is made reports will be visible.

::: good  
![Figure: Good example - SQL RS fixed to correctly display in Chrome](report-display-good_1726800492478.jpg)
:::

More information at: [stackoverflow.com/questions/5968082/ssrs-2008-r2-reports-are-blank-in-safari-and-chrome](https://stackoverflow.com/questions/5968082/ssrs-2008-r2-ssrs-2012-reportviewer-reports-are-blank-in-safari-and-chrome)

Read [how to display reports properly for Reporting Services 2005/2008](https://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSQLReportingServices.aspx#FirefoxChromeReportDisplay20052008).
