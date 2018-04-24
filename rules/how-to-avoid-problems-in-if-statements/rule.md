---
type: rule
archivedreason: 
title: Do you know how to avoid problems in if-statements?
guid: 92b0df3a-dece-492f-b2f8-256890d8d03a
uri: how-to-avoid-problems-in-if-statements
created: 2018-04-24T22:00:00.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-know-how-to-avoid-problems-in-if-statements

---


<p class="ssw15-rteElement-P">Try to avoid problems in if-statements without curly brackets and just one statement which is written one line below the if-statement. Use just one line for such if-statements. If you want to add more statements later on and you could forget to add the curly brackets which may cause problems later on.​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">​if (ProductName == null) ProductName = string.Empty; if (ProductVersion == null)<br> ProductVersion = string.Empty; if (StackTrace == null) StackTrace = string.Empty;</p><dd class="ssw15-rteElement-FigureBad">​​​Figure&#58; Ba​d Example<br></dd><p class="ssw15-rteElement-CodeArea">if (ProductName == null) <br>&#123; <br> ProductName = string.Empty; <br>&#125; <br>if (ProductVersion == null)<br>&#123; <br> ProductVersion = string.Empty; <br>&#125; <br>if (StackTrace == null) <br>&#123; <br> StackTrace = string.Empty;<br>&#125;</p><dd class="ssw15-rteElement-FigureGood">​Figure&#58; Good Example</dd><p>​<br></p>


