---
type: rule
title: Do you suffix unit test classes with "Tests"?
uri: suffix-unit-test-classes-with-tests
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-suffix-unit-test-classes-with-tests
created: 2018-04-25T23:24:57.000Z
archivedreason: null
guid: 7e401815-0507-40bf-a045-ae46ca1db46a
---
Unit test classes should be suffixed with the word "Tests" for better coding readability.

<!--endintro-->

```csharp
[TestFixture] public class SqlValidatorReportTest { }
```

::: bad
Bad example - Unit test class is not suffixed with "Tests"

:::

```csharp
[TestFixture] public class HtmlDocumentTests { }
```

::: good
Good example - Unit test class is suffixed with "Tests"

:::

We have a program called [SSW Code Auditor](https://www.ssw.com.au/ssw/CodeAuditor/) to check for this rule.
