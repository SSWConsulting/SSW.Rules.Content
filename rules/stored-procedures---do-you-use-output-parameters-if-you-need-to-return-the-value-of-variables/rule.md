---
uri: stored-procedures---do-you-use-output-parameters-if-you-need-to-return-the-value-of-variables
title: Stored Procedures - Do you use OUTPUT parameters if you need to return the value of variables?
created: 2019-11-08 17:36:49
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p class="ssw15-rteElement-P">​The RETURN statement is meant for returning the execution status only, but not data. If you need to return the value of variables, use OUTPUT parameters. There is a compelling reason for this - if you use return values rather than output values to return data, money values that you return will silently be truncated.​​<br></p> </span>




