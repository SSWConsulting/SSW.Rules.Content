---
seoDescription: Data layout best practices advise against showing change as a percentage when comparing data sets, instead opting for actual value differences.
type: rule
archivedreason:
title: Data Layout - Do you avoid showing change as a percentage?
guid: 229d49cb-d31a-4577-8d4c-1473ba74e4a5
uri: avoid-showing-change-as-percentage
created: 2023-12-11T14:38:33.0000000Z
authors:
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
  - customization-do-you-know-which-version-of-sql-reporting-services-and-visual-studio-you-are-using
redirects: []
---

When comparing two sets of data in a report (for example, sales this month compared to last), showing the change as a percentage is a bad idea.

<!--endintro-->

For example, if you made 1 sale last month and 2 this month, you have had a 100% increase. If for another product you made 1000 sales last month and 2000 this month, that is also a 100% increase, but you've sold 1000 of that product compared to 1 of the other product.

For this reason, show the difference as an actual value, so you can compare all values easily. See the figures below for examples. To see how to create the negative/positive valued chart, see [Do you use expressions to show the correct scale on charts?](https://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSQLReportingServices.aspx#maxminvalues)

**Bad** - Notice how the "change" column in the report doesn't accurately reflect the difference in downloads - 1 download last month and 2 downloads this month will yield a 100% increase - which looks impressive as a percentage but really isn't.

::: bad  
![Figure: Bad example - The percentage change column in this Reporting Services product downloads report is misleading](productdownloadgraph_rs2005_bad.gif)  
:::

**Good** - This works better just showing the difference between the two values over the 2 months.

::: good  
![Figure: Good example - The column works better as just a difference between the current and previous download totals](productdownloadgraph_rs2005_good.gif)
:::
