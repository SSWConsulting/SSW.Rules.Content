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


<p class="ssw15-rteElement-P">This is often a bad practice if you already are ending Sub you don't need another line.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">Sub MySub<br>…<br>End Sub<br>Exit sub</p><p> </p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example</dd><p class="ssw15-rteElement-CodeArea">Sub MySub<br>…<br>End sub</p><p> </p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example​<br></dd>


