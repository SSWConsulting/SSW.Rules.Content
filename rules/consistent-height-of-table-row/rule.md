---
seoDescription: Ensure your tables have consistent row heights for a professional appearance in all reports.
type: rule
archivedreason:
title: Data Layout - Do you have consistent height of table row across all your reports?
guid: 8ae8f2c2-b0f2-4a55-8233-ee86ab6a3f33
uri: consistent-height-of-table-row
created: 2024-06-03T15:38:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
  - when-to-use-reporting-services
redirects: []

---

Same height of table row across all reports gives users consistent and professional impression.
<!--endintro-->

We use the default height of table row (0.63492cm) as a standard to make sure all tables in our reports have consistent row height.

This rule also applies to height of Textbox in all reports.

::: bad  
![Figure: Bad example - Bad Height](RowHeight_Bad.gif)  
:::

::: good  
![Figure: Good example - Good Height](RowHeight_Good.gif)
:::

::: bad  
![Figure: Bad example - Bad Height In Design View](RSRowHeight_NonStandard_design.jpg)  
:::

::: good  
![Figure: Good example - Good Height In Design View](RSRowHeight_Standard_design.jpg)
:::

::: greybox
We have a program called [SSW Code Auditor](https://codeauditor.com) to check for this rule.
:::
