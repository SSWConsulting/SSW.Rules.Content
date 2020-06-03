---
type: rule
title: Do you know that Enum types should not be suffixed with the word "Enum"?
uri: do-you-know-that-enum-types-should-not-be-suffixed-with-the-word-enum
created: 2018-04-25T23:53:39.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> This is against the .NET Object Naming Conventions and inconsistent with the framework.<br> </span>

<p class="ssw15-rteElement-CodeArea">Public Enum ProjectLanguageEnum CSharp VisualBasic End Enum</p><dd class="ssw15-rteElement-FigureBad"> Bad - Enum type is suffixed with the word &quot;Enum&quot; <br></dd><p class="ssw15-rteElement-CodeArea">Public Enum ProjectLanguage CSharp VisualBasic End Enum</p><dd class="ssw15-rteElement-FigureGood">Good - Enum type is not suffixed with the word &quot;Enum&quot; <br></dd><p class="ssw15-rteElement-YellowBorderBox">We have a program called&#160;<a href="https&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor </a> to check for this rule.</p>
​<br>


