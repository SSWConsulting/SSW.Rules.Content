---
type: rule
title: Do you use resource file to store all the messages and globlal strings?
uri: do-you-use-resource-file-to-store-all-the-messages-and-globlal-strings
created: 2018-04-26T21:08:00.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> Storing all the messages and global strings in one place will make it easy to manage them and to keep the applications in the same style.<br><br> </span>

<dl class="image"><dt><img src="/PublishingImages/Code_StoreMessage.jpg" alt="Code_StoreMessage.jpg" /></dt><dd> ​Store messages in the Message.resx</dd></dl><p class="ssw15-rteElement-CodeArea">Catch(SqlNullValueException sqlex)<br>&#123;<br>Response.Write(&quot;The value cannot be null.&quot;);<br>&#125;</p><dd class="ssw15-rteElement-FigureBad">Bad Example - if you want to change the message, it will cost you lots of time to investigate every try-catch block</dd><p class="ssw15-rteElement-CodeArea">Catch(SqlNullValueException sqlex)<br>&#123;<br>Response.Write(GetGlobalResourceObject(&quot;Messages&quot;, &quot;SqlValueNotNull&quot;));<br>&#125;</p><dd class="ssw15-rteElement-FigureGood">Better Example - better than the hard code, but still wordy<br></dd><p class="ssw15-rteElement-CodeArea">Catch(SqlNullValueException sqlex)<br>&#123;<br>Response.Write(Resources.Messages.SqlValueNotNull); 'Good Code - storing message in resource file. <br>&#125;&#160;</p><dd class="ssw15-rteElement-FigureGood">Good Example <br></dd>


