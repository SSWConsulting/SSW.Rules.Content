---
type: rule
archivedreason: 
title: Do you avoid Microsoft.VisualBasic.Compatibility.dll for Visual Basic.NET projects?
guid: 66108924-ffa0-4179-a125-a158fba970bc
uri: do-you-avoid-microsoft-visualbasic-compatibility-dll-for-visual-basic-net-projects
created: 2009-04-28T03:01:20.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
  noimage: true
related: []
redirects: []

---

This is where you should focus your efforts on eliminating whatever VB6 baggage your programs or developer habits may carry forward into VB.NET. There are better framework options for performing the same functions provided by the compatibility library You should heed this warning from the VS.NET help file: Caution: It is not recommended that you use the VisualBasic.Compatibility namespace for new development in Visual Basic .NET. This namespace may not be supported in future versions of Visual Basic. Use equivalent functions or objects from other .NET namespaces instead.? ad.?   
<!--endintro-->

Avoid:

* InputBox
* ControlArray
* ADO support in Microsoft.VisualBasic.Compatibility.Data
* Environment functions
* Font conversions
