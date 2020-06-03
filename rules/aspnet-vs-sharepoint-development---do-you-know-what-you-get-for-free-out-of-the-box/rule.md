---
type: rule
title: ASP.NET vs SharePoint development - do you know what you get for free out of the box?
uri: aspnet-vs-sharepoint-development---do-you-know-what-you-get-for-free-out-of-the-box
created: 2009-06-16T01:23:22.0000000Z
authors:
- id: 8
  title: John Liu
- id: 18
  title: Jay Lin

---



<span class='intro'> 
  <span style="font-family&#58;'calibri', 'sans-serif';font-size&#58;11pt;" lang="EN-US">SharePoint as a platform on top of ASP.NET gives you many components that you don’t get from ASP.NET out of the box&#58;</span> 
 </span>


  <span style="font-family&#58;'calibri', 'sans-serif';font-size&#58;11pt;" lang="EN-US">
    <span style="font-family&#58;'calibri', 'sans-serif';font-size&#58;11pt;" lang="EN-US">
      <br>
<ul>
    <li>WYSIWYG editing (IE only, no FireFox)<br>
    SharePoint’s rich text editor works really well with IE out of the box, works with SharePoint image libraries, and supports many features and even allows site style configurations to define and restrict styles that can be applied in the site. Unfortunately, it is not a cross browser compliant WYSIWYG editor.<br>
    In ASP.NET there are many 3rd party options here – but you won’t get the integrated support that SharePoint’s editor has, without doing further customization. </li>
    <li>Content Version Control (with Publish and Approval workflow)<br>
    SharePoint gives your end users content version control – they can update their pages and check-in to share it with the team, or publish it for everyone to see. Workflows can be attached to notify the necessary internal reviews.<br>
    SharePoint also tracks changes across versions (except in web part zones), and allows users to compare between different versions.<br>
    In ASP.NET this is not available – you will need to do significant work to achieve this behaviour, or build on top of another ASP.NET platform. </li>
    <li>Permission Control (just assign to Groups)<br>
    SharePoint allows items to be assigned to permission groups and works very well with Active Directory (or other membership providers) directly.<br>
    In ASP.NET site permissions can be specified via web.config but the UI to configure parts of the site is limited. </li>
    <li>Creating a subsite (simple and then appear in menus, breadcrumbs…)<br>
    End users can create subsites in SharePoint that automatically appears in menu navigation and has all the correct breadcrumbs wired up. Subsites forms the necessary site navigation within SharePoint.<br>
    In ASP.NET end users can not create subsites – developers has to do this. </li>
    <li>Spell check<br>
    SharePoint editor web parts come with spell check abilities.<br>
    ASP.NET does not have equivalent – though many browsers now support a client-side spellchecking facility, and some 3rd party rich text editors also have spell check. </li>
    <li>Search (filtered by your permissions) – google only works for anonymous<br>
    SharePoint comes with a highly configurable enterprise search facility. The search result is filtered based on the current user so SharePoint will never show results that you aren’t supposed to see.<br>
    SharePoint search can index Office documents as well as other popular document formats like PDF.<br>
    Search engines like Google performs well for public content, but there is no way for the search crawler to index inside your organization. SharePoint uses its own internal crawler to keep your site’s content up to date in the search results. </li>
</ul>
In ASP.NET&#160;- this is often overlooked – most ASP.NET search facilities are limited to only specific kind of data&#58; e.g. <i>search clients with the ID of SSW</i></span> <br>
</span>



