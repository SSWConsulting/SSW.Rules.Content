---
type: rule
archivedreason: 
title: Control Choice - Do you know when to use options group Radio Buttons instead of ComboBox?
guid: b0118f1a-8750-456e-b82f-41f9464463d0
uri: control-choice-do-you-know-when-to-use-options-group-radio-buttons-instead-of-combobox
created: 2012-11-27T09:01:24.0000000Z
authors: []
related: []
redirects: []

---

When the options are static items (not database driven) and they can fit on the screen (about 2-5 items), they should be radio buttons.

<!--endintro-->

For a ComboBox, user needs 2 clicks to change the value

1. Click the little "v" button to see the available options.
2. Then click the option to select.


For an options group, user can see all the available options without clicking, and select the option with just a click.


::: bad  
![Figure: Bad Example - ComboBox is used for "Job Type" where it contains only 2 options](../../assets/NotUsingRadioButtons.gif)  
:::


::: good  
![Figure: Good Example - Radio Buttons are used and aligned vertically](../../assets/UsingRadioButtons.gif)  
:::
