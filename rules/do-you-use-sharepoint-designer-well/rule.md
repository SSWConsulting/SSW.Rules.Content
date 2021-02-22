---
type: rule
archivedreason: 
title: Do you use SharePoint designer well?
guid: 576544a8-5005-4796-b194-0834c854f87f
uri: do-you-use-sharepoint-designer-well
created: 2009-04-21T03:07:49.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---



  <p>We love SharePoint designer and use it everyday.  </p>
<p>But there are things that it doesn't do naturally, or it does really badly.  Here are some tips on using SharePoint designer well.</p>
<ul>
    <li>Don't use inline CSS - this goes for any website. </li>
    <li>Always put &lt;div class="..."&gt; wrappers around SharePoint controls. This allows us to define styles for SharePoint controls. It is possible to use CssClass like ASP.NET, but then we lose control to SharePoint regarding how that control will be rendered.  Also, some SharePoint controls will eat up your CssClass and not render anything. </li>
    <li>Naming convention for control id! Don't get lazy. </li>
    <li>Turn off Auto indent.  Otherwise SharePoint designer will keep modifying your file whenever it saves the HTML - this will make you very upset.</li>
</ul>

<br><excerpt class='endintro'></excerpt><br>

  <p> </p>
<img style="border-bottom:0px solid;border-left:0px solid;border-top:0px solid;border-right:0px solid;" border="0" alt="Uncheck Auto indent" src="SPIndent.gif" />



