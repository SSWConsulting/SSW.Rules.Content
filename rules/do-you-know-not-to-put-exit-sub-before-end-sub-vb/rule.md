---
type: rule
title: Do you know not to put Exit Sub before End Sub? (VB)
uri: do-you-know-not-to-put-exit-sub-before-end-sub-vb
created: 2018-04-25T21:23:55.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> ​Do not put &quot;Exit Sub&quot; statements before the &quot;End Sub&quot;. The function will end on &quot;End Sub&quot;. &quot;Exit Sub&quot; is serving no real purpose here.<br> </span>

<p class="ssw15-rteElement-CodeArea">Private Sub SomeSubroutine()<br>'Your code here....<br>Exit Sub ' Bad code - Writing Exit Sub before End Sub.<br>End Sub</p><dd class="ssw15-rteElement-FigureBad">Bad example​<br></dd><p class="ssw15-rteElement-CodeArea">Private Sub SomeOtherSubroutine()<br>'Your code here....<br>End Sub</p><dd class="ssw15-rteElement-FigureGood"> Good example​<br></dd><p class="ssw15-rteElement-YellowBorderBox">We have a program called&#160;<a href="https&#58;//www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#ExitSub">SSW Code Auditor</a>&#160;to check for this rule.</p>
​<br>


