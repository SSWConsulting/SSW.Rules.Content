---
type: rule
title: Do you inject your dependencies?
uri: do-you-inject-your-dependencies
created: 2012-10-19T17:23:08.0000000Z
authors:
- id: 24
  title: Adam Stephensen

---



<span class='intro'> <p>Injecting your dependency gives you&#58;</p>
<ul><li>Loosely coupled classes</li>
<li>Increased code reusing</li>
<li>Maintainable code</li>
<li>Testable methods</li>
<li>All dependencies are specified in one place </li>
<li>Class dependencies are clearly visible in the constructor</li></ul> </span>

<img class="ms-rteCustom-ImageArea" alt="inject" src="inject-bad-1.jpg" /> <span class="ms-rteCustom-FigureBad">Figure&#58; Bad Example – A solution where each layer depends on static classes is not maintainable or testable</span> <img class="ms-rteCustom-ImageArea" alt="inject" src="inject-good-1.jpg" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Good Example – Dependencies in each layer should only be interfaces. This allows dependencies to be easily interchanged and unit tests to be written against mock/fake objects</span> <img class="ms-rteCustom-ImageArea" alt="inject" src="inject-bad-2.jpg" /> <span class="ms-rteCustom-FigureBad">Figure&#58; Bad Example – Classes should not include dependencies on database classes or business objects. Both of these classes may contain dependencies on external services like web services or databases</span> <img class="ms-rteCustom-ImageArea" alt="inject" src="inject-good-2.jpg" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Good Example – The dependencies are injected into the class. This enables alternative classes to be injected. For example, a DHLShippingCalculator should be easily substituted for a FedexShippingCalculator. A MockShippingCalculator and MockProductRepository could be injected if we wanted to run unit tests</span> 


