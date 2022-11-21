---
type: rule
title: Microservices - Do you break down your apps?
uri: microservices
authors:
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
created: 2021-11-11T05:54:22.790Z
guid: e4d0411a-6184-4f16-9caf-f522bb07c703
---
There are two common types of application architecture: 
* Monoliths (aka N-Tier applications)
* Microservices

Monoliths have their place. They are easy to get going and often make a lot of sense when you are starting out. However, sometimes your app may grow in size and become difficult to maintain. Then you might want to consider Microservices...

<!--endintro-->

Microservices let you break down your app into little pieces to make them more manageable, replaceable and maintainable. You can also scale out different parts of your app at a granular level.

.NET 6 and Azure have heaps of great tools for developing simple APIs and worker services in a Microservices pattern.

Watch the below video from 35:40 - 46:50
`youtube: https://youtu.be/oPyTZ-HGdn4?t=2141`

## The tools of the trade

* [.NET Worker Services](https://docs.microsoft.com/en-us/dotnet/core/extensions/workers) make it easier to implement dependency injection, configuration and other syntactic sugar using the same patterns you are familiar with in other types of .NET applications

* [Azure Container Apps](https://azure.microsoft.com/en-us/services/container-apps/#overview) give you a way to host different little subsections of the application

* [Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/) gives you a great way to build applications in small, modular, scalable and easy to manage chunks. It provides triggers other than http to handle other common microservice patterns

* [Minimal APIs](https://devblogs.microsoft.com/dotnet/asp-net-core-updates-in-net-6-preview-4/#introducing-minimal-apis) give you a way to write APIs in just a few short lines of code

## What's the point?

* Cost - Provides separation of scalability, keep the hot parts of your app hot and the cold parts of your app cold to achieve maximum pricing efficiency
* Maintainability - Keep code more manageable by making it bite sized chunks
* Simplify code - Write minimal APIs
* Deployment - Standardize deployment with containers
* Testing - Easier to find problems since they are isolated to a specific part of the app
* Cognitive Complexity - Devs can focus on one aspect of the app at a time
* Data - You can use the best way of storing data for each service
* Language - You can use the best language for each service

## What's the downside?
* Upfront Cost - More upfront work is required
* Cognitive Complexity - While individual apps are simpler, the architecture of the app can become more complex
* Health Check - It's harder to know if all parts are alive
* Domain boundaries - You need to define the separation of concerns between different services. Avoid adding dependencies between services because you can create a domino of failures...a house of cards.
* Performance normally suffers as calls are made between services
* Without adequate testing it's harder to maintain
* Using multiple languages and datastores can be both more expensive to host and require more developers

## What new techniques are required
* Contract Testing - To mitigate the risk of changes in one service breaking another, comprehensive tests that check the behaviour of services is required
