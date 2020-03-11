---
type: rule
archivedreason: 
title: What are the different types of test you can have?
guid: 45e92041-c363-4a4a-b86e-50993f24e4fb
uri: the-different-types-of-test
created: 2020-03-11T16:44:58.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
- title: Matt Wicks
  url: https://ssw.com.au/people/matt-wicks
related: []
redirects:
- what-are-the-different-types-of-test-you-can-have

---


These are the types of test you can have&#58;<br>
<br><excerpt class='endintro'></excerpt><br>
<ul><h3 class="ssw15-rteElement-H3">​​​​Smoke test<br></h3><li>You fire up your application and click around prior to giving it to a tester. Most developers do this.<br></li></ul><ul><h3 class="ssw15-rteElement-H3">Unit Tests​​​<br></h3><li>They are coded by a developer</li><li>Quick</li><li>Independent</li><li>Test just 1 method in a class</li><li>Tip&#58; Use mock objects to make it faster and not to be bothered by external dependencies eg. the web service going down. The popular ones are&#58; MOQ, TypeMock, NMock, RhinoMocks, nSubstitute</li></ul><ul><h3 class="ssw15-rteElement-H3">Integrations Tests​<br></h3><li>They are coded by a developer</li><li>Slower</li><li>Test the interaction of components eg. Databases, Web Services</li></ul><ul><h3 class="ssw15-rteElement-H3">Functional Tests​​<br></h3><li>Recorded by a tester</li><li>Verifies the functionality of a system, typically from an end-user perspective</li><li>Tip&#58; Use VS Webtest if you have got no AJAX in your page</li><li>Tip&#58; Use Coded UI Test or Telerik Tests to test the interactivity</li></ul><ul><h3 class="ssw15-rteElement-H3">Load Tests​​<br></h3><li>Setup by developers</li><li>Reuse the web tests</li><li>Simulate expected load on your application</li><li>Tip&#58; Use VS Load tests or 3rd party such as&#160;<a>loadstorm</a></li><li>Use the performance stats as a baseline for regression. You don't want to decrease performance in your application.</li></ul><ul><h3 class="ssw15-rteElement-H3">Stress Tests<br></h3><li>Setup by developers</li><li>Reuse web tests</li><li>Hit your application very hard, and try to see where your limits are (CPU, Network, Memory)​<br></li></ul>


