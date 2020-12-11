---
type: rule
archivedreason: 
title: Do you always avoid On Error Resume Next? (VB Only)
guid: 44ff5d65-56bc-4b02-957d-378c8c0bfc5c
uri: do-you-always-avoid-on-error-resume-next-vb-only
created: 2013-09-11T22:01:01.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

Never use On Error Resume Next in VB (and VB.NET) projects.

 If an error occurred, On Error Resume Next will hide the error and things can go very haywire! In .NET, stop using the On Error syntax and use the try-catch exception syntax for better structural exception handling.

<!--endintro-->

In VB/VBA you should use On Error Resume Next with line of comment and after an offending line of code there should be statement On Error GoTo 0 to reset Errors collection.
<dl class="bad">&lt;dt&gt;<pre>Private Sub cmdSelect_Click()
    Dim varTemp As Variant
    On Error Resume Next
    varTemp = columnADOX.Properties(&quot;RelatedColumn&quot;).Value
        .
        ....many lines of code...
        .
    intRoutesPerDay = 2
    End Sub
</pre>&lt;/dt&gt;<dd>Bad Example – Bad code</dd></dl><dl class="good">&lt;dt&gt;<pre>Private Sub cmdSelect_Click()
    Dim varTemp As Variant
    On Error Resume Next
    'Sometimes there is no related column value
    varTemp = columnADOX.Properties(&quot;RelatedColumn&quot;).Value
    On Error GoTo 0

    .
    ....continuing code...
    .
    End Sub
</pre>&lt;/dt&gt;<dd>Good Example – Good code</dd></dl>
We have a program called [SSW Code Auditor](http&#58;//www.ssw.com.au/ssw/CodeAuditor/Default.aspx) to check for this rule.
