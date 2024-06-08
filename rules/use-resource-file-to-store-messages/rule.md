---
type: rule
title: Do you use resource file to store messages?
uri: use-resource-file-to-store-messages
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-use-resource-file-to-store-messages
created: 2018-04-25T23:19:47.000Z
archivedreason: null
guid: fce44252-62d0-45b3-b459-4e7014bef61e
---
All messages are stored in one central place so it's easy to reuse. Furthermore, it is strongly typed - easy to type with IntelliSense in Visual Studio.

<!--endintro-->

```vbnet
Module Startup Dim HelloWorld As String = "Hello World!" Sub Main() Console.Write(HelloWorld)Console.Read() End Sub End Module
```

::: bad
Bad example of a constant message
:::

::: good\
![Figure: Saving constant message in Resource](BetterCode_ConstantMessages.gif)
:::

```vbnet
Module Startup Sub Main() Console.Write(My.Resources.Messages.Constant_HelloWorld) Console.Read() End Sub End Module
```

::: good
Good example of a constant message 
:::
