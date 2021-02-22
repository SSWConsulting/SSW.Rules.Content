---
type: rule
archivedreason: 
title: Do you create a minimal master page?
guid: 591f621f-a7fb-4ff3-b86d-4ca3fbc085e1
uri: do-you-create-a-minimal-master-page
created: 2009-06-18T06:46:53.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
- title: Jay Lin
  url: https://ssw.com.au/people/jay-lin
related: []
redirects: []

---

To create a master page or reuse an existing master page is a time-consuming process. Because you have to determine what the Office SharePoint Server 2007 page model requires — necessary content placeholders and controls to work with the page layouts.

 Another problem of Default.master is that it contains many tables that are difficult to style.  
<!--endintro-->
     &lt;%@Master language="C#"%&gt;
...
&lt;HEAD runat="server"&gt;
...
&lt;Title ID=onetidTitle&gt;
&lt;asp:ContentPlaceHolder id=PlaceHolderPageTitle runat="server"/&gt;
&lt;/Title&gt;
...
&lt;/HEAD&gt;
&lt;BODY scroll="yes” ... &gt;
&lt;form runat="server" onsubmit="return \_spFormOnSubmitWrapper();"&gt;
&lt;WebPartPages:SPWebPartManager id="m" runat="Server"/&gt;
<font style="background-color&#58;#ffff80;">&lt;table class=&quot;ms-main&quot; CELLPADDING=0 CELLSPACING=0 BORDER=0 WIDTH=&quot;100%&quot; HEIGHT=&quot;100%&quot;&gt;</font>
&lt;tr&gt;
&lt;td&gt;
&lt;asp:ContentPlaceHolder id="PlaceHolderGlobalNavigation" runat="server"&gt;
<font style="background-color&#58;#ffff80;">&lt;table CELLPADDING=0 CELLSPACING=0 BORDER=0 WIDTH=&quot;100%&quot;&gt;</font>
...
&lt;/table&gt;
&lt;/asp:ContentPlaceHolder&gt;
&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
...
&lt;/tr&gt;
&lt;tr&gt;
&lt;td id="onetIdTopNavBarContainer" WIDTH=100% class="ms-bannerContainer"&gt;
&lt;asp:ContentPlaceHolder id="PlaceHolderTopNavBar" runat="server"&gt;
...
&lt;/asp:ContentPlaceHolder&gt;
&lt;/td&gt;
&lt;/tr&gt;
&lt;tr height="100%"&gt;
&lt;td&gt;
<font style="background-color&#58;#ffff80;">&lt;table width=&quot;100%&quot; height=&quot;100%&quot; cellspacing=&quot;0&quot; cellpadding=&quot;0&quot;&gt;</font>
...
&lt;/table&gt;
&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;asp:ContentPlaceHolder id="PlaceHolderFormDigest" runat="server"&gt;
...
&lt;/asp:ContentPlaceHolder&gt;
...
&lt;/form&gt;
&lt;asp:ContentPlaceHolder id="PlaceHolderUtilityContent" runat="server"/&gt;
&lt;asp:ContentPlaceHolder id="PlaceHolderBodyAreaClass" runat="server"/&gt;
&lt;asp:ContentPlaceHolder id="PlaceHolderTitleAreaClass" runat="server"/&gt;
&lt;/BODY&gt;
&lt;/HTML&gt; Bad example - using default master page   
So we recommend using the minimal master page which includes the necessary placeholders.
To create a minimal master page

1. Open SharePoint Designer.
2. On the File menu, click New, point to SharePoint Content, and then click the Page tab.
3. Double-click Master Page to create a new master page.
4. Click Design to show the master page in design view. You should see header and left margin areas and several content placeholders in the master page.
5. Click Code to show the master page in code view.
6. Copy the code into the master page 
SharePoint 2007 - [https://msdn.microsoft.com/en-us/library/office/aa660698(v=office.12).aspx](https&#58;//msdn.microsoft.com/en-us/library/office/aa660698%28v=office.12%29.aspx) 
SharePoint 2010 - [https://msdn.microsoft.com/en-us/library/office/dn205 273.aspx](https&#58;//msdn.microsoft.com/en-us/library/office/dn205273.aspx)
 &lt;%@ Master language=&quot;C#&quot; %&gt;
...
&lt;html&gt;
&#160;&#160;&#160; &lt;WebPartPages&#58;SPWebPartManager runat=&quot;server&quot;/&gt;
&#160;&#160;&#160; &lt;SharePoint&#58;RobotsMetaTag runat=&quot;server&quot;/&gt;
&#160;&#160;&#160; &lt;head runat=&quot;server&quot;&gt;
&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;asp&#58;ContentPlaceHolder runat=&quot;server&quot; id=&quot;head&quot;&gt;
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;title&gt;
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;asp&#58;ContentPlaceHolder id=&quot;PlaceHolderPageTitle&quot; runat=&quot;server&quot; /&gt;
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/title&gt;
&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/asp&#58;ContentPlaceHolder&gt;
&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;Sharepoint&#58;CssLink runat=&quot;server&quot;/&gt;
&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;asp&#58;ContentPlaceHolder id=&quot;PlaceHolderAdditionalPageHead&quot; runat=&quot;server&quot; /&gt;
&#160;&#160;&#160; &lt;/head&gt;
&#160;&#160;&#160; &lt;body onload=&quot;javascript&#58;_spBodyOnLoadWrapper();&quot;&gt;
&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;form runat=&quot;server&quot; onsubmit=&quot;return _spFormOnSubmitWrapper();&quot;&gt;
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;wssuc&#58;Welcome id=&quot;explitLogout&quot; runat=&quot;server&quot;/&gt;
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;PublishingSiteAction&#58;SiteActionMenu runat=&quot;server&quot;/&gt; 
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;PublishingWebControls&#58;AuthoringContainer id=&quot;authoringcontrols&quot; runat=&quot;server&quot;&gt;
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;PublishingConsole&#58;Console runat=&quot;server&quot; /&gt;
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/PublishingWebControls&#58;AuthoringContainer&gt;
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;asp&#58;ContentPlaceHolder id=&quot;PlaceHolderMain&quot; runat=&quot;server&quot; /&gt;
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;asp&#58;Panel visible=&quot;false&quot; runat=&quot;server&quot;&gt;
&#160;&#160;&#160; &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;asp&#58;ContentPlaceHolder id=&quot;PlaceHolderSearchArea&quot; runat=&quot;server&quot;/&gt;
&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160;&#160;&#160;&#160; ...
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;/asp&#58;Panel&gt;
&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/form&gt;
&#160;&#160;&#160; &lt;/body&gt;
&lt;/html&gt; <dd>&#160;&#160;&#160; Good example - using minimal master page </dd> 
7. On the File menu, click Save As, provide a unique file name with the .master extension, and then save the file to the master page gallery (/\_catalogs/masterpage) in your site collection.
