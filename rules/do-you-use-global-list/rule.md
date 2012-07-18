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


<p class="MsoListParagraph"><a name="OLE_LINK16"></a><a name="OLE_LINK15"></a>Global list could be referenced in multiple work item types, if you
are using the same list in different places and want to keep the drop down
items consistent, global list is the best practise.&#160;</p>
<br><excerpt class='endintro'></excerpt><br>
<p class="MsoNormal ssw-rteStyle-CodeArea">​​​<span style="font-size&#58;9pt;font-family&#58;arial, sans-serif;">​​{ltHTMLChar}FIELD
name=&quot;Discipline&quot;
refname=&quot;Microsoft.VSTS.Common.Discipline&quot;
type=&quot;String&quot;{gtHTMLChar}<br><font face="Verdana, sans-serif">&#160;&#160;</font>{ltHTMLChar}HELPTEXT{gtHTMLChar}The discipline to which the task belongs{ltHTMLChar}/HELPTEXT{gtHTMLChar}<br>&#160; {ltHTMLChar}ALLOWEDVALUES expanditems=&quot;true&quot;{gtHTMLChar}<br>&#160; &#160; {ltHTMLChar}LISTITEM value=&quot;Development&quot; /{gtHTMLChar}<br>&#160; &#160; {ltHTMLChar}LISTITEM value=&quot;Test&quot; /{gtHTMLChar}<br>&#160; &#160; {ltHTMLChar}LISTITEM value=&quot;Project Management&quot; /{gtHTMLChar}<br>&#160; &#160; {ltHTMLChar}LISTITEM value=&quot;Requirements&quot; /{gtHTMLChar}<br>&#160; &#160; {ltHTMLChar}LISTITEM value=&quot;Architecture&quot; /{gtHTMLChar}<br>&#160; &#160; {ltHTMLChar}LISTITEM value=&quot;Release Management&quot; /{gtHTMLChar}<br>&#160;&#160;{ltHTMLChar}/ALLOWEDVALUES{gtHTMLChar}<br>{ltHTMLChar}/FIELD{gtHTMLChar}</span></p>
<span class="ssw-rteStyle-FigureBad">​​Figure&#58; Bad Example – embed the list items in
work item type definition<br></span>

<p class="MsoNormal ssw-rteStyle-CodeArea"><span style="font-size&#58;9pt;font-family&#58;verdana, sans-serif;">{ltHTMLChar}?xml
version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?{gtHTMLChar}<br></span><span>{ltHTMLChar}gl&#58;GLOBALLISTS &#160;xmlns&#58;gl=&quot;http&#58;//schemas.microsoft.com/VisualStudio/2005/workitemtracking/globallists&quot;{gtHTMLChar}</span><br><span>&#160;<span class="ssw-rteStyle-Highlight"> {ltHTMLChar}GLOBALLIST name=&quot;Disciplines&quot;{gtHTMLChar}</span></span><br><span>&#160; &#160; {ltHTMLChar}LISTITEM value=&quot;Architecture&quot; /{gtHTMLChar}</span><br><span>&#160; &#160; {ltHTMLChar}LISTITEM value=&quot;Requirements&quot; /{gtHTMLChar}</span><br><span>&#160; &#160; {ltHTMLChar}LISTITEM value=&quot;Development&quot; /{gtHTMLChar}</span><br><span>&#160; &#160; {ltHTMLChar}LISTITEM value=&quot;Release Management&quot; /{gtHTMLChar}</span><br><span>&#160; &#160;&#160;{ltHTMLChar}LISTITEM value=&quot;Project Management&quot; /{gtHTMLChar}</span><br><span>&#160; &#160; {ltHTMLChar}LISTITEM value=&quot;Test&quot; /{gtHTMLChar}</span><br><span>&#160; {ltHTMLChar}/GLOBALLIST{gtHTMLChar}</span><br><span>{ltHTMLChar}/gl&#58;GLOBALLISTS{gtHTMLChar}​</span></p>
<span class="ssw-rteStyle-FigureGood">Figure&#58; Good Example - Save above as
GlobalList.xml file​<span style="font-family&#58;verdana, sans-serif;font-size&#58;9pt;">&#160;</span></span>

<p class="MsoNormal ssw-rteStyle-CodeArea"><span></span><span style="font-size&#58;9pt;font-family&#58;verdana, sans-serif;">{ltHTMLChar}FIELD
name=&quot;Discipline&quot;
refname=&quot;Microsoft.VSTS.Common.Discipline&quot;
type=&quot;String&quot;{gtHTMLChar}<br></span><span style="font-family&#58;verdana, sans-serif;font-size&#58;9pt;">&#160; {ltHTMLChar}HELPTEXT{gtHTMLChar}The discipline to which the task belongs{ltHTMLChar}/HELPTEXT{gtHTMLChar}<br></span><span style="font-family&#58;verdana, sans-serif;font-size&#58;9pt;">&#160; {ltHTMLChar}ALLOWEDVALUES{gtHTMLChar}<br></span><span style="font-family&#58;verdana, sans-serif;font-size&#58;9pt;">&#160; &#160;<span class="ssw-rteStyle-Highlight"> {ltHTMLChar}GLOBALLIST name=&quot;Disciplines&quot; /{gtHTMLChar}</span><br></span><span style="font-family&#58;verdana, sans-serif;font-size&#58;9pt;">&#160; {ltHTMLChar}/ALLOWEDVALUES{gtHTMLChar}<br></span><span style="font-family&#58;verdana, sans-serif;font-size&#58;9pt;">{ltHTMLChar}/FI</span><span style="font-family&#58;verdana, sans-serif;font-size&#58;9pt;">ELD{gtHTMLChar}​​</span></p>
<span class="ssw-rteStyle-FigureGood">Figure&#58; Good Example - Reference a global list
in&#160;work item typ</span><span class="ssw-rteStyle-FigureGood">e&#160;definition</span><span class="ssw-rteStyle-Tip">No</span><span class="ssw-rteStyle-Tip">te&#58;&#160;Global list is defined at the Team
Project Collection level and it needs to be uploaded before the process
template could be uploaded.&#160;</span>
​​​​​​


