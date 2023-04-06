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
  noimage: true
related: []
redirects: []

---

Both controls can represent XML hierarchical data and support Extensible Stylesheet Language (XSL) templates, which can be used to transform an XML file into a the correct format and structure. While TreeView can apply Styles more easily, provide special properties that simplify the customization of the appearance of elements based on their current state. 

<!--endintro-->

```
<asp:Xml ID="Xml1" runat="server" DocumentSource="~/Web.xml"
TransformSource="~/Style.xsl"></asp:Xml>
```
::: bad
**Figure: Bad Code - Use XML to represent XML document using XSL Transformations**
:::

```
<asp:TreeView ID="TreeView1" runat="server" DataSourceID="siteMapDataSource"
ImageSet="Faq" SkipLinkText =""> 
<ParentNodeStyle Font-Bold="False" /> 
<HoverNodeStyle Font-Underline="True" ForeColor="Purple" />   
<SelectedNodeStyle Font-Underline="True" HorizontalPadding="0px"
VerticalPadding="0px" /> 
<NodeStyle Font-Names="Tahoma" Font-Size="8pt" ForeColor="DarkBlue"
HorizontalPadding="5px" NodeSpacing="0px" VerticalPadding="0px" />
</asp:TreeView>
<asp:SiteMapDataSource ID="siteMapDataSource"  runat="server" />
```
::: good
**Figure: Good Code - Use TreeView to represent XML hierarchical data**
:::
