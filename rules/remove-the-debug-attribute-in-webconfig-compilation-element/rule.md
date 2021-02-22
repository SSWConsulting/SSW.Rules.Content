---
type: rule
archivedreason: 
title: Do you remove the debug attribute in Web.config compilation element?
guid: ca1afe81-f9e1-4b6c-92f9-1431257d080a
uri: remove-the-debug-attribute-in-webconfig-compilation-element
created: 2016-08-24T22:22:22.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-remove-the-debug-attribute-in-web-config-compilation-element

---

The debug attribute in the web.config file is very useful for ASP.NET developers. When an error occurs the developer gets detailed error report containing the stack trace, line number and what the error is.

<!--endintro-->

But when debug attribute in the Web.config file is set to true it generates symbolic information (.pdb file) every time the compiler compiles your views as well as disables code optimization. So, it slows down the execution of every page.

So if you are a developer remember to remove the debug attribute and instead use custom error messages for your web pages

We have a program called [SSW Code Auditor](https&#58;//www.ssw.com.au/ssw/codeauditor/) to check for this rule.
