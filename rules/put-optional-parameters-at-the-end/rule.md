---
type: rule
title: Do you put optional parameters at the end?
uri: put-optional-parameters-at-the-end
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-put-optional-parameters-at-the-end
created: 2018-04-26T23:44:44.000Z
archivedreason: null
guid: 319aec53-73ec-4049-8d58-8d0bd84fc246
---
Optional parameters should be placed at the end of the method signature as optional ones tend to be less important. You should put the important parameters first.

<!--endintro-->

```csharp
public void SaveUserProfile(
  [Optional] string username,
  [Optional] string password,
  string firstName,
  string lastName, 
  [Optional] DateTime? birthDate
) {}
```

::: bad
Figure: Bad example - Username and Password are optional and first - they are less important than firstName and lastName and should be put at the end
:::

```csharp
public void SaveUserProfile(
  string firstName,
  string lastName, 
  [Optional] string username,
  [Optional] string password,
  [Optional] DateTime? birthDate
) {}
```

::: good
Figure: Good example - All the optional parameters are the end
:::

**Note:** When using optional parameters, please be sure to use [named para meters](/when-to-use-named-parameters)
