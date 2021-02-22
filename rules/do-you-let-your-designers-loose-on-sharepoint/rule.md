---
type: rule
archivedreason: 
title: Do You Let Your Designers Loose on SharePoint?
guid: 575fef6d-902e-4a53-97b7-ea6eba9fe869
uri: do-you-let-your-designers-loose-on-sharepoint
created: 2009-04-19T23:50:00.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
related: []
redirects: []

---

Do you let your designers loose on your development SharePoint?

This is how we work:

* A designer would imagine and mockup the design using a graphics tool – such as Photoshop
* After the mockups are signed off, we let the designers work on the actual page
* Give them designer permissions to your development site and let them loose with SharePoint designer!


<!--endintro-->

There are many reasons why we believe that designers should work directly in SharePoint, with SharePoint designer:

* In all areas of .NET development, whether it be ASP.NET, WCF or SilverLight, designers are more and more involved with the actual project beyond mockups
* It helps them understand the limitations of SharePoint, which helps their future design to play to its strengths
* They are also better at CSS and DOM than a typical developer, as well as more cross-browser aware
* They are able to make a call on how close a designer can be bent when the implementation is hard or impossible - with developers who can't make that call, they may end up spending a lot of time failing to get the last 2 pixel perfect
* SharePoint designer is sufficiently powerful and offers the only experience currently available for building with SharePoint sites
* SharePoint has built-in check-in and check-out, as well as version controls, publishing and approval controls - all of which are excellent for team development


The major drawback for a designer is the complexity of a SharePoint masterpage:

&lt;insert picture&gt;

Figure: Bad - Nasty looking masterpage

Luckily, we always start with a clean-minimal masterpage, which gives our designers full freedom to implement their vision:

&lt;insert picture&gt;

Figure: Good - clean-minimal masterpage
