---
type: rule
title: What are the different types of test you can have?
uri: what-are-the-different-types-of-test-you-can-have
created: 2020-03-11T16:44:58.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 34
  title: Brendan Richards
- id: 78
  title: Matt Wicks

---



<span class='intro'> These are the types of test you can have&#58;<br> </span>

<ul><h3 class="ssw15-rteElement-H3">​​​​Smoke test<br></h3><li>You fire up your application and click around prior to giving it to a tester. Most developers do this.<br></li></ul><ul><h3 class="ssw15-rteElement-H3">Unit Tests​​​<br></h3><li>They are coded by a developer</li><li>Quick</li><li>Independent</li><li>Test just 1 behaviour in isolation<br></li><li>Tip&#58; Use mock objects to make it faster and not to be bothered by external dependencies eg. the web service going down. The popular ones are&#160;Moq and&#160;nSubstitute</li></ul><ul><h3 class="ssw15-rteElement-H3">Integrations Tests​<br></h3><li>They are coded by a developer</li><li>Slower<br></li><li>Test the interaction of components eg. Databases, Web Services</li></ul><ul><h3 class="ssw15-rteElement-H3">Functional Tests​​<br></h3><li>Verifies the functionality of a system, typically from an end-user perspective<br></li><li>Can be performed manually or executed using an automated framework see&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=5f869f9c-b03d-4194-bd65-142dd0dfc0eb">https&#58;//rules.ssw.com.au/microsoft-recommended-frameworks-for-automated-ui-driven-functional-testing​​</a><br></li></ul><ul><h3 class="ssw15-rteElement-H3">Load Tests​​<br></h3><li>Setup by developers<br></li><li>Simulate expected load on your application<br></li><li>Use the performance stats as a baseline for regression. You don't want to decrease performance in your application.<br></li><li>Tip&#58; try to execute these from the cloud<br></li></ul><ul><h3 class="ssw15-rteElement-H3">Stress Tests<br></h3><li>Setup by developers<br></li><li>Hit your application very hard, and try to see where your limits are (CPU, Network, Memory)​<br></li></ul>


