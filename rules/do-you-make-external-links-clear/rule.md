---
type: rule
title: Do you make external links clear?
uri: do-you-make-external-links-clear
created: 2015-02-16T02:21:22.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 16
  title: Tiago Araujo

---



<span class='intro'> <p>When I create links I follow a few basic rules&#58;
                <br></p> </span>

<ol><li>If a link is to an external site, a 
      <b>visual indication</b> should be provided to the user like this&#58; 
      <a href="http&#58;//www.ssw.com.au/ssw/Redirect/Microsoft/microsoft.htm" target="_blank">This is a link to another site</a>. 
      <dl class="badImage"><p class="ssw15-rteElement-GreyBox">Search Engines (<a class="ignore" href="http&#58;//www.ssw.com.au/ssw/Redirect/Web/Google.htm" target="_blank">http&#58;//www.google.com</a> is by far the best but try other search engines as well)</p><dd>Figure&#58; Bad example - Without visual indication</dd></dl><dl class="goodImage"><p class="ssw15-rteElement-GreyBox">Search Engines (<a href="http&#58;//www.ssw.com.au/ssw/Redirect/Web/Google.htm" target="_blank">http&#58;//www.google.com</a>&#160;is by far the best but try other search engines as well) 
            <br></p><dd>Figure&#58; Good example - With visual indication​<br></dd></dl></li><li>External link <b>images should be inserted by CSS</b> and not embedded in the page source. 
      <dl class="badImage"><dt> 
            <img src="http&#58;//www.ssw.com.au/SSW/Standards/Rules/images/BadLink.gif" alt="" style="margin&#58;5px;" />​ 
         </dt><dd>Figure&#58; Bad example - Why is this in my source code?</dd></dl><dl class="goodImage"><dt> 
            <img src="http&#58;//www.ssw.com.au/SSW/Standards/Rules/images/GoodLink.gif" alt="" style="margin&#58;5px;" /> 
         </dt><dd>Figure&#58; Good example - Icon is added by CSS via a simple declaration.</dd></dl></li></ol><p>We have a program called 
   <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a> to check for this rule.​<br></p>


