---
type: rule
title: C# Code- Do you know String should be @-quoted instead of using escape character for "\\"?
uri: c-code--do-you-know-string-should-be--quoted-instead-of-using-escape-character-for-
created: 2018-04-30T22:20:15.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>The @ symbol specifies that escape characters and line breaks should be ignored when the string is created.</p><p>As per&#58;&#160; <a href="http&#58;//msdn.microsoft.com/en-us/library/c84eby0h%28v=vs.90%29.aspx">Strings</a>&#160;<br></p> </span>

<p class="ssw15-rteElement-CodeArea">​string p2 = &quot;\\My Documents\\My Files\\&quot;;</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example - Using &quot;\\&quot;</dd><p class="ssw15-rteElement-CodeArea">string p2 = @&quot;\My Documents\My Files\&quot;;</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example - Using @​​<br></dd>


