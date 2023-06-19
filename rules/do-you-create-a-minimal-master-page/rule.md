---
type: rule
title: Do you create a minimal master page?
uri: do-you-create-a-minimal-master-page
authors:
  - title: John Liu
    url: https://ssw.com.au/people/john-liu
  - title: Jay Lin
    url: https://ssw.com.au/people/jay-lin
related: []
redirects: []
created: 2009-06-18T06:46:53.000Z
archivedreason: This rule should be archived as no one really creates
  masterpages anymore - classic pages using Master Pages are considered old
guid: 591f621f-a7fb-4ff3-b86d-4ca3fbc085e1
---

To create a master page or reuse an existing master page is a time-consuming process. Because you have to determine what the Office SharePoint Server 2007 page model requires — necessary content placeholders and controls to work with the page layouts.

Another problem of Default.master is that it contains many tables that are difficult to style.  

<!--endintro-->

``` cs
<%@Master language="C#">
...
<HEAD runat="server">
...
<Title ID=onetidTitle><asp:ContentPlaceHolder id=PlaceHolderPageTitle runat="server"/></Title>
...
</HEAD>
<BODY scroll="yes” ... >
<form runat="server" onsubmit="return _spFormOnSubmitWrapper();"><WebPartPages:SPWebPartManager id="m" runat="Server"/><table class="ms-main" CELLPADDING=0 CELLSPACING=0 BORDER=0 WIDTH="100%" HEIGHT="100%"> <tr> <td> <asp:ContentPlaceHolder id="PlaceHolderGlobalNavigation" runat="server"> <table CELLPADDING=0 CELLSPACING=0 BORDER=0 WIDTH="100%"> ... </table> </asp:ContentPlaceHolder> </td> </tr> <tr> ... </tr> <tr> <td id="onetIdTopNavBarContainer" WIDTH=100% class="ms-bannerContainer"> <asp:ContentPlaceHolder id="PlaceHolderTopNavBar" runat="server"> ... </asp:ContentPlaceHolder> </td> </tr> <tr height="100%"> <td> <table width="100%" height="100%" cellspacing="0" cellpadding="0"> ... </table> </td> </tr> </table> <asp:ContentPlaceHolder id="PlaceHolderFormDigest" runat="server"> ... </asp:ContentPlaceHolder> ... </form> <asp:ContentPlaceHolder id="PlaceHolderUtilityContent" runat="server"/> <asp:ContentPlaceHolder id="PlaceHolderBodyAreaClass" runat="server"/> <asp:ContentPlaceHolder id="PlaceHolderTitleAreaClass" runat="server"/> 
</BODY>
</HTML>
```
::: bad
Bad example - using default master page   
:::

So we recommend using the minimal master page which includes the necessary placeholders.

To create a minimal master page

1. Open SharePoint Designer.
2. On the File menu, click New, point to SharePoint Content, and then click the Page tab.
3. Double-click Master Page to create a new master page.
4. Click Design to show the master page in design view. You should see header and left margin areas and several content placeholders in the master page.
5. Click Code to show the master page in code view.
6. Copy the code into the master page  

[SharePoint 2007 - How to: Create a Minimal Master Page](https://learn.microsoft.com/en-us/previous-versions/office/developer/sharepoint-2007/aa660698(v=office.12)?redirectedfrom=MSDN)  

[SharePoint 2010 - Create a minimal master page in SharePoint](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/how-to-create-a-minimal-master-page-in-sharepoint?redirectedfrom=MSDN)

``` cs
<%@ Master language="C#" %> ... <html>     
<WebPartPages:SPWebPartManager runat="server"/>     
<SharePoint:RobotsMetaTag runat="server"/>     
<head runat="server">         
<asp:ContentPlaceHolder runat="server" id="head">             
<title><asp:ContentPlaceHolder id="PlaceHolderPageTitle" runat="server" /></title>
</asp:ContentPlaceHolder>
<Sharepoint:CssLink runat="server"/>
<asp:ContentPlaceHolder id="PlaceHolderAdditionalPageHead" runat="server" />
</head>
<body onload="javascript:_spBodyOnLoadWrapper();">
<form runat="server" onsubmit="return _spFormOnSubmitWrapper();">
<wssuc:Welcome id="explitLogout" runat="server"/>
<PublishingSiteAction:SiteActionMenu runat="server"/>
<PublishingWebControls:AuthoringContainer id="authoringcontrols" runat="server">
<PublishingConsole:Console runat="server" />
</PublishingWebControls:AuthoringContainer>
<asp:ContentPlaceHolder id="PlaceHolderMain" runat="server" />
<asp:Panel visible="false" runat="server">
<asp:ContentPlaceHolder id="PlaceHolderSearchArea" runat="server"/>
...
</asp:Panel>
</form>
</body>
</html>
```
::: good
Good example - using minimal master page
:::

7. On the File menu, click Save As, provide a unique file name with the .master extension, and then save the file to the master page gallery (/\_catalogs/masterpage) in your site collection.
