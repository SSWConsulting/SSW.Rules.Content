---
type: rule
archivedreason: 
title: Do you have a favicon in your webpage?
guid: d9136030-ff29-4617-8d0b-074096ae8120
uri: do-you-have-a-favicon-in-your-webpage
created: 2015-10-13T00:47:56.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related:
- does-your-sharepoint-site-have-a-favicon
redirects: []

---


<p>A Favicon is a small image file included on professionally developed sites. The favicon reflects the look and feel of the website or the organizations' visual identity.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt> 
      <img src="favicon-bad.jpg" alt="" /> 
   </dt><dd>Figure: Bad Example - When you don't add a favicon the user sees a generic icon</dd></dl><dl class="goodImage"><dt> 
      <img src="favicon-good.jpg" alt="" /> 
   </dt><dd> Figure: Good Example - Using the favicon gives your website professional look and feel</dd></dl><h3>Which formats and sizes to use?</h3><p>The format of the image must be one of PNG (a W3C standard), GIF, or ICO. You can export your favicon in all necessary sizes on <a href="https://realfavicongenerator.net/">Favicon Generator website</a>.<br></p><h3>How to implement the favicon?</h3><ol><li>Copy your company's favicon to the root of the site</li><li>Add the highlighted code below inside the &lt;HEAD&gt; tags in your HTML</li></ol><p class="ssw15-rteElement-GreyBox">&lt;head&gt;<br>			 &lt;title&gt;Page Title&lt;/title&gt;<br>			 
   <span class="ssw15-rteStyle-Highlight">&lt;link rel="shortcut icon" href="/images/favicon.ico" type="image/x-icon" /&gt;</span><br>			 &lt;/head&gt;</p>			 
<strong>Figure: One line of HTML lets you add your company's icon to your web page</strong>
<div>
   <b><br></b><strong></strong>
   <p>This works for most websites, including ASPX WebForms, MVC and WordPress.</p><p class="ssw15-rteElement-YellowBorderBox"> We have 
      <a href="https://www.ssw.com.au/ssw/CodeAuditor/">SSW CodeAuditor</a> and 
      <a href="https://www.ssw.com.au/ssw/LinkAuditor/">SSW LinkAuditor</a> to check for this rule.​​<br></p></div>


