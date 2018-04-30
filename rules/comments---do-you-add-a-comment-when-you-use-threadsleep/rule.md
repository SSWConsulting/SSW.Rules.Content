---
type: rule
archivedreason: 
title: Comments - Do you add a comment when you use Thread.Sleep?
guid: 34e9cb81-73a3-4d80-ad1b-141bc19eb37f
uri: comments---do-you-add-a-comment-when-you-use-threadsleep
created: 2018-04-26T22:00:01.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p class="ssw15-rteElement-P">First don’t do it but if you have to add a delay to the process, it should always be commented – as though your life depended on it.​&#160;<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">​Friend Function RefreshSchema() As DialogResult<br>SSW.SQLAuditor.WindowsUI.QueryAnalysisForm.RunScript(Startup.PageQueryAnalyzer.txtScript.Text)<br>System.Windows.Forms.Application.DoEvents()​<br></p><p class="ssw15-rteElement-CodeArea">'This is a sleep to delay the Application.DoEvent process <br>System.Threading.Thread.Sleep(500)<br>System.Windows.Forms.Application.DoEvents() <br>...​<br></p>


