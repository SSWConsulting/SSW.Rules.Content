---
type: rule
title: Do you know the best way to track comments when your code is updated?
uri: do-you-know-the-best-way-to-track-comments-when-your-code-is-updated
created: 2018-04-24T19:53:39.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 78
  title: Matt Wicks

---



<span class='intro'> <p class="ssw15-rteElement-P">​​​​​​It's also important that you have a consistent code comment for your updating, which can be used by other developers to quickly determine the workings of the updating.​​<br></p> </span>

<p class="ssw15-rteElement-P">Example of commenting a method, it is strongly recommended that you add an adequate comment for your updating. <br></p><p class="ssw15-rteElement-CodeArea">'Private Sub iStopwatchOptionsForm_Resizing(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Resize<br>'If Me.WindowState = FormWindowState.Minimized Then<br>'Me.Hide()<br>'End If<br>'End Sub<br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example in VB.NET<br></dd><p class="ssw15-rteElement-CodeArea">'<br>'Commented - we don't need to hide this from when it is minimum size, just leave it on taskbar.<br>' FW, 11/01/2018<br>'<br>'Private Sub iStopwatchOptionsForm_Resizing(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Resize<br>'If Me.WindowState = FormWindowState.Minimized Then<br>'Me.Hide()<br>'End If<br>'End Sub</p><dd class="ssw15-rteElement-FigureGood"> Figure&#58; Good example in VB.NET<br></dd><p class="ssw15-rteElement-CodeArea">Private Sub iStopwatchOptionsForm_Closing(ByVal sender As System.Object, ByVal e As System.ComponentModel.CancelEventArgs) Handles MyBase.Closing<br>'Don't close this form except closing this application - using hide instead;<br>If Not Me.m_isForceClose Then<br>If Me.IsOptionsModified Then<br>If MessageBox.Show(&quot;Do<br>you want to save the changes?&quot;, Me.GetApplicationTitle, MessageBoxButtons.YesNo,<br>MessageBoxIcon.Warning) = DialogResult.Yes Then<br>Me.SaveOptions()<br>End If<br>End If<br>End If<br>End Sub</p><dd class="ssw15-rteElement-FigureBad"> Figure&#58; Bad example in VB.NET<br></dd><p class="ssw15-rteElement-CodeArea">  Private Sub iStopwatchOptionsForm_Closing(ByVal sender As System.Object, ByVal e As System.ComponentModel.CancelEventArgs) Handles MyBase.Closing<br>'Don't close this form except closing this application - using hide instead; <br>If Not Me.m_isForceClose Then<br>'&lt;added by FW, 11/10/2006&gt;<br>' Remind saving the changes if the options were modified.<br>If Me.IsOptionsModified Then<br>If MessageBox.Show(&quot;Do you want to save the changes?&quot;, Me.GetApplicationTitle, MessageBoxButtons.YesNo, MessageBoxIcon.Warning) = DialogResult.Yes Then<br>Me.SaveOptions()<br>End If<br>End If <br>'&lt;/added&gt;<br>...<br>End If<br>End Sub</p><dd class="ssw15-rteElement-FigureGood"> Figure&#58; Good example in VB.NET ​<br></dd>


