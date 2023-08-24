---
type: rule
archivedreason: 
title: Do you know the difference between Calculated Columns and Measures in Power BI?
guid: 0ea58893-e64e-42b4-81bb-be2a2612f046
uri: do-you-know-the-difference-between-calculated-columns-and-measures-in-power-bi
created: 2016-10-24T06:02:07.0000000Z
authors: []
related: []
redirects: []

---

When you run into a wall in Power BI and feel like you've exhausted the out of the box functionality, that when it's time to investigate what a bit of DAX can do for you. 

<!--endintro-->

There are 2 different things you can do with DAX, create a Measure or a Calculated Column.

Calculated columns:
* Stored in the database
* Often used to filter/group data

Measures:
* Computed on aggregates of values
* Computed at query time
* Often used to give a numerical metric

```dax
GroupingColumn = if (value<x, small, if(value<y, medium, large))
```

::: good
Figure - Good Example: Nested if statements are a great way to split up your data into groups

:::
