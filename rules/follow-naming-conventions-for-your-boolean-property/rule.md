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

### Naming Boolean state Variables in Frontend code

When it comes to state management in frameworks like Angular or React, a similar principle applies, but with a focus on the continuity of the action.

For instance, if you are tracking a process or a loading state, the variable should reflect the ongoing nature of these actions. Instead of "isLoaded" or "isProcessed," which suggest a completed state, use names like "isLoading" or "isProcessing."

These names start as false, change to true while the process is ongoing, and revert to false once completed.

```js
const [isLoading, setIsLoading] = useState(false); // Initial state: not loading
```

::: greybox
Note: When an operation begins, isLoading is set to true, indicating the process is active. Upon completion, it's set back to false.
:::

This naming convention avoids confusion, such as a variable named isLoaded that would be true before the completion of a process and then false, which is counterintuitive and misleading.

We have a program called [SSW Code Auditor](https://www.ssw.com.au/ssw/CodeAuditor/) to check for this rule.
