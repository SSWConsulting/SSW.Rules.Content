---
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
![Figure: Bad Example - You can't tell the number of results and there is a scroll bar](../../assets/ComboWF-1.jpg)
:::

::: good
![Figure: Good Example - The number of results is clearly displayed. Long text boxes > 30 entries, another approach can be employed - putting the common ones at the top](../../assets/ComboWF-2.jpg)
:::

::: bad
![Figure: Bad Example - Firstly because it is manual, plus what about the 4th, 5th, etc most common used countries](../../assets/Rule38LongTextCombobox.jpg)
:::

::: bad
![Figure: Bad Example – This was a highly unpopular method of the sorting and counting above](../../assets/rule38SortableCombobox.jpg)
:::

We believe all combos should be able to be sorted ascending/descending and by popularity asc/desc.

::: good
![Figure: Good Example - Is there a better way to sort this?](sort-alpha-numeric.jpg)
:::
