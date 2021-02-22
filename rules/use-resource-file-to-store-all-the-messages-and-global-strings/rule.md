---
type: rule
archivedreason: 
title: Do you use resource file to store all the messages and globlal strings?
guid: 439bff66-ff81-406e-b8b9-ddc3ad440bf4
uri: use-resource-file-to-store-all-the-messages-and-global-strings
created: 2018-04-26T21:08:00.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-use-resource-file-to-store-all-the-messages-and-globlal-strings

---


Storing all the messages and global strings in one place will make it easy to manage them and to keep the applications in the same style.<br><br>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt><img src="Code_StoreMessage.jpg" alt="Code_StoreMessage.jpg" /></dt><dd> ​Store messages in the Message.resx</dd></dl><p class="ssw15-rteElement-CodeArea">Catch(SqlNullValueException sqlex)<br>{<br>Response.Write("The value cannot be null.");<br>}</p><dd class="ssw15-rteElement-FigureBad">Bad Example - if you want to change the message, it will cost you lots of time to investigate every try-catch block</dd><p class="ssw15-rteElement-CodeArea">Catch(SqlNullValueException sqlex)<br>{<br>Response.Write(GetGlobalResourceObject("Messages", "SqlValueNotNull"));<br>}</p><dd class="ssw15-rteElement-FigureGood">Better Example - better than the hard code, but still wordy<br></dd><p class="ssw15-rteElement-CodeArea">Catch(SqlNullValueException sqlex)<br>{<br>Response.Write(Resources.Messages.SqlValueNotNull); 'Good Code - storing message in resource file. <br>} </p><dd class="ssw15-rteElement-FigureGood">Good Example <br></dd>


