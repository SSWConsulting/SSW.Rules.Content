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

<p class="ssw15-rteElement-CodeArea">Public ReadOnly Property Enable As Boolean Get Return true End Get End Property<br>Public ReadOnly Property Invoice As Boolean Get Return m_Invoice End Get End Property</p><dd class="ssw15-rteElement-FigureBad">Bad Example <br></dd><p class="ssw15-rteElement-CodeArea">Public ReadOnly Property Enabled As Boolean Get Return true End Get End Property<br>Public ReadOnly Property IsInvoiceSent As Boolean Get return m_IsInvoiceSent End<br>Get End Property</p><dd class="ssw15-rteElement-FigureGood">Good Example -&#160;Naming Convention for Boolean Property<br></dd><p class="ssw15-rteElement-YellowBorderBox">We have a program called&#160;<a href="https&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a>&#160;to check for this rule.​<br></p>


