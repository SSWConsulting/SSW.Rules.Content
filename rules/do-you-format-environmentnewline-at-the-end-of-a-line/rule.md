---
type: rule
title: Do you format "Environment.NewLine" at the end of a line?
uri: do-you-format-environmentnewline-at-the-end-of-a-line
created: 2018-04-26T21:46:51.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> You&#160;should format &quot;Environment.NewLine&quot; at the end of a line.​​<br>​<br> </span>

<p class="ssw15-rteElement-CodeArea">DialogResult diaResult = MessageBox.Show(this,<br>&quot;The database is not valid.&quot; + Environment.NewLine + &quot;Do you want to upgrade it? &quot;, <br>&quot;Tip&quot;, <br>MessageBoxButtons.YesNo,<br>MessageBoxIcon.Warning);<br></p><dd class="ssw15-rteElement-FigureBad">Bad Example&#58; &quot;Environment.NewLine&quot; isn't at the end of the line <br></dd><p><br></p><p class="ssw15-rteElement-CodeArea">DialogResult diaResult = MessageBox.Show(this,<br>&quot;The database is not valid.&quot; + Environment.NewLine<br>+ &quot;Do you want to upgrade it? &quot;, <br>&quot;Tip&quot;, <br>MessageBoxButtons.YesNo,<br>MessageBoxIcon.Warning);<br></p><dd class="ssw15-rteElement-FigureGood">Good Example&#58;​&#160;&quot;Environment.NewLine&quot; is at the end of the line <br></dd><p>​<br></p>


