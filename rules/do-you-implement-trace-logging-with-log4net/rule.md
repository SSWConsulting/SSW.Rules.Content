---
seoDescription: Implement trace logging using Log4Net to debug .NET applications and gain valuable insights into application behavior.
type: rule
title: Do you implement trace logging (with Log4Net)?
uri: do-you-implement-trace-logging-with-log4net
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T05:37:00.000Z
guid: e0c0517c-3a2f-4ec5-8b0c-9beef911328b
---

By using logging, the developer has access to more information when a particular error occurs like which functions were called, what state is the application currently in and what certain variables are. This is important as a simple stack trace will only tell you **where** the error occurred but not **how** it occurred.

<!--endintro-->

[Log4Net](https://sourceforge.net/projects/log4net/) is an open-source logging library for .NET based on the Log4J library. It provides a simple to use library to enable logging in your application. It provides several logging options such as:

- XML File (Recommended)
- Text File
- Database
- Rolling log file
- Console

Log4Net also provides different levels of tracing - from INFO to DEBUG to ERROR - and allows you to easily change the logging level (through the config file)

We have a program called [SSW CodeAuditor](https://ssw.com.au/ssw/CodeAuditor/) to check for this rule.
