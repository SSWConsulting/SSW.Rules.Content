---
type: rule
archivedreason: 
title: Do you use LINQ instead of CAML?
guid: ceb1e790-eafc-44f3-91b9-c718c7bba67e
uri: do-you-use-linq-instead-of-caml
created: 2009-12-09T04:22:07.0000000Z
authors:
- title: Andy Taslim
  url: https://ssw.com.au/people/andy-taslim
related: []
redirects: []

---


In SharePoint development, it is always a good practice to use LINQ, instead of CAML.<br>
Why CAML is bad?
<ul>
    <li>New language skills required for .NET developers </li>
    <li>No IntelliSense or strongly typed objects </li>
</ul>

<br><excerpt class='endintro'></excerpt><br>

  <p>Why LINQ is good? </p>
<ul>
    <li>No new language skills required </li>
    <li>Easier to read and write </li>
    <li>SPMetal is awesome for generating entity classes </li>
    <li>In the backend, LINQ provider translates as much as it can to CAML first </li>
</ul>
<font class="ms-rteCustom-CodeArea">SPQueryquery = newSPQuery(); <br>
query.Query= String.Format(“<br>
&lt;Where&gt;<br>
&lt;And&gt;<br>
&lt;Contains&gt;&lt;FieldRefName=‘Tags’ /&gt;&lt;ValueType=‘Text’&gt;&#123;0&#125;&lt;/Value&gt;&lt;/Contains&gt;<br>
&lt;IsNotNull&gt;&lt;FieldRefName=‘URL’ /&gt;&lt;/IsNotNull&gt;<br>
&lt;/And&gt;<br>
&lt;/Where&gt;<br>
&lt;OrderBy&gt;<br>
&lt;FieldRefName=‘PostedOn’ Ascending=‘TRUE’ /&gt;<br>
&lt;/OrderBy&gt;”, _filter);<br>
SPListItemCollectionlistItemsColl= resourceList.GetItems(query);</font><br>
<font class="ms-rteCustom-FigureBad">Figure&#58; Bad example – using CAML </font><font class="ms-rteCustom-CodeArea">Var resourceListItems =<br>
From SPListItem item in resourceList.Items<br>
Where item.Tags.ToString().ToLower().Contains(_filter)<br>
&amp;&amp; item.URL.ToString().Length&gt; 0<br>
OrderBy item.PostedOn Ascending</font> &#160;<font class="ms-rteCustom-FigureGood">Figure&#58; Good example – using LINQ</font> 



