---
type: rule
archivedreason: 
title: Do you use TreeView control instead of XML control?
guid: 2dd6eaff-aede-41d2-b46f-d0a715fce3de
uri: do-you-use-treeview-control-instead-of-xml-control
created: 2009-04-29T06:20:33.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
related: []
redirects: []

---



  <br>
Both controls can represent XML hierarchical data and support Extensible Stylesheet Language (XSL) templates, which can be used to transform an XML file into a the correct format and structure. While TreeView can apply Styles more easily, provide special properties that simplify the customization of the appearance of elements based on their current state. 

<br><excerpt class='endintro'></excerpt><br>

  <pre class="brush&#58;c-sharp">&lt;asp&#58;TreeView ID=&quot;TreeView1&quot; runat=&quot;server&quot; DataSourceID=&quot;siteMapDataSource&quot;
ImageSet=&quot;Faq&quot; SkipLinkText =&quot;&quot;&gt; 
&lt;ParentNodeStyle Font-Bold=&quot;False&quot; /&gt; 
&lt;HoverNodeStyle Font-Underline=&quot;True&quot; ForeColor=&quot;Purple&quot; /&gt;   
&lt;SelectedNodeStyle Font-Underline=&quot;True&quot; HorizontalPadding=&quot;0px&quot;
VerticalPadding=&quot;0px&quot; /&gt; 
&lt;NodeStyle Font-Names=&quot;Tahoma&quot; Font-Size=&quot;8pt&quot; ForeColor=&quot;DarkBlue&quot;
HorizontalPadding=&quot;5px&quot; NodeSpacing=&quot;0px&quot; VerticalPadding=&quot;0px&quot; /&gt;
&lt;/asp&#58;TreeView&gt;
&lt;asp&#58;SiteMapDataSource ID=&quot;siteMapDataSource&quot;  runat=&quot;server&quot; /&gt;                    </pre>
<span class="ms-rteCustom-FigureGood">Figure&#58; Good Code - <a href="http&#58;//www.ssw.com.au/Demos/03TreeView/Default.aspx">Use TreeView to represent XML hierarchical data</a></span>
<pre class="brush&#58;c-sharp">&lt;asp&#58;Xml ID=&quot;Xml1&quot; runat=&quot;server&quot; DocumentSource=&quot;~/Web.xml&quot;
TransformSource=&quot;~/Style.xsl&quot;&gt;&lt;/asp&#58;Xml&gt; </pre>
<span class="ms-rteCustom-FigureBad">Figure&#58; Bad Code - <a href="http&#58;//www.ssw.com.au/Demos/03TreeView/XML.aspx">Use XML to represent XML document using XSL Transformations</a></span> 



