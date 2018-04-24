---
type: rule
title: Do you avoid Double-Negative Conditionals in if-statements?
uri: do-you-avoid-double-negative-conditionals-in-if-statements
created: 2018-04-24T22:03:21.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p class="ssw15-rteElement-P">Try to avoid Double-Negative Conditionals in if-statements. Double negative conditionals are difficult to read because developers have to evaluate what is positive state of two negatives. So always try to make a single positive when you write if-statement. <br></p> </span>

<p class="ssw15-rteElement-CodeArea">​if (!IsValid)<br>&#123;<br> // handle no error<br>&#125;<br>else<br>&#123;<br> // handle error<br>&#125;​<br></p><p></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad e​xample​<br></dd><p class="ssw15-rteElement-CodeArea">if (IsValid)<br>&#123;<br> // handle error<br>&#125;<br>else<br>&#123;<br> // handle no error<br>&#125;</p><p></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example​<br></dd><p class="ssw15-rteElement-CodeArea">if (!IsValid)<br>&#123;<br> // handle error<br>&#125;</p><dd class="ssw15-rteElement-FigureGood">​Figure&#58; Another good example<span style="font-size&#58;13px;">​</span></dd>


