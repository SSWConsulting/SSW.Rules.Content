---
type: rule
title: Do you know when to use SmartPart or WebPart?
uri: do-you-know-when-to-use-smartpart-or-webpart
created: 2009-04-09T01:09:00.0000000Z
authors:
- id: 8
  title: John Liu
- id: 18
  title: Jay Lin

---



<span class='intro'> SmartPart is basically a simple but genius idea - it is a simple&#160;web part that can host a user control (ascx) inside it via the Page.LoadControl method. That way, all you have to do as a SharePoint developer is to write the ascx control, and you can do it with the Visual Studio&#160;designer&#160;to arrange the&#160;user control via drag and drop, and then when you want the web part&#160;on a SharePoint page, you load the generic SmartPart, and tell it to load the ascx that you want. <br>
<br>
However, there are some PRO's and CON's when you use a SmartPart&#58; 
 </span>


  <p>PRO</p>
<ol>
    <li>Being able to rapidly create the control's layout and then focus on the code behind - in familiar ASP.NET user control style. </li>
</ol>
<p>CON</p>
<ol>
    <li>Many users switch to full trust for their User Controls and disregard SharePoint security this is very easy to set up, but very bad practice.&#160; The user control dll should be deployed to the GAC. </li>
    <li>Performance is not as good as a&#160;web part&#160;because a SmartPart is &quot;host&quot; by a page. </li>
    <li>Hard to deploy - this is a major problem for SSW because we use solution package to deploy web parts.&#160; The ascx can be deployed manually to wss\VirtualDirectories\, or it can be deployed to the 12 hive via _controlTemplates/ - and then the user control referenced&#160;via ~/_layouts/controlTemplates/ but this is not an intended feature of SharePoint deployment. </li>
    <li>Hard to debug - if the ascx is written with src codebehind, then that file is compiled on demand by ASP.NET you can't debug it easily.&#160; See <font style="background-color&#58;#ff0000;">xxx (link)</font> on how to debug SharePoint. </li>
</ol>
<p>&#160;</p>
<p>Our recommendation&#58;</p>
<ol>
    <li>Understand the difference between SmartParts and Web Parts - don't use SmartParts just because it's &quot;easy&quot; - there are many issues that will come back and hurt the developer. </li>
    <li>If your control does not work with SharePoint directly, or has a lot of layout elements it is OK to use SmartParts </li>
    <li>Otherwise, write your own Web Part. </li>
</ol>



