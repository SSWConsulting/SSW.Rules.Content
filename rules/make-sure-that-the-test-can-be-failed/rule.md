---
type: rule
archivedreason: 
title: Do you make sure that the test can be failed?
guid: fec2a216-ace7-4720-866f-9db216f9d0a9
uri: make-sure-that-the-test-can-be-failed
created: 2020-03-12T23:16:37.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Jason Taylor
  url: https://ssw.com.au/people/jason-taylor
related: []
redirects:
- do-you-make-sure-that-the-test-can-be-failed

---

It's important that the unit tests you develop are capable of failing and that you have seen it fail. A test that can never fail isn't helpful for anyone.

This is a fundamental principle in Test Driven Development (TDD) called Red/Green/Refactor.

<!--endintro-->

A common approach is by returning `NotImplementedException()` from the method you are writing tests for. For Example:

```cs
[Test]
public void ShouldAddTwoNumbers()
{
   var calculator = new Calculator();
   var result = calculator.Sum(10, 11);


   Assert.Equal(21, result);
}

// The method to test in class Calculator ...
public int Sum(int x, int y)
{
   throw new NotImplementedException();
}
```
::: bad
Bad Example: The test fails by throwing a `NotImplementedException`.
:::

This test fails for the wrong reasons, by throwing a `NotImplementedException`. In production, this is not a valid reason for this test to fail.
A `NotImplementedException` is synonymous with "still in development", include a `//TODO: ` marker with some notes about the steps to take to implement the test.


A better approach would be to return a value that is invalid.

```cs
[Test]
public void ShouldCheckIfPositive()
{
   var calculator = new Calculator();
   var result = calculator.IsPositive(10);


   Assert.True(result);
}

// The method to test in class Calculator ...
public int IsPositive(int x)
{
   return -1;
}
```

::: good
Good Example: The test fails by returning an invalid value.
:::

::: greybox
Sometimes there is no clear definition of an invalid value, then it is acceptable to fail a test using `NotImplementedException`. Add additional remarks, notes or steps on what to test and how to implement with a `//TODO: ...` marker. This will asssist you or other developers coming across this failed test. 

Make sure that this test will be implemented before a production release.
:::

```cs
// The method to test in class Calculator ...
public int IsPositive(int x)
{
   //NOTE: ths method has a clear "invalid" value
   return -1;
}
public int Sum(int x, int y)
{
   //NOTE: this method does not have a clear "invalid" value and throws a NotImplementedException and includes a TODO marker
   
   //TODO: need to implement Sum by adding both operands together using return x + y;
   throw NotImplementedException();
}
```
::: good
Good Example: The test fails by returning an invalid result or throwing a `NotImplementedException()` with a `//TODO: ` item.

:::

In this case, the test will fail because the `IsPositive` behavior is incorrect and `Sum` is missing its implementation.

You should do mutation testing to remove false positive tests and test your test suite to have more confidence.
Visit the Wiki for more information about [Mutation Testing](https://en.wikipedia.org/wiki/Mutation_testing)

To perform mutation testing you can use Stryker.NET. 
For more information please visit the [Stryker website](https://stryker-mutator.io/docs/stryker-net/introduction/)


