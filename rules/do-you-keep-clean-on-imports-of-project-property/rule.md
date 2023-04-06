---
type: rule
archivedreason: 
title: Do you keep clean on Imports of Project Property?
guid: 72112f81-4acd-4763-b131-eed3509dde28
uri: do-you-keep-clean-on-imports-of-project-property
created: 2009-04-27T09:22:16.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
  noimage: true
related: []
redirects: []

---

When programming in a Dot Net environment it is a good practice to remove the default imports that aren't used frequently in your code.   
<!--endintro-->

This is because IntelliSense lists will be harder to use and navigate with too many imports. For example if in VB.NET, Microsoft.VisualBasic would be a good item to have in the imports list, because it will be used in most areas of your application.

To remove all the default imports, load Project Property page and select Common properties - Imports.
![Imports VB](ImportsVB.jpg)**Figure: Using aliases with the Imports Statement** 
The Import statement makes it easier to access methods of classes by eliminating the need to explicitly type the fully qualified reference names. Aliases let you assign a friendlier name to just one part of a namespace.

For example, the carriage return-line feed sequence that causes a single piece of text to be displayed on multiple lines is part of the ControlChars class in the Microsoft.VisualBasic namespace. To use this constant in a program without an alias, you would need to type the following code:


```
MsgBox("Some text" & Microsoft.VisualBasic.ControlChars.crlf _
    & "Some more text")
```


Imports statements must always be the first lines immediately following any Option statements in a module. The following code fragment shows how to import and assign an alias to the Microsoft.VisualBasic.ControlChars namespace:


```
Imports CtrlChrs=Microsoft.VisualBasic.ControlChars
```

**Future references to this namespace can be considerably shorter:** 

```
MsgBox("Some text" & CtrlChrs.crlf & "Some more text")
```


If an Imports statement does not include an alias name, elements defined within the imported namespace can be used in the module without qualification. If the alias name is specified, it must be used as a qualifier for names contained within that namespace.
