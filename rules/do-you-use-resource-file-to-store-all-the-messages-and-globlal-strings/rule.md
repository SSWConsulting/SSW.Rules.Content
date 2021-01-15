---
type: rule
archivedreason: 
title: Do you use resource file to store all the messages and globlal strings?
guid: 439bff66-ff81-406e-b8b9-ddc3ad440bf4
uri: do-you-use-resource-file-to-store-all-the-messages-and-globlal-strings
created: 2018-04-26T21:08:00.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- use-resource-file-to-store-all-the-messages-and-global-strings

---

Storing all the messages and global strings in one place will make it easy to manage them and to keep the applications in the same style.


<!--endintro-->


::: ok  
![Store messages in the Message.resx](Code\_StoreMessage.jpg)  
:::



```
Catch(SqlNullValueException sqlex)
{
Response.Write("The value cannot be null.");
}
```




::: bad
Bad Example - if you want to change the message, it will cost you lots of time to investigate every try-catch block  
:::



```
Catch(SqlNullValueException sqlex)
{
Response.Write(GetGlobalResourceObject("Messages", "SqlValueNotNull"));
}
```




::: good
Better Example - better than the hard code, but still wordy

:::



```
Catch(SqlNullValueException sqlex)
{
Response.Write(Resources.Messages.SqlValueNotNull); 'Good Code - storing message in resource file. 
}
```




::: good
Good Example 

:::
