---
type: rule
title: Do you refer to images the correct way in ASP .NET?
uri: do-you-refer-to-images-the-correct-way-in-asp-net
created: 2009-04-28T02:35:45.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>


  <ul>
    <li>Scenario #1&#58; Images that are part of the content of a specific page eg. a picture used only on one page </li>
    <li>Scenario #2&#58;Images that are shared across on user controls which are shared across different pages in a site eg. a shared logo used across the site (commonly in user controls, or master pages) </li>
</ul>
<p>Each of these situations requires a different referencing method.</p>
<p><b>Option #1&#58;Absolute Paths (Root-Relative Paths)</b><br>
Often developers reference all images by using an absolute path (prefixing the path with a slash, which refers to the root of the site), as shown below.</p>
<pre class="brush&#58;c-sharp">&lt;img src=&quot;/Images/spacer.gif&quot; height=&quot;1&quot; width=&quot;1&quot;&gt;
</pre>
<span class="ms-rteCustom-FigureBad">Bad example - Referencing images with absolute paths</span>
<p>This has the advantage that &lt;img&gt; tags can easily be copied between pages, however it should not be used in either situation, because it requires that the website have its own site IIS and be placed in the root (not just an application), or that the entire site be in a subfolder on the production web server. For example, the following combinations of URLs are possible with this approach&#58;</p>
<table style="border-collapse&#58;collapse;" class="clsSSWTable" border="1" cellspacing="0" cellpadding="0" width="100%">
    <tbody>
        <tr>
            <th width="250">Staging Server URL </th>
            <th width="250">Production Server URL </th>
        </tr>
        <tr>
            <td width="250">http&#58;//bee&#58;81/ </td>
            <td width="250">http&#58;//www.ssw.com.au/ </td>
        </tr>
        <tr>
            <td width="250">http&#58;//bee/ssw/ </td>
            <td width="250">http&#58;//www.ssw.com.au/ssw/ </td>
        </tr>
    </tbody>
</table>
<p>As shown above, this approach makes the URLs on the staging server hard to remember, or increases the length of URLs on the production web server.</p>
<p>Verdict for Scenario #1&#58; <img alt="" style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/fail.gif" /></p>
<p>Verdict for Scenario #2&#58; <img alt="" style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/fail.gif" /></p>
<p><b>Option #2&#58;Relative Paths</b><br>
Images that are part of the content of a page should be referenced using relative paths, e.g.</p>
<pre class="brush&#58;c-sharp">&lt;img src=&quot;../Images/spacer.gif&quot; height=&quot;1&quot; width=&quot;1&quot;&gt;
</pre>
<span class="ms-rteCustom-FigureGood">Good example - Referencing images with absolute paths.</span>
<p>However, this approach is not possible with images on user controls, because the relative paths will map to the wrong location if the user control is in a different folder to the page.</p>
<p>Verdict for Scenario #1&#58; <img alt="" style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/pass.gif" /></p>
<p>Verdict for Scenario #2&#58; <img alt="" style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/fail.gif" /></p>
<p><b>Option #3&#58;Application-Relative Paths</b><br>
In order to simplify URLs, ASP.NET introduced a new feature, application relative paths. By placing a tilde (~) in front of a path, a URL can refer to the root of a site, not just the root of the web server. However, this only works on Server Controls (controls with a runat=&quot;server&quot; attribute).</p>
<p>To use this feature, you need either use ASP.NET Server controls or HTML Server controls, as shown below.</p>
<pre class="brush&#58;c-sharp"> &lt;asp&#58;Image ID=&quot;spacerImage&quot; ImageUrl=&quot;~/Images/spacer.gif&quot; Runat=&quot;server&quot; /&gt;
&lt;img id=&quot;spacerImage&quot; src=&quot;~/Images/spacer.gif&quot; originalAttribute=&quot;src&quot; originalPath=&quot;&quot;~/Images/spacer.gif&quot;&quot; runat=&quot;server&quot;&gt;</pre>
<span class="ms-rteCustom-FigureGood">Good example - Application-relative paths with an ASP.NET Server control</span>
<p>Using an HTML Server control creates less overhead than an ASP.NET Server control, but the control does not dynamically adapt its rendering to the user's browser, or provide such a rich set of server-side features.</p>
<p>Verdict for Scenario #1&#58; <img alt="" style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/fail.gif" /></p>
<p>Verdict for Scenario #2&#58; <img alt="" style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/pass.gif" /></p>
<p>Note&#58;A variation on this approach involves calling the Page.ResolveUrl method with inline code to place the correct path in a non-server tag.</p>
<pre class="brush&#58;c-sharp"> &lt;img src='&lt;%# originalAttribute=&quot;src&quot; originalPath=&quot;'&lt;%#&quot; Page.ResolveUrl(&quot;~/Images/spacer.gif&quot;) %&gt;'&gt;</pre>
<span class="ms-rteCustom-FigureBad">Bad example - Page.ResolveUrl method with a non-server tag</span>
<p>This approach is not recommended, because the data binding will create overhead and affect caching of the page. The inline code is also ugly and does not get compiled, making it easy to accidentally introduce syntax errors.</p>
<table class="clsSSWProductTable" cellspacing="2" summary="Code Auditor">
    <tbody>
        <tr>
            <td>We have a program called <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Default.aspx">SSW Code Auditor</a> to check for this rule. </td>
        </tr>
    </tbody>
</table>



