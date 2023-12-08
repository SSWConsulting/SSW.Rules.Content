---
type: rule
archivedreason: 
title: Do you understand that with Angular you read and write to the model... never to the page? (aka Forget about jQuery)
guid: 3cd40e9e-38c3-4558-9a73-65bfb8dc5b6c
uri: angular-read-and-write-to-the-model-never-to-the-page
created: 2016-04-06T20:18:33.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects:
- do-you-understand-that-with-angular-you-read-and-write-to-the-model-never-to-the-page-a-k-a-forget-about-jquery
- do-you-understand-that-with-angular-you-read-and-write-to-the-model-never-to-the-page-(a-k-a-forget-about-jquery)

---

The most common mistake that developers make when moving from jQuery to Angular is that they continue to think about updating the page.

<!--endintro-->

![Figure: In jQuery, you design a page and then use jQuery to perform interactions with the page e.g. reading and setting the values of input boxes, updating the content of divs or handling button events](understand-jquery.png)  

::: bad  
![Figure: Bad Example - using jQuery on Angular views will lead to worlds of pain](understand-badcode.png)  
:::

A fundamental principal of Angular is that you build a Model in JavaScript (or TypeScript) and then on your view you just databind your UI elements to the model. Any changes that are made are made to the model and the view updates automatically.

**In Angular, you do not interact with the page you update the model, and the page is just displaying a view of the model.**

::: good  
![Figure: Good Example - In both AngularJs & Angular 2.0 jQuery is not required on the view. The view binds to properties on a JavaScript model](understand-goodcode.png)  
:::

Further reading: <http://stackoverflow.com/questions/14994391/thinking-in-angularjs-if-i-have-a-jquery-background>
