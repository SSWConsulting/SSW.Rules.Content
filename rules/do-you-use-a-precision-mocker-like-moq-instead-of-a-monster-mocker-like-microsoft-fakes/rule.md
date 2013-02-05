---
type: rule
title: Do you use a ‘Precision Mocker’ like Moq instead of a ‘Monster Mocker’ like Microsoft Fakes?
uri: do-you-use-a-precision-mocker-like-moq-instead-of-a-monster-mocker-like-microsoft-fakes
created: 2013-02-05T13:03:11.0000000Z
authors:
- id: 24
  title: Adam Stephensen

---



<span class='intro'> <p>Using a precision mocking framework (such as Moq or NSubstitute) encourages developers to write maintainable, loosely coupled code.</p>

<p>Mocking frameworks allow you to replace a section of the code you are about to test, with an alternative piece of code.<br>
For example, this allows you to test a method that performs a calculation and saves to the database, without actually requiring a database.
</p> </span>

<p>There are two types of mocking framework.</p><p><strong>The Monster Mocker (e.g. Microsoft Fakes or TypeMock)</strong></p><p>This type of mocking framework is very powerful and allows replacing code that wasn’t designed to be replaced.<br>
This is great for testing legacy code (tightly coupled code with lots of static dependencies) and SharePoint.</p><dl class="badImage"><dt><img src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/monster-mocker.jpg" alt="" /></dt><dd>Figure&#58; Bad Example – Our class is tightly coupled to our authentication provider, and as we add each test we are adding *more* dependencies on this provider. This makes our codebase less and less maintainable. If we ever want to change our authentication provider “OAuthWebSecurity”, it will need to be changed in the controller, and every test that calls it</dd></dl><p><strong>The Precision Mocker (e.g. Moq)</strong></p><p>This mocking framework takes advantage of well written, loosely coupled code.</p><p>The mocking framework creates substitute items to inject into the code under test.</p><dl class="goodImage"><dt><img src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/precision-mocker-1.jpg" alt="" /></dt><dd>Figure&#58; Good Example - An interface describes the methods available on the provider</dd></dl><dl class="goodImage"><dt><img src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/precision-mocker-2.jpg" alt="" /></dt><dd>Figure&#58; Good Example - The authentication provider is injected into the class under test (preferably via the constructor)</dd></dl><dl class="goodImage"><dt><img src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/precision-mocker-3.jpg" alt="" /></dt><dd>Figure&#58; Good Example - The code is loosely coupled. The controller is dependent on an interface, which is injected into the controller via its constructor. The unit test can easily create a mock object and substitute it for the dependency. Examples of this type of framework are Moq and NSubstitute</dd></dl>


