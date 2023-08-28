---
type: rule
archivedreason: 
title: Do you know the difference between data transfer objects and view models?
guid: 3b46e163-56d5-43e5-a035-8dbbcaa40e48
uri: the-difference-between-data-transfer-objects-and-view-models
created: 2019-04-15T21:58:44.0000000Z
authors:
- title: Jason Taylor
  url: /people/jason-taylor
related: []
redirects:
- do-you-know-the-difference-between-data-transfer-objects-and-view-models

---

Data Transfer Objects (DTOs) and View Models (VMs) are not the same concept! The main difference is that while VMs can encapsulate behaviour, DTOs do not.

The purpose of a DTO is the transfer of data from one part of an application to another. Since DTOs do not encapsulate behaviour, they can easily be serialised and deserialized into other formats, e.g. JSON, XML, and so on.

<!--endintro-->

The purpose of a VM is also the transfer of data, however VMs can encapsulate behaviour. This behaviour is useful, for example, when creating a WPF + MVVM application, but not so useful when creating a SPA - since you can't serialize the behaviour and pass it from ASP.NET MVC to the client.

Learn more about the above concepts in the following Weekly Dev Tips podcasts:

·  [Data Transfer Objects (part 1)](https&#58;//www.weeklydevtips.com/008)

·  [Data Transfer Objects (part 2)](https&#58;//www.weeklydevtips.com/009)
