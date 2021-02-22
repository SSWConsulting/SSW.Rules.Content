---
type: rule
archivedreason: 
title: Do you use hidden/visible classes when resizing to hide/show content?
guid: 516a0486-d6d5-4ca2-9171-356115874c60
uri: do-you-use-hidden-visible-classes-when-resizing-to-hide-show-content
created: 2014-06-18T05:16:40.0000000Z
authors:
- title: Ben Cull
  url: https://ssw.com.au/people/ben-cull
related: []
redirects: []

---


<p>When designing responsive websites, it's important to consider what content is appropriate for each screen size. Desktops might have large navigation areas and extra content in a sidebar, whereas the phone might focus on other content.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>By default, bootstrap will wrap the columns and make them full width on phones. If you want to hide content rather than let it wrap you can use the following classes:</p><ul><li>.hidden-xs</li><li>.hidden-sm</li><li>.hidden-md</li><li>.hidden-lg</li></ul><p>As well as being able to hide content per view, you can also selectively show it. This is helpful to add an extra sidebar for very large screens.</p><ul><li>.visible-xs</li><li>​.visible-sm</li><li>.visible-md</li><li>.visible-lg</li></ul><dl class="badImage"><dt> 
      <img src="RulesBootstrap - hidden.png" alt="RulesBootstrap - hidden.png" style="margin:5px;width:550px;" /> 
   </dt><dd>​Bad Example: The mobile view on the right has a large unneccessary title.</dd></dl><p>Remove the title by adding the .hidden-xs class.</p><p class="ssw15-rteElement-CodeArea">    &lt;h1 class="hidden-xs"&gt;ASP.NET&lt;/h1&gt;​<br></p>
<dl class="goodImage">
   <dt> 
      <img src="RulesBootstrap - hidden2.png" alt="RulesBootstrap - hidden2.png" style="margin:5px;width:550px;" /> 
   </dt><dd>G​ood Example: The mobile view is now leaner and cleaner thanks to our .hidden-xs class.</dd></dl>​


