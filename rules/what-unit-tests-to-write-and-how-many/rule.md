---
seoDescription: Do you know what unit tests to write and how many? Learn that 100% Unit Test Coverage is impractical, focus on quality over quantity, and prioritize writing tests for methods with high risk of unintended consequences.
type: rule
title: Do you know what unit tests to write and how many?
uri: what-unit-tests-to-write-and-how-many
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-know-what-unit-tests-to-write-and-how-many
created: 2020-03-11T17:34:49.000Z
archivedreason: null
guid: 2024f813-eb57-4890-a789-2c46d9f7f150
---

Some people aim for 100% Unit Test Coverage but, in the real world, this is 100% impractical. Actually, it seems that the most popular metric in TDD (Test-Driven Development) is to aim for 100% of the methods to be unit tested. However, in practice, this goal is rarely achieved.

::: greybox
**Tip:** Don't focus on meeting a unit test coverage target. Focus on quality over quantity, writing tests that genuinely help to mitigate the risk of code changes.
:::

Unit tests are created to validate and assert that public and protected methods of a class meet an expected outcome based on varying input. This includes both good and bad data being tested, to ensure the method behaves as expected and returns the correct result or traps any errors.

<!--endintro-->

:::info
Remember that unit tests are designed to be small in scope and help mitigate the risk of code changes. When deciding which unit tests to write, think about the risks you're mitigating by writing them. In other words, don't write unit tests for the sake of it, but write them where it makes sense and where they actually help to reduce the risk of unintended consequences of code changes.
:::

✅ Unit tests should be written for:

- Fragile code
  e.g. regular expressions
- When errors can be difficult to spot
  e.g. in rounding, arithmetic and other calculations

:::greybox
**Example:** In a calculation, you would not only test correct input (such as 12/3 = 4) and bad output (such as 12/4 &lt;&gt; 4), but also that 12/0 does not crash the application (instead a DivideByZero exception is expected and should be handled gracefully).
:::
:::greybox
**Example:** Methods returning a Boolean value need to have test cases to cover both true and false.
:::

❌ Unit tests should _not_ be written for:

- **Dependencies**
  e.g. database schemas, datasets, Web Services, DLLs runtime errors (JIT)
- **Performance**
  e.g. slow forms, time-critical applications
- **Generated code**
  Code that has been generated from Code Generators, e.g. SQL database functions (Customer.Select, Customer.Update, Customer.Insert, Customer.Delete)
- **Private methods**
  Private methods should be tested by the unit tests on the public and protected methods calling them and this will indirectly test that the private method behaves as intended. This helps to reduce maintenance as private methods are likely to be refactored (e.g. changed or renamed) often and would require any unit tests against them to be updated frequently.
