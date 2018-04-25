---
type: rule
title: Do you use resource file to store messages?
uri: do-you-use-resource-file-to-store-messages
created: 2018-04-25T23:19:47.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> All message is stored in one central place so it's easy to reuse. Furthermore, it is strongly typed - easy to type with IntelliSense in Visual Studio.<br> </span>

<p class="ssw15-rteElement-CodeArea">Module Startup Dim HelloWorld As String = &quot;Hello World!&quot; Sub Main() Console.Write(HelloWorld)Console.Read() End Sub End Module</p><dd class="ssw15-rteElement-FigureBad">Bad example of a constant message</dd><dl class="goodImage"><dt> <img src="/PublishingImages/BetterCode_ConstantMessages.gif" alt="BetterCode_ConstantMessages.gif" /></dt><dd>Figure&#58; Saving constant message in Resource</dd></dl> 
<p class="ssw15-rteElement-CodeArea">Module Startup Sub Main() Console.Write(My.Resources.Messages.Constant_HelloWorld) Console.Read() End Sub End Module</p><dd class="ssw15-rteElement-FigureGood">Good example of a constant message <br></dd><p>​<br></p>


