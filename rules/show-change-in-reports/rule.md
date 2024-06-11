---
seoDescription: Showcasing changes between previous and current data enhances reports by providing valuable insights into trends and progress.
type: rule
archivedreason:
title: Data Layout - Do you show change in your reports?
guid: 7a272cbc-bdb5-44f7-9877-7e8d38690d1c
uri: show-change-in-reports
created: 2023-12-11T14:38:33.0000000Z
authors:
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
  - customization-do-you-know-which-version-of-sql-reporting-services-and-visual-studio-you-are-using
redirects: []
---

It is important to show previous and current data, as well as the changes between the two.

<!--endintro-->

::: bad  
![Figure: Bad example - Does not show the change between the previous and current data](badNoChange.jpg)  
:::

::: good  
![Figure: Good example - Shows the change between the previous and current data](goodChangeVisible.jpg)
:::

There will be cases in which the Change column has no meaning then you'd better to make this column invisible in your reports. In one of our reports we use an expression on Hidden property of this column to determine whether to show it based on the value of a parameter.

```sql
=iif(Parameters!ComparedExtractionID.Label = "N/A",true,false)
```

**Expression for Hidden property**
