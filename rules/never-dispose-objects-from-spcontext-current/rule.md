---
type: rule
archivedreason: 
title: Never Dispose Objects from SPContext.Current
guid: 4117b350-d8e9-47d3-95a0-f993cd7af6a2
uri: never-dispose-objects-from-spcontext-current
created: 2013-08-29T00:36:26.0000000Z
authors:
- title: William Yin
  url: https://ssw.com.au/people/william-yin
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
related: []
redirects: []

---

Disposing objects in SharePoint is important, but never do it with objects from SPContext.Current. SharePoint will manage disposing these objects itself.






```
using (SPWeb web =  SPContext.Current.Site.RootWeb )
{
 //do something here
}
```




::: bad
Figure: Using statement is trying to dispose current site object - it will cause exception  
:::




Just simplely use "Current" object directly.



```
SPWeb web =  SPContext.Current.Site.RootWeb ;
//do something here
```




::: good
Figure: Use Current objects directly - don't need to dispose them  
:::

<!--endintro-->
