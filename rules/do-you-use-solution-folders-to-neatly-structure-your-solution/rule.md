---
type: rule
archivedreason: 
title: Do you use Solution Folders to Neatly Structure your Solution?
guid: 1196f685-2c8d-43ec-b2bd-108b722f4d1e
uri: do-you-use-solution-folders-to-neatly-structure-your-solution
created: 2009-04-27T08:57:42.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee
related: []

---

All the DLL references and files needed to create a setup.exe should be included in your solution. However, just including them as solution items is not enough, they will look very disordered (especially when you have a lot of solution items). And from the screenshot below, you might be wondering what the \_Instructions.docx is used for...   
<!--endintro-->
<dl class="ssw15-rteElement-ImageArea"><img src="SSW - Rules .NET Projects - Bad Solution.png" alt="SSW - Rules .NET Projects - Bad Solution.png" style="margin:5px;"></dl>

::: bad
Bad example - An unstructured solution folder
:::


An ideal way is to create "sub-solution folders" for the solution items, the common ones are "References" and "Setup". This will make your solution items look neat and in order. Look at the screenshot below, now it makes sense, we know that the \_Instructions.docx contains the instructions of what to do when creating a setup.exe.
<dl class="ssw15-rteElement-ImageArea"><img src="SSW - Rules .NET Projects - Good Solution.png" alt="SSW - Rules .NET Projects - Good Solution.png" style="margin:5px;width:375px;"></dl>

::: good
Good example - A well structured solution folder has 2 folders - "References" and "Setup" 

:::



| We have a program called [SSW Code Auditor](http://www.ssw.com.au/ssw/CodeAuditor/Default.aspx) to check for this rule.  |
| --- |
