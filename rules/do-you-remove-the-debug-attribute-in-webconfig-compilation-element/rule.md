---
type: rule
title: Do you remove the debug attribute in Web.config compilation element?
uri: do-you-remove-the-debug-attribute-in-webconfig-compilation-element
created: 2016-08-24T22:22:22.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> ​​The debug attribute in the web.config file is very useful for ASP.NET developers. When an error occurs the developer gets detailed error report containing the stack trace, line number and what the error is.​<br> </span>

<p>But when debug attribute in the Web.config file is set to true it generates symbolic information (.pdb file) every time the compiler compiles your views as well as disables code optimization.&#160;So, it slows down the execution of every page.<br></p><p class="ssw15-rteElement-P">So if you are a developer remember to remove the debug attribute and instead use custom error messages for your web pages</p><p class="ssw15-rteElement-YellowBorderBox">We have a program called&#160;<a href="https&#58;//www.ssw.com.au/ssw/codeauditor/" target="_blank">SSW Code Auditor​</a>&#160;to check for this rule.​<br></p><p>​<br></p>


