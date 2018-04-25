---
type: rule
archivedreason: 
title: Do you use String.Empty instead of ""?
guid: 939c25b3-d693-42f4-bdbf-d99c1f246633
uri: use-string-empty-instead-of-quotes
created: 2018-04-25T21:51:21.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-use-string-empty-instead-of

---


<p class="ssw15-rteElement-P">Considering the memory management of .NET Framework String.Empty will get higher performance then using &quot;&quot;. <br></p>
<br><excerpt class='endintro'></excerpt><br>
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


