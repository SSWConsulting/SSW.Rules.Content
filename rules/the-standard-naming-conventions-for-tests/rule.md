---
type: rule
title: Do you follow the standard naming conventions for tests?
uri: the-standard-naming-conventions-for-tests
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-follow-the-standard-naming-conventions-for-tests
created: 2020-03-11T20:18:31.000Z
archivedreason: The rule has been replaced by
  [https://ssw.com.au/rules/follow-naming-conventions-for-tests-and-test-projects](/rules/follow-naming-conventions-for-tests-and-test-projects)
guid: 5a6283ea-18d8-4586-a696-06ef05660ce5
---

Ensuring a consistent and organized approach to testing is pivotal in any development process. Do you adhere to the established standard naming conventions for tests? Let's explore the importance of this practice and its impact on the efficiency and clarity of your testing procedures.

> As well as keeping your code tidy, using this naming convention also allows you to use TestDriven.Net's 'Go To Test/Code' command.
> This navigates between your tests and code under test (and back). This is something that test-driven developers end up doing a lot.
> Screen captures at <https://weblogs.asp.net/nunitaddin/testdriven-net-3-0-all-systems-go>
>
> * Jamie Cansdale

<!--endintro-->

| **Test Object**  | **Recommended Style**  | **Example**  |
| --- | --- | --- |
| Project Name | Tests.[Testtypes].Projectname | Tests.Unit.Common,Tests.Unit.WebFrontend,Test.Integration.MainWCFService
Tests.Functional.SilverlightUI, Tests.Functional.WebUI \* |
| Test Fixture Name | [Type]Tests | OrdersTests, CustomerTests, DeveloperTests |
| Test Case | [Function]Test | NullableIntTryParse\_NumberIsValid1\_Return1, StringHelperEncodeTo64\_EncodeAndUnencodeString\_ReturnSameString |
| Set Up | SetUp |   |
| Tear Down | TearDown |   |

\* Test types are categorized into "Unit" "Integration" or "Functional" tests, as explained in "[the different types of test you can have](/different-types-of-testing)"

The main reason why we are categorizing tests is so that we can run different test suites. Eg.

* Unit tests on Gated Checkin
* Integration tests after each check in on the build server
* All tests including the functional tests in the nightly build

#### Samples for Naming of test projects

**Test.Unit.WebUI:** This test project, tests the WebUI project, and is independent of external resources.
That means all tests must pass.

**Test.Integration.WebUI:** This test project tests the WebUI and depends on other external resources (Eg. probably needs a database, web services, etc.).
That means if any external resource is unavailable, the tests will fail.

**Tests.Functional.SilverlightUI:** Tests the Silverlight UI from an end-user perspective by clicking around in the application

::: good  
![Figure: Good example - Naming for a Unit Test Project](UnitTestsProject.jpg)  
:::

#### Samples Naming of test methods

```cs
[TestMethod]
 public void Test_Client()
```

::: bad
Bad example: There is no way to guess what this test does; you have to read the source
:::

```cs
[TestMethod]
 public void PubSubServiceConnectTest_AuctionOk_AuctionInfoReturned()
```

::: good
Good example: We are testing PubSubService.Connect under the scenario that the "Auction status is OK" with an expected behaviour that data is returned  
:::

#### Sample Code for Integration Tests

```cs
using System;
using System.Collections;
using System.Data;
using System.Data.SqlClient;
using NUnit.Framework;
using SSW.NetToolKit.BusinessService;
using SSW.NetToolKit.DataAccess;
namespace SSW.NETToolkit.IntegrationTests
  {
  [TestFixture]
  Public class CustomerTests
    {
    BusinessRules business=new BusinessRules(); 
   
    [Test]
    public void OrderTotal_SimpleExampleInput()
        {
        decimal calculatedGrandTotal = business.CalculateOrderGrandTotal(10248);
        int expected = 440;
        Assert.AreEqual(expected, calculatedGrandTotal, "Calculated grand total didn't match the expect
        }
    [Test]
    public void OderTotal_Discounts()
        {
        decimal calculatedGrandTotal = business.CalculateOrderGrandTotal(10260);
        decimal expected = 1504.65m;
        Assert.AreEqual(expected, calculatedGrandTotal, "Calculated grand total didn't match the expecte
        }
    [Test]
    public void RoundingTest_RoundUp()
        {
        Assert.AreEqual(149.03, business.ApplyRounding(149.0282m), "Incorrect rounding rules applied for
        }
    [Test]
    public void RoundingTest_RoundDown()
        {
        Assert.AreEqual(149.02, business.ApplyRounding(149.0232m), "Incorrect rounding rules applied 
   
        }
    [Test]
    public void RoundingTest_NoRoundingNeeded()
        {
        Assert.AreEqual(149.02, business.ApplyRounding(149.02m), "Incorrect rounding rules applied for 
   
        }
    [Test]
    public void RoundingTest_BorderCondition()
        {
        Assert.AreEqual(149.02, business.ApplyRounding(149.025m), "Incorrect rounding rules applied for
        }
    }
  }
```

![Figure: This rule is consistent with the Visual Studio default](TestGenerationSettings.gif)  

**Tip:** You can create a test project using the Unit Test Wizard: Test &gt; Add New Test

![Figure: Unit Test Wizard 1](AddNewTest.gif)  

![Figure: Unit Test Wizard 2](CreateUnitTests.gif)
