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

We love SharePoint designer and use it everyday.

But there are things that it doesn't do naturally, or it does really badly.  Here are some tips on using SharePoint designer well.

* Don't use inline CSS - this goes for any website.
* Always put &lt;div class="..."&gt; wrappers around SharePoint controls. This allows us to define styles for SharePoint controls. It is possible to use CssClass like ASP.NET, but then we lose control to SharePoint regarding how that control will be rendered.  Also, some SharePoint controls will eat up your CssClass and not render anything.
* Naming convention for control id! Don't get lazy.
* Turn off Auto indent.  Otherwise SharePoint designer will keep modifying your file whenever it saves the HTML - this will make you very upset.


<!--endintro-->


![Uncheck Auto indent](SPIndent.gif)
