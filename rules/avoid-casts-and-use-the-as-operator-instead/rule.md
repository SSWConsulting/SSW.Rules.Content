---
type: rule
archivedreason: 
title: Do you avoid casts and use the "as operator" instead?
guid: b44fe59b-11ab-4ec9-bd57-15c8b93c679e
uri: avoid-casts-and-use-the-as-operator-instead
created: 2018-04-30T18:40:09.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-avoid-casts-and-use-the-as-operator-instead

---

Use casts only if:
a. You know 100% that you get that type back
b. You want to perform a user-defined conversion 

<!--endintro-->



```
private void AMControlMouseLeftButtonUp(object sender, MouseButtonEventArgs e)
{
 var auc = (AMUserControl)sender; 
   
 var aucSessionId = auc.myUserControl.Tag;
 // snip snip snip
}
```




::: bad
Bad example

:::



```
private void AMControlMouseLeftButtonUp(object sender, MouseButtonEventArgs e)
{
 var auc = sender as AMUserControl; 
   
 if (auc != null)
 {
 var aucSessionId = auc.myUserControl.Tag;
 // snip snip snip
 } 
   
}
```




::: good
Good example

:::
  More info here: [http://blog.gfader.com/2010/08/avoid-type-casts-use-operator-and-check.html](http&#58;//blog.gfader.com/2010/08/avoid-type-casts-use-operator-and-check.html)
