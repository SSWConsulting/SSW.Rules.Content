---
type: rule
title: Never Dispose Objects from SPContext.Current
uri: never-dispose-objects-from-spcontextcurrent
created: 2013-08-29T00:36:26.0000000Z
authors:
- id: 9
  title: William Yin
- id: 34
  title: Brendan Richards

---



<span class='intro'> <div>​Althought disposing&#160;objects in SharePoint is important, but never do it with &quot;Current&quot; objects, as you are not allowed to do it.</div><div><br></div><p class="ssw15-rteElement-CodeArea">using (SPWeb web = SPContext.Current.Site.RootWeb)<br>&#123;<br>&#160;//do something here<br>&#125;</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Using statement is trying to dispose current site object - it will cause exception</dd><div><br></div><div>Just simplely use &quot;Current&quot; object directly.</div><p class="ssw15-rteElement-CodeArea">SPWeb web =&#160;SPContext.Current.Site.R​ootWeb​;<br>//do something here</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Use Current objects directly - don't need to dispose them</dd> </span>




