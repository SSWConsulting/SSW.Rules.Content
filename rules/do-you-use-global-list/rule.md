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


<p class="MsoListParagraph">​​<a name="OLE_LINK16"></a><a name="OLE_LINK15"></a>Global list could be referenced in multiple work item types, if you
are using the same list in different places and want to keep the drop down
items con​sistent, global list is the best practise.&#160;</p>
<br><excerpt class='endintro'></excerpt><br>
<p class="MsoNormal ssw-rteStyle-CodeArea">​​​<span style="font-size&#58;9pt;font-family&#58;arial, sans-serif;">​​&lt;FIELD
name=&quot;Discipline&quot;
refname=&quot;Microsoft.VSTS.Common.Discipline&quot;
type=&quot;String&quot;&gt;<br><font face="Verdana, sans-serif">&#160;&#160;</font>&lt;HELPTEXT&gt;The discipline to which the task belongs&lt;/HELPTEXT&gt;<br>&#160; &lt;ALLOWEDVALUES expanditems=&quot;true&quot;&gt;<br>&#160; &#160; &lt;LISTITEM value=&quot;Development&quot; /&gt;<br>&#160; &#160; &lt;LISTITEM value=&quot;Test&quot; /&gt;<br>&#160; &#160; &lt;LISTITEM value=&quot;Project Management&quot; /&gt;<br>&#160; &#160; &lt;LISTITEM value=&quot;Requirements&quot; /&gt;<br>&#160; &#160; &lt;LISTITEM value=&quot;Architecture&quot; /&gt;<br>&#160; &#160; &lt;LISTITEM value=&quot;Release Management&quot; /&gt;<br>&#160;&#160;&lt;/ALLOWEDVALUES&gt;<br>&lt;/FIELD&gt;</span></p>
<span class="ssw-rteStyle-FigureBad">​​Figure&#58; Bad Example – embed the list items in
work item type definition<br></span>

<p class="MsoNormal ssw-rteStyle-CodeArea"><span style="font-size&#58;9pt;font-family&#58;verdana, sans-serif;">&lt;?xml
version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;<br></span><span>&lt;gl&#58;GLOBALLISTS &#160;xmlns&#58;gl=&quot;http&#58;//schemas.microsoft.com/VisualStudio/2005/workitemtracking/globallists&quot;&gt;</span><br><span>&#160;<span class="ssw-rteStyle-Highlight"> &lt;GLOBALLIST name=&quot;Disciplines&quot;&gt;</span></span><br><span>&#160; &#160; &lt;LISTITEM value=&quot;Architecture&quot; /&gt;</span><br><span>&#160; &#160; &lt;LISTITEM value=&quot;Requirements&quot; /&gt;</span><br><span>&#160; &#160; &lt;LISTITEM value=&quot;Development&quot; /&gt;</span><br><span>&#160; &#160; &lt;LISTITEM value=&quot;Release Management&quot; /&gt;</span><br><span>&#160; &#160;&#160;&lt;LISTITEM value=&quot;Project Management&quot; /&gt;</span><br><span>&#160; &#160; &lt;LISTITEM value=&quot;Test&quot; /&gt;</span><br><span>&#160; &lt;/GLOBALLIST&gt;</span><br><span>&lt;/gl&#58;GLOBALLISTS&gt;​</span></p>
<span class="ssw-rteStyle-FigureGood">Figure&#58; Good Example - Save above as
GlobalList.xml file​<span style="font-family&#58;verdana, sans-serif;font-size&#58;9pt;">&#160;</span></span>

<p class="MsoNormal ssw-rteStyle-CodeArea"><span style="font-size&#58;9pt;font-family&#58;verdana, sans-serif;">&lt;FIELD
name=&quot;Discipline&quot;
refname=&quot;Microsoft.VSTS.Common.Discipline&quot;
type=&quot;String&quot;&gt;<br></span><span style="font-family&#58;verdana, sans-serif;font-size&#58;9pt;">&#160; &lt;HELPTEXT&gt;The discipline to which the task belongs&lt;/HELPTEXT&gt;<br></span><span style="font-family&#58;verdana, sans-serif;font-size&#58;9pt;">&#160; &lt;ALLOWEDVALUES&gt;<br></span><span style="font-family&#58;verdana, sans-serif;font-size&#58;9pt;">&#160; &#160;<span class="ssw-rteStyle-Highlight"> &lt;GLOBALLIST name=&quot;Disciplines&quot; /&gt;</span><br></span><span style="font-family&#58;verdana, sans-serif;font-size&#58;9pt;">&#160; &lt;/ALLOWEDVALUES&gt;<br></span><span style="font-family&#58;verdana, sans-serif;font-size&#58;9pt;">&lt;/FI</span><span style="font-family&#58;verdana, sans-serif;font-size&#58;9pt;">ELD&gt;​​</span></p>
<span class="ssw-rteStyle-FigureGood">Figure&#58; Good Example - Reference a global list
in&#160;work item type&#160;definition</span><span class="ssw-rteStyle-Tip">​​Note&#58;&#160;Global list is defined at the Team Project Collection level and it needs to be uploaded before the process template could be&#160;uploaded.&#160;​
</span>​​​​​​​​


