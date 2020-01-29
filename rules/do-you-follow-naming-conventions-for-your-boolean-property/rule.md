---
type: rule
title: Do you follow naming conventions for your Boolean Property?
uri: do-you-follow-naming-conventions-for-your-boolean-property
created: 2018-04-25T21:35:27.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> Boolean Properties must be prefixed by a verb. Verbs like &quot;Supports&quot;, &quot;Allow&quot;, &quot;Accept&quot;, &quot;Use&quot; should be valid. Also properties like &quot;Visible&quot;, &quot;Available&quot; should be accepted (maybe not).&#160;<a href="https&#58;//www.ssw.com.au/ssw/Standards/Rules/RulestoBetterSQLServerdatabases.aspx#BitFields">Here is how we name Boolean columns in SQL databases.</a><br><br> </span>

<p class="ssw15-rteElement-CodeArea">public&#160;bool&#160;Enable &#123; get; set; &#125;<br>public bool&#160;Invoice &#123; get; set; &#125;<br></p><dd class="ssw15-rteElement-FigureBad">Bad Example <br></dd><p class="ssw15-rteElement-CodeArea">public&#160;bool&#160;Enabled&#160;&#123;&#160;get;&#160;set;&#160;&#125;<br>public bool IsInvoiceSent &#123; get; set; &#125;<br></p><dd class="ssw15-rteElement-FigureGood">Good Example -&#160;Naming Convention for Boolean Property<br></dd><p class="ssw15-rteElement-YellowBorderBox">We have a program called&#160;<a href="https&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a>&#160;to check for this rule.​<br></p>


