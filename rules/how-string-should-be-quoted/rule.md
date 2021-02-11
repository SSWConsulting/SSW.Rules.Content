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

Do you know String should be @-quoted instead of using escape character for "\\"?
The @ symbol specifies that escape characters and line breaks should be ignored when the string is created.

As per:  [Strings](http&#58;//msdn.microsoft.com/en-us/library/c84eby0h%28v=vs.90%29.aspx)

<!--endintro-->



```
string p2 = "\\My Documents\\My Files\\";
```




::: bad
Figure: Bad example - Using "\\"  
:::



```
string p2 = @"\My Documents\My Files\";
```




::: good
Figure: Good example - Using @

:::
