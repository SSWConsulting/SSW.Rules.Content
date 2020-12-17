---
type: rule
archivedreason: 
title: C# Code- Do you know String should be @-quoted instead of using escape character for "\\"?
guid: 849c1ee3-a72d-4471-b7db-8c363b663e0e
uri: c-code--do-you-know-string-should-be--quoted-instead-of-using-escape-character-for-
created: 2018-04-30T22:20:15.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

The @ symbol specifies that escape characters and line breaks should be ignored when the string is created. 

As per:  [Strings](http&#58;//msdn.microsoft.com/en-us/library/c84eby0h%28v=vs.90%29.aspx)

<!--endintro-->

string p2 = "\\My Documents\\My Files\\";


::: bad
Figure: Bad example - Using "\\"
:::


string p2 = @"\My Documents\My Files\";


::: good
Figure: Good example - Using @

:::
