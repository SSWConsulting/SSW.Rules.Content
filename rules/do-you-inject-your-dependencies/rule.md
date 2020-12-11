---
type: rule
archivedreason: 
title: Do you inject your dependencies?
guid: 28b28f90-0e00-43ee-826e-5ddab62fc7e4
uri: do-you-inject-your-dependencies
created: 2012-10-19T17:23:08.0000000Z
authors:
- id: 24
  title: Adam Stephensen
related: []

---

Injecting your dependency gives you:

* Loosely coupled classes
* Increased code reusing
* Maintainable code
* Testable methods
* All dependencies are specified in one place
* Class dependencies are clearly visible in the constructor


<!--endintro-->

[[badExample]]
| ![A solution where each layer depends on static classes is not maintainable or testable](inject-bad-1.jpg)
[[goodExample]]
| ![Dependencies in each layer should only be interfaces. This allows dependencies to be easily interchanged and unit tests to be written against mock/fake objects](inject-good-1.jpg)
[[badExample]]
| ![Classes should not include dependencies on database classes or business objects. Both of these classes may contain dependencies on external services like web services or databases](inject-bad-2.jpg)
[[goodExample]]
| ![The dependencies are injected into the class. This enables alternative classes to be injected. For example, a DHLShippingCalculator should be easily substituted for a FedexShippingCalculator. A MockShippingCalculator and MockProductRepository could be injected if we wanted to run unit tests](inject-good-2.jpg)
