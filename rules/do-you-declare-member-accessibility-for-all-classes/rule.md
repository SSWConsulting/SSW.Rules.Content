---
type: rule
archivedreason: 
title: Do you declare member accessibility for all classes?
guid: b1ac5f48-0e88-4eed-8a13-c25ca5a87c6a
uri: do-you-declare-member-accessibility-for-all-classes
created: 2018-04-25T22:45:00.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

Not explicitly specifying the access type for members of a structure or class can be misleading for other developers. The default member accessibility level for classes and structs in Visual C# .NET is always private. In Visual Basic .NET, the default for classes is private, but for structs is public.

<!--endintro-->

Match MatchExpression(string input, string pattern)


::: bad
Figure: Bad - Method without member accessibility declared 

:::


private Match MatchExpression(string input, string pattern)


::: good
Figure: Good - Method with member accessibility declared

:::

<dl class="ssw15-rteElement-ImageArea"><img src="matt-w-screenshot.jpg" alt="matt-w-screenshot.jpg" style="margin:5px;width:750px;height:103px;"> <strong>Figure: Compiler warning given for not explicitly defining member access level</strong> <br></dl>


We have a program called [SSW Code Auditor](https://www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#Interoper) to check for this rule.
