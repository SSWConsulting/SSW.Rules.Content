---
type: rule
archivedreason: 
title: Do you follow naming conventions for your Boolean Property?
guid: f93e0077-6398-425b-8613-b628e9d69707
uri: follow-naming-conventions-for-your-boolean-property
created: 2018-04-25T21:35:27.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-follow-naming-conventions-for-your-boolean-property

---


Boolean Properties must be prefixed by a verb. Verbs like &quot;Supports&quot;, &quot;Allow&quot;, &quot;Accept&quot;, &quot;Use&quot; should be valid. Also properties like &quot;Visible&quot;, &quot;Available&quot; should be accepted (maybe not).&#160;<a href="https&#58;//www.ssw.com.au/ssw/Standards/Rules/RulestoBetterSQLServerdatabases.aspx#BitFields">Here is how we name Boolean columns in SQL databases.</a><br><br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">Public ReadOnly Property Enable As Boolean Get Return true End Get End Property<br>Public ReadOnly Property Invoice As Boolean Get Return m_Invoice End Get End Property</p><dd class="ssw15-rteElement-FigureBad">Bad Example <br></dd><p class="ssw15-rteElement-CodeArea">Public ReadOnly Property Enabled As Boolean Get Return true End Get End Property<br>Public ReadOnly Property IsInvoiceSent As Boolean Get return m_IsInvoiceSent End<br>Get End Property</p><dd class="ssw15-rteElement-FigureGood">Good Example -&#160;Naming Convention for Boolean Property<br></dd><p class="ssw15-rteElement-YellowBorderBox">We have a program called&#160;<a href="https&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a>&#160;to check for this rule.​<br></p>


