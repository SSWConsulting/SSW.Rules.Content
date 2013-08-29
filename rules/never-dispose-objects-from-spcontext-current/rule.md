---
type: rule
archivedreason: 
title: Never Dispose Objects from SPContext.Current
guid: 4117b350-d8e9-47d3-95a0-f993cd7af6a2
uri: never-dispose-objects-from-spcontext-current
created: 2013-08-29T00:36:26.0000000Z
authors:
- title: William Yin
  url: https://ssw.com.au/people/william-yin
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
related: []
redirects: []

---


<div>​Disposing objects in SharePoint is important, but never do it with objects from SPContext.Current. SharePoint will manage disposing these objects itself.​</div><div><br></div><p class="ssw15-rteElement-CodeArea"><strong>using </strong>(SPWeb web = <strong>SPContext.Current.Site.RootWeb</strong>)<br>&#123;<br>&#160;//do something here<br>&#125;</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Using statement is trying to dispose current site object - it will cause exception</dd><div><br></div><div>Just simplely use &quot;Current&quot; object directly.</div><p class="ssw15-rteElement-CodeArea">SPWeb web =&#160;<strong>SPContext.Current.Site.R​ootWeb</strong>​;<br>//do something here</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Use Current objects directly - don't need to dispose them</dd>
<br><excerpt class='endintro'></excerpt><br>



