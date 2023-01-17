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
![Figure: Bad Example - You can't tell the number of results and there is a scroll bar](https://www.ssw.com.au/rules/static/81b4f8bd2902db6fd6ea905dd159e42b/ddb38/ComboWF-1.jpg)
:::

::: good
![Figure: Good Example - The number of results is clearly displayed. Long text boxes larger than 30 entries, another approach can be employed - putting the common ones at the top](https://www.ssw.com.au/rules/static/b57407dcbd0d6982a43653fcfb7837cb/ddb38/ComboWF-2.jpg)
:::

::: bad
![Figure: Bad Example - Firstly because it is manual, plus what about the 4th, 5th, etc most common used countries](https://www.ssw.com.au/rules/static/28e4c8c63d59ab60531c8adb12393a07/adebe/Rule38LongTextCombobox.jpg)
:::

::: bad
![Figure: Bad Example – This was a highly unpopular method of the sorting and counting above](https://www.ssw.com.au/rules/static/28e4c8c63d59ab60531c8adb12393a07/adebe/Rule38LongTextCombobox.jpg)
:::

We believe all combos should be able to be sorted ascending/descending and by popularity asc/desc.

::: good
![Figure: Good Example - Is there a better way to sort this?](sort-alpha-numeric.jpg)
:::
