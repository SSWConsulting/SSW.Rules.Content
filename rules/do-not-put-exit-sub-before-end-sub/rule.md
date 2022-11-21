---
type: rule
archivedreason: 
title: VB.NET Code - Do you know not to put Exit Sub before End Sub?
guid: adf0ec80-f374-4b19-9d92-da46750e5c62
uri: do-not-put-exit-sub-before-end-sub
created: 2018-04-30T22:32:50.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- vb-net-code-do-you-know-not-to-put-exit-sub-before-end-sub

---

This is often a bad practice if you already are ending Sub you don't need another line.

<!--endintro-->

``` vbnet
Sub MySub
...
End Sub
Exit sub
```
::: bad
Figure: Bad example  
:::

``` vbnet
Sub MySub
...
End sub
```
::: good
Figure: Good example
:::
