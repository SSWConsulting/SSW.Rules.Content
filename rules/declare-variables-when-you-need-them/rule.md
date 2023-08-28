---
type: rule
archivedreason: Rule is outdated. Prefer shorter methods that eliminate the need for this rule
title: Do you declare variables when you need them?
guid: 24d23856-bd1a-42c5-b883-793e6c84366a
uri: declare-variables-when-you-need-them
created: 2018-04-24T21:55:53.0000000Z
authors:
- title: Adam Cogan
  url: /people/adam-cogan
related: []
redirects:
- do-you-declare-variables-when-you-need-them

---

Should you declare variables at the top of the function, or declare them when you need to use them? If you come back to your code after a few weeks and you no longer need a variable, you are quite likely to forget to delete the declaration at the top, leaving orphaned variables. Here at SSW, we believe that variables should be declared as they are needed.

<!--endintro-->



```
Private Sub Command0_Click()
Dim dteTodayDate As Date
Dim intRoutesPerDay As Integer
Dim intRoutesToday As Integer
Dim dblWorkLoadToday As Double
dblWorkLoadToday = Date.Now()
.
....many lines of code...
.
intRoutesPerDay = 2
End Sub
```




::: bad
Figure: Bad example 

:::





```
Private Sub Command0_Click()
Dim dteTodayDate As Date
dteTodayDate = Date.Now()
.
....many lines of code...
.
Dim intRoutesPerDay As Integer
intRoutesPerDay = 2
.
....continuing code...
.End Sub
```




::: good
Figure: Good example

:::
