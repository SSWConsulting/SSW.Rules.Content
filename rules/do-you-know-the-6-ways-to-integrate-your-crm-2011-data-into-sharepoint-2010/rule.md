---
type: rule
title: Do you know the 6 ways to integrate your CRM 2011 data into SharePoint 2010?
uri: do-you-know-the-6-ways-to-integrate-your-crm-2011-data-into-sharepoint-2010
created: 2011-08-24T03:52:23.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 24
  title: Adam Stephensen
- id: 9
  title: William Yin

---



<span class='intro'> <p>You have data in CRM 2011, so how do you see it in SharePoint? The data that is stored in CRM entities should be available in SharePoint so users can find and use the data in areas such as&#58;</p>
<p>- SharePoint search</p>
<p>- SharePoint reporting (if you are using SQL Reporting Services in integrated mode)</p>
<p>There are many ways to get to this data, let's go through them&#58;</p> </span>

<div><h3 class="ssw15-rteElement-H3">OPTION 1&#58; SharePoint BCS A​​dapter (provided by the CRM Team) RECOMMENDED</h3><p>This BCS Adapter for CRM 2011 is from the CRM team (It does all of the BCS work for you by interrogating the CRM metadata service).</p><p>Summary&#58; SharePoint BCS -&gt; Pre-built Adapter (.NET Assembly) -&gt; CRM web services - &gt; CRM database</p><table cellspacing="0" cellpadding="0" border="1"><tbody><tr><td width="297" valign="top"><p>Pros</p></td><td width="295" valign="top"><p>Cons</p></td></tr><tr><td width="297" valign="top"><p><img width="9" border="0" title="clip_image002[8]" alt="clip_image002[8]" src="/PublishingImages/correct.gif" height="9" style="border-width&#58;0px;background-image&#58;none;display&#58;inline;margin&#58;5px;" />Read/Write</p><p><img width="9" border="0" title="clip_image002[9]" alt="clip_image002[9]" src="/PublishingImages/correct.gif" height="9" style="border-width&#58;0px;background-image&#58;none;display&#58;inline;margin&#58;5px;" />Minimal coding</p><p><img width="9" border="0" title="clip_image002[10]" alt="clip_image002[10]" src="/PublishingImages/correct.gif" height="9" style="border-width&#58;0px;background-image&#58;none;display&#58;inline;margin&#58;5px;" />Easiest to implement</p><p><img width="9" border="0" title="clip_image002[11]" alt="clip_image002[11]" src="/PublishingImages/correct.gif" height="9" style="border-width&#58;0px;background-image&#58;none;display&#58;inline;margin&#58;5px;" />The likely way forward (Best Practice as Microsoft)</p></td><td width="295" valign="top"><p><img width="9" border="0" title="clip_image004[13]" alt="clip_image004[13]" src="/PublishingImages/wrong.gif" height="9" style="border-width&#58;0px;background-image&#58;none;display&#58;inline;margin&#58;5px;" />Needs to be deployed and published to the web&#160;server.</p><p><img width="9" border="0" title="clip_image004[14]" alt="clip_image004[14]" src="/PublishingImages/wrong.gif" height="9" style="border-width&#58;0px;background-image&#58;none;display&#58;inline;margin&#58;5px;" />Less performance than SQL filter views directly</p><p><img width="9" border="0" title="clip_image004[15]" alt="clip_image004[15]" src="/PublishingImages/wrong.gif" height="9" style="border-width&#58;0px;background-image&#58;none;display&#58;inline;margin&#58;5px;" />Only recently released.</p></td></tr></tbody></table><p><a href="/PublishingImages/figure5.jpg"><img border="0" title="clip_image010" alt="clip_image010" src="/PublishingImages/figure5.jpg" style="border-width&#58;0px;background-image&#58;none;width&#58;582px;display&#58;inline;margin&#58;5px;" /></a>&#160;<br><strong>Figure&#58; CRM data available in SharePoint</strong></p><p class="ssw-rteStyle-Caption"><strong>More information&#58;</strong></p><p>Download from Microsoft</p><p>Read &quot;<em>Connecting to CRM Online 2011 with SharePoint 2010 Business Connectivity Services</em>&quot;</p><p>Run tool to generate the XML mapping (.BDCM)</p><p>This solution uses a BCS Connector – a .NET Assembly responsible for mapping external data into a form usable by SharePoint. This component is loaded and hosted within SharePoint 2010, and communicates with CRM via the CRM Proxy Service.</p></div><p><br></p><h3 class="ssw15-rteElement-H3">Option 2&#58; SQL Server Filtered Views<br></h3>
<p>CRM recommends that you *don't* read from the Tables, so they provide SQL Views for this purpose.</p>
<p>Summary&#58; SharePoint BCS -&gt; CRM database</p>
<table cellspacing="0" cellpadding="0" border="1" style="width&#58;592px;height&#58;202px;"><tbody><tr><td width="297" valign="top"><p>Pros</p></td>
<td width="295" valign="top"><p>Cons</p></td></tr>
<tr><td width="297" valign="top"><p><img width="9" height="9" border="0" title="clip_image002" alt="clip_image002" src="/PublishingImages/correct.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />Easiest</p>
<p><img width="9" height="9" border="0" title="clip_image002[1]" alt="clip_image002[1]" src="/PublishingImages/correct.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />Best performance</p>
<p><img width="9" height="9" border="0" title="clip_image002[2]" alt="clip_image002[2]" src="/PublishingImages/correct.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;margin&#58;0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />Codeless</p></td>
<td width="295" valign="top"><p><img width="9" height="9" border="0" title="clip_image004" alt="clip_image004" src="/PublishingImages/wrong.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />Read-only</p>
<p><img width="9" height="9" border="0" title="clip_image004[1]" alt="clip_image004[1]" src="/PublishingImages/wrong.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;margin&#58;0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />Not available for hosted CRM</p>
<p><img width="9" height="9" border="0" title="clip_image004[2]" alt="clip_image004[2]" src="/PublishingImages/wrong.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;margin&#58;0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" /> Security issues as you are exposing the view.</p></td></tr></tbody></table>
<p>Filtered Views in Microsoft CRM provide access to the data available that supports providing picklist name and id values (lookup tables).</p>
<p class="ssw-rteStyle-Caption"><b>More information&#58; </b></p>
<p>If you only want read-only for CRM on-premises data for SharePoint users, this solution is fine. You create the External Content Type directly against the Filtered Views in the CRM database.&#160; </p>
<p><a href="http&#58;//msdn.microsoft.com/en-us/library/gg328467.aspx">http&#58;//msdn.microsoft.com/en-us/library/gg328467.aspx</a></p>
<p><img width="644" height="266" border="0" title="clip_image005" alt="clip_image005" src="/PublishingImages/figure1.jpg" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />&#160;</p>
<p class="ssw-rteStyle-FigureNormal"><b>Figure&#58; The result of “SELECT * FROM FilteredCtx_Project”. Use Office SharePoint Designer to hook this up.</b></p>
<h3 class="ssw15-rteElement-H3"><br></h3><h3 class="ssw15-rteElement-H3">OPTION 3​&#58; Web Services</h3>
<p>CRM provides web services.</p>
<p>Summary&#58; SharePoint BCS -&gt; Code calling CRM web services - &gt; CRM database​</p>
<table cellspacing="0" cellpadding="0" border="1"><tbody><tr><td width="297" valign="top"><p>Pros</p></td>
<td width="295" valign="top"><p>Cons</p></td></tr>
<tr><td width="297" valign="top"><p><img width="9" height="9" border="0" title="clip_image002[3]" alt="clip_image002[3]" src="/PublishingImages/correct.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;margin&#58;0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />Read/Write</p></td>
<td width="295" valign="top"><p><img width="9" height="9" border="0" title="clip_image004[3]" alt="clip_image004[3]" src="/PublishingImages/wrong.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;margin&#58;0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />Needs lots of code and test work.</p>
<p><img width="9" height="9" border="0" title="clip_image004[4]" alt="clip_image004[4]" src="/PublishingImages/wrong.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;margin&#58;0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />Needs to be deployed and published to the web server.</p>
<p><img width="9" height="9" border="0" title="clip_image004[5]" alt="clip_image004[5]" src="/PublishingImages/wrong.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;margin&#58;0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />Less performance than SQL filter views directly #1</p></td></tr></tbody></table>
<p class="ssw-rteStyle-Tip">#1 Note&#58; Performance could be improved by making the reads from the views and the writes through the web service</p>
<p class="ssw-rteStyle-Caption"><b>More information&#58;&#160; </b></p>
<p>1. Use BCS in VS 2010</p>
<p>2. Write code that calls the CRM web services (that access the CRM data)</p>
<p>3. Test</p>
<p>4. Deploy</p>
<h3 class="ssw15-rteElement-H3"><br></h3><h3 class="ssw15-rteElement-H3">OPTION 4​​&#58; Expose OData from CRM as RSS</h3>
<p>The CRM 2011 OData Query Designer can be used to build queries to expose the data from CRM as RSS</p>
<table cellspacing="0" cellpadding="0" border="1"><tbody><tr><td width="297" valign="top"><p>Pros</p></td>
<td width="295" valign="top"><p>Cons</p></td></tr>
<tr><td width="297" valign="top"><p><img width="9" height="9" border="0" title="clip_image002[4]" alt="clip_image002[4]" src="/PublishingImages/correct.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;margin&#58;0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />Easy configuration</p></td>
<td width="295" valign="top"><p><img width="9" height="9" border="0" title="clip_image004[6]" alt="clip_image004[6]" src="/PublishingImages/wrong.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;margin&#58;0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />50 records limit. Need to page through the results.</p>
<p><img width="9" height="9" border="0" title="clip_image004[7]" alt="clip_image004[7]" src="/PublishingImages/wrong.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;margin&#58;0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />Possible issues with firewalls and proxies because it uses Integrated Security for authentication. </p>
<p><img width="9" height="9" border="0" title="clip_image004[8]" alt="clip_image004[8]" src="/PublishingImages/wrong.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;margin&#58;0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />Read-Only</p>
<p><img width="9" height="9" border="0" title="clip_image004[9]" alt="clip_image004[9]" src="/PublishingImages/wrong.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;margin&#58;0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />No easy way to consume</p></td></tr></tbody></table>
<p><b><br></b>Note&#58; You can really only call the OData endpoint from an application that already has an authentication cookie with the CRM server. <br>i.e. you can't impersonate and call it like you can the standard WCF endpoints <br>So it is really only suited to calling from Silverlight and JavaScript web resources that are delivered inside CRM (because they have the cookie)</p>
<p class="ssw-rteStyle-Caption"><b>More information&#58; </b></p>
<p>The first step is to expose the data&#58; </p>
<p>1. Install <a href="http&#58;//crm2011odatatool.codeplex.com/">http&#58;//crm2011odatatool.codeplex.com</a></p>
<p>2. Make a query </p>
<p><img width="539" height="391" border="0" title="clip_image006" alt="clip_image006" src="/PublishingImages/figure2.jpg" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;padding-left&#58;0px;width&#58;539px;padding-right&#58;0px;display&#58;inline;height&#58;391px;padding-top&#58;0px;" />&#160;</p>
<p class="ssw-rteStyle-FigureNormal"><b>Figure&#58; Designing a query</b></p>
<p>3. See the data</p>
<p><img width="547" height="347" border="0" title="clip_image007" alt="/SoftwareDevelopment/rulestobettercrm/PublishingImages/figure3.jpg" src="/PublishingImages/figure3.jpg" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;padding-left&#58;0px;width&#58;547px;padding-right&#58;0px;display&#58;inline;height&#58;347px;padding-top&#58;0px;" />&#160;</p>
<p><b>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;<span class="ssw-rteStyle-FigureNormal">&#160; Figure&#58; See the data - RSS source for xtc_countrySet</span></b></p>
<p>The second step (and the problem) is consuming the data</p>
<p><b><img width="244" height="87" border="0" title="clip_image009" alt="clip_image009" src="/PublishingImages/figure4.jpg" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" /></b>&#160;</p>
<p class="ssw-rteStyle-FigureNormal"><b>Figure&#58; BCS has no option to consume RSS data. Please Microsoft SharePoint Team, we need a new 'Data Source Type' = OData</b></p>
<p>In summary, CRM 2011 can exposes OData, but SharePoint 2010 BCS doesn't consume OData.</p>
<p>The 3 options to consume the OData/RSS data&#58;</p>
<p>· Consume the OData by SQL Server, via TSQL ???&#160;&#160;&#160; Then use BCS to call SQL Server. <br>Summary&#58; SharePoint BCS -&gt; DataSourceType&#58; SQL Server -&gt; OData- &gt; CRM database</p>
<p>You would need to be crazy to go down this route <a href="http&#58;//www.vishalseth.com/post/2009/12/22/Call-a-webservice-from-TSQL-%28Stored-Procedure%29-using-MSXML.aspx">http&#58;//www.vishalseth.com/post/2009/12/22/Call-a-webservice-from-TSQL-(Stored-Procedure)-using-MSXML.aspx</a></p>
<p>· Consume the OData by a BCS adapter + code calling web services (same story as above). <br>Summary&#58; SharePoint BCS -&gt; code calling OData- &gt; CRM database</p>
<p>· Consume the RSS by &quot;SharePoint RSS view web part&quot; directly. <br>Summary&#58; SharePoint RSS view web part -&gt; OData- &gt; CRM database <br>(not recommended as it could not be used in &quot;SharePoint Search&quot;)</p>
<p>So OData is all things horrible because it is hard to eat &#58;-(</p>
<h3 class="ssw15-rteElement-H3"><br></h3><h3 class="ssw15-rteElement-H3">OPTION 5&#58; BizTalk​</h3>
<p>Biztalk is built for mapping systems together, unfortunately this solution is only considered for large enterprises.</p>
<p>Summary&#58; SharePoint BCS -&gt; BizTalk Database - &gt; CRM database</p>
<table cellspacing="0" cellpadding="0" border="1"><tbody><tr><td width="297" valign="top"><p>Pros</p></td>
<td width="295" valign="top"><p>Cons</p></td></tr>
<tr><td width="297" valign="top"><p><img width="9" height="9" border="0" title="clip_image002[5]" alt="clip_image002[5]" src="/PublishingImages/correct.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;margin&#58;0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />Read/Write</p>
<p><img width="9" height="9" border="0" title="clip_image002[6]" alt="clip_image002[6]" src="/PublishingImages/correct.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;margin&#58;0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />The BizTalk data centre can also provide data for any system.</p>
<p><img width="9" height="9" border="0" title="clip_image002[7]" alt="clip_image002[7]" src="/PublishingImages/correct.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;margin&#58;0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />Requires little code if users already have BizTalk</p></td>
<td width="295" valign="top"><p><img width="9" height="9" border="0" title="clip_image004[10]" alt="clip_image004[10]" src="/PublishingImages/wrong.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;margin&#58;0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />BizTalk &#58;-)</p>
<p><img width="9" height="9" border="0" title="clip_image004[11]" alt="clip_image004[11]" src="/PublishingImages/wrong.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;margin&#58;0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />Deployment - Needs external work to deploy BizTalk server.</p>
<p><img width="9" height="9" border="0" title="clip_image004[12]" alt="clip_image004[12]" src="/PublishingImages/wrong.gif" style="background-image&#58;none;border-width&#58;0px;border-style&#58;none;margin&#58;0px;padding-left&#58;0px;padding-right&#58;0px;display&#58;inline;padding-top&#58;0px;" />Licence Cost</p></td></tr></tbody></table>
<p class="ssw-rteStyle-Caption"><b><br></b></p><p class="ssw-rteStyle-Caption"><br></p>
<h3 class="ssw15-rteElement-H3">Option 6&#58; OData 3rd Party solutions (doesn't exist)</h3>
<p>Today SharePoint 2010 exposes lists and document libraries as OData, but does not natively consume OData.</p>
<p>What does this mean?</p>
<p>- CRM 2011 exposes it data as OData, but cannot consume OData</p>
<p>- SharePoint 2010 exposes it data as OData, but cannot consume OData</p>
<p>....and there are no 3rd party solutions to solve this...</p>


