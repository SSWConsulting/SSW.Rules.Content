---
type: rule
archivedreason: 
title: Controls - Do you disable buttons that are unavailable?
guid: 08c912b7-1296-4442-9380-d30e255b1dcd
uri: controls-do-you-disable-buttons-that-are-unavailable
created: 2012-11-27T09:10:26.0000000Z
authors: 
- title: Jayden Alchin
  url: https://ssw.com.au/people/jayden-alchin
related: []
redirects: []

---

A button should be disabled if it is unavailable, if clicking it would generate an error message, or if it would carry out no function. However, buttons should not be hidden from view simply because they are unavailable, as it confuses the user.
<!--endintro-->

Different button states must have clear and distinct styling that differentiates them from each other and emphasizes them through the creation of a visual hierarchy. 

When buttons are in a disabled state the accepted standard is to “grey it out”. Using colour to create contrast like this serves to lower the emphasis on disabled buttons in favour of active ones. Lowering opacity or outline-only greyed buttons are other common ways to indicate a disabled state (Note the latter is only effective if outline buttons are not present elsewhere in the UI). Disabled buttons should also never display on-hover or on-click styles, to further convey their disabled state to the user. 

::: bad  
![Figure: Bad Example - Low contrast between disabled and active button styles.](disabled-button-bad.png)  
:::

::: good
![Figure: Good Example - High contrast creates distinct visual hierarchy](disabled-button-good.png)  
:::
