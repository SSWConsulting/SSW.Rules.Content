---
type: rule
archivedreason: 
title: Do you use string interpolation when formatting strings
guid: b3edf18e-2d0e-456c-83a1-615761899bb9
uri: do-you-use-string-interpolation-when-formatting-strings
created: 2020-01-29T05:13:02.0000000Z
authors:
- id: 66
  title: Liam Elliott
- id: 78
  title: Matt Wicks
related: []

---


String Interpolation - greatly reduces the amount of boilerplate code required when working with strings<br>Formatting strings on the fly was previously a task which required a stack of boilerplate code<br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">​​var s = String.Format(&quot;Profit is $&#123;0&#125; this year&quot;, p.TotalEarnings - p.Totalcost);<br></p><dd class="ssw15-rteElement-FigureBad">​​​Figure&#58; Bad Example - Using String.Format() makes the code difficult to read<br></dd><p class="ssw15-rteElement-CodeArea">​​​var s = &quot;Profit is $&#123;p.TotalEarnings - p.Totalcost&#125; this year&quot;;<br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - String Interpolation is very human readable<br></dd>


