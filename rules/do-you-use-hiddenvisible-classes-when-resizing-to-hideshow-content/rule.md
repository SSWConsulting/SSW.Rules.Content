---
type: rule
title: Do you use hidden/visible classes when resizing to hide/show content?
uri: do-you-use-hiddenvisible-classes-when-resizing-to-hideshow-content
created: 2014-06-18T05:16:40.0000000Z
authors:
- id: 37
  title: Ben Cull

---



<span class='intro'> <p>When designing responsive websites, it's important to consider what content is appropriate for each screen size. Desktops might have large navigation areas and extra content in a sidebar, whereas the phone might focus on other content.</p> </span>

<p>​</p><p>By default, bootstrap will wrap the columns and make them full width on phones. If you want to hide content rather than let it wrap you can use the following classes&#58;</p><p>&#160;</p><p>.hidden-xs</p><p>.hidden-sm</p><p>.hidden-md</p><p>.hidden-lg</p><p>&#160;</p><p>As well as being able to hide content per view, you can also selectively show it. This is helpful to add an extra sidebar for very large screens.</p><p>&#160;</p><p>.visible-xs</p><p>​.visible-sm</p><p>.visible-md</p><p>.visible-lg</p><p><br></p><p><img src="/WebSites/RulesToBetterUIBootstrap/PublishingImages/Pages/Do-you-use-hidden-xs-when-resizing-to-hide-content/RulesBootstrap%20-%20hidden.png" alt="RulesBootstrap - hidden.png" style="margin&#58;5px;width&#58;650px;" /><br></p><dd class="ssw15-rteElement-FigureBad">​Bad Example&#58; The mobile view on the right has a large unneccessary title.</dd><p class="ssw15-rteElement-P">​​​​<br></p><p class="ssw15-rteElement-P">Remove the title by adding the .hidden-xs class.</p><p class="ssw15-rteElement-CodeArea">&#160; &#160; &lt;h1 class=&quot;hidden-xs&quot;&gt;ASP.NET&lt;/h1&gt;​<br></p><p class="ssw15-rteElement-P"><br></p><p class="ssw15-rteElement-P"><img src="/WebSites/RulesToBetterUIBootstrap/PublishingImages/Pages/Do-you-use-hidden-xs-when-resizing-to-hide-content/RulesBootstrap%20-%20hidden2.png" alt="RulesBootstrap - hidden2.png" style="margin&#58;5px;width&#58;650px;" /><br></p><dd class="ssw15-rteElement-FigureGood">Good Example&#58; The mobile view is now leaner and cleaner thanks to our .hidden-xs class.</dd><p class="ssw15-rteElement-P">​<br></p>


