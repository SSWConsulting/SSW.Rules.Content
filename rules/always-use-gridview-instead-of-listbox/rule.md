---
seoDescription: Improve user experience and control by choosing a GridView over a ListBox, offering multiple columns, header rows with checkable items, and sub-control customization.
type: rule
title: Do you always use GridView instead of ListBox?
uri: always-use-gridview-instead-of-listbox
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T02:01:00.000Z
guid: 62fdd9ea-cbec-4e93-8547-1da7c2ec13fa
---

Always choose a GridView (over a ListBox) because it can have:

<!--endintro-->

1. Multiple columns
2. Checkboxes in the header of the control, which enables users to easily check or uncheck all items
3. Add sub-controls added such as buttons, links, charts, and even customized controls to the Gridview. This means you get unlimited flexibility with the GridView

::: bad
![Figure: Bad example - No header rows and no checkbox to check or uncheck all items. None of this can be done with the ListView](datagridviewbad.png)
:::

::: good
![Figure: Good example - A header row and a checkbox to control all items, and multiple columns give users a richer experience. This can all be done using a GridView](datagridviewgood.png)
:::
