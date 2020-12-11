---
type: rule
archivedreason: 
title: Do you suffix unit test classes with "Tests"?
guid: 7e401815-0507-40bf-a045-ae46ca1db46a
uri: do-you-suffix-unit-test-classes-with-tests
created: 2018-04-25T23:24:57.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

Unit test classes should be suffixed with the word "Tests" for better coding readability.

<!--endintro-->

[TestFixture] public class SqlValidatorReportTest { }


::: bad
Bad - Unit test class is not suffixed with "Tests"

:::


[TestFixture] public class HtmlDocumentTests { }


::: good
Good - Unit test class is suffixed with "Tests"

:::


We have a program called [SSW Code Auditor](https&#58;//www.ssw.com.au/ssw/CodeAuditor/) to check for this rule.
