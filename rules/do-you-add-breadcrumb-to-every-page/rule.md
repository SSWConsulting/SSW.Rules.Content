---
type: rule
archivedreason: 
title: Do you add breadcrumb to every page?
guid: 5234a2b4-12b1-4043-9c41-cafc041e5a45
uri: do-you-add-breadcrumb-to-every-page
created: 2015-02-16T01:46:30.0000000Z
authors: []
related: []

---

Keep a breadcrumb on every page is necessary. With this navigation tool,  users can easily location themselves and find the targets quickly. But  don't link yourself!

<!--endintro-->
<dl class="image">&lt;dt&gt; 
      <img alt="add breadcrumb to the top of the page" src="../../assets/WebsiteLayout_Breadcrumb_1.gif" style="margin:5px;">
   &lt;/dt&gt;<dd>Figure: The breadcrumb</dd></dl>
So every page should have a SiteMapPath Control.
<dl class="code">&lt;dt&gt; 
      <span style="background-color:yellow;"><></span> ID="SiteMapPath1" runat="server" SiteMapProvider="SiteMapProvider1"/> &lt;/dt&gt;<dd>Figure: SiteMapPath Control (Note: 
      <a href="http://www.ssw.com.au/ssw/redirect/ssw/CodeAuditor.htm">Code Auditor</a> checks for the yellow highlighted text)</dd></dl>
