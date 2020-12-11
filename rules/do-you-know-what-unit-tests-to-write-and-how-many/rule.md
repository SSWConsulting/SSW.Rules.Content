---
type: rule
archivedreason: 
title: Do you know what unit tests to write and how many?
guid: 2024f813-eb57-4890-a789-2c46d9f7f150
uri: do-you-know-what-unit-tests-to-write-and-how-many
created: 2020-03-11T17:34:49.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

People aim for 100% Unit Test Coverage but in the real world, this is 100% impractical. Actually it seems that the most popular metric in TDD (Test Driven Development) is to aim for 100% of methods to be unit tested. However, in the real world, this goal is rarely, if ever, achieved. Unit tests are created to validate and assert that public and protected methods of a class meet an expected outcome based on varying input. This includes both good and bad data being tested, to ensure the method behaves as expected and returns the correct result or traps any errors.

<!--endintro-->

Generally, private methods should not have unit tests written for them as they are not exposed to other objects outside the original class. These private methods are likely to be refactored (eg. changed, renamed) over time and will require the unit tests to be updated and this becomes a maintenance nightmare. So how do private methods get tested? Private methods should be tested by the unit tests on the public and protected methods calling them and this will indirectly test the private method behaves as intended.

E.g. You would test correct input such as 12/3 = 4 plus bad input such as 12/4 &lt;&gt; 4 and that 12/0 does not crash the application, and instead a DivideByZero Exception is thrown and handled gracefully.

E.g. Methods returning a Boolean value need to have both true and false test cases.

Unit tests should be written for:

* Fragile Code - e.g. Regular Expressions
* When errors can be difficult to spot - e.g. Rounding, arithmetic, calculations


Unit tests should not be written for:

* Dependencies - e.g. DLLs Run time errors (JIT)
* Dependencies - e.g. Database Schema, Datasets, Web Services
* Performance - e.g. Slow forms, Time-critical applications
* When code has been generated from Code Generators eg. SQL database functions (Customer.Select, Customer.Update, Customer. Insert, Customer. Delete)
* When unit tests become bigger than the original function eg. When you know to insert items into a database in the SetUp to test a function that uses the database
* For Private methods because these will be tested by the public functions calling them, and they are likely to be change or refactored.
