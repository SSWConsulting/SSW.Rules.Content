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
      <img src="/PublishingImages/favicon-bad.jpg" alt="" /> 
   </dt><dd>Figure&#58; Bad Example - When you don't add a favicon the user sees a generic icon</dd></dl><dl class="goodImage"><dt> 
      <img src="/PublishingImages/favicon-good.jpg" alt="" /> 
   </dt><dd> Figure&#58; Good Example - Using the favicon gives your website professional look and feel</dd></dl><h3>Which formats and sizes to use?</h3><p>The format of the image must be one of PNG (a W3C standard), GIF, or ICO. You can export your favicon in all necessary sizes on&#160;<a href="https&#58;//realfavicongenerator.net/">Favicon Generator website</a>.<br></p><h3>How to implement the favicon?</h3><ol><li>Copy your company's favicon to the root of the site</li><li>Add the highlighted code below inside the {ltHTMLChar}HEAD{gtHTMLChar} tags in your HTML</li></ol><p class="ssw15-rteElement-GreyBox">{ltHTMLChar}head{gtHTMLChar}<br>    {ltHTMLChar}title{gtHTMLChar}Page Title{ltHTMLChar}/title{gtHTMLChar}<br>    
   <span class="ssw15-rteStyle-Highlight">{ltHTMLChar}link rel=&quot;shortcut icon&quot; href=&quot;/images/favicon.ico&quot; type=&quot;image/x-icon&quot; /{gtHTMLChar}</span><br>    {ltHTMLChar}/head{gtHTMLChar}</p>    
<strong>Figure&#58; One line of HTML lets you add your company's icon to your web page</strong>
<div>
   <b><br></b><strong></strong>
   <p>This works for most websites, including ASPX WebForms, MVC and WordPress.</p><p class="ssw15-rteElement-YellowBorderBox"> We have 
      <a href="https&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW CodeAuditor</a> and 
      <a href="https&#58;//www.ssw.com.au/ssw/LinkAuditor/">SSW LinkAuditor</a> to check for this rule.​​<br></p></div>


