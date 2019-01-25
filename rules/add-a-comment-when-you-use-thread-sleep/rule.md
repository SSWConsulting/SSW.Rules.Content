---
type: rule
archivedreason: 
title: Comments - Do you add a comment when you use Thread.Sleep?
guid: 34e9cb81-73a3-4d80-ad1b-141bc19eb37f
uri: add-a-comment-when-you-use-thread-sleep
created: 2018-04-26T22:00:01.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- comments-do-you-add-a-comment-when-you-use-thread-sleep

---


<p class="ssw15-rteElement-P">​​​First don’t do it and find the right fix.&#160;But if you have to, it should always be commented – as though your life depended on it.​&#160;<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">public DialogResult&#160;RefreshSchema() &#123;<br>&#160; &#160; SSW.SQLAuditor.WindowsUI.QueryAnalysisForm.RunScript(Startup.PageQueryAnalyzer.txtScript.Text)<br>&#160; &#160;&#160;System.Windows.Forms.Application.DoEvents()<br>&#160; &#160; //&#160;This is a sleep to delay the Application.DoEvent process.​<br>&#160; &#160; System.Threading.Thread.Sleep(500)<br>&#160; &#160; System.Windows.Forms.Application.DoEvents()<br>&#160; &#160; ...<br>&#125;​<span style="font-size&#58;1rem;">​</span><br></p>


