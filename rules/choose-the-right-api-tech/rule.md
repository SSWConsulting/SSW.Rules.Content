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


REST is well established and most developers choose it by default when starting a new project. But now we have a choice&#160;and, depdending on your requirements, there may be a better option.<br>
<br><excerpt class='endintro'></excerpt><br>
<p>We rarely build standalone, self-contained applications anymore, and if you're building a data driven solution, you will have components that need to talk to each other somehow. This is usually a UI, which is&#160;occasioanlly a desktop rich client but more often a SPA or mobile app, and a back end.&#160;We achieve this by exposing an API on our back-end that our&#160;front-end client UI can talk to.<br></p><p>REST is well established as the protocol for this and most developers would choose this without giving it a second thought. But there are 2 other major players now, and depending on your requirements these could be better options for you.<br></p><h3 class="ssw15-rteElement-H3">REST<br></h3>​REST is built on top of HTTP and adopts the HTTP verbs to send and request data. REST and HTTP are both well understood by most developers, operating systems, runtimes and HTTP stacks, so using REST gives you confidence that your solution will run nearly anywhere. Also, by taking advantage of the HTTP protocol, you benefit from a lot of features this brings you out of the box, like being able to transfer rich content like videos and images, client-side caching out fo the box, and standardised response codes that other developers can understand if they are consuming your API.<div><br><div><h3 class="ssw15-rteElement-H3">gRPC<br></h3><p>gRPC,&#160;developed by Google, uses protobuf files (rather than JSON) for its payload and transfers over HTTP/2 rather than over HTTP. protobuf files define your payload and are human readable files, but the&#160;payload itself is serialized into binary, leading to much smaller transfer sizes. Additionally, HTTP/2, which is more a successor to HTTP rather than an incremental version increase, is much faster.</p><p>The result is that gRPC offers more efficiency (less bandwidth) and better performance (faster) than REST. gRPC is open source and there are libraries for most platforms, runtimes and languages. If performance is of a primary concern, gRPC may be the best option for you. However, as gRPC uses HTTP/2, and HTTP/2 is not yet as widely supported and implemented as HTTP, y ou must consider whether your client applications will be able to leverage this technology.<br></p><p>For more information, see our rule&#58;&#160;<a href=/when-to-use-grpc>Do you know when to use gRPC?​</a><br></p><h3 class="ssw15-rteElement-H3">​GraphQL<br></h3></div></div><div>GraphQL is a query language for APIs, developed by Facebook and open-sourced in 2015. GraphQL enables API or back-end developers to expose a flexible query interface, rather than well-defined data resources or view models, that front-end developers can consume. GraphQL is good for when you want to expose your entire data set to your consumers, or when you are ready to build your back-end, but your front end requirements are not yet well defined.<br></div><div><br></div><div>For more information, see our rule&#58;&#160;<a href=/graphql-when-to-use>Do you know when to use GraphQL?​</a><br><br></div><div><br></div><h3 class="ssw15-rteElement-H3">1, 2, or all 3<br></h3><p>​​​The best thing about all of these is that they are not mutually exclusive. You can use combinations of them that best suit your needs, rather than compromising to find the best general fit.<br></p><p>NOTE&#58; Some people might consider this a '3-headed beast'; the more you implement, the more you have to support. There could be scenarios where 2 or more of these options are a great fit and the right choice, but make sure you consider this carefully.<br></p><br>


