---
type: rule
title: Do you know not to put Exit Sub before End Sub? (VB)
uri: put-exit-sub-before-end-sub
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-know-not-to-put-exit-sub-before-end-sub-vb
  - do-you-know-not-to-put-exit-sub-before-end-sub-(vb)
created: 2018-04-25T21:23:55.000Z
archivedreason: null
guid: 6c503b8d-daba-4869-bde2-54b29d040b3b
---
Do not put "Exit Sub" statements before the "End Sub". The function will end on "End Sub". "Exit Sub" is serving no real purpose here.

<!--endintro-->

```vbnet
Private Sub SomeSubroutine()
'Your code here....
Exit Sub ' Bad code - Writing Exit Sub before End Sub.
End Sub
```

::: bad
Bad example

:::

```vbnet
Private Sub SomeOtherSubroutine()
'Your code here....
End Sub
```

::: good
Good example

:::

We have a program called [SSW Code Auditor](https://www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#ExitSub) to check for this rule.