---
type: rule
archivedreason: 
title: Do you suffix unit test classes with "Tests"?
guid: 7e401815-0507-40bf-a045-ae46ca1db46a
uri: suffix-unit-test-classes-with-tests
created: 2018-04-25T23:24:57.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-suffix-unit-test-classes-with-tests

---


Unit test classes should be suffixed with the word &quot;Tests&quot; for better coding readability.<br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">​[TestFixture] public class SqlValidatorReportTest &#123; &#125;<br></p><dd class="ssw15-rteElement-FigureBad">Bad - Unit test class is not suffixed with &quot;Tests&quot;​<br></dd><p class="ssw15-rteElement-CodeArea">[TestFixture] public class HtmlDocumentTests &#123; &#125; 
  &#160;​<br></p><dd class="ssw15-rteElement-FigureGood">Good - Unit test class is suffixed with &quot;Tests&quot;​<br></dd>
<p class="ssw15-rteElement-YellowBorderBox">We have a program called&#160;<a href="https&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a>&#160;to check for this rule.<br></p>


