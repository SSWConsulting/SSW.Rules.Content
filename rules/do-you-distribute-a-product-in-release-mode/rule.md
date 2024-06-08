---
type: rule
title: Do you distribute a product in Release mode?
uri: do-you-distribute-a-product-in-release-mode
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Ryan Tee
    url: https://ssw.com.au/people/ryan-tee
    noimage: true
related: []
redirects: []
created: 2009-05-05T06:48:04.000Z
archivedreason: null
guid: fe6201ba-9b95-420c-80f5-9e02b14d12b2
---
We like to have debugging information in our application, so that we can view the line number information in the stack trace. However, we won't release our product in Debug mode, for example if we use "#if Debug" statement in our code we don't want them to be compiled in the release version. 

If we want line numbers, we simply need  **Debugging Information** . You can change an option in the project settings so these will be generated in when using Release build.   

<!--endintro-->

```csharp
#if DEBUG MessageBox.Show("Application started"); #endif
```

**Figure: Code that should only run in Debug mode, we certainly don't want this in the release version.** 

![Figure: Set "Generate Debugging Information" to True on the project properties page (VS 2003)](DebugConfiguration.gif)

![Figure: Set "Debug Info" to "pdb-only" on the Advanced Build Settings page (VS 2005)](VS2005AdvancedBuildSettings.gif)
