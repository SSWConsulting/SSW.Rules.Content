---
type: rule
archivedreason: 
title: Do you turn off auto activation on farm and web application scope features?
guid: 441f7199-d068-433d-8396-ab122fc8c8e5
uri: do-you-turn-off-auto-activation-on-farm-and-web-application-scope-features
created: 2010-04-21T12:58:32.0000000Z
authors:
- id: 8
  title: John Liu
related: []

---

Each SharePoint packages contains features that can be targetted at various scopes.  

 You need to pay special attention when you are targetting the Web Application scope.

 The feature XML looks like this.

<font class="ms-rteCustom-CodeArea"><p><span style="font-family&#58;'courier new';color&#58;blue;font-size&#58;10pt;">&lt;</span><span style="font-family&#58;'courier new';color&#58;#a31515;font-size&#58;10pt;">Feature</span> <span style="font-family&#58;'courier new';color&#58;red;font-size&#58;10pt;">Id</span><span style="font-family&#58;'courier new';color&#58;blue;font-size&#58;10pt;">=</span><span style="font-family&#58;'courier new';font-size&#58;10pt;">&quot;&#123;<font color="#0000ff">GUID&#125;</font>&quot; <span style="color&#58;red;">Title</span><span style="color&#58;blue;">=</span>&quot;<span style="color&#58;blue;">WebApplicationConfiguration</span>&quot; <span style="color&#58;red;">Scope</span><span style="color&#58;blue;">=</span>&quot;<span style="color&#58;blue;">WebApplication</span>&quot; <span style="color&#58;red;">Version</span><span style="color&#58;blue;">=</span>&quot;<span style="color&#58;blue;">1.0.0.0</span>&quot; <span style="color&#58;red;">Hidden</span><span style="color&#58;blue;">=</span>&quot;<span style="color&#58;blue;">FALSE</span>&quot; <span style="color&#58;red;">DefaultResourceFile</span><span style="color&#58;blue;">=</span>&quot;<span style="color&#58;blue;">core</span>&quot; <span style="color&#58;red;">xmlns</span><span style="color&#58;blue;">=</span>&quot;<span style="color&#58;blue;"><font color="#0000ff">http&#58;//schemas.microsoft.com/sharepoint/</font></span>&quot; <span style="color&#58;blue;">&gt;</span>
<p style="margin&#58;0cm 0cm 0pt;"><span style="font-family&#58;'courier new';color&#58;blue;font-size&#58;10pt;">&#160; &lt;</span><span style="font-family&#58;'courier new';color&#58;#a31515;font-size&#58;10pt;">ElementManifests</span><span style="font-family&#58;'courier new';color&#58;blue;font-size&#58;10pt;"> /&gt;</span></p>
<p style="margin&#58;0cm 0cm 0pt;"><span style="font-family&#58;'courier new';color&#58;blue;font-size&#58;10pt;">&lt;/</span><span style="font-family&#58;'courier new';color&#58;#a31515;font-size&#58;10pt;">Feature</span><span style="font-family&#58;'courier new';color&#58;blue;font-size&#58;10pt;">&gt;</span>&#160;&#160;</p>
</span></p>
<p>&#160;</p></font>



But there is a problem...

<!--endintro-->
 The problem with this web application feature is that it will activate by default on All new Web Applications created on that farm, regardless of what the web application or root site template is.

 The best practice is to make sure you use the additional attribute ActivateOnDefault and set it to False.  Then SharePoint administrators can choose to activate the feature after a new web application is created.
  <font class="ms-rteCustom-CodeArea"><span style="font-family&#58;'courier new';color&#58;blue;font-size&#58;10pt;">&lt;</span><span style="font-family&#58;'courier new';color&#58;#a31515;font-size&#58;10pt;">Feature</span> <span style="font-family&#58;'courier new';color&#58;red;font-size&#58;10pt;">Id</span><span style="font-family&#58;'courier new';color&#58;blue;font-size&#58;10pt;">=</span><span style="font-family&#58;'courier new';font-size&#58;10pt;">&quot;&#123;<font color="#0000ff">GUID&#125;</font>&quot; <span style="color&#58;red;">Title</span><span style="color&#58;blue;">=</span>&quot;<span style="color&#58;blue;">WebApplicationConfiguration</span>&quot; <span style="color&#58;red;">Scope</span><span style="color&#58;blue;">=</span>&quot;<span style="color&#58;blue;">WebApplication</span>&quot; <span style="color&#58;red;">Version</span><span style="color&#58;blue;">=</span>&quot;<span style="color&#58;blue;">1.0.0.0</span>&quot; <span style="color&#58;red;">Hidden</span><span style="color&#58;blue;">=</span>&quot;<span style="color&#58;blue;">FALSE</span>&quot; <span style="color&#58;red;">DefaultResourceFile</span><span style="color&#58;blue;">=</span>&quot;<span style="color&#58;blue;">core</span>&quot; <span style="color&#58;red;">xmlns</span><span style="color&#58;blue;">=</span>&quot;<span style="color&#58;blue;"><font color="#0000ff">http&#58;//schemas.microsoft.com/sharepoint/</font></span>&quot;&#160;<br>
<span style="font-family&#58;'courier new';font-size&#58;10pt;"><span style="background&#58;yellow;color&#58;red;">ActivateOnDefault</span><span style="background&#58;yellow;color&#58;blue;">=</span><span style="background&#58;yellow;">&quot;<span style="color&#58;blue;">False</span>&quot;</span></span><span style="color&#58;blue;">&gt;</span>
<p style="margin&#58;0cm 0cm 0pt;"><span style="font-family&#58;'courier new';color&#58;blue;font-size&#58;10pt;">&#160; &lt;</span><span style="font-family&#58;'courier new';color&#58;#a31515;font-size&#58;10pt;">ElementManifests</span><span style="font-family&#58;'courier new';color&#58;blue;font-size&#58;10pt;"> /&gt;</span></p>
<p style="margin&#58;0cm 0cm 0pt;"><span style="font-family&#58;'courier new';color&#58;blue;font-size&#58;10pt;">&lt;/</span><span style="font-family&#58;'courier new';color&#58;#a31515;font-size&#58;10pt;">Feature</span><span style="font-family&#58;'courier new';color&#58;blue;font-size&#58;10pt;">&gt;</span> </p>
</span></font>
