

---
uri: do-you-know-what-unit-tests-to-write-and-how-many
title: Do you know what unit tests to write and how many?
created: YYYY-03-DD 17:34:49
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p class="ssw15-rteElement-P">People aim for 100% Unit Test Coverage but in the real world, this is 100% impractical. Actually it seems that the most popular metric in TDD (Test Driven Development) is to aim for 100% of methods to be unit tested. However, in the real world, this goal is rarely, if ever, achieved. Unit tests are created to validate and assert that public and protected methods of a class meet an expected outcome based on varying input. This includes both good and bad data being tested, to ensure the method behaves as expected and returns the correct result or traps any errors.​​<br></p> </span>

<p>Generally, private methods should not have unit tests written for them as they are not exposed to other objects outside the original class. These private methods are likely to be refactored (eg. changed, renamed) over time and will require the unit tests to be updated and this becomes a maintenance nightmare. So how do private methods get tested? Private methods should be tested by the unit tests on the public and protected methods calling them and this will indirectly test the private method behaves as intended.<br></p><p>E.g. You would test correct input such as 12/3 = 4 plus bad input such as 12/4 &lt;&gt; 4 and that 12/0 does not crash the application, and instead a DivideByZero Exception is thrown and handled gracefully.</p><p>E.g. Methods returning a Boolean value need to have both true and false test cases.</p><p>Unit tests should be written for&#58;</p><ul><li>Fragile Code - e.g. Regular Expressions<br></li><li>When errors can be difficult to spot - e.g. Rounding, arithmetic, calculations<br></li></ul><p>Unit tests should not be written for&#58;</p><ul><li>Dependencies - e.g. DLLs Run time errors (JIT)<br></li><li>Dependencies - e.g. Database Schema, Datasets, Web Services<br></li><li>Performance - e.g. Slow forms, Time-critical applications<br></li><li>When code has been generated from Code Generators eg. SQL database functions (Customer.Select, Customer.Update, Customer. Insert, Customer. Delete)</li><li>When unit tests become bigger than the original function eg. When you know to insert items into a database in the SetUp to test a function that uses the database</li><li>For Private methods because these will be tested by the public functions calling them, and they are likely to be change or refactored.<br></li></ul>


