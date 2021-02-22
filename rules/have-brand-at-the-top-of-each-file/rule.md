---
type: rule
archivedreason: 
title: Comments - Do you have brand at the top of each file?
guid: f758f222-b220-47f5-aac5-cabe8401ad2f
uri: have-brand-at-the-top-of-each-file
created: 2018-04-23T23:39:43.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- comments-do-you-have-brand-at-the-top-of-each-file

---

The brand is the summary of our company.

<!--endintro-->

The brand should contain the copyright declaration.


::: bad
Bad header comments

:::



```
///<summary>
///'----------------------------------------------
/// Copyright 2017 Superior Software for Windows 
/// www.ssw.com.au All Rights Reserved.
///'----------------------------------------------
/// Comment: User class to handle user preference and login information
/// Authors:   DDK,PH
/// Reviewers: AC,RD
///</summary>
///'----------------------------------------------
```





::: good
Good header comments

:::




```
/// Copyright 2017 www.ssw.com.au
```
