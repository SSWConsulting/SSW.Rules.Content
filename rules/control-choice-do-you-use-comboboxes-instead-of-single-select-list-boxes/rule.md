---
type: rule
archivedreason: 
title: Control Choice - Do you use ComboBoxes instead of single-select List Boxes?
guid: 1562073d-ec2c-42fe-b9c1-9b6d6feb6842
uri: control-choice-do-you-use-comboboxes-instead-of-single-select-list-boxes
created: 2012-11-27T08:52:24.0000000Z
authors: []
related: []
redirects: []

---

ComboBoxes are better than List Boxes  **for data entry** because:

* They occupy less screen space
* They are less trouble to scroll through, owing to the fact that you can afford to have more room for the list (as it's collapsed most of the time)
* As you can see in the figures below, using a combo also makes the required field indicator (\*) easier to see.


<!--endintro-->


::: bad  
![Figure: Bad Example - Using list boxes](../../assets/ListBoxesAreEvil\_SingleSelectBad.gif)  
:::


::: good  
![Figure: Good Example - Using ComboBoxes - takes up less screen space and the required field indication is easy to see](../../assets/ListBoxesAreEvil\_SingleSelectGood.gif)  
:::

 **Note: When are single-select list boxes OK?** 

As mentioned before, there are exceptions to this rule. It would be hard to imagine the Include/Exclude boxes in the SQL Server Enterprise Manager's Server Registration Wizard being handled with ComboBoxes, for example.

![Figure: Include/Exclude Listboxes are an example of a valid use for List Boxes](../../assets/ListBoxesAreEvil\_ExceptForThisOne.gif)  


| We have a program called [SSW Code Auditor](http://www.ssw.com.au/ssw/CodeAuditor/) to check for this rule. |
| --- |
