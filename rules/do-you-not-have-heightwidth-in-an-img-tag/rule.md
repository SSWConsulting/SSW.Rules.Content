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


<p>The <b>&lt;img&gt;</b> tag of HTML has 2 attributes that should not be used - height and width. &#160;Any image resizing should&#160; be done via CSS.&#160;If the height / width ratio doesn't match that of original image, the image will be stretched.</p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt>
      <img src="/PublishingImages/streched-image.jpg" alt="Stretched image which looks ugly" /> 
   </dt><dd> Figure&#58; Bad example - Stretched image caused by inline​ height/width ratio that doesn't match</dd></dl><dl class="goodImage"><dt>
      <img src="/PublishingImages/non-streched-image.jpg" alt="Image looks fine" />​ 
   </dt><dd> Figure&#58; Good example - Avoiding inline​ height/width ratio keeps the image as original</dd></dl><p class="ssw15-rteElement-YellowBorderBox"> We have a program called 
   <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#IMGWidth">SSW Code Auditor</a> to check for this rule. </p>


