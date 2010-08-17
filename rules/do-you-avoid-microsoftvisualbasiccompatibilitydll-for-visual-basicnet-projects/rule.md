---
type: rule
title: Do you avoid Microsoft.VisualBasic.Compatibility.dll for Visual Basic.NET projects?
uri: do-you-avoid-microsoftvisualbasiccompatibilitydll-for-visual-basicnet-projects
created: 2009-04-28T03:01:20.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> This is where you should focus your efforts on eliminating whatever VB6 baggage your programs or developer habits may carry forward into VB.NET. There are better framework options for performing the same functions provided by the compatibility library You should heed this warning from the VS.NET help file&#58; Caution&#58; It is not recommended that you use the VisualBasic.Compatibility namespace for new development in Visual Basic .NET. This namespace may not be supported in future versions of Visual Basic. Use equivalent functions or objects from other .NET namespaces instead.? ad.? 
 </span>


  <p>Avoid&#58;</p>
<ul>
    <li>InputBox </li>
    <li>ControlArray </li>
    <li>ADO support in Microsoft.VisualBasic.Compatibility.Data </li>
    <li>Environment functions </li>
    <li>Font conversions</li>
</ul>



