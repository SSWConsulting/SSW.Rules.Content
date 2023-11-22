---
type: rule
archivedreason: 
title: ASP.NET vs SharePoint development - do you know what you get for free out of the box?
guid: 0d0d049e-49fe-458a-95f6-814b1bf1961c
uri: asp-net-vs-sharepoint-development-do-you-know-what-you-get-for-free-out-of-the-box
created: 2009-06-16T01:23:22.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
- title: Jay Lin
  url: https://ssw.com.au/people/jay-lin
related: []
redirects: []

---

SharePoint as a platform on top of ASP.NET gives you many components that you don’t get from ASP.NET out of the box:
<!--endintro-->


* WYSIWYG editing (IE only, no FireFox)

    SharePoint’s rich text editor works really well with IE out of the box, works with SharePoint image libraries, and supports many features and even allows site style configurations to define and restrict styles that can be applied in the site. Unfortunately, it is not a cross browser compliant WYSIWYG editor.

    In ASP.NET there are many 3rd party options here – but you won’t get the integrated support that SharePoint’s editor has, without doing further customization.
* Content Version Control (with Publish and Approval workflow)

    SharePoint gives your end users content version control – they can update their pages and check-in to share it with the team, or publish it for everyone to see. Workflows can be attached to notify the necessary internal reviews.

    SharePoint also tracks changes across versions (except in web part zones), and allows users to compare between different versions.

    In ASP.NET this is not available – you will need to do significant work to achieve this behaviour, or build on top of another ASP.NET platform.
* Permission Control (just assign to Groups)

    SharePoint allows items to be assigned to permission groups and works very well with Active Directory (or other membership providers) directly.

    In ASP.NET site permissions can be specified via web.config but the UI to configure parts of the site is limited.
* Creating a subsite (simple and then appear in menus, breadcrumbs…)

    End users can create subsites in SharePoint that automatically appears in menu navigation and has all the correct breadcrumbs wired up. Subsites forms the necessary site navigation within SharePoint.

    In ASP.NET end users cannot create subsites – developers has to do this.
* Spell check

    SharePoint editor web parts come with spell check abilities.

    ASP.NET does not have equivalent – though many browsers now support a client-side spellchecking facility, and some 3rd party rich text editors also have spell check.
* Search (filtered by your permissions) – google only works for anonymous

    SharePoint comes with a highly configurable enterprise search facility. The search result is filtered based on the current user so SharePoint will never show results that you aren’t supposed to see.

    SharePoint search can index Office documents as well as other popular document formats like PDF.

    Search engines like Google performs well for public content, but there is no way for the search crawler to index inside your organization. SharePoint uses its own internal crawler to keep your site’s content up to date in the search results.


In ASP.NET - this is often overlooked – most ASP.NET search facilities are limited to only specific kind of data: e.g. *search clients with the ID of SSW*
