---
type: rule
title: Do you create a private repository for reusable internal code?
uri: do-you-create-a-private-repository-for-reusable-internal-code
created: 2014-11-27T18:57:56.0000000Z
authors:
- id: 34
  title: Brendan Richards

---



<span class='intro'> <p>Nuget is great for managing publicly available packages, but it’s also surprisingly easy to create and publish your own packages to your own nuget server for internal code reuse across multiple solutions.</p> </span>

<dl class="image"><dt> 
      <img src="/PublishingImages/private-nuget-1.png" alt="private-nuget-1.png" style="width&#58;600px;" />&#160;</dt><dd>Figure&#58; You can create your own nuget server by simply creating a new asp.net web project and adding the Nuget.Server package</dd></dl><dl class="image"><dt> 
      <img src="/PublishingImages/private-nuget-2.png" alt="private-nuget-2.png" style="width&#58;600px;" />
   </dt><dd>Figure&#58; Add your new server as a package source under Tools | Options | Nuget Package Manager | Package Sources</dd></dl>


