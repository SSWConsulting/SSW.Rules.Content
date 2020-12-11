---
type: rule
archivedreason: 
title: Stored Procedures - Do you use OUTPUT parameters if you need to return the value of variables?
guid: ef02d880-7a94-47e3-bcc3-ae0ed5c13e86
uri: stored-procedures---do-you-use-output-parameters-if-you-need-to-return-the-value-of-variables
created: 2019-11-08T17:36:49.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

The RETURN statement is meant for returning the execution status only, but not data. If you need to return the value of variables, use OUTPUT parameters. There is a compelling reason for this - if you use return values rather than output values to return data, money values that you return will silently be truncated.

<!--endintro-->
