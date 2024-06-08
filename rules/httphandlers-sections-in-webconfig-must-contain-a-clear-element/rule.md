---
type: rule
title: Do you know 'httpHandlers' or 'httpModules' sections in web.config must contain a 'remove' or 'clear' element?
uri: httphandlers-sections-in-webconfig-must-contain-a-clear-element
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Danijel Malik
    url: https://ssw.com.au/people/danijel-malik
related: []
redirects:
  - do-you-know-that-httphandlers-or-httpmodules-sections-in-web-config-must-contain-a-remove-or-a-clear-element
  - do-you-know-that-httphandlers-or-httpmodules-sections-in-web-config-must-contain-a-remove3f3f3f-or-a-clear-element
  - you-know-that-httphandlers-or-httpmodules-sections-in-web-config-must-contain-a-remove-or-a-clear-element
  - do-you-know-that-httphandlers-or-httpmodules-sections-in-web-config-must-contain-a-remove-or-clear-element
created: 2013-02-06T12:55:03.000Z
archivedreason: null
guid: 14359e59-b047-4e0b-aef5-f79ccd3eb373
---

If web.config contains a `<httpHandlers>` or `<httpModules>` section, that section must contain a `<remove... />` or a `<clear />` element.

This basically forces developers to explicitly enable inheritance in nested virtual directories. In 99% of cases this developers won't use inheritance on these two sections, however it causes issues when somebody wants to add a module or handler to the parent virtual directory.

<!--endintro-->

``` aspnet
<configuration>
   <system.web>
      <httpHandlers>
         <add verb="*" 
              path="*.New" 
              type="MyHandler.New,MyHandler"/>
         <add verb="GET,HEAD" 
              path="*.MyNewFileExtension" 
              type="MyHandler.MNFEHandler,MyHandler.dll"/>
     </httpHandlers>
   <system.web>
</configuration>
```

::: bad
Figure: Bad example
:::

``` aspnet
<configuration>
   <system.web>
      <httpHandlers>
         <clear/>
         <add verb="*" 
              path="*.New" 
              type="MyHandler.New,MyHandler"/>
         <add verb="GET,HEAD" 
              path="*.MyNewFileExtension" 
              type="MyHandler.MNFEHandler,MyHandler.dll"/>
     </httpHandlers>
   <system.web>
<configuration>
```

::: good
Figure: Good example
:::
