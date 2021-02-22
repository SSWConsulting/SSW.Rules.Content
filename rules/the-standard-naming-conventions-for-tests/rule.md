---
type: rule
archivedreason: The rule has been replaced by https://rules.ssw.com.au/follow-naming-conventions-for-tests-and-test-projects
title: Do you follow the standard naming conventions for tests?
guid: 5a6283ea-18d8-4586-a696-06ef05660ce5
uri: the-standard-naming-conventions-for-tests
created: 2020-03-11T20:18:31.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-follow-the-standard-naming-conventions-for-tests

---


<p class="ssw15-rteElement-Reference">Hi Adam,<br><br>As well as keeping your code tidy, using this naming convention also allows you to use TestDriven.Net's 'Go To Test/Code' command.<br>This navigates between your tests and code under test (and back). This is something that test-driven developers end up doing a lot.<br>Screen captures at <a href="https://weblogs.asp.net/nunitaddin/testdriven-net-3-0-all-systems-go">https://weblogs.asp.net/nunitaddin/testdriven-net-3-0-all-systems-go</a><br><br>- Jamie Cansdale<br></p>
<br><excerpt class='endintro'></excerpt><br>
<table cellspacing="0" width="100%" class="ssw15-rteTable-default"><tbody><tr><td class="ssw15-rteTable-default" style="width:33.3333%;"> 
            <strong>Test Object</strong></td><td class="ssw15-rteTable-default" style="width:33.3333%;"> 
            <strong>Recommended Style</strong></td><td class="ssw15-rteTable-default" style="width:33.3333%;"> 
            <strong>Example</strong></td></tr><tr><td class="ssw15-rteTable-default">Project Name</td><td class="ssw15-rteTable-default">Tests.[Testtypes].Projectname</td><td class="ssw15-rteTable-default">Tests.Unit.Common,Tests.Unit.WebFrontend,Test.Integration.MainWCFService<br>Tests.Functional.SilverlightUI, Tests.Functional.WebUI *</td></tr><tr><td class="ssw15-rteTable-default">Test Fixture Name</td><td class="ssw15-rteTable-default">[Type]Tests</td><td class="ssw15-rteTable-default">OrdersTests, CustomerTests, DeveloperTests</td></tr><tr><td class="ssw15-rteTable-default">Test Case</td><td class="ssw15-rteTable-default">[Function]Test</td><td class="ssw15-rteTable-default">NullableIntTryParse_NumberIsValid1_Return1, StringHelperEncodeTo64_EncodeAndUnencodeString_ReturnSameString</td></tr><tr><td class="ssw15-rteTable-default">Set Up</td><td class="ssw15-rteTable-default">SetUp</td><td class="ssw15-rteTable-default"> </td></tr><tr><td class="ssw15-rteTable-default">Tear Down</td><td class="ssw15-rteTable-default">TearDown</td><td class="ssw15-rteTable-default"> </td></tr></tbody></table><p> 
   <br> 
</p><p>*Test types are categorized into "Unit" "Integration" or "Functional" tests, as explained in "<a href="https://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterUnitTests.aspx#TypesOfTests">2. What are the different types of test you can have?</a>"</p><p>The main reason why we are categorizing tests is so that we can run different test suites. Eg.</p><ul><li>Unit tests on Gated Checkin</li><li>Integration tests after each check in on the build server</li><li>All tests including the functional tests in the nightly build</li></ul><p> 
   <strong>Samples for Naming of test projects</strong><br>Test.Unit.WebUI: This test project, tests the WebUI project, and is independent of external resources.<br>That means all tests must pass.<br>Test.Integration.WebUI: This test project tests the WebUI and depends on other external resources (Eg. probably needs a database, web services, etc.).<br>That means if any external resource is unavailable, the tests will fail.<br>Tests.Functional.SilverlightUI: Tests the Silverlight UI from an end-user perspective by clicking around in the application</p><dl class="goodImage"><dt>
      <img src="UnitTestsProject.jpg" alt="UnitTestsProject.jpg" />
   </dt><dd>Figure: Good example - Naming for a Unit Test Project</dd></dl> 
<span style="color:#cc4141;font-family:"segoe ui", "trebuchet ms", tahoma, arial, verdana, sans-serif;font-size:18px;">Samples Naming of test methods​​​</span>
<p class="ssw15-rteElement-CodeArea"> [TestMethod]<br> public void Test_Client()</p><dd class="ssw15-rteElement-FigureBad">Bad example: There is no way to guess what this test does; you have to read the source​​<br></dd><p class="ssw15-rteElement-CodeArea"> [TestMethod]<br> public void PubSubServiceConnectTest_AuctionOk_AuctionInfoReturned()</p><dd class="ssw15-rteElement-FigureGood">Good Example: We are testing PubSubSe​rvice.Connect under the scenario that the "Auction status is OK" with an expected behaviour that data is returned</dd><p>Sample Code for Integration Tests:</p><p class="ssw15-rteElement-CodeArea">using System;<br>using System.Collections;<br>using System.Data;<br>using System.Data.SqlClient;<br>using NUnit.Framework;<br>using SSW.NetToolKit.BusinessService;<br>using SSW.NetToolKit.DataAccess;<br>namespace SSW.NETToolkit.IntegrationTests<br>  {<br>  [TestFixture]<br>  Public class CustomerTests<br>    {<br>    BusinessRules business=new BusinessRules(); 
   <br>    [Test]<br>    public void OrderTotal_SimpleExampleInput()<br>        {<br>        decimal calculatedGrandTotal = business.CalculateOrderGrandTotal(10248);<br>        int expected = 440;<br>        Assert.AreEqual(expected, calculatedGrandTotal, "Calculated grand total didn't match the expect<br>        }<br>    [Test]<br>    public void OderTotal_Discounts()<br>        {<br>        decimal calculatedGrandTotal = business.CalculateOrderGrandTotal(10260);<br>        decimal expected = 1504.65m;<br>        Assert.AreEqual(expected, calculatedGrandTotal, "Calculated grand total didn't match the expecte<br>        }<br>    [Test]<br>    public void RoundingTest_RoundUp()<br>        {<br>        Assert.AreEqual(149.03, business.ApplyRounding(149.0282m), "Incorrect rounding rules applied for<br>        }<br>    [Test]<br>    public void RoundingTest_RoundDown()<br>        {<br>        Assert.AreEqual(149.02, business.ApplyRounding(149.0232m), "Incorrect rounding rules applied 
   <br>        }<br>    [Test]<br>    public void RoundingTest_NoRoundingNeeded()<br>        {<br>        Assert.AreEqual(149.02, business.ApplyRounding(149.02m), "Incorrect rounding rules applied for 
   <br>        }<br>    [Test]<br>    public void RoundingTest_BorderCondition()<br>        {<br>        Assert.AreEqual(149.02, business.ApplyRounding(149.025m), "Incorrect rounding rules applied for<br>        }<br>    }<br>  }<br></p>
​
<dl class="image"><dt><img src="TestGenerationSettings.gif" alt="TestGenerationSettings.gif" /></dt><dd>Figure: This rule is consistent with the Visual Studio default</dd></dl> 
   <b>Tip: </b>You can create a test project using the Unit Test Wizard: Test &gt; Add New Test<p></p><dl class="image"><dt>​​<img src="AddNewTest.gif" alt="AddNewTest.gif" /></dt><dd>Figure: Unit Test Wizard 1</dd></dl><dl class="image"><dt><img src="CreateUnitTests.gif" alt="CreateUnitTests.gif" /></dt><dd>Figure: Unit Test Wizard 2</dd></dl>


