---
type: rule
archivedreason: 
title: Control Choice - Do you know when to use CheckBoxes?
guid: 3176b22d-ed88-4909-8a77-3e6e652eae7e
uri: control-choice-do-you-know-when-to-use-checkboxes
created: 2012-11-27T08:51:11.0000000Z
authors: []
related: []
redirects: []

---

If the option only contains 2 choices, and the answer is a Boolean type value where the opposite value is clear (e.g. Enabled/Disabled, True/False, Yes/No, On/Off), it should always be a checkbox.


::: bad  
![Figure: Bad Example - Boolean options not using CheckBox](../../assets/NotUsingCheckBox.gif)  
:::


::: good  
![Figure: Good Example - A CheckBox is used for Boolean type value](../../assets/UsingCheckBox.gif)  
:::

<!--endintro-->

Only 1 CheckBox is used as the opposite value is clear, such controls are often CheckBoxes in a ListView too. E.g.:


::: good  
![Figure: Good Example - CheckBoxes in a ListView](../../assets/CheckBoxesInListView.gif)  
:::

CheckBoxes are also suitable to use for enable or disable sections and to tell the user that these sections do not need configuring for the application to run.


::: good  
![Figure: Good Example - CheckBoxes are used (although no opposite values), because they are clear when the CheckBoxes aren't ticked, the sections are disabled](../../assets/CheckBoxSection.gif)  
:::


::: bad  
![Figure: Bad Example - This screen implies that Configuring Credentials is required](../../assets/UseCheckBoxBad.gif)  
:::


::: good  
![Figure: Good Example - This screen uses a CheckBox to signify that Configure Credentials is optional](../../assets/UseCheckBoxGood.gif)  
:::

If there are only two options available on the form (usually a yes/no answer), the use of a checkbox is more intuitive than radio buttons. Only use radio buttons if there are more than two options.


::: bad  
![Figure: Bad Example – Radio buttons are not appropriate when there are only two options](../../assets/radio-for-two-options.jpg)  
:::


::: good  
![Figure: Good Example – These yes/no questions have a better representation with checkboxes](../../assets/checkbox-for-two-options.jpg)  
:::
