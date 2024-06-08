---
type: rule
archivedreason: 
title: Do you use a ‘Precision Mocker’ like NSubstitute instead of a ‘Monster Mocker’ like Microsoft Fakes?
guid: 927a0909-7880-4b30-9c0c-f2ff65110905
uri: use-a-precision-mocker-instead-of-a-monster-mocker
created: 2013-02-05T13:03:11.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
- title: William Liebenberg
  url: https://ssw.com.au/people/william-liebenberg
related: []
redirects:
- do-you-use-a-precision-mocker-like-moq-instead-of-a-monster-mocker-like-microsoft-fakes
- do-you-use-a-precision-mocker’-like-moq-instead-of-a-monster-mocker’-like-microsoft-fakes

---

Using a precision mocking framework (such as [NSubstitute](https://nsubstitute.github.io/)) encourages developers to write maintainable, loosely coupled code.

Mocking frameworks allow you to replace a section of the code you are about to test, with an alternative piece of code.
 For example, this allows you to test a method that performs a calculation and saves to the database, without actually requiring a database.

<!--endintro-->

There are two types of mocking framework.

### The Monster Mocker (e.g. Microsoft Fakes or TypeMock)


This type of mocking framework is very powerful and allows replacing code that wasn’t designed to be replaced.
 This is great for testing legacy code, tightly coupled code with lots of static dependencies (like DateTime.Now) and SharePoint.


::: bad  
![Figure: Bad Example – Our class is tightly coupled to our authentication provider, and as we add each test we are adding \*more\* dependencies on this provider. This makes our codebase less and less maintainable. If we ever want to change our authentication provider “OAuthWebSecurity”, it will need to be changed in the controller, and every test that calls it](monster-mocker.jpg)  
:::

### The Precision Mocker (e.g. NSubstitute)


This mocking framework takes advantage of well written, loosely coupled code.

The mocking framework creates substitute items to inject into the code under test.

::: good
![Figure: Good Example - An interface describes the methods available on the provider](nsubstitute-1.png)  
:::


::: good  
![Figure: Good Example - The Product Repository is injected into the ProductService class (via constructor injection)](nsubstitute-2.png)  
:::


::: good  
![Figure: Good Example - The code is loosely coupled. The ProductService is dependent on an interface of the Product Repository, which is injected into the ProductService via its constructor. The unit test can easily create a mock object of the Product Repository and substitute it for the dependency. NSubstitute is one of the most popular mocking libraries.](nsubstitute-3.png)  
:::
