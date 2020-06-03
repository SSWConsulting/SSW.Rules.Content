---
type: rule
title: Do you use Filtered Views or Fetch for CRM Custom Reports?
uri: do-you-use-filtered-views-or-fetch-for-crm-custom-reports
created: 2012-12-10T18:40:08.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 32
  title: Mehmet Ozdemir

---



<span class='intro'> <p>The built-in CRM report wizard is great for users to quickly and easily create reports in CRM.</p>
<dl class="image"><dt><img src="/PublishingImages/custom-reports-1.jpg" alt="" /></dt><dd>Figure&#58; The starting point</dd></dl> </span>

<p>But when the user wants to create a report that needs additional totals, different formatting, summaries in the header etc. A custom report is required.</p><p>Do you use Filtered Views or Fetch?</p><p><a href="http&#58;//msdn.microsoft.com/en-us/library/gg309722.aspx">Filtered Views</a>&#160;allows the report developer to query underlying SQL data directly. Filtered views are fully compliant with the Microsoft Dynamics CRM security model. When you run a report that obtains data from filtered views, the Microsoft Dynamics CRM security role determines what data you can view in the report.</p><dl class="image"><dt><img src="/PublishingImages/custom-reports-2.jpg" alt="" /></dt><dd>Figure&#58; Filtered Views in the CRM SQL Database</dd></dl><p><a href="http&#58;//technet.microsoft.com/en-us/library/bb928434.aspx">Fetch</a>&#160;is a proprietary query language that is used in Microsoft Dynamics CRM. It is based on a schema that describes the capabilities of the language. The FetchXML language supports similar query capabilities as query expression. It is used primarily as a serialized form of query expression, used to save a query as a user owned saved view in the userquery entity or as an organization owned view in the savedquery entity.</p><p>Now with that out of the way which one do I use?</p><ol><li>If you’re using CRM Online then you have no choice, you will use Fetch as CRM Online does not allow access to the underlying CRM SQL Database.</li><li><strong>If you are using On-Premise CRM and are *unlikely* to ever migrate to CRM Online then Filtered Views is the right choice.</strong></li><li>If you are using On-Premise CRM and there is *<strong>any*</strong>&#160;chance of moving the CRM Online then use Fetch (otherwise your custom reports will need to be re-written to use Fetch).</li></ol><p>Fetch Restrictions&#58;</p><ul class="ul1"><li>
      Fetch does not support RIGHT OUTER JOIN and FULL OUTER JOIN.</li><li>
      Fetch does not support EXISTS/IN condition with sub-query/expression.</li><li>
      <strong>An amount of 5000 returned records maximum.</strong></li><li>
      No “UNION” selects.</li><li>
      You cannot specify group by / sum queries – You can only select the records in detail and then perform the aggregation in your report.</li><li>
      Number of entity join (link) limitations.</li><li>
      <strong>FetchXML reports cannot use non-CRM online data sources.</strong></li><li>
      Learning curve – for report writers that are not familiar with FetchXML the syntax is quite different from SQL.</li></ul><p>What do you need get started writing Fetch based CRM Custom Reports?</p><ul class="ul1"><li>
      Visual Studio (or BIDS, SSDT etc)</li><li>
     <a href="http&#58;//www.microsoft.com/en-au/download/details.aspx?id=27823"><span class="s4">Dynamics Report Authoring Extensions</span></a></li></ul><p>Get up and running quickly with Fetch&#58;</p><ol class="ol1"><li>Create your report using the CRM Reporting Wizard</li><li>Save the RDL file</li><li>Import RDL file into Reporting Services Project</li><li>Update and enhance report</li><li>Upload back into CRM</li></ol><p>More advanced users will have a boilerplate(s) for the various CRM report styles they produce and just build on top of the template.</p><p>Here’s an example of a before (CRM Wizard) and after (Visual Studio) for an Activity Report&#58;</p><dl class="image"><dt><img src="/PublishingImages/custom-reports-3.jpg" alt="" /></dt><dd>Figure&#58; Report created using CRM Wizard</dd></dl><dl class="image"><dt><img src="/PublishingImages/custom-reports-3.jpg" alt="" /></dt><dd>Figure&#58; Report updated in Visual Studio</dd></dl><p>Five enhancements that required a custom report&#58;</p><ul><li>
      Company logo top left</li><li>
      Total call minutes in header</li><li>
      Total call count and minutes totals for staff</li><li>
      Links to regarding account (in a grouping)</li><li>
      Colour coded series for charts that relate back to the report data headings</li></ul><p>More Information&#58; </p><ul><li><a href="http&#58;//blogs.msdn.com/b/crminthefield/archive/2012/11/27/custom-reporting-in-microsoft-dynamics-crm-fetch-vs-filtered-views.aspx">Custom Reporting in Microsoft Dynamics CRM - Fetch vs. Filtered Views</a></li><li>
   <a href="http&#58;//social.technet.microsoft.com/wiki/contents/articles/10234.microsoft-dynamics-crm-2011-develop-fetch-xml-based-ssrs-reports-in-visual-studio-2008.aspx">Developing Fetch XML Based SSRS Reports</a>​</li></ul>
​


