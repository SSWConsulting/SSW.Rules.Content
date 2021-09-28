---
type: rule
title: Do you always avoid On Error Resume Next? (VB Only)
uri: do-you-always-avoid-on-error-resume-next-vb-only
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-always-avoid-on-error-resume-next-(vb-only)
created: 2013-09-11T22:01:01.000Z
archivedreason: Archiving as this rule isn't valid anymore
guid: 44ff5d65-56bc-4b02-957d-378c8c0bfc5c
---

Never use On Error Resume Next in VB (and VB.NET) projects.

 If an error occurred, On Error Resume Next will hide the error and things can go very haywire! In .NET, stop using the On Error syntax and use the try-catch exception syntax for better structural exception handling.

<!--endintro-->

In VB/VBA you should use On Error Resume Next with line of comment and after an offending line of code there should be statement On Error GoTo 0 to reset Errors collection.

```vb
Private Sub cmdSelect_Click()
    Dim varTemp As Variant
    On Error Resume Next
    varTemp = columnADOX.Properties("RelatedColumn").Value
        .
        ....many lines of code...
        .
    intRoutesPerDay = 2
    End Sub
```
::: bad
Bad Example – Bad code
:::

```vb
Private Sub cmdSelect_Click()
    Dim varTemp As Variant
    On Error Resume Next
    'Sometimes there is no related column value
    varTemp = columnADOX.Properties("RelatedColumn").Value
    On Error GoTo 0

    .
    ....continuing code...
    .
    End Sub
```
::: good
Good Example – Good code
:::
