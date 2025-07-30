---
seoDescription: Learn how displaying zero numbers as blank in reports enhances readability using formats like '#,#' for cleaner data presentation.
type: rule
archivedreason:
title: Data Layout - Do you display zero number as blank in reports?
guid: 05330d1a-22b5-4f50-aa67-7b9a13605f25
uri: display-zero-number-as-blank
created: 2023-12-11T14:38:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- when-to-use-reporting-services
redirects: []

---

It looks better to display zero numbers as blank than to leave lots of '0' in a report.

<!--endintro-->

::: bad  
![Figure: Bad example - Bad zero number format](AvoidZeroNum_Bad.gif)  
:::

::: good  
![Figure: Good example - Good zero number format](AvoidZeroNum_good.gif)
:::

It's easy to do with a simple format code '#,#'.

![Figure: Format code](AvoidZeroNum_format.gif)
