---
type: rule
title: Do you know that you should never throw an exception using System.Exception?
uri: do-you-know-that-you-should-never-throw-an-exception-using-systemexception
created: 2013-09-11T21:27:14.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 38
  title: Drew Robson

---



<span class='intro'> <p class="p1">​​​While everyone knows that '<span class="s1">catch (Exception ex)'</span> is bad, no one has really noticed that&#160;'<span class="s1">throw new Exception()'</span> is worse.</p><p class="p2">System.Exception is a very extensive class, and it is inherited by all other exception classes. If you throw an exception with the code 'throw new Exception()', what you need subsequently to handle the exception will be the infamous 'catch (Exception ex)'.</p> </span>

<p>As a standard, you should use an exception class with the name that best describes the exception's detail. All exception classes in .NET Framework follow this standard very well. As a result, when you see exceptions like FileNotFoundException or DivideByZeroException, you know what's happening just by looking at the exception's name. The .NET Framework has provided us a comprehensive list of exception classes that can we can use. If you really can't find one that is suitable for the situation, then create your own exception class with the name that best describes the exception (eg&#58; EmployeeListNotFoundException).</p>
<p>Also, System.ApplicationException should be avoided as well unless it's an exception related to the application. While it's acceptable and should be used in certain cases, be aware that using it broadly&#160;will be just as bad as 'throw new Exception()'.</p><p>
               <span class="ssw-rteStyle-YellowBorderBox">We have a program called&#160;<a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Default.aspx">SSW Code Auditor</a>&#160;to check for this rule.</span></p>


