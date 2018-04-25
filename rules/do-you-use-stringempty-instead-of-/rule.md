---
type: rule
title: Do you use String.Empty instead of ""?
uri: do-you-use-stringempty-instead-of-
created: 2018-04-25T21:51:21.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p class="ssw15-rteElement-P">Considering the memory management of .NET Framework String.Empty will get higher performance then using &quot;&quot;. <br></p> </span>

<p class="ssw15-rteElement-CodeArea">​public string myString 
   <br>&#123;<br> get<br> &#123;<br> return ;<br> &#125; 
   <br>&#125; 
   <br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad code. Low performance​​<br></dd><p class="ssw15-rteElement-CodeArea">public string myString<br>&#123; 
   <br> get 
   <br> &#123; 
   <br> return string.Empty; 
   <br> &#125; 
   <br>&#125;​<br></p><dd class="ssw15-rteElement-FigureGood">
   Figure&#58; Good code. Higher performance<br></dd><p class="ssw15-rteElement-YellowBorderBox">We have a program called&#160;<a href="https&#58;//www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#TimeSpan">SSW Code Auditor</a>&#160;to check for this rule.​<br></p>


