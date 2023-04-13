---
type: rule
archivedreason: 
title: Do you name your dependencies to avoid problems with minification?
guid: a234f979-bc20-4415-8e9a-caf2b9cfc4fc
uri: do-you-name-your-dependencies-to-avoid-problems-with-minification
created: 2014-10-07T14:42:09.0000000Z
authors:
- title: Ben Cull
  url: https://ssw.com.au/people/ben-cull
related:
- do-you-know-the-common-design-patterns-part-2-example
redirects: []

---

Angular uses parameter names to determine which dependencies to inject. When you minify your angular code, the parameter names are changed, so you must name your dependencies to ensure they work correctly. 

<!--endintro-->

The standard way to inject your dependencies looks a little like the following. We're defining a controller in this case.

``` js
phonecatApp.controller('PhoneListCtrl', function ($scope, $http) {...}
```

::: bad
Code: Bad example - This code will break when minified  
:::

When this code is minified the parameters are renamed. This means that the dependency injector no longer knows which services to inject.

You can fix this in 2 ways. The first one uses the `$inject` property to identify the name of the parameters in order:

``` js
function PhoneListCtrl($scope, $http) {...}
PhoneListCtrl.$inject = ['$scope', '$http'];
phonecatApp.controller('PhoneListCtrl', PhoneListCtrl);
```

::: good
Code: Good example - This code names the parameters using the $inject property  
:::

The second and **preferred** option is to pass an array containing the names, followed by the function itself. Take a look:

``` js
phonecatApp.controller('PhoneListCtrl', ['$scope', '$http', function($scope, $http) {...}]);
```

::: good
Code: Better example - This code names the parameters inline which is a little cleaner
:::

Using this method will ensure you don't run into problems with minification. If you'd like to know more, check out the [Angular tutorial for Dependency Injection](https://docs.angularjs.org/tutorial/step_05).
