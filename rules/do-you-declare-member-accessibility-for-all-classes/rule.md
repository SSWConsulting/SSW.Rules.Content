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

Not explicitly specifying the access type for members of a structure or class can be deceiving for other developers that are using this structure or class. The default structure and class members access in Visual C# .NET is always private. The default class member access in Visual Basic .NET is private. However, the default structure member access in Visual Basic .NET is public.

<!--endintro-->

Match MatchExpression(string input, string pattern)


::: bad
Figure: Bad - Method without member accessibility declared 

:::


private Match MatchExpression(string input, string pattern)


::: good
Figure: Good - Method with member accessibility declared
:::


We have a program called [SSW Code Auditor](https&#58;//www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#Interoper) to check for this rule.
