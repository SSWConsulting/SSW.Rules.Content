---
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

* Fragile code - e.g. regular expressions
* When errors can be difficult to spot, e.g. in rounding, arithmetic and other calculations

E.g. You would test correct input such as 12/3 = 4 plus bad input such as 12/4 &lt;&gt; 4 and that 12/0 does not crash the application, and instead a DivideByZero Exception is thrown and handled gracefully.

E.g. Methods returning a Boolean value need to have both true and false test cases.

❌ Unit tests should *not* be written for:

* Dependencies - e.g. DLLs runtime errors (JIT)
* Dependencies - e.g. database schema, datasets, Web Services
* Performance - e.g. slow forms, time-critical applications
* When code has been generated from Code Generators eg. SQL database functions (Customer.Select, Customer.Update, Customer. Insert, Customer. Delete)
* When unit tests become bigger than the original function eg. When you know to insert items into a database in the SetUp to test a function that uses the database
* For Private methods \
because these will be tested by the public functions calling them, and they are likely to be change or refactored.

Generally, private methods should not have unit tests written for them as they are not exposed to other objects outside the original class. These private methods are likely to be refactored (e.g. changed or renamed) often and would require any unit tests to be updated frequently, so this becomes a maintenance nightmare. How should private methods be tested then? Private methods should be tested by the unit tests on the public and protected methods calling them and this will indirectly test that the private method behaves as intended.