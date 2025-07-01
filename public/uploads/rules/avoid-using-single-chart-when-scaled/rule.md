---
seoDescription: Avoid using a single chart when you need it to be scaled, instead use an embedded chart within the table for dynamic chart lists.
type: rule
archivedreason:
title: Data Layout - Do you avoid using a single chart when you need it to be scaled?
guid: 85eec401-261c-4054-82eb-f73c9d951160
uri: avoid-using-single-chart-when-scaled
created: 2023-12-11T14:38:33.0000000Z
authors:
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
  - customization-do-you-know-which-version-of-sql-reporting-services-and-visual-studio-you-are-using
redirects: []
---

<!--endintro-->

::: bad  
![Figure: Bad example - Just a chart - poor scaling for only 1 record](RulesToBetterBusinessIntelligence_ChartBad1.gif)  
:::

::: bad  
![Figure: Bad example - Just a chart - poorly scaling when many records](RulesToBetterBusinessIntelligence_ChartBad2.gif)  
:::

The reason for this problem is that the 'size' property of the chart control doesn't support expressions like 'Count(Rows) or queried values like 'Fields!RowCount.Value', so the chart control cannot adjust its size according to the data.

The solution for this problem is to use an embedded chart within the table - this will create a dynamic chart list similar to the list shown below.

![Figure: Size property of the chart control](ChartProperties_size.jpg)

::: good  
![Figure: Good example - A table with chart](RulesT12.gif)
:::

To do this, you need to create a table in your report and add a chart into each of the rows.

![Figure: Embedded chart in a table will generate dynamic chart list](RulesToRS-chart-1.gif)

**Note:** When rendering a report to your browser or an email, Reporting Services generates a separate image for every single image in the report, even if they are identical. When you are using graphs, images or charts in your report, this can cause a large number of images to be generated. Always include a red warning at the top of any emailed reports so that users do not try and forward or reply to them. Use a warning like this:

<span style="color:red">**Warning:** Do not reply to or forward this report in an email - Outlook may slow down or even hang.</span>
