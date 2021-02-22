---
type: rule
archivedreason: 
title: Do you know to do data you need CAML?
guid: 81609e41-a911-4a99-9f54-fdaa2fb4a374
uri: do-you-know-to-do-data-you-need-caml
created: 2009-05-21T23:18:19.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
- title: Jay Lin
  url: https://ssw.com.au/people/jay-lin
related: []
redirects: []

---



  <span lang="EN-AU">CAML is the XML definition for all things in SharePoint, in deployment, and in creating templates, CAML is the only format.</span>
<p class="MsoNormal"><span lang="EN-AU">In SharePoint development, you will also need to know CAML, in particular, how to write a query in CAML.</span></p>
<ul>
    <li>
    <div class="MsoNormal"><span lang="EN-AU" style="font-family:symbol;"><span><span style="font:7pt 'times new roman';"> </span></span></span><span lang="EN-AU">Widely used in Content Query Web Parts</span></div>
    </li>
    <li>
    <div class="MsoNormal"><span lang="EN-AU"></span><span lang="EN-AU">Also used in SharePoint content reports</span></div>
    </li>
    <li>
    <div class="MsoNormal"><span lang="EN-AU"></span><span lang="EN-AU">In code, used by SPSiteDataQuery object</span></div>
    <span lang="EN-AU"></span></li>
</ul>
<ul>
    <div class="title"><a href="http://msdn.microsoft.com/en-us/library/ms426449.aspx">Introduction to Collaborative Application Markup Language (CAML)</a>
    <div class="title"> </div>
    <div class="title">
    <div class="title"><a href="http://msdn.microsoft.com/en-us/library/ms467521.aspx">Query Schema</a></div>
    </div>
    </div>
</ul>

<br><excerpt class='endintro'></excerpt><br>

  <p>  </p>
<dl class="goodCode">
    <dt>
    <pre>&lt;Query&gt;<br>    &lt;OrderBy&gt;<br>        &lt;FieldRef Name="Modified" Ascending="FALSE"&gt;&lt;/FieldRef&gt;<br>    &lt;/OrderBy&gt;<br>    &lt;Where&gt;<br>        &lt;And&gt;<br>            &lt;Neq&gt;<br>                &lt;FieldRef Name="Status"&gt;&lt;/FieldRef&gt;<br>                &lt;Value Type="Text"&gt;Completed&lt;/Value&gt;<br>            &lt;/Neq&gt;<br>            &lt;IsNull&gt;<br>                &lt;FieldRef Name="Sent"&gt;&lt;/FieldRef&gt;<br>            &lt;/IsNull&gt;<br>        &lt;/And&gt;<br>    &lt;/Where&gt;<br>&lt;/Query&gt;</pre>
    </dt>
    <dd>Figure: Example of CAML query </dd>
</dl>
<p class="MsoNormal"><span lang="EN-AU">You can see - CAML is essentially the same as SQL WHERE syntax, but wrapped in an XML format.</span></p>
<p class="MsoNormal"><span lang="EN-AU"></span><span lang="EN-AU">Problems with CAML:</span></p>
<ol>
    <li>
    <div class="MsoNormal"><span lang="EN-AU"><span lang="EN-AU" style="font-family:'calibri','sans-serif';font-size:11pt;">CAML is XML and is case sensitive – including attributes names. </span></span>
    <dl class="badCode">
        <dt>
        <pre>&lt;Query&gt;<br>    &lt;Where&gt;<br>        &lt;Or&gt;<br>            &lt;Eq&gt;<br>              &lt;FieldRef <font color="#400040" style="background-color:rgb(255, 255, 0);">name</font>="Status" /&gt; <br>            &lt;Value Type="Text"&gt;Completed&lt;/Value&gt;<br>            &lt;/Eq&gt;<br>            &lt;IsNull&gt;<br>                &lt;FieldRef <font style="background-color:rgb(255, 255, 0);">Name</font>="Status" /&gt;<br>            &lt;/IsNull&gt;<br>        &lt;/Or&gt;<br>    &lt;/Where&gt;<br>&lt;/Query&gt;</pre>
        </dt>
        <dd>     Figure: Example of CAML query </dd>
    </dl>
    </div>
    </li>
    <li>
    <div class="MsoNormal"><span lang="EN-AU"><span lang="EN-AU" style="font-family:'calibri','sans-serif';font-size:11pt;"><span lang="EN-AU" style="font-family:'calibri','sans-serif';font-size:11pt;">SharePoint is not good at telling you if you made a mistake with your CAML query. </span></span></span>
    <dl class="badImage">
        <dt><img src="CAMLError.png" alt="" /> </dt>
        <dd>     Figure: Debug error message</dd>
    </dl>
    </div>
    </li>
    <li>
    <div class="MsoNormal"><span lang="EN-AU"><span lang="EN-AU" style="font-family:'calibri','sans-serif';font-size:11pt;"><span lang="EN-AU" style="font-family:'calibri','sans-serif';font-size:11pt;"><span lang="EN-AU" style="font-family:'calibri','sans-serif';font-size:11pt;">Hard to debug.</span></span></span></span><br>
    <font color="#ff0000">Tips:</font> Use 3rd Party tools - U2U CAML Query Builder
    <dl class="goodImage">
        <dt><img src="U2U.png" alt="" /> </dt>
        <dd>     Figure: U2U CAML Query Builder</dd>
    </dl>
         <font color="#ff0000">Note:</font> U2U CAML Builder is the best tool that we have. There are some occasional UI and interface issues, but for creating CAML and testing it against live SharePoint lists it gets the job done. And it’s FREE! </div>
    </li>
</ol>
<p class="MsoNormal"><span lang="EN-AU"><span lang="EN-AU" style="font-family:'calibri','sans-serif';font-size:11pt;"></span></span> </p>
<p> </p>



