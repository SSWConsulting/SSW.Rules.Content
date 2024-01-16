---
type: rule
archivedreason: already covered by rule [https://www.ssw.com.au/rules/do-you-have-a-consistent-net-solution-structure](/rules/do-you-have-a-consistent-net-solution-structure)
title: Do you name your assemblies consistently (<CompanyName>.<ComponentName>)?
guid: 30f404cf-bad3-4fee-8afd-c2e6a93635ca
uri: do-you-name-your-assemblies-consistently-companyname-componentname
created: 2009-04-28T02:16:10.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
  noimage: true
related: []
redirects:
- do-you-name-your-assemblies-consistently-(-companyname-componentname-)
- do-you-name-your-assemblies-consistently-(companyname-componentname)

---

Assembly names should reflect the the functionality that it provides. For example,  
<!--endintro-->

```cs
System.IO
```

contains all the classes that deal with inputs and outputs. As a general rule of thumb your assemblies should be named as follows:

&lt;CompanyName&gt;.&lt;ComponentName&gt; (e.g. SSW.Framework)

This allows a developer to know who developed the assembly and give the developer a general idea of what the assembly can be used for.
