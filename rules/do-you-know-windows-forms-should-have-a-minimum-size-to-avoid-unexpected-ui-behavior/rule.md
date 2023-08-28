---
type: rule
archivedreason: 
title: Do you know Windows Forms should have a minimum size to avoid unexpected UI behavior
guid: 08de57ee-b4ff-4438-943b-5851b0da30fa
uri: do-you-know-windows-forms-should-have-a-minimum-size-to-avoid-unexpected-ui-behavior
created: 2015-06-30T08:31:56.0000000Z
authors:
- title: Adam Cogan
  url: /people/adam-cogan
related: []
redirects: []

---

If windows form does not setup a minimum size, your users could have unpredictable form behaviour as seen below:
<img alt="Bad window form" src="../../assets/Bugsize.gif" style="margin:5px;padding:15px;border:1px solid #cccccc;background:#eeeeee;">

::: bad
Figure: Bad Example - Unexpected window form  
:::



<!--endintro-->

Therefore, a standard has been built to ensure Windows forms have a minimum size.
![Good window form](../../assets/Minisize.gif)

::: good
Figure: Good Example - User friendly window form  
:::
