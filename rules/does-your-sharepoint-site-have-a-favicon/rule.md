---
type: rule
title: Does your SharePoint site have a favicon?
uri: does-your-sharepoint-site-have-a-favicon
created: 2009-04-21T03:40:52.0000000Z
authors:
- id: 8
  title: John Liu
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>All websites should be following 
   <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulestoBetterWebsitesGraphics.aspx#Favicon">the favicon rule</a>.</p><p>A Favicon is a small image file included on nearly all professional developed sites. When a browser hits your web site and a user bookmarks that site then the favicon.ico graphic will be displayed in the browser’s URL/address line upon subsequent visits to that site. </p> </span>

<p>Let's see how it's done for SharePoint&#58;</p>
<div class="greyBox">
   <p>&lt;head runat=&quot;server&quot;&gt; 
      <br> &#160;&#160;&#160; &lt;meta name=&quot;GENERATOR&quot; content=&quot;Microsoft SharePoint&quot;&gt; 
      <br> &#160;&#160;&#160; &lt;meta http-equiv=&quot;Content-Type&quot; content=&quot;text/html; charset=utf-8&quot;&gt;  
      <br> &#160;&#160;&#160; &lt;!--Placeholder for additional overrides--&gt; 
      <br> &#160;&#160;&#160; &lt;asp&#58;ContentPlaceHolder ID=&quot;PlaceHolderAdditionalPageHead&quot; runat=&quot;server&quot; /&gt; 
      <br> &#160;&#160;&#160; 
      <font style="background-color&#58;#ffff00;">&lt;link rel=&quot;shortcut icon&quot; href=&quot;~/Style Library/Images/SSW/Rules/ssw.ico&quot; type=&quot;image/x-icon&quot; /&gt;</font><br> &lt;/head&gt; </p></div> 
<span><strong>Figure&#58; One line of HTML lets you add your company's icon to&#160; your web page</strong></span>


