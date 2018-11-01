---
type: rule
title: Practices - Do you use a Service to share reusable logic?
uri: practices---do-you-use-a-service-to-share-reusable-logic
created: 2018-11-01T21:11:35.0000000Z
authors:
- id: 82
  title: Barry Sanders
- id: 34
  title: Brendan Richards

---



<span class='intro'> <p>A Service is a singleton object with a lifetime scope of the application.&#160; It is instantiated only once during the lifetime of an application.&#160; When combined with Angular’s Dependency Injection, a service can be injected into any component in an application via Constructor Injection. This makes a Service perfect for sharing reusable functionality throughout an application.</p> </span>

<p>A common example of when you’d use a Service is when you want to retrieve data from a WebApi using the HttpClient. There may be several places in your application where you need to retrieve the same list of data. By placing this functionality in a Service it gets rid of the duplicated code in the components that make the WebApi call. <br></p><dl class="badImage"><dt><img src="/PublishingImages/reusable-service-bad.jpg" alt="reusable-service-bad.jpg" /></dt><dd>Figure&#58; Bad Example - Code that is reusable should be placed in a Service</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/reusable-service-good.jpg" alt="reusable-service-good.jpg" /></dt><dd>Figure&#58; Good Example - ​ Reusable code is placed in a Service and the component calls the Service</dd></dl>


