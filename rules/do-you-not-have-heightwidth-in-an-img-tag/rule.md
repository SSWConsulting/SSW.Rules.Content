---
type: rule
archivedreason: 
title: Do you *not* have height/width in an <img> tag?
guid: 7b56ba87-23be-47a8-a534-f86990c45d44
uri: do-you-not-have-heightwidth-in-an-img-tag
created: 2014-12-22T12:28:11.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 16
  title: Tiago Araujo
related: []

---

The  **
![]()** tag of HTML has 2 attributes that should not be used -  **"height"** and **"width"** .  Any image resizing should  be done via CSS. If the height / width ratio doesn't match that of original image, the image will be stretched.

<!--endintro-->
<dl class="badImage"><p class="ssw15-rteElement-CodeArea"><img src="images/codeauditor-logo.png" alt="Code Auditor logo"><mark>width="150" height="100"</mark> /><br></p>&lt;dt&gt;
      <img src="streched-image.jpg" alt="Stretched image which looks ugly"> 
   &lt;/dt&gt;<dd> Figure: Bad example - Stretched image caused by inline height/width ratio that doesn't match</dd></dl><dl class="goodImage"><p class="ssw15-rteElement-CodeArea"><img src="images/codeauditor-logo.png" alt="Code Auditor logo"><br></p>&lt;dt&gt;
      <img src="non-streched-image.jpg" alt="Image looks fine"> 
   &lt;/dt&gt;<dd> Figure: Good example - Avoiding inline height/width ratio keeps the image as original</dd></dl>
We have a program called     [SSW Code Auditor](http://www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#IMGWidth) to check for this rule.
