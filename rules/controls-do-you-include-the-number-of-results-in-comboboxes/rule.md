---
seoDescription: Enhance form usability by showing result counts in ComboBoxes for better user experience.
type: rule
title: Controls - Do you include the number of results in ComboBoxes?
uri: controls-do-you-include-the-number-of-results-in-comboboxes
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
created: 2012-11-27T08:40:47.000Z
archivedreason: null
guid: da34f7bf-dc4e-412c-97ad-bb7fdacf595b
---
When designing your form, you should try to help your user whenever it's possible. So it's a good idea to include the number of results in ComboBoxes.

<!--endintro-->

### For Windows Forms

::: bad
![Figure: Bad example - You can't tell the number of results and there is a scroll bar](combowf-1.jpg)
:::

::: good
![Figure: Good example - The number of results is clearly displayed. Long text boxes larger than 30 entries, another approach can be employed - putting the common ones at the top](combowf-2.jpg)
:::

::: bad
![Figure: Bad example - Firstly because it is manual, plus what about the 4th, 5th, etc most common used countries](rule38longtextcombobox.jpg)
:::

::: bad
![Figure: Bad example – This was a highly unpopular method of the sorting and counting above](rule38sortablecombobox.jpg)
:::

We believe all combos should be able to be sorted ascending/descending and by popularity asc/desc.

::: good
![Figure: Good example - A better way to sort this](sort-alpha-numeric.jpg)
:::
