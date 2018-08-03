---
type: rule
archivedreason: 
title: Do you make external links clear?
guid: d178549e-bdef-4636-8dc7-b3514b360bd0
uri: do-you-make-external-links-clear
created: 2015-02-16T02:21:22.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects: []

---


<p>When creating&#160;links,​​ you should&#160;follow a few basic rules&#58;
​                <br></p>
<br><excerpt class='endintro'></excerpt><br>
<ol><li>If your link is an internal link, then it should navigate&#160;within the same window. If the link is external, it should open in a new tab and be visually clear to the user that it will lead them away from the current site, that way it is not a surprise.<br></li><li>If a link is to an external site, a 
      <b>visual indication</b> should be provided to the user like this&#58; 
      <a href="http&#58;//www.ssw.com.au/ssw/Redirect/Microsoft/microsoft.htm" target="_blank">This is a link to another site</a>. 
      <dl class="badImage"><p class="ssw15-rteElement-GreyBox">Search Engines (<a class="ignore" href="http&#58;//www.ssw.com.au/ssw/Redirect/Web/Google.htm" target="_blank">http&#58;//www.google.com</a> is by far the best but try other search engines as well)</p><dd>Figure&#58; Bad example - Without visual indication</dd></dl><dl class="goodImage"><p class="ssw15-rteElement-GreyBox">Search Engines (<a href="http&#58;//www.ssw.com.au/ssw/Redirect/Web/Google.htm" target="_blank">http&#58;//www.google.com</a>&#160;is by far the best but try other search engines as well</p><dd>Figure&#58; Good example - With visual indication<br></dd></dl></li><li>External link 
      <strong>external indicators should be inserted by CSS</strong> as following&#58; 
      <dl class="goodImage"><p class="ssw15-rteElement-CodeArea">a[href*=&quot;//&quot;]&#58;not([href*=&quot;mysite.com&quot;])&#58;after &#123; 
            <br>&#160; &#160; content&#58; url(https&#58;//www.ssw.com.au/ssw/images/external.gif); 
            <br>&#160; &#160; padding-left&#58; 4px;<br>&#125;</p><dd>Figure&#58; Good example - Icon is added by CSS via a simple declaration<br></dd></dl></li></ol><p class="ssw15-rteElement-YellowBorderBox">We have a program called 
   <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a> to check for this rule.<br></p> ​<br>
<div><h3>Related&#160;Rule 
      <br></h3><ul><li>
         <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=1d8a7afd-9762-4bfd-971c-cacd787c28bb">
Do you make external links open on a new tab?​​</a>​<br></li></ul>
   <br>
</div>


