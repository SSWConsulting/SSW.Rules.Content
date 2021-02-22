---
type: rule
archivedreason: 
title: Do you know that you should never throw an exception using System.Exception?
guid: d1c0e7ba-09e6-4b89-b2d5-695e47e18064
uri: do-you-know-that-you-should-never-throw-an-exception-using-system-exception
created: 2013-09-11T21:27:14.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Drew Robson
  url: https://ssw.com.au/people/drew-robson
related: []
redirects: []

---

While everyone knows that 'catch (Exception ex)' is bad, no one has really noticed that 'throw new Exception()' is worse.

System.Exception is a very extensive class, and it is inherited by all other exception classes. If you throw an exception with the code 'throw new Exception()', what you need subsequently to handle the exception will be the infamous 'catch (Exception ex)'.

<!--endintro-->

As a standard, you should use an exception class with the name that best describes the exception's detail. All exception classes in .NET Framework follow this standard very well. As a result, when you see exceptions like FileNotFoundException or DivideByZeroException, you know what's happening just by looking at the exception's name. The .NET Framework has provided us a comprehensive list of exception classes that we can use. If you really can't find one that is suitable for the situation, then create your own exception class with the name that best describes the exception (e.g.: EmployeeListNotFoundException).

Also, System.ApplicationException should be avoided as well unless it's an exception related to the application. While it's acceptable and should be used in certain cases, be aware that using it broadly will be just as bad as 'throw new Exception()'.

We have a program called [SSW Code Auditor](http&#58;//www.ssw.com.au/ssw/CodeAuditor/Default.aspx) to check for this rule.
