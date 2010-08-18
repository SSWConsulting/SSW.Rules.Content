---
type: rule
title: Do you use SharePoint designer well?
uri: do-you-use-sharepoint-designer-well
created: 2009-04-21T03:07:49.0000000Z
authors:
- id: 8
  title: John Liu
- id: 1
  title: Adam Cogan

---



<span class='intro'> 
  <p>We love SharePoint designer and use it everyday.&#160; </p>
<p>But there are things that it doesn't do naturally, or it does really badly.&#160; Here are some tips on using SharePoint designer well.</p>
<ul>
    <li>Don't use inline CSS - this goes for any website. </li>
    <li>Always put &lt;div class=&quot;...&quot;&gt; wrappers around SharePoint controls. This allows us to define styles for SharePoint controls. It is possible to use CssClass like ASP.NET, but then we lose control to SharePoint regarding how that control will be rendered.&#160; Also, some SharePoint controls will eat up your CssClass and not render anything. </li>
    <li>Naming convention for control id! Don't get lazy. </li>
    <li>Turn off Auto indent.&#160; Otherwise SharePoint designer will keep modifying your file whenever it saves the HTML - this will make you very upset.</li>
</ul>
 </span>


  <p>&#160;</p>
<img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" alt="Uncheck Auto indent" src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/SPIndent.gif" />



