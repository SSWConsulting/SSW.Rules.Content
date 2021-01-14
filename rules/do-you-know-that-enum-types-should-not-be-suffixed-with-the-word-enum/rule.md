---
type: rule
archivedreason: 
title: Do you know that Enum types should not be suffixed with the word "Enum"?
guid: d9faf190-a42e-4ab8-b318-eb8b0178dee8
uri: do-you-know-that-enum-types-should-not-be-suffixed-with-the-word-enum
created: 2018-04-25T23:53:39.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- enum-types-should-not-be-suffixed-with-the-word-enum

---

This is against the .NET Object Naming Conventions and inconsistent with the framework.

<!--endintro-->



```
Public Enum ProjectLanguageEnum CSharp VisualBasic End Enum
```



::: bad
Bad - Enum type is suffixed with the word "Enum" 

:::



```
Public Enum ProjectLanguage CSharp VisualBasic End Enum
```



::: good
Good - Enum type is not suffixed with the word "Enum" 

:::

We have a program called [SSW Code Auditor](https&#58;//www.ssw.com.au/ssw/CodeAuditor/) to check for this rule.
