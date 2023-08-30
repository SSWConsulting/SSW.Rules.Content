---
type: rule
title: Do you follow naming conventions for your Boolean Property?
uri: follow-naming-conventions-for-your-boolean-property
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-follow-naming-conventions-for-your-boolean-property
created: 2018-04-25T21:35:27.000Z
archivedreason: null
guid: f93e0077-6398-425b-8613-b628e9d69707
---
Boolean Properties must be prefixed by a verb. Verbs like "Supports", "Allow", "Accept", "Use" should be valid. Also properties like "Visible", "Available" should be accepted (maybe not). [Here is how we name Boolean columns in SQL databases.](https://www.ssw.com.au/ssw/Standards/Rules/RulestoBetterSQLServerdatabases.aspx#BitFields)

<!--endintro-->

```csharp
public bool Enable { get; set; }
public bool Invoice { get; set; }
```

::: bad
Bad Example 

:::

```csharp
public bool Enabled { get; set; }
public bool IsInvoiceSent { get; set; }
```

::: good
Good Example - Naming Convention for Boolean Property

:::

We have a program called [SSW Code Auditor](https://www.ssw.com.au/ssw/CodeAuditor/) to check for this rule.