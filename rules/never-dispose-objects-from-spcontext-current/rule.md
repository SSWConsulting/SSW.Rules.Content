---
type: rule
title: Never Dispose Objects from SPContext.Current
uri: never-dispose-objects-from-spcontext-current
authors:
  - title: William Yin
    url: https://ssw.com.au/people/william-yin
  - title: Brendan Richards
    url: https://ssw.com.au/people/brendan-richards
related: []
redirects: []
created: 2013-08-29T00:36:26.000Z
archivedreason: null
guid: 4117b350-d8e9-47d3-95a0-f993cd7af6a2
---
Disposing objects in SharePoint is important, but never do it with objects from `SPContext.Current`. SharePoint will manage disposing these objects itself.

```csharp
using (SPWeb web =  SPContext.Current.Site.RootWeb)
{
    //do something here
}
```

::: bad
Figure: Using statement is trying to dispose current site object - it will cause exception  
:::

Just simply use "Current" object directly.

```csharp
SPWeb web =  SPContext.Current.Site.RootWeb;
//do something here
```

::: good
Figure: Use Current objects directly - don't need to dispose them  
:::

<!--endintro-->
