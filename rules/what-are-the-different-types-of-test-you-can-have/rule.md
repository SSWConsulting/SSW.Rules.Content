

---
uri: what-are-the-different-types-of-test-you-can-have
title: What are the different types of test you can have?
created: YYYY-03-DD 16:44:58
authors:
  - id: 1
    title: Adam Cogan
  - id: 34
    title: Brendan Richards
  - id: 78
    title: Matt Wicks
---




<span class='intro'> Here are some of the common techniques used for testing software.<br> </span>

<ul><h3 class="ssw15-rteElement-H3">​​​​Smoke test<br></h3><li>You fire up your application and click around prior to giving it to a tester. Most developers do this.<br></li></ul><ul><h3 class="ssw15-rteElement-H3">Unit Tests​​​<br></h3><li>They are coded by a developer</li><li>Quick</li><li>Independent</li><li>Test just 1 behaviour in isolation<br></li><li>Tip&#58; Use mock objects to make it faster and not to be bothered by external dependencies eg. the web service going down. The popular ones are&#160;Moq and&#160;nSubstitute</li></ul><ul><h3 class="ssw15-rteElement-H3">Integrations Tests​<br></h3><li>They are coded by a developer</li><li>Slower<br></li><li>Test the interaction of components eg. Databases, Web Services</li></ul><ul><h3 class="ssw15-rteElement-H3">Functional Tests​​<br></h3><li>Verifies the functionality of a system, typically from an end-user perspective<br></li><li>Can be performed manually or executed using an automated framework see&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=5f869f9c-b03d-4194-bd65-142dd0dfc0eb">https&#58;//rules.ssw.com.au/microsoft-recommended-frameworks-for-automated-ui-driven-functional-testing​​</a><br></li></ul><h3 class="ssw15-rteElement-H3">Subcutaneous&#160;Tests<br></h3><p>Subcutaneous (as in just benath the skin) are a type of integration/functional test that operate just below the UI -&#160; and&#160;are good for automated functional testing that would otherwise be difficult to achive by manipulating the UI itself.&#160;</p><p></p><ul><li>Written by developers<br></li><li>Test the&#160;full underlying behaviour of your app but bypasses the UI<br></li><li>Requires business logic to be implemented in the API / middle layer and not in the UI.<br></li><li>Tests can be much easier to write than using&#160;technologies that drive a UI (such as Selemium)<br></li></ul><p></p><ul><h3 class="ssw15-rteElement-H3">Load Tests​​<br></h3><li>Setup by developers<br></li><li>Simulate expected load on your application<br></li><li>Use the performance stats as a baseline for regression. You don't want to decrease performance in your application.<br></li><li>Tip&#58; try to execute these from the cloud<br></li></ul><ul><h3 class="ssw15-rteElement-H3">Stress Tests<br></h3><li>Setup by developers<br></li><li>Hit your application very hard, and try to see where your limits are (CPU, Network, Memory)​<br></li></ul><div><br></div><h3 class="ssw15-rteElement-H3">The Testing Pyramid<br></h3><div><img src="/SiteAssets/the-different-types-of-test/TestPyramid.png" alt="TestPyramid.png" style="margin&#58;5px;width&#58;400px;height&#58;308px;" /><br></div><div><strong>Figure&#58; the testing pyramid</strong><br></div><div><br></div><div>The concept of a testing pyramid was introduced by&#160;​Mike&#160;Cohn.<br></div><div>It's a metaphor that gives a&#160;guideline on how many tests we should write in each area.</div><div><br></div><div>At the bottom of the pyramid are small, isolated unit tests. These should be simple, easy to write and fast to execute. Our projects should aim to have many of these tests. As you move up the pyramid, complexity (such as the number of involved services) increases. So these tests become progressively harder to wite and slower to run. You should aim to write fewer tests as you move up the pyramid.<br></div><div>​<br><br></div><div><br></div>


