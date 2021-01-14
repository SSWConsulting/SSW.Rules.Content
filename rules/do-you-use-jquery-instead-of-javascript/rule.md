---
type: rule
archivedreason: 
title: Do you use jQuery instead of JavaScript?
guid: 7ced5ecb-1893-4305-b85f-962c36a9c50b
uri: do-you-use-jquery-instead-of-javascript
created: 2016-11-17T15:55:05.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- use-jquery-instead-of-javascript

---

jQuery is the MUST HAVE tool for web developers. There are 3 good reasons why you should use jQuery.

1. Cross Browsers (IE 6.0+, Firefox 2+, Safari 3.0+, Opera 9.0+, Chrome)
2. Powerful and easy to use
    * Same selectos as CSS
    * Designer can learn it fast
    * More readable JavaScript code
3. Plug-ins - Tons of useful plug-ins and functionalities



<!--endintro-->



```
window.onload = function() { alert("Welcome"); }
```



::: bad
Figure: Bad Example - Using JavaScript 'onload' event

:::



```
$(document).ready(function() { alert("Welcome!"); });
```



::: good
Figure: Good Example - using jQuery document 'ready' event

:::
