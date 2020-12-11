---
type: rule
archivedreason: 
title: Do you know where bottlenecks can happen?
guid: 4671b023-5b53-4327-aa02-98d7eae52daf
uri: do-you-know-where-bottlenecks-can-happen
created: 2016-04-28T18:32:53.0000000Z
authors:
- id: 3
  title: Eric Phan
- id: 78
  title: Matt Wicks
related: []

---

For modern applications, there are many layers and moving parts that need to seamlessly work together to deliver our application to the end user.

<!--endintro-->
<dl class="image"> &lt;dt&gt; <img src="bottleneck.png" alt="bottleneck.png"> &lt;/dt&gt;<dd>Figure: Bottlenecks can happen anywhere! Call out diagrammatically where you think the bottlenecks are happenning<br></dd></dl>
The issues can be in:

### SQL Server

* Slow queries
* Timeouts
* Bad configuration
* Bad query plans
* Lack of resources
* Locking


### Business Logic

* Inefficient code
* Chatty code
* Long running processes
* Not making use of multicore processors


### Front end

* Too many requests to server a page
* Page size
* Large images
* No Caching


### Connection between SQL and Web

* Lack of bandwidth
* Too much chatter


### Connection between Web and Internet

* Poor uplink (e.g. 1mbps uploads)
* Too many hops


### Connection between Web and End users

* Geographically too far (e.g. US servers, AU users)


### Infrastructure

* Misconfiguration
* Resource contention
