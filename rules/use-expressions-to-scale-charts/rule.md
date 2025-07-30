---
seoDescription: Data Layout - Use expressions to show the correct scale on charts, ensuring accurate visualization of data in Reporting Services 2005.
type: rule
archivedreason:
title: Data Layout - Do you use expressions to show the correct scale on charts?
guid: c74b30a3-3593-4b32-a996-6dd96256ab07
uri: use-expressions-to-scale-charts
created: 2023-12-11T14:38:33.0000000Z
authors:
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
  - customization-do-you-know-which-version-of-sql-reporting-services-and-visual-studio-you-are-using
redirects: []
---

<!--endintro-->

In Reporting Services 2005 you can use an expression to specify the scale of your charts. If you do not specify a maximum value for your y axis, the bar charts become inaccurate, as you can see in this figure.

::: bad  
![Figure: Bad example - With no scale value set, the charts do not display based on the correct scale](RSRulesChartBad.gif)  
:::

Here's how to set the scale.

1. In Layout view, add a new row to the bottom of the table

2. At the bottom of the column with the chart, set the textbox value to =Max(Fields!MyTotal.Value), where "MyTotal" is the Data field you're using in the chart.

![Figure: Add a new row to your table and set the max value](RSRulesChart01.gif)

3. Set the textbox's Name property to MaxMyTotal (e.g. MaxCount)

4. Set the new row's Visibility/Hidden property to true - you don't want to show it in the report

5. Open the Chart properties and select the "Y Axis" tab

6. Set the Maximum value to the value of the textbox, i.e. "=ReportItems!MaxMyTotal.Value"

![Figure: Set the maximum value to the value of the textbox](RSRulesChart02.gif)

7. If you expect to have negative values in the chart (e.g. when comparing 2 values), set the Minimum to -1 multiplied by the max value, i.e. "=-1 \* ReportItems!MaxMyTotal.Value". Otherwise set it to 0 (zero).

8. If you expect to have negative values in the chart, select the chart value in the Data tab and click "Edit..." . Go to **Appearance->Series Style->Fill** and enter the following expression:

```sql
=iif(Fields!Change.Value > 0, "Green", "Red")
```

Where "Change" is the name of your data field. This sets the color of the bar to green if it is positive, and red if it is negative

9. Click OK and preview the report. The chart will now be using the maximum value across all the charts.

::: good  
![Figure: Good example - The scale is now correct](RSRulesChart03.gif)
:::

::: greybox
This way is tedious and a "hack". We think that the scale should be automatically set with an option to customize it via an expression. See our suggestion about this on [Microsoft SQL Reporting Services Suggestions](https://www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/ReportingServices.aspx#ChartExpressions).

Updated - fixed by Microsoft, see <https://learn.microsoft.com/en-us/sql/reporting-services/report-design/set-a-minimum-or-maximum-on-a-gauge-report-builder-and-ssrs?view=sql-server-ver16>&WT.mc_id=DP-MVP-33518
:::
