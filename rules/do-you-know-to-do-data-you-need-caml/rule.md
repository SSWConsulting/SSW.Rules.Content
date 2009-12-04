---
type: rule
title: Do you know to do data you need CAML?
uri: do-you-know-to-do-data-you-need-caml
created: 2009-05-21T23:18:19.0000000Z
authors:
- id: 8
  title: John Liu
- id: 18
  title: Jay Lin

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>

<p>&#160; 
<dl class="goodCode">
<dt><pre>&lt;Query&gt;<br>    &lt;OrderBy&gt;<br>        &lt;FieldRef Name=&quot;Modified&quot; Ascending=&quot;FALSE&quot;&gt;&lt;/FieldRef&gt;<br>    &lt;/OrderBy&gt;<br>    &lt;Where&gt;<br>        &lt;And&gt;<br>            &lt;Neq&gt;<br>                &lt;FieldRef Name=&quot;Status&quot;&gt;&lt;/FieldRef&gt;<br>                &lt;Value Type=&quot;Text&quot;&gt;Completed&lt;/Value&gt;<br>            &lt;/Neq&gt;<br>            &lt;IsNull&gt;<br>                &lt;FieldRef Name=&quot;Sent&quot;&gt;&lt;/FieldRef&gt;<br>            &lt;/IsNull&gt;<br>        &lt;/And&gt;<br>    &lt;/Where&gt;<br>&lt;/Query&gt;</pre></dt>
<dd>Figure&#58; Example of CAML query&#160;</dd></dl>
<p class="MsoNormal"><span lang="EN-AU">You can see - CAML is essentially the same as SQL WHERE syntax, but wrapped in an XML format.</span></p>
<p class="MsoNormal"><span lang="EN-AU"></span><span lang="EN-AU">Problems with CAML&#58;</span></p>
<ol>
<li>
<div class="MsoNormal"><span lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;11pt;" lang="EN-AU">CAML is XML and is case sensitive – including attributes names.&#160;</span></span> 
<dl class="badCode">
<dt><pre>&lt;Query&gt;<br>    &lt;Where&gt;<br>        &lt;Or&gt;<br>            &lt;Eq&gt;<br>              &lt;FieldRef <font style="background-color&#58;#ffff00;" color="#400040">name</font>=&quot;Status&quot; /&gt; <br>            &lt;Value Type=&quot;Text&quot;&gt;Completed&lt;/Value&gt;<br>            &lt;/Eq&gt;<br>            &lt;IsNull&gt;<br>                &lt;FieldRef <font style="background-color&#58;#ffff00;">Name</font>=&quot;Status&quot; /&gt;<br>            &lt;/IsNull&gt;<br>        &lt;/Or&gt;<br>    &lt;/Where&gt;<br>&lt;/Query&gt;<br></pre></dt>
<dd>&#160;&#160;&#160;&#160;&#160;Figure&#58; Example of CAML query&#160;</dd></dl></div></li>
<li>
<div class="MsoNormal"><span lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;11pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;11pt;" lang="EN-AU">SharePoint is not good at telling you if you made a mistake with your CAML query. </span></span></span>
<dl class="badImage">
<dt><img src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/CAMLError.png" /></dt>
<dd>&#160;&#160;&#160;&#160; Figure&#58; Debug error message</dd></dl></div></li>
<li>
<div class="MsoNormal"><span lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;11pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;11pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;11pt;" lang="EN-AU">Hard to debug.</span></span></span></span><br><font color="#ff0000">Tips&#58;</font> Use 3rd Party tools - U2U CAML Query Builder 
<dl class="goodImage">
<dt><img src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/U2U.png" /></dt>
<dd>&#160;&#160;&#160;&#160; Figure&#58; U2U CAML Query Builder</dd></dl>&#160;&#160;&#160;&#160; <font color="#ff0000">Note&#58;</font> U2U CAML Builder is the best tool that we have. There are some occasional UI and interface issues, but for creating CAML and testing it against live SharePoint lists it gets the job done. And it’s FREE! </div></li></ol>
<p class="MsoNormal"><span lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;11pt;" lang="EN-AU"></span></span>&#160;</p></span></span></span></span>
<p></p>


