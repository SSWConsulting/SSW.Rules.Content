---
type: rule
archivedreason: 
title: Sound - Did you know that a message box automatically plays a beep?
guid: 81d5da16-4a3d-420e-b92c-f73a0791b290
uri: sound---did-you-know-that-a-message-box-automatically-plays-a-beep
created: 2012-11-27T02:57:30.0000000Z
authors: []
related: []

---

<dl class="goodImage">&lt;dt&gt;<img border="0" alt="Windows plays sounds for message boxes" src="../../assets/Win7SoundError.png">&lt;/dt&gt;
<dd>Figure: Good Example - Windows message boxes plays a sound... which cannot be captured in screenshot form.</dd></dl>
<!--endintro-->

A message box automatically provides this functionality so there is no need to manually put a beep right before a message box pops up.
<dl class="badCode">&lt;dt&gt;<pre>        Dim Message As String = "You did not enter a server name. Cancel this operation?"
        Dim Caption As String = "No Server Name Specified"
        Dim Buttons As Integer = MessageBoxButtons.YesNo
        Beep()
        result = MessageBox.Show( Me, Message, Caption, Buttons)
                    </pre>&lt;/dt&gt;
<dd>Figure: Bad example - The sound on the button is hardcoded in this code snippet</dd></dl><dl class="goodCode">&lt;dt&gt;<pre>        Dim Message As String = "You did not enter a server name. Cancel this operation?"
        Dim Caption As String = "No Server Name Specified"
        Dim Buttons As Integer = MessageBoxButtons.YesNo
        result = MessageBox.Show( Me, Message, Caption, Buttons)
                    </pre>&lt;/dt&gt;
<dd>Figure: The code is not present in this example as it is automatically done</dd></dl>
