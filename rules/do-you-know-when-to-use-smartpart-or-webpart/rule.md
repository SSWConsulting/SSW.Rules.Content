---
type: rule
archivedreason: 
title: Do you know when to use SmartPart or WebPart?
guid: 2f0015c3-d4b3-4ac4-a9c5-b76827e995cb
uri: do-you-know-when-to-use-smartpart-or-webpart
created: 2009-04-09T01:09:00.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
- title: Jay Lin
  url: https://ssw.com.au/people/jay-lin
related: []
redirects: []

---

SmartPart is basically a simple but genius idea - it is a simple web part that can host a user control (ascx) inside it via the Page.LoadControl method. That way, all you have to do as a SharePoint developer is to write the ascx control, and you can do it with the Visual Studio designer to arrange the user control via drag and drop, and then when you want the web part on a SharePoint page, you load the generic SmartPart, and tell it to load the ascx that you want. 

 However, there are some PRO's and CON's when you use a SmartPart:   
<!--endintro-->

PRO

1. Being able to rapidly create the control's layout and then focus on the code behind - in familiar ASP.NET user control style.


CON

1. Many users switch to full trust for their User Controls and disregard SharePoint security this is very easy to set up, but very bad practice.  The user control dll should be deployed to the GAC.
2. Performance is not as good as a web part because a SmartPart is "host" by a page.
3. Hard to deploy - this is a major problem for SSW because we use solution package to deploy web parts.  The ascx can be deployed manually to wss\VirtualDirectories\, or it can be deployed to the 12 hive via \_controlTemplates/ - and then the user control referenced via ~/\_layouts/controlTemplates/ but this is not an intended feature of SharePoint deployment.
4. Hard to debug - if the ascx is written with src codebehind, then that file is compiled on demand by ASP.NET you can't debug it easily.  See <font style="background-color&#58;rgb(255, 0, 0);">xxx (link)</font> on how to debug SharePoint.




Our recommendation:

1. Understand the difference between SmartParts and Web Parts - don't use SmartParts just because it's "easy" - there are many issues that will come back and hurt the developer.
2. If your control does not work with SharePoint directly, or has a lot of layout elements it is OK to use SmartParts
3. Otherwise, write your own Web Part.
