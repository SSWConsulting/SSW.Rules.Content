---
type: rule
title: Do you use String.Empty instead of ""?
uri: use-string-empty-instead-of-quotes
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-use-string-empty-instead-of
created: 2018-04-25T21:51:21.000Z
archivedreason: null
guid: 939c25b3-d693-42f4-bdbf-d99c1f246633
---
Since .NET 5+, the choice between using String.Empty and "" is a stylistic decision for the team. In .NET Framework, "" is less efficient than String.Empty from a memory perspective which can result in better performance due to faster garbage collection.

From the team that worked on performance in .NET: [String.Empty vs "" in modern .NET language](https://youtube.com/clip/UgkxIv8HnqTApTo6VOuEvBkAx3VnjY6RioCh)

<!--endintro-->

```csharp
public string myString 
   
{
 get
 {
 return ;
 } 
   
}
```

::: bad
Figure: Bad code if used in .NET Framework. Low performance

:::

```csharp
public string myString
{ 
   
 get 
   
 { 
   
 return string.Empty; 
   
 } 
   
}
```

::: good
Figure: Good code if used in .NET Framework. Higher performance

:::

We have a program called [SSW Code Auditor](https://www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#StringEmpty) to check for this rule.