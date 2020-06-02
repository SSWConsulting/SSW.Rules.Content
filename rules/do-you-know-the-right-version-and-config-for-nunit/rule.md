---
uri: do-you-know-the-right-version-and-config-for-nunit
title: Do you know the right version and config for nUnit?
created: 2020-03-12 23:01:15
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> There are multiple versions of NUnit and .NET Framework, the following will explain how to use them correctly.<br> </span>

<ol><ul><li>if your application was built with .NET Framework 1.1, NUnit 2.2.0 which was built with .NET Framework 1.1 is the best choice if you compact it into the installation package, You then don't need any additional config - it will auto use .NET Framework 1.1 to reflect your assembly;<br></li><ul><li>If there is only .NET Framework 2.0 on the client-side​, how to make it works?<br>Just add the&#160;<strong>yellow</strong>&#160;into nunit-gui.exe.config (it is under the same folder as nunit-gui.exe), which will tell NUnit to reflect your assembly with .NET Framework 2.0;</li><p class="ssw15-rteElement-CodeArea">...<br>&lt;startup&gt;<br>&lt;supportedRuntime version=&quot;v2.0.50727&quot; /&gt;<br>&lt;supportedRuntime version=&quot;v1.1.4322&quot; /&gt;<br>&lt;supportedRuntime version=&quot;v1.0.3705&quot; /&gt;<br>&lt;requiredRuntime version=&quot;v1.0.3705&quot; /&gt;<br>&lt;/startup&gt;<br>...</p></ul><li>if your application was built with .NET Framework 2.0, then you may get choices&#58;</li><ul><li>NUnit 2.2.7 or higher (built with .NET framework 2.0) (recommended)<br>Then you don't need any extra configuration for NUnit, just follow the default;</li><li>NUnit 2.2.0 or lower (built with .NET Framework 1.1)<br>Then you need to add the yellow statement (see above in this section);<br></li></ul></ul></ol>


