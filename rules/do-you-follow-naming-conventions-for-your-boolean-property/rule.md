---
type: rule
archivedreason: 
title: Do you follow naming conventions for your Boolean Property?
guid: f93e0077-6398-425b-8613-b628e9d69707
uri: do-you-follow-naming-conventions-for-your-boolean-property
created: 2018-04-25T21:35:27.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- follow-naming-conventions-for-your-boolean-property

---

Boolean Properties must be prefixed by a verb. Verbs like "Supports", "Allow", "Accept", "Use" should be valid. Also properties like "Visible", "Available" should be accepted (maybe not). [Here is how we name Boolean columns in SQL databases.](https&#58;//www.ssw.com.au/ssw/Standards/Rules/RulestoBetterSQLServerdatabases.aspx#BitFields)


<!--endintro-->



```
public bool Enable { get; set; }
public bool Invoice { get; set; }
```




::: bad
Bad Example 

:::



```
public bool Enabled { get; set; }
public bool IsInvoiceSent { get; set; }
```




::: good
Good Example - Naming Convention for Boolean Property

:::

We have a program called [SSW Code Auditor](https&#58;//www.ssw.com.au/ssw/CodeAuditor/) to check for this rule.
