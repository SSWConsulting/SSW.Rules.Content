---
type: rule
archivedreason: 
title: Do you use Global List?
guid: 07e5066e-4c30-46e4-b5b4-010eaf570cd2
uri: do-you-use-global-list
created: 2012-07-18T07:23:54.0000000Z
authors:
- title: Lei Xu
  url: https://ssw.com.au/people/lei-xu
related: []
redirects: []

---

Global list could be referenced in multiple work item types, if you are using the same list in different places and want to keep the drop down items consistent, global list is the best practise.

<!--endintro-->

```
&lt;FIELD
name="Discipline"
refname="Microsoft.VSTS.Common.Discipline"
type="String"&gt;
<font face="Verdana, sans-serif">&#160;&#160;</font>&lt;HELPTEXT&gt;The discipline to which the task belongs&lt;/HELPTEXT&gt;
  &lt;ALLOWEDVALUES expanditems="true"&gt;
    &lt;LISTITEM value="Development" /&gt;
    &lt;LISTITEM value="Test" /&gt;
    &lt;LISTITEM value="Project Management" /&gt;
    &lt;LISTITEM value="Requirements" /&gt;
    &lt;LISTITEM value="Architecture" /&gt;
    &lt;LISTITEM value="Release Management" /&gt;
  &lt;/ALLOWEDVALUES&gt;
&lt;/FIELD&gt;
```
::: bad
Figure: Bad Example – embed the list items in work item type definition
:::

```
&lt;?xml
version="1.0" encoding="utf-8"?&gt;
&lt;gl:GLOBALLISTS  xmlns:gl="http://schemas.microsoft.com/VisualStudio/2005/workitemtracking/globallists"&gt;
  &lt;GLOBALLIST name="Disciplines"&gt;
    &lt;LISTITEM value="Architecture" /&gt;
    &lt;LISTITEM value="Requirements" /&gt;
    &lt;LISTITEM value="Development" /&gt;
    &lt;LISTITEM value="Release Management" /&gt;
    &lt;LISTITEM value="Project Management" /&gt;
    &lt;LISTITEM value="Test" /&gt;
  &lt;/GLOBALLIST&gt;
&lt;/gl:GLOBALLISTS&gt;
Figure: Good Example - Save above as
GlobalList.xml file 
&lt;FIELD
name="Discipline"
refname="Microsoft.VSTS.Common.Discipline"
type="String"&gt;
  &lt;HELPTEXT&gt;The discipline to which the task belongs&lt;/HELPTEXT&gt;
  &lt;ALLOWEDVALUES&gt;
    &lt;GLOBALLIST name="Disciplines" /&gt;
  &lt;/ALLOWEDVALUES&gt;
&lt;/FIELD&gt;
```
::: good
Figure: Good Example - Reference a global list in work item type definitionNote: Global list is defined at the Team Project Collection level and it needs to be uploaded before the process template could be uploaded
:::
