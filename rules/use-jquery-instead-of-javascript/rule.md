---
type: rule
title: Do you use jQuery instead of JavaScript?
uri: use-jquery-instead-of-javascript
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-use-jquery-instead-of-javascript
created: 2016-11-17T15:55:05.000Z
archivedreason: null
guid: 7ced5ecb-1893-4305-b85f-962c36a9c50b
---

jQuery is the MUST HAVE tool for web developers. There are 3 good reasons why you should use jQuery.

1. Cross Browsers (Edge, Firefox, Safari, Opera, Chrome)
2. Powerful and easy to use
    * Same selectos as CSS
    * Designer can learn it fast
    * More readable JavaScript code
3. Plugins - Tons of useful plugins and functionalities

<!--endintro-->

```js
window.onload = function() { alert("Welcome"); }
```
::: bad
Figure: Bad example - Using JavaScript 'onload' event
:::


```js
$(document).ready(function() { alert("Welcome!"); });
```
::: good
Figure: Good example - Using jQuery document 'ready' event
:::
