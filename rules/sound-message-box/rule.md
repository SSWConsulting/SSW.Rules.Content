---
type: rule
title: Sound - Did you know that a message box automatically plays a beep?
uri: sound-message-box
authors: 
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: 
  - sound-did-you-know-that-a-message-box-automatically-plays-a-beep
created: 2012-11-27T02:57:30.000Z
archivedreason: null
guid: 81d5da16-4a3d-420e-b92c-f73a0791b290
---

A message box automatically provides this functionality so there is no need to manually put a beep right before a message box pops up.

<!--endintro-->

::: good  
![Figure: Good example - Windows message boxes plays a sound... which cannot be captured in screenshot form.](../../assets/Win7SoundError.png)  
:::

```csharp
string message = "You did not enter a server name. Cancel this operation?";
string caption = "No Server Name Specified";
MessageBoxButtons buttons = MessageBoxButtons.YesNo;
System.Media.SystemSounds.Beep.Play();
DialogResult result = MessageBox.Show(this, message, caption, buttons);
```

::: bad
Figure: Bad example - The sound on the button is hardcoded in this code snippet
:::

```csharp
string message = "You did not enter a server name. Cancel this operation?";
string caption = "No Server Name Specified";
MessageBoxButtons buttons = MessageBoxButtons.YesNo;
DialogResult result = MessageBox.Show(this, message, caption, buttons);
```

::: good
Figure: Good example - The code is not present in this example as it is automatically done
:::
