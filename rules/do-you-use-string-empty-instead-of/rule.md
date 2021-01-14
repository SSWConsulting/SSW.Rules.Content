---
type: rule
archivedreason: 
title: Do you use String.Empty instead of ""?
guid: 939c25b3-d693-42f4-bdbf-d99c1f246633
uri: do-you-use-string-empty-instead-of
created: 2018-04-25T21:51:21.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- use-string-empty-instead-of-quotes

---

Considering the memory management of .NET Framework String.Empty will get higher performance then using "".

<!--endintro-->



```
public string myString 
   
{
 get
 {
 return ;
 } 
   
}
```



::: bad
Figure: Bad code. Low performance

:::



```
public string myString
{ 
   
 get 
   
 { 
   
 return string.Empty; 
   
 } 
   
}
```



::: good
Figure: Good code. Higher performance

:::

We have a program called [SSW Code Auditor](https&#58;//www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#TimeSpan) to check for this rule.
