---
type: rule
title: Do you know this quick fix for SharePoint JavaScript errors that prevents you from switching page layout?
uri: do-you-know-this-quick-fix-for-sharepoint-javascript-errors-that-prevents-you-from-switching-page-layout
created: 2011-03-23T09:51:35.0000000Z
authors:
- id: 8
  title: John Liu

---



<span class='intro'> Follow the step to fix SharePoint JavaScript errors&#58;
 </span>


  <ol>
    <li>Your content editor is trying to change page layout via the Ribbon in SharePoint 2010 <br>
    <img alt="" class="ms-rteCustom-ImageArea" src="/PublishingImages/PagelayoutInRibbon.jpg" />&#160;<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Click Page Layout in the Ribbon</font> </li>
    <li>But they get a JavaScript error<br>
    <p>Webpage error details<br>
    <br>
    User Agent&#58; Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)<br>
    Timestamp&#58; Wed, 22 Dec 2010 01&#58;33&#58;17 UTC</p>
    <p>Message&#58; Object required<br>
    Line&#58; 2<br>
    Char&#58; 6422<br>
    Code&#58; 0<br>
    URI&#58;<a href="http&#58;//intranet.ssw.com.au/_layouts/cui.js?rev=wvoVpqlQb30nGo4DjDk8Kg%3D%3D">http&#58;//intranet.ssw.com.au/_layouts/cui.js?rev=wvoVpqlQb30nGo4DjDk8Kg%3D%3D</a></p>
    </li>
</ol>
<p>This error is likely caused by SharePoint trying to render available page layouts for the page to switch to, but there is an error.</p>
A very quick fix that can be applied by a site owner is&#58;<br>
<ol>
    <li>Site Settings | Look and Feel | Page layouts and site templates&#160; </li>
    <li>Restrict the valid number of page layouts that can be used, instead of allowing &quot;Pages in this site can use any layout&quot;<img alt="" class="ms-rteCustom-ImageArea" src="/PublishingImages/RestrictedPageLayout.jpg" /><font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Restrict valid page layouts </font></li>
    <li>This fixes the Ribbon menu<br>
    <img alt="" class="ms-rteCustom-ImageArea" src="/PublishingImages/RibbonMenu01.jpg" /><font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Ribbon menu fixed!</font> </li>
    <li>Tell your sys admin that there are broken packages in SharePoint and must be fixed ASAP </li>
</ol>



