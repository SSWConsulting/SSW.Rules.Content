---
type: rule
title: Sound - Did you know that a message box automatically plays a beep?
uri: sound-did-you-know-that-a-message-box-automatically-plays-a-beep
authors: 
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
created: 2012-11-27T02:57:30.000Z
archivedreason: null
guid: 81d5da16-4a3d-420e-b92c-f73a0791b290
---

A message box automatically provides this functionality so there is no need to manually put a beep right before a message box pops up.

<!--endintro-->

::: good  
![Figure: Good example - Windows message boxes plays a sound... which cannot be captured in screenshot form.](../../assets/Win7SoundError.png)  
:::

```vbnet
Dim Message As String = "You did not enter a server name. Cancel this operation?"
Dim Caption As String = "No Server Name Specified"
Dim Buttons As Integer = MessageBoxButtons.YesNo
Beep()
result = MessageBox.Show( Me, Message, Caption, Buttons)
```
::: bad
Figure: Bad example - The sound on the button is hardcoded in this code snippet
:::

```vbnet
Dim Message As String = "You did not enter a server name. Cancel this operation?"
Dim Caption As String = "No Server Name Specified"
Dim Buttons As Integer = MessageBoxButtons.YesNo
result = MessageBox.Show( Me, Message, Caption, Buttons)
```
::: good
Figure: Good example - The code is not present in this example as it is automatically done
:::
