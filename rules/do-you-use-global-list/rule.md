---
type: rule
archivedreason: 
title: Do you use Global List in TFS?
guid: 07e5066e-4c30-46e4-b5b4-010eaf570cd2
uri: do-you-use-global-list
created: 2012-07-18T07:23:54.0000000Z
authors:
- title: Lei Xu
  url: https://ssw.com.au/people/lei-xu
related: []
redirects: []

---

Global List could be referenced in multiple work item types, if you are using the same list in different places and want to keep the drop down items consistent, global list is the best practice.

<!--endintro-->

```xml
<FIELD
name="Discipline"
refname="Microsoft.VSTS.Common.Discipline"
type="String">
<font face="Verdana, sans-serif">&#160;&#160;</font><HELPTEXT>The discipline to which the task belongs</HELPTEXT>
  <ALLOWEDVALUES expanditems="true">
    <LISTITEM value="Development" />
    <LISTITEM value="Test" />
    <LISTITEM value="Project Management" />
    <LISTITEM value="Requirements" />
    <LISTITEM value="Architecture" />
    <LISTITEM value="Release Management" />
  </ALLOWEDVALUES>
</FIELD>
```
::: bad
Figure: Bad example – Embed the list items in work item type definition
:::

```xml
<?xml
version="1.0" encoding="utf-8"?>
<gl:GLOBALLISTS  xmlns:gl="http://schemas.microsoft.com/VisualStudio/2005/workitemtracking/globallists">
  <GLOBALLIST name="Disciplines">
    <LISTITEM value="Architecture" />
    <LISTITEM value="Requirements" />
    <LISTITEM value="Development" />
    <LISTITEM value="Release Management" />
    <LISTITEM value="Project Management" />
    <LISTITEM value="Test" />
  </GLOBALLIST>
</gl:GLOBALLISTS>
Figure: Good Example - Save above as
GlobalList.xml file 
<FIELD
name="Discipline"
refname="Microsoft.VSTS.Common.Discipline"
type="String">
  <HELPTEXT>The discipline to which the task belongs</HELPTEXT>
  <ALLOWEDVALUES>
    <GLOBALLIST name="Disciplines" />
  </ALLOWEDVALUES>
</FIELD>
```
::: good
Figure: Good example - Reference a global list in work item type definitionNote: Global list is defined at the Team Project Collection level and it needs to be uploaded before the process template could be uploaded
:::
