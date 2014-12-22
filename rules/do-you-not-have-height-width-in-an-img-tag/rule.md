---
type: rule
archivedreason: 
title: Do you *not* have height/width in an <img> tag?
guid: 7b56ba87-23be-47a8-a534-f86990c45d44
uri: do-you-not-have-height-width-in-an-img-tag
created: 2014-12-22T12:28:11.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects: []

---


<p>The 
   <b>{ltHTMLChar}img{gtHTMLChar}</b> tag of HTML has 2 attributes - height and width -&#160;but any image resizing should&#160;​be done via CSS.&#160;If the height / width ratio doesn't match that of original image, the image will be stretched.</p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt>
      <img src="/WebSites/RulesToBetterWebsitesLayout/PublishingImages/streched-image.jpg" alt="Stretched image which looks ugly" /> 
   </dt><dd> Figure&#58; Bad example - Stretched image which looks ugly</dd></dl><p class="ssw15-rteElement-YellowBorderBox"> We have a program called 
   <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#IMGWidth">SSW Code Auditor</a> to check for this rule. </p>


