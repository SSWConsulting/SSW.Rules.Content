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
    <div class="MsoNormal"><span style="font-family&#58;symbol;" lang="EN-AU"><span><span style="font&#58;7pt 'times new roman';">&#160;</span></span></span><span lang="EN-AU">Widely used in Content Query Web Parts</span></div>
    </li>
    <li>
    <div class="MsoNormal"><span lang="EN-AU"></span><span lang="EN-AU">Also used in SharePoint content reports</span></div>
    </li>
    <li>
    <div class="MsoNormal"><span lang="EN-AU"></span><span lang="EN-AU">In code, used by SPSiteDataQuery object</span></div>
    <span lang="EN-AU"></span></li>
</ul>
<ul>
    <div class="title"><a href="http&#58;//msdn.microsoft.com/en-us/library/ms426449.aspx">Introduction to Collaborative Application Markup Language (CAML)</a>
    <div class="title">&#160;</div>
    <div class="title">
    <div class="title"><a href="http&#58;//msdn.microsoft.com/en-us/library/ms467521.aspx">Query Schema</a></div>
    </div>
    </div>
</ul>

<br><excerpt class='endintro'></excerpt><br>

  <p>&#160; </p>
<dl class="goodCode">
    <dt>
    <pre>{ltHTMLChar}Query{gtHTMLChar}<br>    {ltHTMLChar}OrderBy{gtHTMLChar}<br>        {ltHTMLChar}FieldRef Name=&quot;Modified&quot; Ascending=&quot;FALSE&quot;{gtHTMLChar}{ltHTMLChar}/FieldRef{gtHTMLChar}<br>    {ltHTMLChar}/OrderBy{gtHTMLChar}<br>    {ltHTMLChar}Where{gtHTMLChar}<br>        {ltHTMLChar}And{gtHTMLChar}<br>            {ltHTMLChar}Neq{gtHTMLChar}<br>                {ltHTMLChar}FieldRef Name=&quot;Status&quot;{gtHTMLChar}{ltHTMLChar}/FieldRef{gtHTMLChar}<br>                {ltHTMLChar}Value Type=&quot;Text&quot;{gtHTMLChar}Completed{ltHTMLChar}/Value{gtHTMLChar}<br>            {ltHTMLChar}/Neq{gtHTMLChar}<br>            {ltHTMLChar}IsNull{gtHTMLChar}<br>                {ltHTMLChar}FieldRef Name=&quot;Sent&quot;{gtHTMLChar}{ltHTMLChar}/FieldRef{gtHTMLChar}<br>            {ltHTMLChar}/IsNull{gtHTMLChar}<br>        {ltHTMLChar}/And{gtHTMLChar}<br>    {ltHTMLChar}/Where{gtHTMLChar}<br>{ltHTMLChar}/Query{gtHTMLChar}</pre>
    </dt>
    <dd>Figure&#58; Example of CAML query&#160;</dd>
</dl>
<p class="MsoNormal"><span lang="EN-AU">You can see - CAML is essentially the same as SQL WHERE syntax, but wrapped in an XML format.</span></p>
<p class="MsoNormal"><span lang="EN-AU"></span><span lang="EN-AU">Problems with CAML&#58;</span></p>
<ol>
    <li>
    <div class="MsoNormal"><span lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;11pt;" lang="EN-AU">CAML is XML and is case sensitive – including attributes names.&#160;</span></span>
    <dl class="badCode">
        <dt>
        <pre>{ltHTMLChar}Query{gtHTMLChar}<br>    {ltHTMLChar}Where{gtHTMLChar}<br>        {ltHTMLChar}Or{gtHTMLChar}<br>            {ltHTMLChar}Eq{gtHTMLChar}<br>              {ltHTMLChar}FieldRef <font style="background-color&#58;#ffff00;" color="#400040">name</font>=&quot;Status&quot; /{gtHTMLChar} <br>            {ltHTMLChar}Value Type=&quot;Text&quot;{gtHTMLChar}Completed{ltHTMLChar}/Value{gtHTMLChar}<br>            {ltHTMLChar}/Eq{gtHTMLChar}<br>            {ltHTMLChar}IsNull{gtHTMLChar}<br>                {ltHTMLChar}FieldRef <font style="background-color&#58;#ffff00;">Name</font>=&quot;Status&quot; /{gtHTMLChar}<br>            {ltHTMLChar}/IsNull{gtHTMLChar}<br>        {ltHTMLChar}/Or{gtHTMLChar}<br>    {ltHTMLChar}/Where{gtHTMLChar}<br>{ltHTMLChar}/Query{gtHTMLChar}</pre>
        </dt>
        <dd>&#160;&#160;&#160;&#160;&#160;Figure&#58; Example of CAML query&#160;</dd>
    </dl>
    </div>
    </li>
    <li>
    <div class="MsoNormal"><span lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;11pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;11pt;" lang="EN-AU">SharePoint is not good at telling you if you made a mistake with your CAML query. </span></span></span>
    <dl class="badImage">
        <dt><img alt="" src="/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/CAMLError.png" /> </dt>
        <dd>&#160;&#160;&#160;&#160; Figure&#58; Debug error message</dd>
    </dl>
    </div>
    </li>
    <li>
    <div class="MsoNormal"><span lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;11pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;11pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;11pt;" lang="EN-AU">Hard to debug.</span></span></span></span><br>
    <font color="#ff0000">Tips&#58;</font> Use 3rd Party tools - U2U CAML Query Builder
    <dl class="goodImage">
        <dt><img alt="" src="/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/U2U.png" /> </dt>
        <dd>&#160;&#160;&#160;&#160; Figure&#58; U2U CAML Query Builder</dd>
    </dl>
    &#160;&#160;&#160;&#160; <font color="#ff0000">Note&#58;</font> U2U CAML Builder is the best tool that we have. There are some occasional UI and interface issues, but for creating CAML and testing it against live SharePoint lists it gets the job done. And it’s FREE! </div>
    </li>
</ol>
<p class="MsoNormal"><span lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;11pt;" lang="EN-AU"></span></span>&#160;</p>
<p>&#160;</p>



