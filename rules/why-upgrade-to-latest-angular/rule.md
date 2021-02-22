---
type: rule
archivedreason: 
title: Do you know why to upgrade from AngularJS to Angular?
guid: cbb12ff9-a562-44ce-a4c3-6d0579a44147
uri: why-upgrade-to-latest-angular
created: 2017-10-23T05:33:25.0000000Z
authors:
- title: Anthony Nguyen
  url: https://ssw.com.au/people/anthony-nguyen
- title: Jason Taylor
  url: https://ssw.com.au/people/jason-taylor
related: []
redirects:
- why-upgrade-to-angular-2
- do-you-know-why-to-upgrade-from-angularjs-to-angular

---

Do you know why it is a good idea to upgrade your AngularJS application to the latest version of Angular (Angular 7, was Angular 6, was Angular 5, was Angular 4, was Angular 2+, and from here on will be known as Angular)?

<!--endintro-->

There are a number of reasons why you should consider migrating your AngularJS application to the latest version,

1. **Dynamism** 
The most annoying feature of AngularJS 1.x is that we can’t add anything dynamically. In contrast, in Angular, we can create a component, configure a router and register a service in a pleasant way. One of the basic concepts of Angular 2 is that after clicking on some menu item we can dynamically pull the part of the application responsible for the application display. To do it in AngularJS we had to hack the framework, use undocumented functions and gaps in the framework – things that we actually shouldn’t do.
2. **Component-based** 
Angular is entirely component-based. This feature enforces thinking in components and as a result, we get an application that is neatly and naturally divided into separate parts - at least if you don’t create one component for the entire subpage. Component-based application development is usually faster due to easy creation and reasoning. Well designed components are also reusable which makes an application code more coherent.
3. **Dependency injection** 
There is a simpler, more intelligible dependency injection container in Angular. Few developers knew the difference between provider, service, and factory in Angular 1 and there is no such problem in Angular. Now the default setting is class instance - only if you want to use a different raw value you need to declare it explicitly using an easily understandable object literal.
4. **TypeScript Support** 
The latest version of Angular fully embraces Typescript. For those unfamiliar with this term, TypeScript Lang builds on top of what you already know about JavaScript but incorporates many additional tools to your ability to refactor code, write in modern JS (ECMAScript 2015), and compile to the older versions depending on browser request. Another important facet is IDE integration is that it makes easier to scale large projects through refactoring your whole code base at the same time. Its inbuilt code completion tool effectively saves your precious time from having to look up various features from the libraries you use individually.
