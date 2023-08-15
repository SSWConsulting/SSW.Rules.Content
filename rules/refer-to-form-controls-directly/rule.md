---
type: rule
title: Do you refer to form controls directly?
uri: refer-to-form-controls-directly
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-refer-to-form-controls-directly
created: 2018-04-25T18:05:11.000Z
archivedreason: null
guid: f5a0ec53-9abd-49b2-90ac-ad01daf5d6d6
---
When programming in form based environments one thing to remember is not to refer to form controls directly. The correct way is to pass the controls values that you need through parameters. 

<!--endintro-->

There are a number of benefits for doing this:

1. Debugging is simpler because all your parameters are in one place
2. If for some reason you need to change the control's name then you only have to change it in one place
3. The fact that nothing in your function is dependant on outside controls means you could very easily reuse your code in other areas without too many problems re-connecting the parameters being passed in

It's a correct method of programming.

```vbnet
Private Sub Command0_Click()
 CreateSchedule
End Sub
Sub CreateSchedule()
 Dim dteDateStart As Date
 Dim dteDateEnd As Date
 dteDateStart = Format(Me.ctlDateStart,"dd/mm/yyyy") 'Bad Code - refering the form control directly
 dteDateEnd = Format(Me.ctlDateEnd, "dd/mm/yyyy")
 .....processing code
End Sub
```

::: bad
Bad example
:::

```vbnet
Private Sub Command0_Click()
 CreateSchedule(ctlDateStart, ctlDateEnd)
End Sub
Sub CreateSchedule(pdteDateStart As Date, pdteDateEnd As Date)
 Dim dteDateStart As Date
 Dim dteDateEnd As Date
 dteDateStart = Format(pdteDateStart, "dd/mm/yyyy") 'Good Code - refering the parameter directly
 dteDateEnd = Format(pdteDateEnd, "dd/mm/yyyy")
 &....processing code
End Sub
```

::: good
Good example
:::
