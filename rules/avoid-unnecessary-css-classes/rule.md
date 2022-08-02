---
type: rule
title: do you avoid unnecessary CSS classes?
uri: avoid-unnecessary-css-classes
authors:
  - title: Geordie Robinson
    noimage: true
  - title: Tiago Araujo
    url: https://www.ssw.com.au/people/tiago-araujo
created: 2022-07-28T06:06:37.551Z
guid: ca1b7770-298b-4035-b45d-a570fa0ee77b

---
When making or editing CSS or HTML content it is important to avoid adding classes and ID's unnecessarily.

It can be tempting to add classes on elements, it is often the most obvious solution to CSS problems but doing so will lead to overly cluttered code and a host of overly specific solutions. When working on CSS it is almost always better to remove content rather than adding additional classes. 

<!--endintro-->

::: bad
![Figure: Bad Example - The "View-All-Link" class is unessessary because the "arrow-next" class already exists](unessessary-class.jpg)
:::

::: good
![Figure: Good Example - Instead of making an additional class, use the "arrow-next" class with an additional modifier](good-css-class.jpg)
:::
