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
```
.View-All-Link{
  float: right;
  padding-top: 16.8px;
  padding-right: 20px;
}
```
![Figure: Bad Example - The "View-All-Link" class was added unnecessarily]
:::

::: good
```
<a target="_blank" rel="noopener noreferrer float-right" class="float-right" 
href="https://www.youtube.com/playlist?list=PLIzW_0dAIKv3mjBeK8eyJbe1bOGWJX_UV">View All</a>
```
![Figure: Good Example - Using the bootstrap class "float-right" has the same affect without adding a new class]
:::
