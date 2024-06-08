---
type: rule
title: Do you know the right version and config for nUnit?
uri: the-right-version-and-config-for-nunit
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-know-the-right-version-and-config-for-nunit
created: 2020-03-12T23:01:15.000Z
archivedreason: This applies to .Net Framework 1 and 2
guid: 3c39ccb8-123f-461c-9023-e08ca4e27e29
---

There are multiple versions of NUnit and .NET Framework, the following will explain how to use them correctly.

<!--endintro-->

* if your application was built with .NET Framework 1.1, NUnit 2.2.0 which was built with .NET Framework 1.1 is the best choice if you compact it into the installation package, You then don't need any additional config - it will auto use .NET Framework 1.1 to reflect your assembly;
* If there is only .NET Framework 2.0 on the client-side, how to make it works?
Just add the  **yellow**  into nunit-gui.exe.config (it is under the same folder as nunit-gui.exe), which will tell NUnit to reflect your assembly with .NET Framework 2.0;


```xml
...
<startup>
<supportedRuntime version="v2.0.50727" />
<supportedRuntime version="v1.1.4322" />
<supportedRuntime version="v1.0.3705" />
<requiredRuntime version="v1.0.3705" />
</startup>
...
```


* if your application was built with .NET Framework 2.0, then you may get choices:
* NUnit 2.2.7 or higher (built with .NET framework 2.0) (recommended)
Then you don't need any extra configuration for NUnit, just follow the default;
        * NUnit 2.2.0 or lower (built with .NET Framework 1.1)
Then you need to add the yellow statement (see above in this section);
