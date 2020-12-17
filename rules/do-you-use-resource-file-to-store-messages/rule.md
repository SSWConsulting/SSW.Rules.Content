---
type: rule
archivedreason: 
title: Do you use resource file to store messages?
guid: fce44252-62d0-45b3-b459-4e7014bef61e
uri: do-you-use-resource-file-to-store-messages
created: 2018-04-25T23:19:47.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

All messages are stored in one central place so it's easy to reuse. Furthermore, it is strongly typed - easy to type with IntelliSense in Visual Studio.

<!--endintro-->

Module Startup Dim HelloWorld As String = "Hello World!" Sub Main() Console.Write(HelloWorld)Console.Read() End Sub End Module


::: bad
Bad example of a constant message
:::

<dl class="goodImage">&lt;dt&gt; <img src="BetterCode_ConstantMessages.gif" alt="BetterCode_ConstantMessages.gif">&lt;/dt&gt;<dd>Figure: Saving constant message in Resource</dd></dl>
Module Startup Sub Main() Console.Write(My.Resources.Messages.Constant\_HelloWorld) Console.Read() End Sub End Module


::: good
Good example of a constant message 

:::
