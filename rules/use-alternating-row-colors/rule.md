---
seoDescription: Enhance report readability with alternating row colors using White and Gainsboro.
type: rule
archivedreason:
title: Data Layout - Do you use alternating row colors?
guid: e0403fd3-ddbb-43e8-847b-4cb83e8180e7
uri: use-alternating-row-colors
created: 2023-12-11T14:38:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
  - when-to-use-reporting-services
redirects: []

---

For readability, always use alternating row colors.

<!--endintro-->

Use White and Gainsboro (a light shade of grey). Select the row, and enter this expression in the BackgroundColor property:

```sql
= iif(RowNumber(Nothing) Mod 2, "White", "Gainsboro")
```

::: good  
![Figure: Good example - Alternating row colors greatly improve the readability of reports, and is very easy to do in Reporting Services](RSRules_alternatingcolors.gif)
:::
