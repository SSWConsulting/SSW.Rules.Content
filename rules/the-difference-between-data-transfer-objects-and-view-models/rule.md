---
type: rule
archivedreason: 
title: Do you know the difference between data transfer objects and view models?
guid: 3b46e163-56d5-43e5-a035-8dbbcaa40e48
uri: the-difference-between-data-transfer-objects-and-view-models
created: 2019-04-15T21:58:44.0000000Z
authors:
- title: Jason Taylor
  url: https://ssw.com.au/people/jason-taylor
related: []
redirects:
- do-you-know-the-difference-between-data-transfer-objects-and-view-models

---


<p class="ssw15-rteElement-P">Data Transfer Objects (DTOs) and View Models (VMs) are not the same concept! The main difference is that while VMs can encapsulate behaviour, DTOs do not.</p><p class="ssw15-rteElement-P">The purpose of a DTO is the transfer of data from one part of an application to another. Since DTOs do not encapsulate behaviour, they can easily be serialised and deserialized into other formats, e.g. JSON, XML, and so on.​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>The purpose of a VM is also the transfer of data, however VMs can encapsulate behaviour. This behaviour is useful, for example,&#160;when creating a WPF + MVVM application, but not so useful when creating a SPA - since you can't serialize the behaviour and pass it from ASP.NET MVC to the client.<br></p><p>Learn more about the above concepts in the following Weekly Dev Tips podcasts&#58;<br></p><p>·&#160; <a href="https&#58;//www.weeklydevtips.com/008">Data Transfer Objects (part 1)</a></p><p>·&#160; <a href="https&#58;//www.weeklydevtips.com/009">Data Transfer Objects (part 2)</a>​<br></p>


