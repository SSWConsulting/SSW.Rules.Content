---
type: rule
title: Do you use standalone components?
guid: 2088c2e1-7243-45cc-b812-ee228856ddc1
uri: standalone-components
created: 2023-08-24T19:01:24.0000000Z
authors: 
  - title: Anton Polkanov
    url: https://www.ssw.com.au/people/anton-polkanov/
  - title: Chris Clement
    url: https://www.ssw.com.au/people/chris-clement/
---

[Standalone components](https://angular.io/guide/standalone-components) were introduced in Angular 14 and should be used instead of modules for every new component you create.

<!--endintro-->

There is a number of advantages of using standalone components over modules as they:

1. Reduce the amount of boilerplate code. They don't belong to a particular NgModule and don't have to be declared, so can be used in any part of the application
2. Streamline component creation
3. Allow to lazy-load the component without using an NgModule
4. Flatten the learning curve for new developer as the concept of NgModules is off the table

To make a component standalone, set `standalone: true`

```javascript
@Component({
  standalone: true,
  selector: 'my-component',
  imports: [FooComponent],
  template: `
    ...
    <foo-component></foo-component>
  `,
})
export class MyComponent {
  // component logic
}
```

<!--endintro-->
