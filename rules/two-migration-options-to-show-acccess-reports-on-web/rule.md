---
type: rule
archivedreason: SSW Access Reporter is no longer supported
title: Do you know your 2 migration options to show your Access reports on the web?
guid: 1dd7391c-30cd-4585-90c6-f81e09856c24
uri: two-migration-options-to-show-acccess-reports-on-web
created: 2023-12-12T11:38:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- customization-do-you-know-which-version-of-sql-reporting-services-and-visual-studio-you-are-using
redirects: []

---

<!--endintro-->

The greatest advantage for Access Developers is that with Reporting Services your reports can become available on the web. If you have a heap of Access reports, what are the choices for getting them on the web?

1. Keep the existing reports in Access and expose them on the web with [SSW Access Reporter](https://ssw.com.au/ssw/accessreporter/). This is the least amount of work, as SSW Access Reporter is a utility that delivers existing Access reports online with minimal re-coding. [Download a free trial](https://ssw.com.au/ssw/accessreporter/) today and try it out for yourself.

::: good  
![Figure: Good Example - If you want to avoid migrating then SSW Access Reporter delivers your Access reports online so you can view them anywhere](ReportManager.gif)
:::

2. Import the reports into Reporting Services. Reporting Services has built-in support for importing and converting reports from Access. We have had plenty of success with it, but you will need to re-code things like conditional formatting and any code behind.

::: good  
![Figure: Good Example - Reporting Services has built-in support for importing your Access reports](rsrulesimportreports.gif)
:::
