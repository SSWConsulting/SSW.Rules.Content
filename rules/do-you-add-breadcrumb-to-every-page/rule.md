---
type: rule
title: Do you add breadcrumb to every page?
uri: do-you-add-breadcrumb-to-every-page
created: 2015-02-16T01:46:30.0000000Z
authors: []

---



<span class='intro'> <p>Keep a breadcrumb on every page is necessary. With this navigation tool,
 users can easily location themselves and find the targets quickly. But 
don't link yourself!</p> </span>

<dl class="image"><dt> 
      <img alt="add breadcrumb to the top of the page" src="http&#58;//www.ssw.com.au/SSW/Standards/Rules/Images/WebsiteLayout_Breadcrumb_1.gif" style="margin&#58;5px;" />
   </dt><dd>Figure&#58; The breadcrumb</dd></dl><p>So every page should have a SiteMapPath Control.</p><dl class="code"><dt> 
      <span style="background-color&#58;yellow;">&lt;asp&#58;SiteMapPath</span> ID=&quot;SiteMapPath1&quot; runat=&quot;server&quot; SiteMapProvider=&quot;SiteMapProvider1&quot;/&gt; </dt><dd>Figure&#58; SiteMapPath Control (Note&#58; 
      <a href="http&#58;//www.ssw.com.au/ssw/redirect/ssw/CodeAuditor.htm">Code Auditor</a> checks for the yellow highlighted text)</dd></dl>


