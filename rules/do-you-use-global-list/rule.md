---
type: rule
archivedreason: 
title: Do you use Global List?
guid: 07e5066e-4c30-46e4-b5b4-010eaf570cd2
uri: do-you-use-global-list
created: 2012-07-18T07:23:54.0000000Z
authors:
- id: 10
  title: Lei Xu
related: []

---


<p class="MsoListParagraph"><a name="OLE_LINK16"></a><a name="OLE_LINK15"></a>Global list could be referenced in multiple work item types, if you
are using the same list in different places and want to keep the drop down
items consistent, global list is the best practise.&#160;</p>
<br><excerpt class='endintro'></excerpt><br>
​​<span style="font-size&#58;10pt;font-family&#58;consolas;">&lt;FIELD
name=&quot;Discipline&quot;
refname=&quot;Microsoft.VSTS.Common.Discipline&quot;
type=&quot;String&quot;&gt;</span><p class="MsoListParagraph"><a name="OLE_LINK19"></a>&#160;</p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;
&lt;HELPTEXT&gt;The discipline to which the task belongs&lt;/HELPTEXT&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;
&lt;ALLOWEDVALUES expanditems=&quot;true&quot;&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;&#160;&#160;
&lt;LISTITEM value=&quot;Development&quot; /&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;&#160;&#160;
&lt;LISTITEM value=&quot;Test&quot; /&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;&#160;&#160;
&lt;LISTITEM value=&quot;Project Management&quot; /&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;&#160;&#160;
&lt;LISTITEM value=&quot;Requirements&quot; /&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;&#160;&#160;
&lt;LISTITEM value=&quot;Architecture&quot; /&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;&#160;&#160;
&lt;LISTITEM value=&quot;Release Management&quot; /&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;
&lt;/ALLOWEDVALUES&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&lt;/FIELD&gt;</span></p>

<p class="MsoListParagraph">Figure&#58; Bad Example – embed the list items in
work item type definition </p>

<p class="MsoListParagraph">&#160;</p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&lt;?xml
version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&lt;gl&#58;GLOBALLISTS
xmlns&#58;gl=&quot;</span><a href="http&#58;//schemas.microsoft.com/VisualStudio/2005/workitemtracking/globallists"><span style="font-size&#58;10pt;font-family&#58;consolas;">http&#58;//schemas.microsoft.com/VisualStudio/2005/workitemtracking/globallists</span></a><span style="font-size&#58;10pt;font-family&#58;consolas;">&quot;&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;&#160;&#160;
<span style="background-color&#58;yellow;">&lt;GLOBALLIST
name=&quot;Disciplines&quot;&gt;</span></span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;&#160;&#160;&#160;&#160;&#160;&#160;
&lt;LISTITEM value=&quot;Architecture&quot; /&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;&#160;&#160;&#160;&#160;&#160;&#160;
&lt;LISTITEM value=&quot;Requirements&quot; /&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;&#160;&#160;&#160;&#160;&#160;&#160;
&lt;LISTITEM value=&quot;Development&quot; /&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;&#160;&#160;&#160;&#160;&#160;&#160;
&lt;LISTITEM value=&quot;Release Management&quot; /&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;&#160;&#160;&#160;&#160;&#160;&#160;
&lt;LISTITEM value=&quot;Project Management&quot; /&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;&#160;&#160;&#160;&#160;&#160;&#160;
&lt;LISTITEM value=&quot;Test&quot; /&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;&#160;&#160;
&lt;/GLOBALLIST&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&lt;/gl&#58;GLOBALLISTS&gt;</span></p>

<p class="MsoListParagraph">Figure&#58; Good Example - Save above as
GlobalList.xml file</p>

<p class="MsoListParagraph">&#160;</p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&lt;FIELD
name=&quot;Discipline&quot;
refname=&quot;Microsoft.VSTS.Common.Discipline&quot; type=&quot;String&quot;&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;
&lt;HELPTEXT&gt;The discipline to which the task belongs&lt;/HELPTEXT&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;
&lt;ALLOWEDVALUES&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;&#160;&#160;
<span style="background-color&#58;yellow;">&lt;GLOBALLIST
name=&quot;Disciplines&quot; /&gt;</span></span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&#160;
&lt;/ALLOWEDVALUES&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;">&lt;/FIELD&gt;</span></p>

<p class="MsoListParagraph">Figure&#58; Good Example - Reference a global list
in your work item type definition </p>

<p class="MsoListParagraph">&#160;</p>

<p class="MsoListParagraph">Note&#58; Global list is defined at the Team
Project Collection level and it needs to be uploaded before the process
template could be uploaded.&#160;</p>



