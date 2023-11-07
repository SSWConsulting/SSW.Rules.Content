---
type: rule
title: Do you declare variables when you need them?
uri: declare-variables-when-you-need-them
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-declare-variables-when-you-need-them
created: 2018-04-24T21:55:53.000Z
archivedreason: Rule is outdated. Prefer shorter methods that eliminate the need for this rule
guid: 24d23856-bd1a-42c5-b883-793e6c84366a
---
Should you declare variables at the top of the function, or declare them when you need to use them? If you come back to your code after a few weeks and you no longer need a variable, you are quite likely to forget to delete the declaration at the top, leaving orphaned variables. Here at SSW, we believe that variables should be declared as they are needed.

<!--endintro-->

```vbnet
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

```vbnet
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