---
type: rule
archivedreason: 
title: Do you know the best way to track comments when your code is updated?
guid: 6ebf5337-9271-40bc-80ac-620a0db284e3
uri: comment-when-your-code-is-updated
created: 2018-04-24T19:53:39.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Matt Wicks
  url: https://ssw.com.au/people/matt-wicks
related: []
redirects:
- do-you-know-the-best-way-to-track-comments-when-your-code-is-updated

---


​​​​​​​​It's important that you have consistent commenting for your code, which can be used by other developers to quickly determine the workings of the application. The comments should always represent the rationale of the current behaviour.<br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-P">Since applications evolve over time - don't add comments to your code with datetime stamps. If a developer needs to see why the code behaves the way it does right now - your commit history is the best place to tell the story of why the code has evolved.​​​ <br></p><p class="ssw15-rteElement-P">Commands such as git blame or Visual Studio's annotate are great ways of seeing who and when a line of code was changed. <br><br></p><p class="ssw15-rteElement-CodeArea">private void iStopwatchOptionsForm_Resizing(object sender, System.EventArgs e) {<br>    // Don't close this form except closing this application - using hide instead; <br>    if (!this.m_isForceClose) {<br>       <span style="background-color:#ff3300;"> // &lt;added by FW, 11/10/2006&gt;</span><br>        // Remind saving the changes if the options were modified.<br>        if (this.IsOptionsModified) {<br>            if (MessageBox.Show("Do<br>you want to save the changes?", Me.GetApplicationTitle, MessageBoxButtons.YesNo,<br>MessageBoxIcon.Warning) = DialogResult.Yes) {<br>                this.SaveOptions()<br>            }<br>        }<br>        // &lt;/added&gt;<br>    }<br>}<br></p><dd class="ssw15-rteElement-FigureBad">Figure: Bad example - timestamped comments add noise to the code<br></dd><p class="ssw15-rteElement-P"><img src="comment annotations.png" alt="comment annotations.png" style="margin:5px;width:808px;" /><br></p><dd class="ssw15-rteElement-FigureGood"> Figure: Good example - we can tell who added the comment using annotations<br></dd>


