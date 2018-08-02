

---
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p class="ssw15-rteElement-P">​​​First don’t do it but if you have to add a delay to the process, it should always be commented – as though your life depended on it.​&#160;<br></p> </span>

<p class="ssw15-rteElement-CodeArea">​Friend Function RefreshSchema() As DialogResult<br>SSW.SQLAuditor.WindowsUI.QueryAnalysisForm.RunScript(Startup.PageQueryAnalyzer.txtScript.Text)<br>System.Windows.Forms.Application.DoEvents()​<br></p><p class="ssw15-rteElement-CodeArea">'This is a sleep to delay the Application.DoEvent process <br>System.Threading.Thread.Sleep(500)<br>System.Windows.Forms.Application.DoEvents() <br>...​<br></p>


