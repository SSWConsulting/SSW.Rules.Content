---
type: rule
title: Do you refer to form controls directly?
uri: do-you-refer-to-form-controls-directly
created: 2018-04-25T18:05:11.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>When programming in form based environments one thing to remember is not to refer to form controls directly. The correct way is to pass the controls values that you need through parameters. There are a number of benefits for doing this&#58;</p><ol><li>Debugging is simpler because all your parameters are in one place</li><li>If for some reason you need to change the control's name then you only have to change it in one place.</li><li>The fact that nothing in your function is dependant on outside controls means you could very easily reuse your code in other areas without too many problems re-connecting the parameters being passed in.</li></ol><p>It's a correct method of programming. <br></p><br> </span>

<p class="ssw15-rteElement-CodeArea">​​Private Sub Command0_Click()<br> CreateSchedule<br>End Sub<br>Sub CreateSchedule()<br> Dim dteDateStart As Date<br> Dim dteDateEnd As Date<br> dteDateStart = Format(Me.ctlDateStart,&quot;dd/mm/yyyy&quot;) 'Bad Code - refering the form control directly<br> dteDateEnd = Format(Me.ctlDateEnd, &quot;dd/mm/yyyy&quot;)<br> .....processing code<br>End Sub</p><dd class="ssw15-rteElement-FigureBad">Bad Example​​<br></dd><p class="ssw15-rteElement-CodeArea">Private Sub Command0_Click()<br> CreateSchedule(ctlDateStart, ctlDateEnd)<br>End Sub<br>Sub CreateSchedule(pdteDateStart As Date, pdteDateEnd As Date)<br> Dim dteDateStart As Date<br> Dim dteDateEnd As Date<br> dteDateStart = Format(pdteDateStart, &quot;dd/mm/yyyy&quot;) 'Good Code - refering the parameter directly<br> dteDateEnd = Format(pdteDateEnd, &quot;dd/mm/yyyy&quot;)<br> &amp;....processing code<br>End Sub</p><dd class="ssw15-rteElement-FigureGood">​Good Example​​<br></dd>


