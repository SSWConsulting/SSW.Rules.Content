---
type: rule
title: Do you use one class per file?
uri: do-you-use-one-class-per-file
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Ryan Tee
    url: https://ssw.com.au/people/ryan-tee
    noimage: true
related: []
redirects: []
created: 2009-05-05T02:03:55.000Z
archivedreason: null
guid: e1c3a18a-a6fe-41af-a652-8facd4eda898
---

Each class definition should live in its own file. This ensures it's easy to locate class definitions outside the Visual Studio IDE (e.g. SourceSafe, Windows Explorer)

<!--endintro-->

The **only** exception should be classes that collectively forms one atomic unit of reuse should live in one file. 


```cs
class MyClass
{
    // ...
}

class MyClassAEventArgs
{
    // ...
}

class MyClassBEventArgs
{
    // ...
}

class MyClassAException
{
    // ...
}

class MyClassBException
{
    // ...
}
```
::: bad
Bad example - 1 project, 1 file
:::
