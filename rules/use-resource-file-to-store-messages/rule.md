---
type: rule
archivedreason: 
title: Do you use resource file to store messages?
guid: fce44252-62d0-45b3-b459-4e7014bef61e
uri: use-resource-file-to-store-messages
created: 2018-04-25T23:19:47.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-use-resource-file-to-store-messages

---


All messages are stored in one central place so it's easy to reuse. Furthermore, it is strongly typed - easy to type with IntelliSense in Visual Studio.<br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">Module Startup Dim HelloWorld As String = "Hello World!" Sub Main() Console.Write(HelloWorld)Console.Read() End Sub End Module</p><dd class="ssw15-rteElement-FigureBad">Bad example of a constant message</dd><dl class="goodImage"><dt> <img src="BetterCode_ConstantMessages.gif" alt="BetterCode_ConstantMessages.gif" /></dt><dd>Figure: Saving constant message in Resource</dd></dl> 
<p class="ssw15-rteElement-CodeArea">Module Startup Sub Main() Console.Write(My.Resources.Messages.Constant_HelloWorld) Console.Read() End Sub End Module</p><dd class="ssw15-rteElement-FigureGood">Good example of a constant message <br></dd><p>​<br></p>


