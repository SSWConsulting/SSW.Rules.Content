---
type: rule
archivedreason:
title: Do you have a report which refreshes your data source?
guid: 3add728c-be25-45eb-ba58-584e23ccb117
uri: report-that-refreshes-data-source
created: 2024-09-16T09:15:00.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- when-to-use-reporting-services
redirects: []

---

If you have a SQL database data source with data coming from an external source (i.e. MYOB), then you should create a report which allows user to manually refresh data.

<!--endintro-->

Your report should have:

* A checkbox/radio button which allows user to trigger the refresh.
* A table display the history of previous refresh including start time, duration and status...

::: good  
![Figure: Good example - A report with a radio button allows you to refresh data and a table showing the history](ReportRefreshData.jpg)
:::
