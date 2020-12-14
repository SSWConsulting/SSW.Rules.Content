---
type: rule
archivedreason: 
title: C# Code - Do you use string literals?
guid: 849c1ee3-a72d-4471-b7db-8c363b663e0e
uri: how-string-should-be-quoted
created: 2018-04-30T22:20:15.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- c-code-do-you-use-string-literals

---


<p>Do you know String should be @-quoted instead of using escape character for &quot;\\&quot;?<br>The @ symbol specifies that escape characters and line breaks should be ignored when the string is created.<br></p><p>As per&#58;&#160; <a href="http&#58;//msdn.microsoft.com/en-us/library/c84eby0h%28v=vs.90%29.aspx">Strings</a>&#160;<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">​string p2 = &quot;\\My Documents\\My Files\\&quot;;</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example - Using &quot;\\&quot;</dd><p class="ssw15-rteElement-CodeArea">string p2 = @&quot;\My Documents\My Files\&quot;;</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example - Using @​​​<br></dd>


