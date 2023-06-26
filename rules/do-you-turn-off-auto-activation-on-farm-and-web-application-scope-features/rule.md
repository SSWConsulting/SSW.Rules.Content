---
type: rule
title: Do you turn off auto activation on farm and web application scope features?
uri: do-you-turn-off-auto-activation-on-farm-and-web-application-scope-features
authors:
  - title: John Liu
    url: https://ssw.com.au/people/john-liu
related: []
redirects: []
created: 2010-04-21T12:58:32.000Z
archivedreason: null
guid: 441f7199-d068-433d-8396-ab122fc8c8e5
---
Each SharePoint packages contains features that can be targetted at various scopes. You need to pay special attention when you are targetting the Web Application scope.

The feature XML looks like this.
```xml
<Feature 
    Id="{GUID}"
    Title="WebApplicationConfiguration" 
    Scope="WebApplication" 
    Version="1.0.0.0" 
    Hidden="FALSE" 
    DefaultResourceFile="core" 
    xmlns="http://schemas.microsoft.com/sharepoint/" 
>
  <ElementManifests />
</Feature>
```

But there is a problem...

<!--endintro-->

The problem with this web application feature is that it will activate by default on all new Web Applications created on that farm, regardless of what the web application or root site template is.

The best practice is to make sure you use the additional attribute `ActivateOnDefault` and set it to False. Then SharePoint administrators can choose to activate the feature after a new web application is created.

```xml
<Feature 
    Id="{GUID}" 
    Title="WebApplicationConfiguration" 
    Scope="WebApplication" 
    Version="1.0.0.0" 
    Hidden="FALSE" 
    DefaultResourceFile="core" 
    xmlns="http://schemas.microsoft.com/sharepoint/"
    ActivateOnDefault="False"
>
  <ElementManifests />
</Feature>
```
