---
type: rule
title: Do you avoid using duplicate connection string in web.config?
uri: do-you-avoid-using-duplicate-connection-string-in-webconfig
created: 2009-05-11T06:55:57.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>

<dl class="badCode">
<dt style="width&#58;92.01%;height&#58;172px;"><pre>&lt;connectionStrings&gt;<br>   &lt;add name=&quot;ConnectionString&quot; connectionString=&quot;Server=(local);<br>Database=NorthWind;&quot; /&gt;<br>&lt;/connectionStrings&gt;<br>&lt;appSettings&gt;<br>   &lt;add key=&quot;ConnectionString&quot; value=&quot;Server=(local);Database=NorthWind;&quot;/&gt;<br>&lt;/appSettings&gt;<br>                     </pre>
<dd>Bad example - use duplicate connection string in web.config. </dd></dl>
<table id="table5" class="clsSSWProductTable" cellspacing="2" summary="Code Auditor" cellpadding="2">
<tbody>
<tr>
<td>We have a program called <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a> to check for this rule.</td></tr></tbody></table>


