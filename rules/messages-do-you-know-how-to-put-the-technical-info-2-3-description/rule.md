---
type: rule
archivedreason: 
title: Messages - Do you know how to put the technical info? (2/3 Description)
guid: f4ac7f2e-12d8-45d6-a8a6-027862ae2ae2
uri: messages-do-you-know-how-to-put-the-technical-info-2-3-description
created: 2012-11-27T04:36:22.0000000Z
authors: []
related: []
redirects:
- messages-do-you-know-how-to-put-the-technical-info-(2-3-description)

---

#### Description

The description should explain *what the error was*, followed by the *why it occurred*. Information that is useful for debugging should be included with errors where possible in a "Details" section. You should also avoid making the text unnecessarily wide. e.g.

<!--endintro-->


::: bad  
![Figure: Bad Example - A message box that does not intuitively alert the user](../../assets/BadMessageBox.gif)  
:::

* This is confusing, because it uses different terminology to the title ("estimate" instead of "quote")
* There is no punctuation
* The word "Error" is meaningless
* Line breaks are not present, so the message box is too wide and the text may wrap in the wrong spot



::: good  
![Figure: Good Example - A message box that is clear, consistent and intuitive](../../assets/GoodMessageBox.gif)  
:::

* Terminology is consistent
* Punctuation is present
* "Details" indicates that this information is useful for debugging
* The text is split across three lines, and the technical information after Details is separated from the description of the error
