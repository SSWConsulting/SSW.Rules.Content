---
seoDescription: Always put JavaScript in a separate file to maintain consistent line numbers during debugging and improve performance through browser caching
type: rule
archivedreason:
title: Do you always put JavaScript in a separate file?
guid: 1d6f7924-8e0a-4dfa-b8dc-d3960cfcd3b7
uri: always-put-javascript-in-a-separate-file
created: 2016-09-01T18:32:24.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-always-put-javascript-in-a-separate-file
---

ASP.NET injects many lines during page rendering, so if you are using inline JavaScript, the line numbers will change during client side JavaScript debugging in VS.NET, FireBug or IE8 developer Tools.

<!--endintro-->

::: bad  
![Figure: Bad Code - Using Inline JavaScript](JavaScriptBad1.jpg)  
:::

::: bad  
![Figure: Bad Code - On PostBack Line numbers are changed for Inline JavaScript](JavaScriptBad.jpg)  
:::

::: good  
![Figure: Good Code - Using JavaScript on Separate file](JavaScriptGood.jpg)  
:::

So you should always put JavaScript in a separate file. Then the line numbers will stay consistent during debugging.
Keeping JavaScript in a separate file is also good for production as it improves performance due to browser caching.

**Note:** During development, remember to hit CTRL-F5 to force the browser to re-fetch the files from the server or you may be debugging old version of the JavaScript file.
