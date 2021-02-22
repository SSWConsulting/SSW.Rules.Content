---
type: rule
archivedreason: 
title: Do you choose the right web API technology for your project?
guid: cbab12b7-da75-4de9-a915-429a2f3a0389
uri: choose-the-right-api-tech
created: 2020-10-23T03:30:42.0000000Z
authors:
- title: Matt Goldman
  url: https://ssw.com.au/people/matt-goldman
related: []
redirects:
- do-you-choose-the-right-web-api-technology-for-your-project

---

REST is well established and most developers choose it by default when starting a new project. But now we have a choice and, depdending on your requirements, there may be a better option.

<!--endintro-->

We rarely build standalone, self-contained applications anymore, and if you're building a data driven solution, you will have components that need to talk to each other somehow. This is usually a UI, which is occasioanlly a desktop rich client but more often a SPA or mobile app, and a back end. We achieve this by exposing an API on our back-end that our front-end client UI can talk to.

REST is well established as the protocol for this and most developers would choose this without giving it a second thought. But there are 2 other major players now, and depending on your requirements these could be better options for you.

### REST

REST is built on top of HTTP and adopts the HTTP verbs to send and request data. REST and HTTP are both well understood by most developers, operating systems, runtimes and HTTP stacks, so using REST gives you confidence that your solution will run nearly anywhere. Also, by taking advantage of the HTTP protocol, you benefit from a lot of features this brings you out of the box, like being able to transfer rich content like videos and images, client-side caching out fo the box, and standardised response codes that other developers can understand if they are consuming your API.



### gRPC


gRPC, developed by Google, uses protobuf files (rather than JSON) for its payload and transfers over HTTP/2 rather than over HTTP. protobuf files define your payload and are human readable files, but the payload itself is serialized into binary, leading to much smaller transfer sizes. Additionally, HTTP/2, which is more a successor to HTTP rather than an incremental version increase, is much faster.

The result is that gRPC offers more efficiency (less bandwidth) and better performance (faster) than REST. gRPC is open source and there are libraries for most platforms, runtimes and languages. If performance is of a primary concern, gRPC may be the best option for you. However, as gRPC uses HTTP/2, and HTTP/2 is not yet as widely supported and implemented as HTTP, y ou must consider whether your client applications will be able to leverage this technology.

For more information, see our rule: [Do you know when to use gRPC?](/when-to-use-grpc)

### GraphQL




GraphQL is a query language for APIs, developed by Facebook and open-sourced in 2015. GraphQL enables API or back-end developers to expose a flexible query interface, rather than well-defined data resources or view models, that front-end developers can consume. GraphQL is good for when you want to expose your entire data set to your consumers, or when you are ready to build your back-end, but your front end requirements are not yet well defined.





For more information, see our rule: [Do you know when to use GraphQL?](/graphql-when-to-use)






### 1, 2, or all 3


The best thing about all of these is that they are not mutually exclusive. You can use combinations of them that best suit your needs, rather than compromising to find the best general fit.

NOTE: Some people might consider this a '3-headed beast'; the more you implement, the more you have to support. There could be scenarios where 2 or more of these options are a great fit and the right choice, but make sure you consider this carefully.
