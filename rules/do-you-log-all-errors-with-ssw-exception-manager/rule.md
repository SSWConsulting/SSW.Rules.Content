---
seoDescription: Log all unhandled exceptions to provide developers with sufficient information to fix bugs when they occur, using a customized exception management block that logs to a database via a web service.
type: rule
title: Do you log all errors (with SSW Exception Manager)?
uri: do-you-log-all-errors-with-ssw-exception-manager
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T05:37:00.000Z
guid: e34839fb-b482-4c4c-8e0d-e6a5565a6f31
---

All unhandled exceptions should be logged to provide developers with sufficient information to fix bugs when they occur. There are two options we for logging exceptions:

<!--endintro-->

The Microsoft **Exception Management Application Block**Microsoft provides full source code for the EMAB, which is fully extensible with custom logging target extensions. We decided to customize the EMAB to produce the SSW Exception Management Block, which logs exceptions to a database using a web service, allowing us to keep a history of all exceptions.

![Figure: Exception Reporting Web Service](exceptionreportingservice.gif)

Your code should not contain any empty catch blocks as this can hamper exception handling and debugging.

We have a program called [SSW Code Auditor](https://ssw.com.au/ssw/CodeAuditor/) to check for this rule.

We have a program called [SSW .NET Toolkit](https://ssw.com.au/ssw/NETToolkit/) that implements Exception Logging and Handling
