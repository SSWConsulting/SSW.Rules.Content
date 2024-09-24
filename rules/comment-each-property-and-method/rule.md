---
type: rule
title: Comments - Do you comment each property and method?
uri: comment-each-property-and-method
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - comments-do-you-comment-each-property-and-method
created: 2018-04-24T17:58:34.000Z
archivedreason: out of date
guid: 7fe395e0-d32c-44c2-866e-839684c78966
---

It's important that you have a consistent code comment standard throughout an application, regardless of language. Therefore, other developers can quickly determine the workings of a function/sub/class/stored procedure. Ideally, the code should be as simple and self-explanatory as possible.

<!--endintro-->

**UPDATE:** See Robert Martin Chapter 4: Comments  [Clean Code: A Handbook of Agile Software Craftsmanship](https&#58;//www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)

E.g. catch (InteropServices.COMException ex) //Catch all COM Exceptions from third-party COM component

In JavaScript and HTML, you should put these comments between the 
&lt;HEAD&gt; and &lt;/HEAD&gt;
tags.

To delimit the comments (ie top and bottom), you should use the standard block comment markers of 
&lt;!-- and --&gt;. 

A CSS file should be delimited with the block comment marks of 
/\* and \*/.

If the file contains any function/sub module/class declaration, comments will be contained to each of them containing at least the following:

* function/sub module/class name
* role of the function/sub module/class declaration


**Above a method or property declaration:**



```cs
/// <summary>
/// 
/// </summary>
/// <param name="sender"></param>
/// <param name="e"></param>
/// <remarks ></remarks>
```



**Bonus - you can automatically generate documentation - but the number of clients that want this is minimal.**
