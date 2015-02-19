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
                </p> </span>

<ol><li> If a link is to an external site, a visual indication should be provided to the user like this&#58; 
      <a target="_blank" href="http&#58;//www.ssw.com.au/ssw/Redirect/Microsoft/microsoft.htm">This is a link to another site</a>. 
      <dl class="badImage"><p class="ssw15-rteElement-GreyBox"> Search Engines (<a target="_blank" href="http&#58;//www.ssw.com.au/ssw/Redirect/Web/Google.htm" class="ignore">http&#58;//www.google.com</a> is by far the best but try other search engines as well)</p><dd>Figure&#58; Bad example - Without visual indication</dd></dl><dl class="goodImage"><p class="ssw15-rteElement-GreyBox">Search Engines (<a target="_blank" href="http&#58;//www.ssw.com.au/ssw/Redirect/Web/Google.htm">http&#58;//www.google.com</a> is by far the best but try other search engines as well) </p><dd>Figure&#58; Good example - With visual indication</dd></dl></li><li> All external links should NOT open in a New Window - this behaviour should be up to the user's discretion and not pre-determined by your site. New windows opening without the user's permission is considered spam behaviour. </li><li> External links should always go through a Redirect file to allow monitoring of click-throughs. We store all redirects in a redirect folder - /ssw/Redirect/[SubCategoryAsRequired] to 
      <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterGoogleRankings.aspx#Robotstxtfile">avoid reducing our Google Ranking</a>. 
      <p> 
         <strong>Developer Note&#58;</strong> Do not use META refresh - instead, use server-side code (such as an ASP Response.Redirect), as this will send the proper &quot;Object moved&quot; message to the client and the redirect will be picked up by 
         <a href="http&#58;//www.ssw.com.au/ssw/Standards/DeveloperGeneral/WebdevelopmentTools.aspx#BrokenLinks">SSW Link Auditor</a>. There is also the possibility that the user has disabled META refreshes in the browser security options, as the redirect is performed on the client, not the server. </p><dl class="badImage"><p class="ssw15-rteElement-GreyBox">Microsoft Knowledge Base - 
            <a target="_blank" href="http&#58;//support.microsoft.com/support">http&#58;//support.microsoft.com/support</a> (Great for issues/bugs in your programs) </p><dd>Figure&#58; Bad example - Go through a direct link</dd></dl><dl class="goodImage"><p class="ssw15-rteElement-GreyBox">Microsoft Knowledge Base - 
            <a target="_blank" href="http&#58;//www.ssw.com.au/ssw/Redirect/Microsoft/MicrosoftSupport.htm">http&#58;//support.microsoft.com/support</a> (Great for issues/bugs in your programs) </p><dd>Figure&#58; Good example - Go through a redirect file</dd></dl><dl class="code"><dt> &lt;% Response.Redirect(&quot;http&#58;//www.link.com&quot;) %&gt; </dt><dd>Figure&#58; Sample Code for a Redirect File</dd></dl></li><li> External link images should be inserted by CSS and not embedded in the page source. 
      <dl class="badImage"><dt> 
            <img src="http&#58;//www.ssw.com.au/SSW/Standards/Rules/images/BadLink.gif" alt="" style="margin&#58;5px;" /> 
         </dt><dd>Figure&#58; Bad example - Why is this in my source code?</dd></dl><dl class="goodImage"><dt> 
            <img src="http&#58;//www.ssw.com.au/SSW/Standards/Rules/images/GoodLink.gif" alt="" style="margin&#58;5px;" /> 
         </dt><dd>Figure&#58; Good example - Icon is added by CSS via a simple declaration.</dd></dl></li></ol><p>We have a program called 
   <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a> to check for this rule. </p>


