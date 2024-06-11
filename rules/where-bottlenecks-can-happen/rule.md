---
seoDescription: Identify and optimize performance bottlenecks across SQL Server, business logic, front-end, connections, and infrastructure layers to enhance overall application speed.
type: rule
archivedreason:
title: Do you know where bottlenecks can happen?
guid: 4671b023-5b53-4327-aa02-98d7eae52daf
uri: where-bottlenecks-can-happen
created: 2016-04-28T18:32:53.0000000Z
authors:
  - title: Eric Phan
    url: https://ssw.com.au/people/eric-phan
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
related: []
redirects:
  - do-you-know-where-bottlenecks-can-happen
---

For modern applications, there are many layers and moving parts that need to seamlessly work together to deliver our application to the end user.

<!--endintro-->

![Figure: Bottlenecks can happen anywhere! Call out diagrammatically where you think the bottlenecks are happenning](bottleneck.png)

The issues can be in:

### SQL Server

- Slow queries
- Timeouts
- Bad configuration
- Bad query plans
- Lack of resources
- Locking

### Business Logic

- Inefficient code
- Chatty code
- Long running processes
- Not making use of multicore processors

### Front end

- Too many requests to server a page
- Page size
- Large images
- No Caching

### Connection between SQL and Web

- Lack of bandwidth
- Too much chatter

### Connection between Web and Internet

- Poor uplink (e.g. 1mbps uploads)
- Too many hops

### Connection between Web and End users

- Geographically too far (e.g. US servers, AU users)

### Infrastructure

- Misconfiguration
- Resource contention
