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



<span class='intro'> ​​​​​​​​It's important that you have consistent commenting for your code, which can be used by other developers to quickly determine the workings of the application. The comments should always represent the rationale of the current behaviour.<br> </span>

<p class="ssw15-rteElement-P">Since applications evolve over time - don't add comments to your code with datetime stamps. If a developer needs to see why the code behaves the way it does right now - your commit history is the best place to tell the story of why&#160;the code has evolved.​​​&#160;<br></p><p class="ssw15-rteElement-P">Commands such as git blame or Visual Studio's annotate are great ways of seeing who and when a line of code was changed.&#160;<br><br></p><p class="ssw15-rteElement-CodeArea">private void&#160;iStopwatchOptionsForm_Resizing(object&#160;sender, System.EventArgs e) &#123;<br>&#160; &#160;&#160;//&#160;Don't close this form except closing this application - using hide instead;&#160;<br>&#160; &#160; if (!this.m_isForceClose) &#123;<br>&#160; &#160; &#160; &#160;<span style="background-color&#58;#ff3300;">&#160;//&#160;&lt;added by FW, 11/10/2006&gt;</span><br>&#160; &#160; &#160; &#160; //&#160;Remind saving the changes if the options were modified.<br>&#160; &#160; &#160; &#160; if (this.IsOptionsModified) &#123;<br>&#160; &#160; &#160; &#160; &#160; &#160;&#160;if&#160;(MessageBox.Show(&quot;Do<br>you want to save the changes?&quot;, Me.GetApplicationTitle, MessageBoxButtons.YesNo,<br>MessageBoxIcon.Warning) = DialogResult.Yes) &#123;<br>&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160;this.SaveOptions()<br>&#160; &#160; &#160; &#160; &#160; &#160;&#160;&#125;<br>&#160; &#160; &#160; &#160; &#125;<br>&#160; &#160; &#160; &#160; //&#160;&lt;/added&gt;<br>&#160; &#160; &#125;<br>&#125;<br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example - timestamped comments add noise to the code<br></dd><p class="ssw15-rteElement-P"><img src="/SiteAssets/comment-when-your-code-is-updated/comment%20annotations.png" alt="comment annotations.png" style="margin&#58;5px;width&#58;808px;" /><br></p><dd class="ssw15-rteElement-FigureGood"> Figure&#58; Good example - we can tell who added the comment using annotations<br></dd>


