---
type: rule
title: Do you know why to upgrade from AngularJS to Angular?
uri: do-you-know-why-to-upgrade-from-angularjs-to-angular
created: 2017-10-23T05:33:25.0000000Z
authors:
- id: 60
  title: Anthony Nguyen
- id: 81
  title: Jason Taylor

---



<span class='intro'> <p>​​Do you know why it is a good idea to upgrade your AngularJS application to the latest version of Angular (Angular 7, was Angular 6, was Angular 5, was Angular 4, was Angular 2+, and from here on will be known as Angular)?​​<br></p> </span>

<p>There are a number of reasons why you should consider migrating your AngularJS application to the latest version,&#160;<br></p><ol><li><strong>Dynamism</strong><br>The most annoying feature of AngularJS 1.x is that we can’t add anything dynamically. In contrast, in Angular,&#160;we can create a component, configure a router and register a service in a pleasant way. One of the basic concepts of Angular 2 is that after clicking on some menu item we can dynamically pull the part of the application responsible for the application display. To do it in AngularJS we had to hack the framework, use undocumented functions and gaps in the framework – things that we actually shouldn’t do.&#160;</li><li><strong>Component-based</strong><br>Angular&#160;is entirely component-based. This feature enforces thinking in components and as a&#160;result, we get an application&#160;that is neatly and naturally divided into separate parts - at least if you don’t create one component for the entire subpage. Component-based application development is usually faster due to easy creation and reasoning. Well designed components are also reusable which makes an application code more coherent.</li><li><strong>Dependency injection</strong><br>There is a simpler, more intelligible dependency injection container in Angular. Few developers knew the difference between provider, service, and factory in Angular 1 and there is no such problem in Angular. Now the default setting is class instance - only if you want to use a different raw value you need to declare it explicitly using an easily understandable object literal.</li><li><strong>TypeScript Support</strong><br>The latest version of Angular fully embraces Typescript. For those unfamiliar with this term, TypeScript Lang builds on top of what you already know about JavaScript but incorporates many additional tools to your ability to refactor code, write in modern JS (ECMAScript 2015), and compile to the older versions depending on browser request.&#160;Another important facet is IDE integration is that it makes easier to scale large projects through refactoring your whole code base at the same time. Its inbuilt code completion tool effectively saves your precious time from having to look up various features from the libraries you use individually.<br></li></ol>


