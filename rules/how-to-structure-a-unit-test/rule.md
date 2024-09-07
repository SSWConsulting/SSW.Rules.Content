---
seoDescription: Learn how to structure a unit test with Adam Cogan's 3 A's - Arrange, Act, and Assert.
type: rule
title: Do you know how to structure a unit test (aka the 3 a's)?
uri: how-to-structure-a-unit-test
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-know-how-to-structure-a-unit-test-aka-the-3-as
  - do-you-know-how-to-structure-a-unit-test-(aka-the-3-as)
created: 2020-03-11T16:51:15.000Z
archivedreason: null
guid: 5af6b8fd-5e65-4c68-8342-527090a61125
---

A test verifies expectations. Traditionally it has the form of 3 major steps:

1. Arrange
2. Act
3. Assert

<!--endintro-->

In the "Arrange" step we get everything ready and make sure we have all things handy for the "Act" step.

The "Act" step executes the relevant code piece that we want to test.

The "Assert" step verifies our expectations by stating what we were expecting from the system under test.

Developers call this the "AAA" syntax.

```cs
[TestMethod]
public void TestRegisterPost_ValidUser_ReturnsRedirect()
{
   // Arrange
   AccountController controller = GetAccountController();
   RegisterModel model = new RegisterModel()
   {
      UserName = "someUser",
      Email = "goodEmail",
      Password = "goodPassword",
      ConfirmPassword = "goodPassword"
   };
   // Act
   ActionResult result = controller.Register(model);
   // Assert
   RedirectToRouteResult redirectResult = (RedirectToRouteResult)result;
   Assert.AreEqual("Home", redirectResult.RouteValues["controller"]);
   Assert.AreEqual("Index", redirectResult.RouteValues["action"]);
}
```

::: good
Figure: A good structure for a unit test

:::
