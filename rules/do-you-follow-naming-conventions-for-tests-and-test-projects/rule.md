---
type: rule
archivedreason: 
title: Do you follow naming conventions for tests and test projects?
guid: 1aea50c6-b2cc-4e1e-a483-34b4776e0e1e
uri: do-you-follow-naming-conventions-for-tests-and-test-projects
created: 2020-03-24T00:04:10.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 34
  title: Brendan Richards
- id: 78
  title: Matt Wicks
related: []

---


<h3 class="ssw15-rteElement-H3">Test Projects​​<br></h3><p>Tests should always live in separate projects – and you usually create a project from a template for your chosen test framework.<br>Because your test projects are startup projects (in that they can be independently started), they should target specific .Net runtimes and not just .Net Standard.<br>A Unit test project usually targets a single code project.</p><h3 class="ssw15-rteElement-H3">Project Naming​<br></h3><p>Integration and unit tests should be kept separate and should be named to clearly distinguish the two.<br>This is to make it easier to run only unit tests on your build server (and this should be possible as unit tests should have no external dependencies)&#160;<br>Integration tests require dependencies and often won't run as part of your build process.&#160; These should be automated later in the DevOps pipeline.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3">​Test Project Location​<br></h3><p>Test projects can be located either&#58;<br></p><ul><li>directly next to the project under test – which makes them easy to find&#160;</li><li>or in a separate tests location – which makes it easier to deploy the application without tests included.<br></li></ul><dl class="badImage"><dt>
      <img src="/PublishingImages/clean-architecture-naming.png" alt="clean-architecture-naming.png" />
   </dt><dd>Figure&#58; In Jason Taylor’s Clean Architecture template, the tests are clearly placed in a separate location which makes it easy to deploy to production without them.&#160;It’s easy to tell which project is under test and what style of tests will be found in each test project. 
      <a href="https&#58;//github.com/jasontaylordev/CleanArchitecture">https&#58;//github.com/jasontaylordev/CleanArchitecture​</a></dd></dl><h3 class="ssw15-rteElement-H3">​Naming Conventions for Tests​​<br></h3>There are a few “schools of thought” when it comes to naming the tests themselves.&#160;<br>Internal consistency within a project is important.<br>It’s usually a bad idea to name tests after the class or method under test – as this naming can quickly get out-of-sync if you use refactoring tools – and one of the key benefits from unit testing is the confidence to refactor!<br>&#160;<br>Remember that descriptive names are useful – but the choice of name is not the developer’s only opportunity to create readable tests.<br>
<ul><li>Aim to make the body of the test easy to read with clear Arrange, Act, and Assert steps.</li><li>Use a good assertion library to make test failures informative</li><li>Use comments and refer to bug reports to document the “why” when you have a test for a specific edge-case.&#160;</li><li>Remember that the F12 shortcut will navigate from the body of your test straight to the method you’re calling.</li><li>The point of a naming convention is to make code more readable, not less - so use your judgement and call in others to verify your readability.<br></li></ul><dl class="badImage"><dt><img src="/PublishingImages/bad-naming.png" alt="bad-naming.png" />​</dt><dd>Figure&#58; Bad Example - From the test explorer view you cannot tell what a test is meant to test from the name</dd></dl><p class="ssw15-rteElement-CodeArea"> 
   <b>[Method/PropertyName]_Should_[ExpectedBehavior]_When_[StateUnderTest]</b></p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; The &quot;should&quot;&#160;naming convention is effective – it encourages developers to clearly define the expected result upfront without requiring too much verbosity.</dd>&#160;<br>For example to test a tax calculation&#58;&#160;<b>Checkout_Should_Add10Precent_When_CountryIsAustralia</b>.<b></b><br> 
<p class="ssw15-rteElement-CodeArea"><b>Withdraw_Should_ThrowException_When_InvalidAccountInfo</b><br><br><b>Purchase_Should_Suceed_When_BalanceIsWithinCreditLimit</b><br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Examples - Without looking at code, I know what the unit tests are trying to do<br></dd><p>A list of other suggested conventions can be found here&#58;&#160;<a href="https&#58;//dzone.com/articles/7-popular-unit-test-naming">7 Popular Unit Test Naming Conventions</a>.</p>


