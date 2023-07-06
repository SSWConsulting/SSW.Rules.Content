---
type: rule
archivedreason: 
title: Do you know where to add style files for deployment?
guid: fa61b04c-a32c-4b7d-a8e3-f260d158af0f
uri: style-files-for-deployment-in-sharepoint
created: 2009-04-20T00:13:00.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
related: []
redirects: 
- do-you-know-where-to-add-design-files-for-deployment

---

When a designer (or a developer) adds style (CSS) files to SharePoint - care must be taken regarding where the files are placed:

* Some places are are not suitable because they are not good for deployment
* Other places may have permission issues - designers can't access them
* Some files are part of the site definition and should not be customized


<!--endintro-->

So the rules are:

1. Never modify out of the box SharePoint files in /Style Library/ - those files are part of the site definition, if you customize them they are hard to deploy
2. Start with a clean, minimal masterpage
3. Create and reference your own CSS files and put them under /Style Library/CSS/&lt;client&gt;/
4. You may want to further divide your CSS paths according to the areas of the site that your CSS is designed for:

    E.g. /Style Library/CSS/SSW/Clients/layout.css
5. Designers can modify the XSL file as well!

    put them under /Style Library/XSL Style Sheets/&lt;client&gt;/
