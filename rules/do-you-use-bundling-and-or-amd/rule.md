---
type: rule
archivedreason: 
title: Do you use Bundling and/or AMD
guid: b51f62d0-83ea-4c94-b565-8e51552e846f
uri: do-you-use-bundling-and-or-amd
created: 2015-06-16T07:41:41.0000000Z
authors:
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
- title: Duncan Hunter
  url: https://ssw.com.au/people/duncan-hunter
related:
- do-you-treat-javascript-like-a-real-language
- do-you-know-which-version-of-jquery-to-use
- do-you-use-hyperlinks-instead-of-javascript-to-open-pages
redirects: []

---

Minification and AMD are techniques to improve javascript performance. They can both can be used with vanilla JavaScript and with Typescript 
<!--endintro-->

### AMD and RequireJs

AMD is a client-side technology that allows you to break you Js code into small inter-dependent modules. The modules (and thier dependencies) required to render a particular page are determined at runtime and subsequently downloaded by Javascript. RequireJs is a popular AMD implementation.


::: good
Pro: Only the js modules you need are downloaded  
:::


::: bad
Con: Each module is downloaded in a separate http request  
:::

### Bundling and Minification


This is a server side technique that combines and optimises client side files into single, optimised downloads.

ASP.Net contains excellent server-side bundling support as outlined here: [http://www.asp.net/mvc/overview/performance/bundling-and-minification](http&#58;//www.asp.net/mvc/overview/performance/bundling-and-minification)

ASP.Net vnext & VS 2015 also provides support for using task runners like Gulp or Grunt for bundling and minification.


::: good
Pro: Fewer Http requests and smaller files  
:::


::: bad
Con: All client side modules are included in a single download  
:::
