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

First don’t do it and find the right fix. But if you have to, it should always be commented – as though your life depended on it.

<!--endintro-->



```
public DialogResult RefreshSchema() {
    SSW.SQLAuditor.WindowsUI.QueryAnalysisForm.RunScript(Startup.PageQueryAnalyzer.txtScript.Text)
    System.Windows.Forms.Application.DoEvents()
    // This is a sleep to delay the Application.DoEvent process.
    System.Threading.Thread.Sleep(500)
    System.Windows.Forms.Application.DoEvents()
    ...
}
```
