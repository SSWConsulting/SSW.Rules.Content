---
type: rule
title: Comments - Do you add a comment when you use Thread.Sleep?
uri: comments---do-you-add-a-comment-when-you-use-threadsleep
created: 2018-04-26T22:00:01.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p class="ssw15-rteElement-P">​​​First don’t do it and find the right fix.&#160;But if you have to, it should always be commented – as though your life depended on it.​&#160;<br></p> </span>

<p class="ssw15-rteElement-CodeArea">public DialogResult&#160;RefreshSchema() &#123;<br>&#160; &#160; SSW.SQLAuditor.WindowsUI.QueryAnalysisForm.RunScript(Startup.PageQueryAnalyzer.txtScript.Text)<br>&#160; &#160;&#160;System.Windows.Forms.Application.DoEvents()<br>&#160; &#160; //&#160;This is a sleep to delay the Application.DoEvent process.​<br>&#160; &#160; System.Threading.Thread.Sleep(500)<br>&#160; &#160; System.Windows.Forms.Application.DoEvents()<br>&#160; &#160; ...<br>&#125;​<span style="font-size&#58;1rem;">​</span><br></p>


