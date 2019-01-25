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



<span class='intro'> <p class="ssw15-rteElement-P">​​​​​​​It's also important that you have a consistent code comment for your updating, which can be used by other developers to quickly determine the workings of the updating.​​<br></p> </span>

<p class="ssw15-rteElement-P">Example of commenting a method, it is strongly recommended that you add an adequate comment for your updating. <br></p><p class="ssw15-rteElement-CodeArea">private void&#160;iStopwatchOptionsForm_Resizing(object&#160;sender, System.EventArgs e) &#123;<br>&#160; &#160; if (this.WindowState = FormWindowState.Minimized) &#123;<br>&#160; &#160; &#160; &#160;&#160;this.Hide()<br>&#160; &#160; &#125;<br>&#125;<br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example<br></dd><p class="ssw15-rteElement-CodeArea">//<br>//&#160;Commented - we don't need to hide this from when it is minimum size, just leave it on taskbar.<br>// FW, 11/01/2018<br>//<br>private void&#160;iStopwatchOptionsForm_Resizing(object&#160;sender, System.EventArgs e) &#123;<br>&#160; &#160; if (this.WindowState = FormWindowState.Minimized) &#123;<br>&#160; &#160; &#160; &#160;&#160;this.Hide()<br>&#160; &#160; &#125;<br>&#125;<br></p><dd class="ssw15-rteElement-FigureGood"> Figure&#58; Good example<br></dd><p class="ssw15-rteElement-CodeArea">private void&#160;iStopwatchOptionsForm_Resizing(object&#160;sender, System.EventArgs e) &#123;<br>&#160; &#160; //&#160;​Don't close this form except closing this application - using hide instead;<br>&#160; &#160; if (!this.m_isForceClose) &#123;<br>&#160; &#160; &#160; &#160;&#160;if (this.IsOptionsModified) &#123;<br>&#160; &#160; &#160; &#160; &#160; &#160;&#160;if&#160;(MessageBox.Show(&quot;Do<br>you want to save the changes?&quot;, Me.GetApplicationTitle, MessageBoxButtons.YesNo,<br>MessageBoxIcon.Warning) = DialogResult.Yes) &#123;<br>&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160;this.SaveOptions()<br>&#160; &#160; &#160; &#160; &#160; &#160;&#160;&#125;<br>&#160; &#160; &#160; &#160; &#125;<br>&#160; &#160; &#125;<br>&#125;<br></p><dd class="ssw15-rteElement-FigureBad"> Figure&#58; Bad example<br></dd><p class="ssw15-rteElement-CodeArea">  private void&#160;iStopwatchOptionsForm_Resizing(object&#160;sender, System.EventArgs e) &#123;<br>&#160; &#160;&#160;//&#160;Don't close this form except closing this application - using hide instead; <br>&#160; &#160; if (!this.m_isForceClose) &#123;<br>&#160; &#160; &#160; &#160;&#160;//&#160;&lt;added by FW, 11/10/2006&gt;<br>&#160; &#160; &#160; &#160; //&#160;Remind saving the changes if the options were modified.<br>&#160; &#160; &#160; &#160; if (this.IsOptionsModified) &#123;<br>&#160; &#160; &#160; &#160; &#160; &#160;&#160;if&#160;(MessageBox.Show(&quot;Do<br>you want to save the changes?&quot;, Me.GetApplicationTitle, MessageBoxButtons.YesNo,<br>MessageBoxIcon.Warning) = DialogResult.Yes) &#123;<br>&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160;this.SaveOptions()<br>&#160; &#160; &#160; &#160; &#160; &#160;&#160;&#125;<br>&#160; &#160; &#160; &#160; &#125;<br>&#160; &#160; &#160; &#160; //&#160;&lt;/added&gt;<br>&#160; &#160; &#125;<br>&#125;<br></p><dd class="ssw15-rteElement-FigureGood"> Figure&#58; Good example​<br></dd>


