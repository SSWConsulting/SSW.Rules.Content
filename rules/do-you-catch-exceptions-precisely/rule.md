---
type: rule
title: Do you catch exceptions precisely?
uri: do-you-catch-exceptions-precisely
created: 2013-09-11T19:22:41.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 38
  title: Drew Robson

---



<span class='intro'> <p>In the try and catch block, if you always catch for normal 
   <a href="http&#58;//msdn.microsoft.com/en-us/library/system.exception.aspx">
      <span class="s1">Exception</span></a> you will never know where the true problem is. When using try we should always expect some exception may happen, in our code we always catch the specific exceptions.</p> </span>

<dl class="bad"><dt><pre>try 
&#123; 
     connection.Open();
&#125;
catch (Exception ex) 
&#123; 
     return ex.ToString ();
&#125;
</pre></dt><dd>Bad code – Catching the general Exception</dd></dl><dl class="bad"><dt><pre>try 
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
</pre></dt><dd>Good code - Catch with specific Exception</dd></dl><p><span class="ssw-rteStyle-YellowBorderBox">We have a program called&#160;</span><a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#Except" target="_blank"><span class="ssw-rteStyle-YellowBorderBox">SSW Code Auditor to check for this rule.</span></a></p><a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#Except" target="_blank">
</a>


