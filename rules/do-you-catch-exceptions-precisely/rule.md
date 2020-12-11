---
type: rule
archivedreason: 
title: Do you catch exceptions precisely?
guid: 1072907b-d837-45e1-9db5-2a9236bf362f
uri: do-you-catch-exceptions-precisely
created: 2013-09-11T19:22:41.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 38
  title: Drew Robson
related: []

---

In the try and catch block, if you always catch for normal     [Exception](http&#58;//msdn.microsoft.com/en-us/library/system.exception.aspx) you will never know where the true problem is. When using try you should always expect some exception may happen, so in our code we always catch the specific exceptions.

<!--endintro-->
<dl class="bad">&lt;dt&gt;<pre>try 
&#123; 
     connection.Open();
&#125;
catch (Exception ex) 
&#123; 
     return ex.ToString ();
&#125;
</pre>&lt;/dt&gt;<dd>Bad code – Catching the general Exception</dd></dl><dl class="good">&lt;dt&gt;<pre>try 
&#123; 
     connection.Open(); 
&#125;
catch (InvalidOperationException ex) 
&#123; 
     return ex.ToString(); 
&#125;
catch (SqlException ex) 
&#123; 
     return ex.ToString(); 
&#125;
</pre>&lt;/dt&gt;<dd>Good code - Catch with specific Exception</dd></dl>
We have a program called  [SSW Code Auditor to check for this rule.](http&#58;//www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#Except)
