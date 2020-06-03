---
type: rule
title: VB.NET Code - Do you know not to put Exit Sub before End Sub?
uri: vbnet-code---do-you-know-not-to-put-exit-sub-before-end-sub
created: 2018-04-30T22:32:50.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p class="ssw15-rteElement-P">This is often a bad practice if you already are ending Sub you don't need another line.<br></p> </span>

<p class="ssw15-rteElement-CodeArea">Sub MySub<br>…<br>End Sub<br>Exit sub</p><p> </p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example</dd><p class="ssw15-rteElement-CodeArea">Sub MySub<br>…<br>End sub</p><p> </p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example​<br></dd>


